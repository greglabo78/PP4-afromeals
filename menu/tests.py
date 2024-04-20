from django.test import TestCase
from unittest.mock import patch
from django.db import models
import unittest

from .models import MealItem, DrinkItem, MEAL_TYPE, DRINK_TYPE

# Create your tests here.
class TestMealItemModel(unittest.TestCase):
    def setUp(self):
        # Setting up a mock instance of MealItem to test without database
        self.meal = MealItem(
            meal_id=1,
            meal_name="Eggs Benedict",
            description="A dish consisting of poached eggs on English muffins, Canadian bacon, and hollandaise sauce.",
            price=12.50,
            meal_type=0,  # Breakfast
            available=True
        )

    def test_string_representation(self):
        self.assertEqual(str(self.meal), "Eggs Benedict")

    def test_default_meal_type(self):
        new_meal = MealItem()
        self.assertEqual(new_meal.meal_type, 3)  # Checking the default type is 'New'

    def test_meal_availability(self):
        self.assertTrue(self.meal.available)

class TestDrinkItemModel(unittest.TestCase):
    def setUp(self):
        # Setting up a mock instance of DrinkItem to test without database
        self.drink = DrinkItem(
            drink_id=1,
            drink_name="Mojito",
            description="A Cuban cocktail made with rum, sugar, lime juice, soda water, and mint.",
            price=8.00,
            drink_type=2,  # Cocktails
            available=True
        )

    def test_string_representation(self):
        self.assertEqual(str(self.drink), "Mojito")

    def test_default_drink_type(self):
        new_drink = DrinkItem()
        self.assertEqual(new_drink.drink_type, 3)  # Checking the default type is 'New'

    def test_drink_availability(self):
        self.assertTrue(self.drink.available)