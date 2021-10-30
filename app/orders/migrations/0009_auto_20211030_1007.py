# Generated by Django 3.2.8 on 2021-10-30 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_measurements_finalstyle'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurements',
            name='bar',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Bar'),
        ),
        migrations.AddField(
            model_name='measurements',
            name='big_pocket',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Big Pocket'),
        ),
        migrations.AddField(
            model_name='measurements',
            name='fold_length',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Fold Length'),
        ),
        migrations.AddField(
            model_name='measurements',
            name='fold_width',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Fold Width'),
        ),
        migrations.AddField(
            model_name='measurements',
            name='front_chest',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Front Chest'),
        ),
        migrations.AddField(
            model_name='measurements',
            name='front_pocket',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Front Pocket'),
        ),
        migrations.AddField(
            model_name='measurements',
            name='length',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Length'),
        ),
        migrations.AddField(
            model_name='measurements',
            name='shoulder',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Size Collar'),
        ),
        migrations.AddField(
            model_name='measurements',
            name='size_collar',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Size Collar'),
        ),
        migrations.AddField(
            model_name='measurements',
            name='size_pocket',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Size Pocket'),
        ),
        migrations.AddField(
            model_name='measurements',
            name='sleeve_length',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Sleeve Length'),
        ),
        migrations.AddField(
            model_name='measurements',
            name='two_line',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Two Line'),
        ),
        migrations.AddField(
            model_name='measurements',
            name='width_collar',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Width Collar'),
        ),
    ]
