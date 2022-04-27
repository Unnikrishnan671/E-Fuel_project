from django.db import models

class bunk(models.Model):
    owner_ide = models.IntegerField(default='0', null=True, blank=True)
    bunk_name = models.CharField(max_length=100)
    vehicle_type = models.BooleanField(default=False)
    connector = models.BooleanField(default=False)
    email = models.EmailField(max_length=240, null=True)
    phone = models.CharField(max_length=240, null=True)
    address =models.CharField(max_length=225)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    pincode = models.CharField(max_length=240, null=True)
    image = models.ImageField(upload_to="images/", null=True)

    def __str__(self):
        return self.bunk_name

class category(models.Model):
    category_name = models.CharField(max_length=225)
    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name=models.CharField(max_length=40)
    product_image= models.ImageField(upload_to='images/',null=True,blank=True)
    price = models.PositiveIntegerField()
    description=models.CharField(max_length=40)
    category = models.ForeignKey(category, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.product_name

class bunk_booked(models.Model):
    Bunk = models.ForeignKey(bunk, on_delete=models.CASCADE, null=True)
    user_ide = models.IntegerField(default='0', null=True, blank=True)
    name = models.CharField(max_length=240, null=True)
    email = models.EmailField(max_length=240, null=True)
    phone = models.CharField(max_length=240, null=True)
    uservehicle_type = models.BooleanField(default=False)
    userconnector = models.BooleanField(default=False)
    date = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    time = models.TimeField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    status = models.CharField(max_length=240, null=True, default='')

    def __str__(self):
        return self.name

