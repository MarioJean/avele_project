from django.contrib import admin
from.models import Blogpost, Comment

admin.site.register(Blogpost)

admin.site.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "name","email","publish","status")
    list_filter = ("status", "publish")
    search_fields = ("name","email","comment")
