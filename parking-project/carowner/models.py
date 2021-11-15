from django.db import models
from parkingowner.models import Parking
from users.models import CustomUser

# Create your models here.


#Car Owner Model

class CarOwner(models.Model):
	user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
	favoriteLocations = models.CharField(max_length=100,blank=True)
	cash = models.IntegerField(default=0,blank=True)

	def __str__(self):
		return self.user.firstName + self.user.lastName



class Car(models.Model):
	owner = models.ForeignKey(CarOwner,on_delete=models.CASCADE)
	carName = models.CharField(max_length=100)
	pelak = models.CharField(max_length=8,unique=True)
	color = models.CharField(max_length=100)
	

	def __str__(self):
		return self.pelak


class Comment(models.Model):
	parking = models.ForeignKey(Parking, on_delete=models.CASCADE)
	owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
	content = models.TextField()
	dateAdded = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.content

