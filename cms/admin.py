from django.contrib import admin

import cms.models

# Register your models here.

class CommentInline(admin.TabularInline):
    # autocomplete_fields = ['comment_set']
    model = cms.models.Comment
    extra = 0
    min = 1
    max = 10


@admin.register(cms.models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "body", "created_on", "comments"]
    inlines = [CommentInline]

    def comments(self, obj):
        comments_ = obj.comment_set.all()
        if comments_.count()== 0:
            return "No comments"
        return ", ".join([comment.body for comment in comments_])

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("comment_set")


@admin.register(cms.models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(cms.models.Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
