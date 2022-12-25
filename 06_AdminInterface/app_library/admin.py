from django.contrib import admin
from app_library.models import Publisher, Author, Book


class BookInline(admin.TabularInline):
    model = Book


class PublisherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'genre']
    list_filter = ['is_active', 'city']
    inlines = [BookInline]


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name']
    search_fields = ['first_name', 'last_name', 'biography']
    fieldsets = (
        ('Основные сведения', {
            'fields': ('first_name', 'second_name', 'last_name', 'country', 'city')
        }),
        ('Биографические данные', {
            'fields': ('biography', ),
            'classes': ['collapse']
        }),
        ('Кoнтакты', {
            'fields': ('phone', 'email', 'personal_page', 'facebook', 'twitter')
        })

    )


class BookAdmin(admin.ModelAdmin):
    pass


admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
