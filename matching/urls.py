from django.urls import path
from . import views

app_name = 'matching'

urlpatterns = [
    path('api/like/', views.api_send_like, name='api_send_like'),
    path('api/dislike/', views.api_send_dislike, name='api_send_dislike'),
    path('matching/users/', views.MatchingUsers.as_view(), name='matching_users'),
    path('like/users/', views.LikeUsers.as_view(), name='like_users'),
    path('', views.Top.as_view(), name='top'),
]
