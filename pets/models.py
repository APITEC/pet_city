from django.db import models
from users.models import User


# Create your models here.
class PetType(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Pet(models.Model):
    name = models.CharField(max_length=25)
    type = models.ForeignKey(PetType, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    birth_date = models.DateField()

    def __str__(self):
        return self.name + ' (' + self.type.name + ')'


class FoodType(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Feeding(models.Model):
    name = models.CharField(max_length=25)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    type = models.ForeignKey(FoodType, on_delete=models.CASCADE)
    time = models.TimeField()

    def __str__(self):
        return self.pet.name + ' - ' + self.name + ' (' + str(self.time) + ')'