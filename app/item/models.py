from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_migrate

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

def create_default_categories(sender, **kwargs):
    if Category.objects.count() == 0:
        Category.objects.create(name='Toys')
        Category.objects.create(name='Clothes')
        Category.objects.create(name='Furnitures')

post_migrate.connect(create_default_categories)
