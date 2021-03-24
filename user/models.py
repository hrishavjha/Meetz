from django.contrib.auth.models import User
from django.db import models


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class UserDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=6, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    about = models.TextField(blank=True, null=True)
    dp = models.FileField(upload_to=user_directory_path, null=True, blank=True)
    lastOnline = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    relationship = models.CharField(max_length=20, null=True, blank=True)
    isPrivate = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.username)
