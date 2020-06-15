from django.contrib import admin
from .models import Entry


class RegEntry(admin.ModelAdmin):
    list_display = ('post_date', 'post_title')


admin.site.register(Entry, RegEntry)

