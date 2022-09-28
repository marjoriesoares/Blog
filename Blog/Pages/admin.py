from django.contrib import admin
from .models import Pages

class PagesAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','date')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Pages, PagesAdmin)
