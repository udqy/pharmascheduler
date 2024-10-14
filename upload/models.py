from django.db import models

class Product(models.Model):
    product_id = models.AutoField(primary_key=True, default=0)
    product_name = models.CharField(max_length=255, unique=True, default='')

    def __str__(self):
        return self.product_name

    class Meta:
        db_table = "products"

class Ingredient(models.Model):
    ingredient_id = models.AutoField(primary_key=True, default=0)
    ingredient_name = models.CharField(max_length=255, unique=True, default='')

    def __str__(self):
        return self.ingredient_name

    class Meta:
        db_table = "ingredients"

class Composition(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        return f"{self.product.product_name} - {self.ingredient.ingredient_name} ({self.quantity})"

    class Meta:
        db_table = "composition"
        unique_together = ('ingredient', 'product')