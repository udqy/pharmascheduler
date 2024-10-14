from django.db import models

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)  # Auto increment
    product_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.product_name
    
    class Meta:
        db_table = "products"

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()  # Assuming product_id is an integer
    product_name = models.CharField(max_length=255)
    quantity = models.FloatField()

    def __str__(self):
        return f'Order {self.order_id} - {self.product_name} ({self.quantity})'

    class Meta:
        db_table = "orders"
