from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class DatedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserProfile(DatedModel):
    user = models.OneToOneField(
        User, related_name='user_profile', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(max_length=512, blank=True, null=True)
    mobile = models.CharField(max_length=13, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    picture = models.CharField(max_length=200, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    user_longitude = models.FloatField(blank=True, null=True)
    user_latitude = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.user.username


# Signal Functions
def create_profile(sender, instance, created, **kwargs):
    """
    The functions used to check if user profile is not created
    and created the user profile without saving role and hospital
    :param sender:
    :param instance:
    :param created:
    :param kwargs:
    :return:
    """
    if created and not UserProfile.objects.filter(user=instance):
        return UserProfile.objects.create(
            user=instance
        )


# Signals
post_save.connect(create_profile, sender=User)
