# Generated by Django 3.2.5 on 2021-07-24 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orders',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='receiver_address',
            new_name='receiver_addres',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='receiver',
            new_name='receiver_name',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='weigth',
            new_name='weight',
        ),
    ]
