# Generated by Django 3.2.8 on 2021-10-30 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20211030_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurements',
            name='finalstyle',
            field=models.CharField(choices=[('FS1', 'FinalStyle1'), ('FS2', 'FinalStyle2')], default='FS1', max_length=5),
        ),
    ]
