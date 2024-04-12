from django.contrib import admin

from .models import Post,Category,Tag,Paraqraf
# Register your models here.



admin.site.register(Post)
list_display= ("title","description","img","slug","categories","tags")
readonly_fields=("slug")
list_filters=("category")
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Paraqraf)