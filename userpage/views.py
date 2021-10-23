import json

from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import ListView
from django.core.paginator import Paginator

from userpage.models import Post, Profile, Likes, Following


def user_home(request):
    user = Following.objects.get(user = request.user)
    followed_user = user.followed.all()
    post = Post.objects.filter(user__in=followed_user).order_by("-pk") | Post.objects.filter(user=request.user).order_by('-pk')
    liked_ = [i for i in post if Likes.objects.filter(post=i, user=request.user)]
    custom_user = Profile.objects.get(user=request.user)
    return render(request, 'userpage/post_page.html', {'post': post, 'liked_post': liked_, 'user': custom_user})


def post(request):
    if request.method == "POST":
        caption_ = request.POST.get('caption', '')
        image_ = request.FILES['image']
        user_ = request.user
        post_obj = Post(user=user_, caption=caption_, image=image_)
        post_obj.save()
        messages.success(request, "Posted")
        return redirect('userhome')
    else:
        messages.error(request, 'Something went wrong!! not posted ')
        return redirect('userhome')


def delete_post(request, ID):
    post_ = Post.objects.filter(pk=ID)
    image_path = post_[0].image.url
    post_.delete()
    messages.info(request, 'Post deleted')
    return redirect('userhome')


def user_profile(request, username):
    user = User.objects.filter(username=username)
    if user:
        user = user[0]
        profile = Profile.objects.get(user=user)
        post = getPost(user)
        bio = profile.bio
        connection = profile.connection

        user_image = profile.image
        is_following = Following.objects.filter(user=request.user, followed=user)
        following_obj = Following.objects.get(user=user)
        following = following_obj.followed.count()
        follower = following_obj.follower.count()

        data = {'user_obj': user, 'bio': bio, 'connection': connection, 'follower': follower, 'following': following, 'user_image': user_image, 'post': post, 'connection_f': is_following}
    else:
        return HttpResponse("No such User")
    return render(request, 'userpage/user_profile.html', data)


def getPost(user):
    post_obj = Post.objects.filter(user=user)
    img_list = [post_obj[i:i + 3] for i in range(0, len(post_obj), 3)]
    return img_list


def like_dislike_post(request):
    post_id = request.GET.get("likeId", "")
    post = Post.objects.get(pk=post_id)
    user = request.user
    like = Likes.objects.filter(post=post, user=user)
    liked = False
    if like:
        Likes.dislike(post, user)
    else:
        liked = True
        Likes.like(post, user)
    resp = {
        "liked": liked,
    }
    response = json.dumps(resp)
    return HttpResponse(response, content_type="application/json")


def comment(request):
    comment_ = request.GET.get('comment_text', '')
    print(comment_)
    return render(request, "userpage/comments.html")


def follow(request, username):
    main_user = request.user
    to_follow = User.objects.get(username=username)
    following = Following.objects.filter(user=main_user, followed=to_follow)
    is_following = True if following else False

    if is_following:
        Following.unfollow(main_user, to_follow)
        is_following = False
    else:
        Following.follow(main_user, to_follow)
        is_following = True

    resp = {
        "following": is_following,
    }
    response = json.dumps(resp)
    return HttpResponse(response, content_type="application/json")


class Search(ListView):
    model = User
    template_name = "userpage/user_search.html"
    paginate_by = 2

    def get_queryset(self):
        username = self.request.GET.get("username", "")
        print("username: ", username)
        queryset = User.objects.filter(username__icontains=username)
        return queryset
