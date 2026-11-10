from django.contrib import admin
from .models import Post, Comment, Tag


admin.site.register(Post)
admin.site.register(Comment)



class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Tag, TagAdmin)