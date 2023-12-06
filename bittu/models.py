from django.db import models

# Create your models here.
class Contact(models.Model):
    FirstName = models.CharField(max_length=122)
    LastName = models.CharField(max_length=122)
    Province = models.CharField(max_length=122)
    City = models.CharField(max_length=122)
    Address = models.CharField(max_length=122)
    Address2 = models.CharField(max_length=122)
    EmailAddress = models.CharField(max_length=122)
    PhoneNumber = models.CharField(max_length=122)
    desc = models.TextField()

    def __str__(self):
        return self.FirstName