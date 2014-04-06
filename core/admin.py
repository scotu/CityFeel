from models import EntryQueue, Area, SourceForArea, EntryClassification, ApiRequests

from django.contrib import admin


class EntryQueueAdmin(admin.ModelAdmin):
    list_display = ('origin', 'origin_id', 'author_id', 'author', 'analysis',)


class AreaAdmin(admin.ModelAdmin):
    list_display = ('description', 'lat', 'long', 'rad',)


class SourceForAreaAdmin(admin.ModelAdmin):
    list_display = ('name', 'area', 'max_id', 'since_id',)


class ApiRequestsAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'counter', 'until',)


admin.site.register(EntryQueue, EntryQueueAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(SourceForArea, SourceForAreaAdmin)
admin.site.register(EntryClassification)
admin.site.register(ApiRequests, ApiRequestsAdmin)
