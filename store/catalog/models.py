from django.core import validators
from django.db import models

from catalog.payment import ItemPayment

__all__ = ["Item"]


class Item(models.Model):
    name = models.CharField(
        "имя",
        max_length=150,
        help_text="Максимум 150 символов",
        unique=True,
    )
    description = models.TextField(
        "описание",
        max_length=512,
    )
    price = models.IntegerField(
        "стоимость",
        validators=[
            validators.MinValueValidator(0),
        ],
    )

    payment_price_id = models.CharField(
        "идентификатор платёжной системы",
        max_length=128,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        product = ItemPayment.create_product(self)
        price = ItemPayment.create_price(self, product)
        self.payment_price_id = price.id
        super().save(*args, **kwargs)
