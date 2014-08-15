from django.db import models
from django.contrib.auth.models import User
from uuidfield import UUIDField


class Task(models.Model):
    """
    Simple task model, has UUID field 'key'
    """
    key = UUIDField(auto=True)
    account = models.ForeignKey(User)
    title = models.CharField(max_length=100, blank=False)
    completed = models.BooleanField(default=False)

    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'task'
        verbose_name_plural = 'tasks'
