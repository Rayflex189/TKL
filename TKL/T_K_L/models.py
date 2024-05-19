from django.db import models

# Create your models here.

class Details(models.Model):
    transaction = models.CharField(max_length=200, default='Current transaction name')
    senders_name = models.CharField(max_length=200, default='Current senders name')
    senders_country = models.CharField(max_length=200, default='Current senders country name')
    recipent_name = models.CharField(max_length=200, default='Current Recipients name')
    recipent_country = models.CharField(max_length=200, default='Current country name')
    recipent_bank = models.CharField(max_length=200, default='Current recipient bank name')
    senders_bank = models.CharField(max_length=200, default='Current senders bank name')
    Total_Transfer_Amount = models.CharField(max_length=200, default='Current Total transfer amount')
    current_date = models.DateField(auto_now=True)
    status_update = models.CharField(max_length=200, default='In progress')
    status_text = models.CharField(max_length=200, default='current overhead or current payments due')
    estimated_delivery_time = models.CharField(max_length=200, default='time duration of funds unlocking proccess')
    Recipients_IBAN = models.CharField(max_length=200, default='DE31269513110168360295')
    image = models.ImageField(upload_to='images/', default="image_field")
    
    def __str__(self):
        return self.transaction