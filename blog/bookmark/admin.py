from django.contrib import admin
from bookmark.models import Bookmark, Answer

class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('title','content')
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Bookmark, BookmarkAdmin)