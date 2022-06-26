from django.db import models
from django.contrib.auth.models import User



class Avatar(models.Model):
    blog = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="avatars", null=True, blank=True)