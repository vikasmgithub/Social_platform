from django.contrib import admin
from .models import Posts
# Register your models here.

class PostsAdmin(admin.ModelAdmin):
    list_display = ('title','create_at','slug')


admin.site.register(Posts,PostsAdmin)