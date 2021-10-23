from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.contrib.auth.models import User
from userpage.models import Profile, Following


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        Following.objects.create(user=instance)
        print("profile created")


@receiver(m2m_changed, sender=Following.followed.through)
def follow_add(sender, instance, action, reverse, pk_set, **kwargs):
    followed_users = []
    logged_user = User.objects.get(username=instance)
    for i in pk_set:
        user = User.objects.get(pk=i)
        following_obj = Following.objects.get(user=user)
        # following_obj = Following.objects.filter(followed=user)
        followed_users.append(following_obj)

    if action == "pre_add":
        for i in followed_users:
            i.follower.add(logged_user)
            i.save()

    if action == "pre_remove":
        for i in followed_users:
            i.follower.remove(logged_user)
            i.save()
