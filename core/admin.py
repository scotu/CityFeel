from models import EntryQueue

from django.contrib import admin


class EntryQueueAdmin(admin.ModelAdmin):
    list_display = ('origin', 'origin_id', 'author_id', 'author', 'analysis',)


admin.site.register(EntryQueue, EntryQueueAdmin)
