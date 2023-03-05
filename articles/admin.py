from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import Article, Comment


# class CommentInline(admin.StackedInline):
#     model = Comment
#     extra = 0  # new, remove rxtra empty fields


class CommentInline(admin.TabularInline):  # new
    model = Comment
    extra = 0


class ArticleAdmin(admin.ModelAdmin):  # new
    inlines = [
        CommentInline,
    ]


admin.site.register(Article, ArticleAdmin)  # new
admin.site.register(Comment)
