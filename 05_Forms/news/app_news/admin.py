from django.contrib import admin
from app_news.models import News, Comments, User
from django.contrib.auth.admin import UserAdmin


class CommentsInline(admin.TabularInline):
    model = Comments


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'flag']
    list_filter = ['flag']
    inlines = [CommentsInline]
    actions = ['flag_is_active', 'flag_is_deactive']

    def flag_is_active(self, request, queryset):
        queryset.update(flag='Active')

    def flag_is_deactive(self, request, queryset):
        queryset.update(flag='Deactive')

    flag_is_active.short_description = 'Сделать Пост активным'
    flag_is_deactive.short_description = 'Сделать Пост неактивным'


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_short_text']
    list_filter = ['name']
    actions = ['give_ban']

    def give_ban(self, request, queryset):
        queryset.update(text='!BAN!')

    give_ban.short_description = 'Удалить пост'


@admin.register(User)
class MyAdminUser(UserAdmin):
    pass
