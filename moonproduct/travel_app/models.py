from django.db import models


class Employee(models.Model):
    username=models.CharField(max_length=250,default='',unique=True)
    password=models.CharField(max_length=250,default='')
    name=models.CharField(max_length=250,default='')
    carmodel=models.CharField(max_length=1000,default='')
    carnum=models.CharField(max_length=1000,default='')
    contactnum=models.CharField(max_length=1000,default='')
    location=models.CharField(max_length=1000,default='')


    def __str__(self):
        return self.username +" " + self.contactnum

class BookTrip(models.Model):
    driver=models.ForeignKey(Employee,on_delete=models.CASCADE)
    p_name=models.CharField(max_length=250,default='')
    pickup_time = models.DateTimeField()
    p_pickup=models.CharField(max_length=250,default='')
    p_destination=models.CharField(max_length=250,default='')
    p_phone = models.CharField(max_length=15,default='')

    def __str__(self):
        return self.p_pickup+'<->'+self.p_destination+' at '+str(self.pickup_time)
