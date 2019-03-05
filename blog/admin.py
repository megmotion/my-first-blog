from django.contrib import admin
from .models import Post, Comment


class PostModelAdmin(admin.ModelAdmin):
	list_display = ["__str__", "author", "created_date", "published_date"]
	list_filter = ["author", "created_date", "published_date"]
	search_fields =["title"]
	class Meta:
		model = Post

admin.site.register(Post,PostModelAdmin)
admin.site.register(Comment)
