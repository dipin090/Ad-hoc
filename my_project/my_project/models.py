from django.db import models


class hospital_department(models.Model):
    dep_id=models.IntegerField(primary_key=True)
    dep_name=models.CharField(max_length=100)

class paitents(models.Model):
    p_id=models.IntegerField(primary_key=True)
    p_name = models.CharField(max_length=100)
    age = models.IntegerField()
    appoinment = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100)
    dep_id=models.ForeignKey(hospital_department,related_name='task',on_delete=models.CASCADE)
