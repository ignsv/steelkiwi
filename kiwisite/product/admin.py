from django.contrib import admin
from .models import Product, Category



# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    # autocomplete slug based on name. Frontend utocomplete
    # remove it if Key_error slug not found raises
    prepopulated_fields = {'slug': ("name",)}


class CategoryAdmin(admin.ModelAdmin):
    # autocomplete slug based on name. JFrontend utocomplete
    # remove it if Key_error slug not found raises
    prepopulated_fields = {'slug': ("name",)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)


