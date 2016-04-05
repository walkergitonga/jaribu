from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

# Create your models here.
class Inquiry(models.Model):
    SERVICES = (
    ('DATA', 'Data'),
    ('AIRTIME', 'Airtime'),
    ('AIRTIME 4 CASH', 'Airtime 4 Cash'),
    )

    DEPARTMENTS = (
        ('BUSINESS', 'Business'),
        ('DESIGN', 'Design'),
        ('PAYPAL', 'PayPal'),
    )
    
    fullname     = models.CharField(max_length=50)
    phonenumber  = models.CharField(max_length=50)
    service      = models.CharField(max_length=50, choices=SERVICES)
    complaint    = models.TextField(max_length=500)
    department   = models.CharField(max_length=50, choices=DEPARTMENTS)
    
    def __str__(self):
        return self.complaint