from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.CharField(max_length=500)
    image = models.ImageField(upload_to='post', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user) + " " + str(self.date.date())


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile', default="default/default.jpg", blank=True, null=True)
    bio = models.CharField(max_length=200, blank=True)
    connection = models.CharField(max_length=100, blank=True)
    follower = models.IntegerField(default=0)
    following = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user)


class Likes(models.Model):
    user = models.ManyToManyField(User, related_name='linkingUser')
    post = models.OneToOneField(Post, on_delete=models.CASCADE)

    @classmethod
    def like(cls, post, linking_user):
        obj, create = cls.objects.get_or_create(post=post)
        obj.user.add(linking_user)

    @classmethod
    def dislike(cls, post, dislinking_user):
        obj, create = cls.objects.get_or_create(post=post)
        obj.user.remove(dislinking_user)

    def __str__(self):
        return str(self.post)


class Following(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followed = models.ManyToManyField(User, related_name="followed")
    follower = models.ManyToManyField(User, related_name="follower")

    @classmethod
    def follow(cls, user, another_account):
        obj, create = cls.objects.get_or_create(user=user)
        obj.followed.add(another_account)
        print("followed")

    @classmethod
    def unfollow(cls, user, another_account):
        obj, create = cls.objects.get_or_create(user=user)
        obj.followed.remove(another_account)
        print("unfollowed")

    def __str__(self):
        return str(self.user)
