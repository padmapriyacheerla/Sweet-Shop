from django.db import models


class Users(models.Model):
    full_name = models.CharField(max_length=225)
    email = models.EmailField()
    mobile = models.CharField(max_length=225)
    Password = models.CharField(max_length=225)
    objects = None


class Contact(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField()
    message = models.TextField()
    objects = None


class AdminUsers(models.Model):
    username = models.CharField(max_length=225, default='Admin')
    email = models.EmailField()
    Password = models.CharField(max_length=225)
    objects = None


class Sweets(models.Model):
    Name = models.CharField(max_length=225)
    price = models.CharField(max_length=225)
    Category = models.TextField()
    Image = models.ImageField(upload_to='Sweets/')
    Stock = models.IntegerField()
    objects = None
    DoesNotExist = None


class Order(models.Model):
    user = models.CharField(max_length=225, null=True, blank=True)
    sweet = models.CharField(max_length=225)
    quantity = models.CharField(max_length=225)
    address = models.CharField(max_length=225)
    phone = models.CharField(max_length=225, null=True, blank=True)
    objects = None
    DoesNotExist = None
