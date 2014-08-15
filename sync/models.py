from django.db import models
from django.contrib.auth.models import User


class Hash(models.Model):
    """
    keeps a log of MD5 hashes of a dataset, this way hashes do not need to be recalculated every poll hit
    """
    account = models.ForeignKey(User)
    hash = models.CharField(max_length=32)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "[{0.account.username}]({0.date}) - {0.hash:<5.5}".format(self)

    class Meta:
        unique_together = (('account', 'hash'))
        verbose_name = 'hash'
        verbose_name_plural = 'hashes'