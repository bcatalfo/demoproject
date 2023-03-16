from django.db import models


# Create your models here.


class MenuCategory(models.Model):
    menu_category_name = models.CharField(max_length=200)


class Menu(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    price = models.IntegerField(null=False)
    category_id = models.ForeignKey(
        MenuCategory, on_delete=models.PROTECT, default=None
    )

    def __str__(self):
        return self.name + " : " + self.cuisine


class Person(models.Model):
    Person_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    age = models.IntegerField(null=True)
