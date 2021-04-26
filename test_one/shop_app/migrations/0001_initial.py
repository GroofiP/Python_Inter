# Generated by Django 3.1.3 on 2021-04-16 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop_Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_product', models.CharField(max_length=255, verbose_name='Название продукта')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обнолвения')),
                ('unit', models.CharField(max_length=255, verbose_name='Единица измерение')),
                ('provider', models.CharField(max_length=255, verbose_name='Поставщик')),
                ('price', models.DecimalField(decimal_places=1, default=0, max_digits=10, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Карточка товара',
                'verbose_name_plural': 'Карточки товаров',
            },
        ),
    ]