# Generated by Django 3.2.8 on 2021-10-29 21:58

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_pricingplans'),
    ]

    operations = [
        migrations.CreateModel(
            name='Measurements',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('collar', models.CharField(choices=[('C1', 'Collar1'), ('C2', 'Collar2'), ('C3', 'Collar3'), ('C4', 'Collar4')], default='C1', max_length=2)),
                ('zip', models.CharField(choices=[('Z1', 'Zip1'), ('Z2', 'Zip2'), ('Z3', 'Zip3'), ('Z4', 'Zip4')], default='Z1', max_length=2)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_measurement', to='orders.orderbook')),
            ],
            options={
                'verbose_name': 'Measurements',
                'verbose_name_plural': 'Measurement',
                'ordering': ['-id'],
            },
        ),
    ]