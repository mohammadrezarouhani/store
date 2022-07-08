from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Like(models.Model):
    place_at=models.DateField(auto_now=True)
    

class LikedItem(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    content_type=models.ForeignKey(ContentType,on_delete=models.CASCADE)
    content_id=models.PositiveIntegerField()
    content_obejct=GenericForeignKey()
