from django.contrib import admin

# Register your models here.
from .models import Posts,Director,Tag,Comments

class DirectorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email_address')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    list_display = ('title', 'directed_by', 'release_date', 'summary', 'tag_names')
    list_filter = ('title', 'directed_by', 'release_date')
    search_fields = ('title', 'directed_by__first_name', 'directed_by__last_name', 'release_date')

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'post')

admin.site.register(Posts,PostAdmin)
admin.site.register(Director,DirectorAdmin)
admin.site.register(Tag)
admin.site.register(Comments,CommentsAdmin)