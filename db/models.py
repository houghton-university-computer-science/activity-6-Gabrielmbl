from django.db import models

# Create your models here.
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser


class OrderItem(models.Model):
	id = models.AutoField(
                auto_created = True,
                primary_key = True,
                serialize = False, 
                verbose_name ='ID')
	order = models.ForeignKey('Order', on_delete=models.PROTECT)
	product = models.ForeignKey('Product', on_delete=models.PROTECT)
	quantity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(999)])

	def __str__(self):
		return str(self.order) + " " + str(self.product) + " " + str(self.quantity)

class Product(models.Model):
	id = models.AutoField(
                auto_created = True,
                primary_key = True,
                serialize = False, 
                verbose_name ='ID')
	description = models.TextField()
	name = models.CharField(max_length=15)
	price = models.FloatField()
	product_id = models.CharField(max_length=5)

	def __str__(self):
		return str(self.name) + ": $" + str(self.price)

class Order(models.Model):
	id = models.AutoField(
                auto_created = True,
                primary_key = True,
                serialize = False, 
                verbose_name ='ID')
	customer = models.ForeignKey('Customer', on_delete=models.PROTECT)
	order_date = models.DateField()

	def __str__(self):
		return str(self.customer) + " " + str(self.order_date)

class Customer(models.Model):
	id = models.AutoField(
                auto_created = True,
                primary_key = True,
                serialize = False, 
                verbose_name ='ID')
	user = models.ForeignKey('User', on_delete=models.PROTECT)
	email = models.TextField()
	mailing_address = models.TextField()
	name = models.CharField(max_length=12)
	phone = models.CharField(max_length=11) 

	def __str__(self):
		return str(self.user)

class User(AbstractUser):
	def __str__(self):
		return str(self.first_name) + " " + str(self.last_name)


