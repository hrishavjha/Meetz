from django.contrib.auth.models import User
from django.db import models


def path_gen(instance, filename):
    return 'post_{0}/{1}'.format(instance.user.username, filename)


class Post(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    postId = models.AutoField(primary_key=True)
    postText = models.TextField(blank=True, null=True)
    postImage = models.FileField(upload_to=path_gen, null=True, blank=True)
    postDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.postId)
