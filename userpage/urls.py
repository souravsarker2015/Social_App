from django.urls import path
from userpage import views

urlpatterns = [
    path('', views.user_home, name='userhome'),
    path('post/', views.post, name='post'),
    path('like_dislike_post/', views.like_dislike_post, name='like_dislike_post'),
    path('comment/', views.comment, name='comment'),
    path("search/", views.Search.as_view(), name='search_user'),
    path("delete/<int:ID>", views.delete_post, name='delete_post'),
    path("<str:username>", views.user_profile, name='user_profile'),
    path("user/follow/<str:username>", views.follow, name='follow'),

]
