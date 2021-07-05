from django.db import models

# Create your models here.
class Add_Mail(models.Model):
    mail = models.EmailField(max_length=254)
    added_by = models.CharField(max_length=50)

    def __str__(self):
        return self.mail
    