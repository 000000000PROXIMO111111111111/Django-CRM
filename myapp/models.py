from django.db import models
# Create your models here.
# Product description and corresponding prices
class Record(models.Model): #Django will pluralize class names
    Time_Stamp=models.DateTimeField(auto_now_add=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zipcode=models.CharField(max_length=50)

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")
        