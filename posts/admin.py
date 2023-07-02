from django.contrib import admin
from .models import Post , Vote

# Register your models here.
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('',)

admin.site.register(Post)
admin.site.register(Vote)

# class Voteadmin