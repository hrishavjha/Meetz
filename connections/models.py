from django.contrib.auth.models import User
from django.db import models


class Friend(models.Model):
    fromUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name="RequestSender")
    toUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name="RequestReceiver")
    createdOn = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.fromUser)


class Group(models.Model):
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE)
    groupId = models.AutoField(primary_key=True)
    groupName = models.CharField(max_length=20, blank=False, null=False)
    groupDesc = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.groupId)

