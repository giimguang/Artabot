from django.contrib import admin
from .models import Post,User_Report

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ["id","title","artist","language"]
    search_fields = ["title"]
    list_filter = ["language"]
admin.site.register(Post, PostAdmin)

class RequestAdmin(admin.ModelAdmin):
    list_display = ["id","report"]
    search_fields = ["gmail"]
admin.site.register(User_Report, RequestAdmin)