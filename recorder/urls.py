from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('user/', views.user_dashboard, name='user_dashboard'),
    path('karaoke/<int:song_id>/', views.karaoke_player, name='karaoke_player'),           # old (optional)
    path('karaoke/<int:song_id>/<slug:slug>/', views.karaoke_player, name='karaoke_player_with_slug'), # old with slug
    path('toggle_share/<int:song_id>/', views.toggle_share, name='toggle_share'),
    path('upload_song/', views.upload_song, name='upload_song'),
    path('upload_recording/<int:song_id>/', views.upload_recording, name='upload_recording'),
    # NEW: song ID + slug – ఇదే మనకు కావాల్సిన format
    path('<int:song_id>/<slug:slug>/', views.karaoke_player, name='song_detail'),
]
