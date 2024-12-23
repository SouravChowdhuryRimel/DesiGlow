from django.db import models

# Create your models here.









class Product(models.Model):
    username = models.CharField(max_length=99, blank=True, null=True)
    product_name = models.CharField(max_length=99, blank=True, null=True)
    product_price = models.FloatField(blank=True, null=True)
    
    # Define choices for product categories
    PRODUCT_CATEGORIES = [
        ('T-Shirt', 'T-Shirt'),
        ('Shirt', 'Shirt'),
        ('Winter Jacket', 'Winter Jacket'),
        ('Jeans', 'Jeans'),
        ('Panjabi', 'Panjabi'),
        ('Pajama', 'Pajama'),
        ('Polo', 'Polo'),
        ('Tops & T-Shirt', 'Tops & T-Shirt'),
        ('Kamiz/Kurti', 'Kamiz/Kurti'),
        ('Wallet', 'Wallet'),
        ('Bag', 'Bag'),
        ('Cap', 'Cap'),
        ('Sunglasses', 'Sunglasses'),
    ]
    
    product_category = models.CharField(
        max_length=99, 
        choices=PRODUCT_CATEGORIES, 
        blank=True, 
        null=True,
    )
    
    product_description = models.TextField(blank=True, null=True)
    additional_information = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    photo = models.ImageField(upload_to='product_photo/', blank=True, null=True)
    extra_photo1 = models.ImageField(upload_to='product_photo/', blank=True, null=True)
    extra_photo2 = models.ImageField(upload_to='product_photo/', blank=True, null=True)
    extra_photo3 = models.ImageField(upload_to='product_photo/', blank=True, null=True)
    extra_photo4 = models.ImageField(upload_to='product_photo/', blank=True, null=True)
    
    def __str__(self):
        return self.product_name





class Review(models.Model):
    username = models.CharField(max_length=99, blank=True, null=True)
    product_id = models.IntegerField(blank=True, null=True)
    review = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True, blank=True, null=True)
    
    def __str__(self):
        return self.username





class Cart(models.Model):
    username = models.CharField(max_length=99, blank=True, null=True)
    product_name = models.CharField(max_length=99, blank=True, null=True)
    product_price = models.FloatField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    photo = models.ImageField(upload_to='cart/', blank=True, null=True)
    size = models.CharField(max_length = 99, blank = True, null = True)
    
    def __str__(self):
        return self.product_name








class MyOrder(models.Model):
    username = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address1 = models.CharField(max_length=255, blank=True, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zip = models.CharField(max_length=20, blank=True, null=True)
    subtotal = models.CharField(max_length=20, blank=True, null=True)
    total = models.CharField(max_length=20, blank=True, null=True)
    product_details = models.TextField(blank=True, null=True)
    payment_details = models.CharField(max_length=20, blank=True, null=True)
    payment_status = models.BooleanField(default=False)
    shipped_status = models.BooleanField(default=False)
    delivery_status = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True, blank=True, null=True)
    size = models.CharField(max_length = 99, blank = True, null = True)
    
    # Add any other fields you need for your order model

    def __str__(self):
        return f"Order by {self.username}"





class Merchant(models.Model):
    username = models.CharField(max_length=99, blank=True, null=True)
    first_name = models.CharField(max_length=99, blank=True, null=True)
    last_name = models.CharField(max_length=99, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    shop_name = models.CharField(max_length=99, blank=True, null=True)
    email = models.CharField(max_length=99, blank=True, null=True)
    verified = models.BooleanField(default=False)
    
    def __str__(self):
        return self.shop_name




    