from django.db import models

# Create your models here.
class employee(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to = 'images')
    desc = models.TextField()


class electrician(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to = 'images')
    desc = models.TextField()

class plumber(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to = 'images')
    desc = models.TextField()

class renovator(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to = 'images')
    desc = models.TextField()

class carpenter(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to = 'images')
    desc = models.TextField()

class house_keeper(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to = 'images')
    desc = models.TextField()


class AC_service(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to = 'images')
    desc = models.TextField()

class TV_service(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to = 'images')
    desc = models.TextField()


    