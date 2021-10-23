from django.contrib import admin
from .models import Post, Profile, Likes,Following


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['caption', 'image', 'date']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'image', 'bio', 'connection', 'follower', 'following']


admin.site.register(Likes)
admin.site.register(Following)
