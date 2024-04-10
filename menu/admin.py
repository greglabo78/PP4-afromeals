from django.contrib import admin
from .models import MealItem, DrinkItem
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(MealItem)
class MealAdmin(SummernoteModelAdmin):
    list_display = ('meal_name', 'meal_type', 'price', 'available')
    search_fields = ('meal_name', 'description')
    list_filter = ('available', 'meal_type')
    summernote_fields = ('description')

@admin.register(DrinkItem)
class DrinkAdmin(SummernoteModelAdmin):
    list_display = ('drink_name', 'drink_type', 'price', 'available')
    search_fields = ('drink_name', 'description')
    list_filter = ('available', 'drink_type')
    summernote_fields = ('description')


