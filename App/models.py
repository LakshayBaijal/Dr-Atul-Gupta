from django.db import models

# Create your models here.

class Mails(models.Model):
    name = models.CharField(max_length=15)
    maildate = models.DateField(auto_now=True)

    email = models.CharField(max_length=15)
    mobile = models.CharField(max_length=15,blank=True)
    subject = models.CharField(max_length=100)
    message = models.TextField(blank=True,max_length=400)

    def __str__(self):
        return (str(self.maildate) + ' ||  ' + self.name)
    