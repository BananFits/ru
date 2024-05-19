from django.contrib import admin

from .models import Travel

# Register your models here.
@admin.register(Travel)
class TravelAdmin(admin.ModelAdmin):
    fields = ['title', 'slug','content', 'is_published']
    #readonly_fields = ['slug']
    prepopulated_fields = {"slug":("title",)}
    list_display = ('id', 'title', 'slug', 'content', 'is_published')
    list_display_links = ('id', )
    list_editable = ('title',)
