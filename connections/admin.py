from django.contrib import admin

from .models import (
    Group,
    Friend,
)

admin.site.register(Group)
admin.site.register(Friend)