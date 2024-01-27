from django.db import models


# Create your models here.

class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount = models.PositiveIntegerField(help_text='discount in percentage')
    required_amount = models.PositiveBigIntegerField(help_text='required amount to use coupon', default=100)
    active = models.BooleanField(default=True)
    active_date = models.DateField()
    expiration_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.code
