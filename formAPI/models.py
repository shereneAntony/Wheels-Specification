from django.db import models

# Create your models here.

class WheelSpecification(models.Model):
    form_number=models.CharField(max_length=100,unique=True)
    submitted_by=models.CharField(max_length=100)
    submitted_date=models.DateField()
    condemning_dia=models.CharField(max_length=100)
    last_shop_issue_size=models.CharField(max_length=100)
    tread_diameter_new=models.CharField(max_length=100)
    wheel_gauge=models.CharField(max_length=100)


