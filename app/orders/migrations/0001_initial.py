# Generated by Django 3.2.8 on 2021-10-29 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FabricType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Fabric Title')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Fabric Types',
                'verbose_name_plural': 'Fabric Type',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='TailoringStyle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Tailoring Title')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Tailoring Style',
                'verbose_name_plural': 'Tailoring Style',
                'ordering': ['-id'],
            },
        ),
    ]