from django.db import models

# Create your models here.
class Bank(models.Model):
    bankName = models.CharField("Bank name", max_length=255, blank = True, null = True)
    bankCode = models.CharField("Bank code", max_length=255, blank = True, null = True)

    class Meta:
        db_table='banks'

    def __str__(self):
        return self.bankName


