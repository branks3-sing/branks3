from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('ads.txt', views.ads_txt),
    path('', views.landing_view, name='landing'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('user/', views.user_dashboard, name='user_dashboard'),
    path('karaoke/<int:song_id>/', views.karaoke_player, name='karaoke_player'),           # old (optional)
    path('karaoke/<int:song_id>/<slug:slug>/', views.karaoke_player, name='karaoke_player_with_slug'), # old with slug
    path('toggle_share/<int:song_id>/', views.toggle_share, name='toggle_share'),
    path('upload_song/', views.upload_song, name='upload_song'),
    path('upload_recording/<int:song_id>/', views.upload_recording, name='upload_recording'),
    # NEW: song ID + slug – format
    path('<int:song_id>/<slug:slug>/', views.karaoke_player, name='song_detail'),
    path('delete_song/<int:song_id>/', views.delete_song, name='delete_song'),

    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),

    path('songs/', views.songs_page, name='songs_page'),
    path('faq/', views.faq, name='faq'),
    path('terms/', views.terms, name='terms'),


    path(
        "robots.txt",
        TemplateView.as_view(
            template_name="robots.txt",
            content_type="text/plain"
        ),
    ),

    path(
        "sitemap.xml",
        TemplateView.as_view(
            template_name="sitemap.xml",
            content_type="application/xml"
        ),
    ),
    path('google727bc10ed02ce07b', views.google_verification),
]
