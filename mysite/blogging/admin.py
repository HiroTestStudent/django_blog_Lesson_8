from django.contrib import admin

from blogging.models import Post, Category

# Register your models here.

class CategoryInlineAdmin(admin.TabularInline):

    model = Category.posts.through
    extra = 1

class PostAdmin(admin.ModelAdmin):

    inlines = [CategoryInlineAdmin, ]


class CategoryAdmin(admin.ModelAdmin):

    exclude = ('posts', )


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

# Note: I found the similar example on this website: https://cewing.github.io/training.codefellows/lectures/day27/django_admin.html
