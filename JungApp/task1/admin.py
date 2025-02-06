from django.contrib import admin
from .models import Game, Buyer  # Импортируйте ваши модели

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size')  # Отображаемые поля
    list_filter = ('size', 'cost')  # Фильтрация по полям
    search_fields = ('title',)  # Поиск по полю
    list_per_page = 20  # Ограничение на количество записей

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age')  # Отображаемые поля
    list_filter = ('balance', 'age')  # Фильтрация по полям
    search_fields = ('name',)  # Поиск по полю
    list_per_page = 30  # Ограничение на количество записей
    readonly_fields = ('balance',)  # П

# Register your models here.
