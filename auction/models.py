from django.db import models
from common.models import DatedModel
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=150)
    address = models.TextField(max_length=512, blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class CompanyUser(DatedModel):
    user = models.OneToOneField(
        User, related_name='company_user', on_delete=models.CASCADE)
    company = models.ForeignKey(
        Company, blank=True, null=True,
        related_name='user_company', on_delete=models.SET_NULL
    )


class Category(models.Model):
    name = models.CharField(max_length=150)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Attachment(models.Model):
    image = models.ImageField(upload_to='images/')
    status = models.BooleanField(default=True)


class Auction(models.Model):
    title = models.CharField(max_length=150)
    company = models.ForeignKey(
        Company, blank=True, null=True,
        related_name='auction_company', on_delete=models.SET_NULL
    )
    category = models.ForeignKey(
        Category, blank=True, null=True,
        related_name='auction_category', on_delete=models.SET_NULL
    )
    address = models.TextField(max_length=512, blank=True, null=True)
    published_date = models.DateField(blank=True, null=True)
    start_time = models.TextField(blank=True, null=True)
    end_time = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=150)
    auction = models.ForeignKey(
        Auction, blank=True, null=True,
        related_name='product_auction', on_delete=models.SET_NULL
    )
    category = models.ForeignKey(
        Category, blank=True, null=True,
        related_name='product_category', on_delete=models.SET_NULL
    )
    make = models.CharField(max_length=150, blank=True, null=True)
    model = models.CharField(max_length=150, blank=True, null=True)
    size = models.CharField(max_length=150, blank=True, null=True)
    capacity = models.CharField(max_length=150, blank=True, null=True)
    color = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)

    media = models.ForeignKey(
        Attachment, blank=True, null=True,
        related_name='media_product', on_delete=models.SET_NULL
    )
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
