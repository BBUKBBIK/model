from django.contrib import admin

# Register your models here.
from .models import Blog,Comment
admin.site.register(Comment)
admin.site.register(Blog)