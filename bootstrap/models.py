from django.db import models

class formModel(models.Model):
    email = models.EmailField(max_length=100)
    phone = models.BigIntegerField(primary_key=True)

    def __str__(self):
        return self.email