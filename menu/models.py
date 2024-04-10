from django.db import models



MEAL_TYPE = ((0, 'Breakfast'), (1, 'lunch'), (2, 'Dinner'), (3, 'New'))
DRINK_TYPE = ((0, 'Wines'), (1, 'Beers'), (2, 'Cocktails'), (3, 'New'))

# Create your models here.
class MealItem(models.Model):
    meal_id = models.AutoField(primary_key=True)
    meal_name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    meal_type = models.IntegerField(
        choices=MEAL_TYPE,
        default=3
        )
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ['-meal_type']

    def __str__(self):
        return self.meal_name

class DrinkItem(models.Model):
    drink_id = models.AutoField(primary_key=True)
    drink_name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    drink_type = models.IntegerField(
        choices=DRINK_TYPE,
        default=3
        )
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ['-available']

    def __str__(self):
        return self.drink_name