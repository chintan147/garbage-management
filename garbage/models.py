from django.db import models

# Create your models here.

class Admin(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Password = models.CharField(max_length=50)
    Role = models.CharField(max_length=50)
    Phone = models.CharField(max_length=12, default="phone")
    Location = models.CharField(max_length=100, default="location")

    def get_object():
        return Admin.objects.get(Role="Admin")

class User(models.Model):
    User = models.ForeignKey(Admin, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Role = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    Phone = models.CharField(max_length=12)
    OTP = models.IntegerField(null=True)
    #is_verified = models.BooleanField(default=False)
    #is_created = models.DateField(default=False)
    # is_active = models.BooleanField(default=False)

#class Recycler(models.Model):
    #recycler = models.ForeignKey(Admin, on_delete=models.CASCADE)
    #Name = models.CharField(max_length=100)
    #Email = models.EmailField(max_length=100)
    #Password = models.CharField(max_length=50)

class GarbageCollector(models.Model):
    GC = models.ForeignKey(Admin, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=50)
    Role = models.CharField(max_length=50)
    Password = models.CharField(max_length=30)
    Gender = models.CharField(max_length=6)
    Phone = models.CharField(max_length=12)
    Address = models.CharField(max_length=100)
    Location = models.CharField(max_length=15, default="location")
    

class Request(models.Model):
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    GC_id = models.ForeignKey(GarbageCollector, on_delete=models.CASCADE)
    Status = models.CharField(max_length=10, default="Pending")
    Garbage_Type = models.CharField(max_length=50, default="Garbage_Type")
    Garbage_Description = models.CharField(max_length=100, default="Garbage_Description")
    Phone = models.CharField(max_length=12, default="Phone")
    Address = models.CharField(max_length=100, default="Empty")
    Date = models.CharField(max_length=40, default="Empty")
    Quantity = models.IntegerField(null=True)
    pay_status = models.CharField(max_length=10, default="Pending")

class GarbageItem(models.Model):
    req_fk = models.ForeignKey(Request,on_delete=models.CASCADE)
    Item_Name = models.CharField(max_length=100)
    Item_Quantity = models.IntegerField(null=True)
    Item_Type = models.CharField(max_length=50, default="Garbage_Type")
    Item_Price = models.IntegerField(null=True)
    Item_Description = models.CharField(max_length=100, default="Garbage_Description")
    Date = models.CharField(max_length=40, default="Empty")
    pay_status = models.CharField(max_length=30, default="Pending")






class Product(models.Model):
    admin_fk = models.ForeignKey(Admin, on_delete=models.CASCADE, default=None)
    ProductName = models.CharField(max_length=30, default="name")
    Description = models.CharField(max_length=50, default="description")
    Date = models.DateField(null=True)
    ProductType = models.CharField(max_length=30, default="type")
    Quantity = models.IntegerField(null=True)
    Price = models.IntegerField(null=True)
    Image = models.ImageField(null=True, blank=True,upload_to="gallery")
    Image_Name=models.CharField(max_length=50,default="name")

class Cart(models.Model):
    temp = models.ForeignKey(Admin, on_delete=models.CASCADE, default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Quantity = models.IntegerField(null=True)
    Price = models.IntegerField(null=True)
    Total = models.IntegerField(null=True)


class GarbageType(models.Model):
    Garbage_type = models.CharField(max_length=10)
    #Price = models.IntegerField()

class Order(models.Model):
    Name = models.CharField(max_length=10)
    Productname = models.CharField(max_length=10)
    Price = models.IntegerField()
    Quantity = models.CharField(max_length=5)
    Total = models.IntegerField()

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    full_name = models.CharField(max_length=30)
    Phone = models.CharField(max_length=12)
    Email = models.EmailField(max_length=30)
    Subject = models.EmailField(max_length=50)
    Message = models.CharField(max_length=200)
    Date = models.CharField(max_length=50, default=None)




