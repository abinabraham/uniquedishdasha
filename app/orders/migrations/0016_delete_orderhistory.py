# Generated by Django 3.2.8 on 2021-10-30 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_alter_orderhistory_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrderHistory',
        ),
    ]