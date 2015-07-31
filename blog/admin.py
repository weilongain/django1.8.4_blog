from django.contrib import admin
from .models import MyBlog,Tag
# Register your models here.


class MyBlogAdmin(admin.ModelAdmin):
    list_display = ["tittle","tittle_sm","pub_date","publisher"]


admin.site.register(MyBlog,MyBlogAdmin)
admin.site.register(Tag)