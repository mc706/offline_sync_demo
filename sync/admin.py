from django.contrib import admin
from sync.models import Hash


class HashAdmin(admin.ModelAdmin):
    list_display = ['account', 'timestamp', 'hash']


admin.site.register(Hash, HashAdmin)