from django.db import models


class Admin(models.Model):

    name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "admin"
     

class Staff(models.Model):

    staff_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, null=True)
    phone = models.CharField(max_length=15, null=True)
    gender = models.CharField(max_length=10,  blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    joining_date = models.DateField(blank=True, null=True)  
    role = models.CharField(max_length = 20)
    pic = models.ImageField(upload_to='staff_pics/', null=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "staff"