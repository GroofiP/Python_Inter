from django.db import models


class Shop_Item(models.Model):
    name_product = models.CharField(max_length=255, verbose_name="Название продукта")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обнолвения")
    unit = models.CharField(max_length=255, verbose_name="Единица измерение")
    provider = models.CharField(max_length=255, verbose_name="Поставщик")
    price = models.DecimalField(max_digits=10, decimal_places=1, default=0, verbose_name="Цена")

    def __str__(self):
        return self.name_product

    class Meta:
        verbose_name = "Карточка товара"
        verbose_name_plural = "Карточки товаров"
