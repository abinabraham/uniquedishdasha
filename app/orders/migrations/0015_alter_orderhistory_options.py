# Generated by Django 3.2.8 on 2021-10-30 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_orderhistory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderhistory',
            options={'ordering': ['-pk'], 'verbose_name': 'Order History', 'verbose_name_plural': 'Order History'},
        ),
    ]