from django.contrib import admin
from .models import Author, Contact,Post
# @admin.register(Author)
class AutherAdmin(admin.ModelAdmin):
    list_display=['id','user']

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display=['id','title']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=['id','name','email','phone','message']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['id','title','overview','time_upload','author','thumbnaill']
