from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType



class Tag(models.Model):
    label=models.CharField(max_length=255)


class TaggedItem(models.Model):
    tag=models.ForeignKey(Tag,on_delete=models.CASCADE)
    content_type=models.ForeignKey(ContentType,on_delete=models.CASCADE)
    content_id=models.PositiveIntegerField()
    content_objec=GenericForeignKey('content_type','content_id')