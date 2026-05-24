import os
import hashlib
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.conf import settings
from .models import Song, UserProfile, Recording
from django.http import HttpResponse

from django.views.generic import TemplateView
from django.templatetags.static import static
from django.shortcuts import redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            try:
                profile = UserProfile.objects.get(user=user)
                if profile.role == 'admin':
                    return redirect('/admin/?page=songs')
                else:
                    return redirect('/user/')
            except UserProfile.DoesNotExist:
                return redirect('/user/')
        else:
            return render(request, 'recorder/login.html', {'error': 'Invalid credentials!'})
    return render(request, 'recorder/login.html')

def logout_view(request):
    auth_logout(request)
    return redirect('/')

@login_required
def admin_dashboard(request):
    profile = UserProfile.objects.get(user=request.user)
    if profile.role != 'admin':
        return redirect('/user/')
    
    page = request.GET.get('page', 'songs')
    songs = Song.objects.all()
    
    context = {
        'username': request.user.username,
        'page': page,
        'songs': songs,
    }
    return render(request, 'recorder/admin_dashboard.html', context)

@login_required
def user_dashboard(request):
    songs = Song.objects.filter(is_shared=True)
    context = {
        'username': request.user.username,
        'songs': songs,
    }
    return render(request, 'recorder/user_dashboard.html', context)

@csrf_exempt
@require_http_methods(["POST"])
def toggle_share(request, song_id):
    if not request.user.is_authenticated:
        return JsonResponse({'success': False, 'error': 'Login required'}, status=403)
    
    try:
        profile = UserProfile.objects.get(user=request.user)
        if profile.role != 'admin':
            return JsonResponse({'success': False, 'error': 'Admin only'}, status=403)
        
        song = Song.objects.get(id=song_id)
        song.is_shared = not song.is_shared
        song.save()
        return JsonResponse({'success': True, 'is_shared': song.is_shared})
    except (UserProfile.DoesNotExist, Song.DoesNotExist):
        return JsonResponse({'success': False, 'error': 'Not found'}, status=404)

def karaoke_player(request, song_id, slug=None):   # slug optional
    song = get_object_or_404(Song, id=song_id)

    # --------------------------------------------------------------
    
    if slug is None:
        from django.utils.text import slugify
        new_url = f"/{song.id}/{slugify(song.name)}/"
        return redirect(new_url)
    # --------------------------------------------------------------

    # Anonymous user handling
    if not request.user.is_authenticated:
        if song.is_shared:
            return render(request, 'recorder/karaoke_player.html', {
                'song': song,
                'username': 'Guest',
                'role': 'guest'
            })
        else:
         
            return redirect(f'/login/?next=/{song.id}/{slug}/')

    # Authenticated user
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile = None

    if profile and profile.role == 'admin':
        # admin can access all
        pass
    elif not song.is_shared:
        return redirect('/user/')

    return render(request, 'recorder/karaoke_player.html', {
        'song': song,
        'username': request.user.username,
        'role': profile.role if profile else 'user'
    })

@login_required
def upload_song(request):
    if request.method == 'POST':
        profile = UserProfile.objects.get(user=request.user)
        if profile.role != 'admin':
            return redirect('/admin/')
        
        song_name = request.POST.get('song_name', '').strip()
        original_file = request.FILES.get('original_file')
        accompaniment_file = request.FILES.get('accompaniment_file')
        lyrics_image = request.FILES.get('lyrics_image')
        
        if original_file and accompaniment_file:
            if song_name:
                final_name = song_name[:200]
            else:
                final_name = os.path.splitext(original_file.name)[0].replace('_original', '').strip()
                final_name = final_name or 'New Song'
            
            song = Song.objects.create(
                name=final_name,
                original_file=original_file,
                accompaniment_file=accompaniment_file,
                uploaded_by=request.user.username
            )
            if lyrics_image:
                song.lyrics_image = lyrics_image
                song.save()
            
            return redirect('/admin/?page=songs')
    
    return redirect('/admin/')

@csrf_exempt
def upload_recording(request, song_id):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Login required'}, status=401)
    
    if request.method == 'POST' and request.FILES.get('recording'):
        try:
            song = Song.objects.get(id=song_id)
            recording = request.FILES['recording']
            filename = f"recording_{song_id}_{request.user.username}_{int(os.times()[4]*1000)}.webm"
            path = os.path.join(settings.MEDIA_ROOT, 'recordings', filename)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            
            with open(path, 'wb+') as destination:
                for chunk in recording.chunks():
                    destination.write(chunk)
            
            Recording.objects.create(
                song=song,
                user=request.user.username,
                file=f'recordings/{filename}'
            )
            
            return JsonResponse({
                'final_url': f'/media/recordings/{filename}',
                'message': 'Recording saved successfully'
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request'}, status=400)

@login_required
@require_http_methods(["POST"])
def delete_song(request, song_id):
    try:
        # Admin 
        profile = UserProfile.objects.get(user=request.user)
        if profile.role != 'admin':
            return JsonResponse({'success': False, 'error': 'Admin only'}, status=403)
        
        song = Song.objects.get(id=song_id)
        

        if song.original_file and os.path.isfile(song.original_file.path):
            os.remove(song.original_file.path)
        if song.accompaniment_file and os.path.isfile(song.accompaniment_file.path):
            os.remove(song.accompaniment_file.path)
        if song.lyrics_image and os.path.isfile(song.lyrics_image.path):
            os.remove(song.lyrics_image.path)
        

        song.delete()
        
        return JsonResponse({'success': True})
    except UserProfile.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'User profile not found'}, status=404)
    except Song.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Song not found'}, status=404)
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)

def ads_txt(request):
    data = "google.com, pub-2373888797323762, DIRECT, f08c47fec0942fa0"
    return HttpResponse(data, content_type="text/plain")

def landing_view(request):
    """Display random shared songs and a login button."""
    shared_songs = Song.objects.filter(is_shared=True)
    # Randomly select up to 6 songs (or adjust the number as needed)
    random_songs = shared_songs.order_by('?')[:6]
    return render(request, 'recorder/home_public.html', {'songs': random_songs})
def privacy_policy(request):
    return render(request, 'recorder/privacy_policy.html')

def contact(request):
    return render(request, 'recorder/contact.html')

def about(request):
    return render(request, 'recorder/about.html')


def songs_page(request):
    songs = Song.objects.filter(is_shared=True)
    return render(request, 'recorder/songs.html', {
        'songs': songs
    })
def faq(request):
    return render(request, 'recorder/faq.html')

def terms(request):
    return render(request, 'recorder/terms.html')

def google_verification(request):
    return redirect('/static/googlea1b2c3d4e5.html')

