from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=40, unique=True)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # auto slugify slugField only when Category instance creates
        #remove if not self.id to auto slagify when Category instance updates
        if not self.id:
            self.slug = slugify(self.name)

        super(Category, self).save(*args, **kwargs)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, unique=True)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    created_at = models.DateTimeField("creation date")
    modified_at = models.DateTimeField("modification date")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # auto slugify slugField only when Product instance creates
        # remove if not self.id to auto slagify when Product instance updates
        if not self.id:
            self.slug = slugify(self.name)

        super(Product, self).save(*args, **kwargs)




