from django.contrib import admin
from .models  import *


class WorkFileInline(admin.TabularInline):
    model = WorkFile
    extra = 1

class WorkAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = (WorkFileInline,)

admin.site.register(Work, WorkAdmin)
admin.site.register(WorkInfo)
admin.site.register(WorkFile)