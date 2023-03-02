from django.db import models
from manage import init_django

init_django()

class Model(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ContentRating(Model):
    title = models.CharField(max_length=255)
    ageLimit = models.IntegerField()
    description = models.TextField()

class Publisher(Model):
    title = models.TextField()

class Platform(Model):
    title = models.TextField()

class Genre(Model):
    title = models.TextField()

class Product(Model):
    title = models.TextField()
    description = models.TextField()
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    releaseDate = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    price = models.IntegerField()
    contentRating = models.ForeignKey(ContentRating, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    isAvailable = models.BooleanField()

class Customer(Model):
    firstName = models.TextField()
    lastName = models.TextField()
    email = models.TextField()
    phone_num = models.TextField()
    dateOfBirth = models.DateField

class WishList(Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)

class Sales(Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.TextField()
    dateOfSales = models.DateField()

class Discount(Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    dateFrom = models.DateField()
    dateUntil = models.DateField()
    prc = models.DecimalField(decimal_places=2,max_digits=2)
