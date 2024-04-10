from django.shortcuts import render
from .models import MealItem, DrinkItem

def menu_view(request):
    """
    View function to display both meals and drinks.
    """
    meal_list = MealItem.objects.all()
    drink_list = DrinkItem.objects.all()
    
    context = {
        'meal_list': meal_list,
        'drink_list': drink_list,
    }
    
    return render(request, 'menu/menu_page.html', context)
