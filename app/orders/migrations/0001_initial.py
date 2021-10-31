# Generated by Django 3.2.8 on 2021-10-31 20:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import simple_history.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FabricType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Fabric Title')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Fabric Types',
                'verbose_name_plural': 'Fabric Type',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Measurements',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('measure_id', models.CharField(blank=True, max_length=100, null=True, verbose_name='Measurement ID')),
                ('collar', models.CharField(choices=[('C1', 'Collar1'), ('C2', 'Collar2'), ('C3', 'Collar3'), ('C4', 'Collar4')], default='C1', max_length=2)),
                ('zip', models.CharField(choices=[('Z1', 'Zip1'), ('Z2', 'Zip2'), ('Z3', 'Zip3'), ('Z4', 'Zip4')], default='Z1', max_length=2)),
                ('pocket', models.CharField(choices=[('P1', 'Pocket1'), ('P2', 'Pocket2'), ('P3', 'Pocket3'), ('P4', 'Pocket4')], default='P1', max_length=2)),
                ('pockettwo', models.CharField(choices=[('P21', 'PocketTwo1'), ('P22', 'PocketTwo2'), ('P23', 'PocketTwo3'), ('P24', 'PocketTwo4'), ('P25', 'PocketTwo5'), ('P26', 'PocketTwo6')], default='P21', max_length=5)),
                ('tie', models.CharField(choices=[('T1', 'Tie1'), ('T2', 'Tie2'), ('T3', 'Tie3'), ('T4', 'Tie4'), ('T5', 'Tie5'), ('T6', 'Tie6'), ('T7', 'Tie7'), ('T8', 'Tie8'), ('T9', 'Tie9')], default='T1', max_length=5)),
                ('penpocket', models.CharField(choices=[('PP1', 'PenPocket1'), ('PP2', 'PenPocket2'), ('PP3', 'PenPocket3'), ('PP4', 'PenPocket4'), ('PP5', 'PenPocket5'), ('PP6', 'PenPocket6')], default='PP1', max_length=5)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sholderOne', models.CharField(blank=True, max_length=50, null=True, verbose_name='Shoulder One')),
                ('sholderTwo', models.CharField(blank=True, max_length=50, null=True, verbose_name='Shoulder Two')),
                ('mainWidth', models.CharField(blank=True, max_length=50, null=True, verbose_name='Main Width')),
                ('penPocket_select', models.CharField(blank=True, max_length=50, null=True, verbose_name='Pen Pocket')),
                ('insidePocket', models.CharField(blank=True, max_length=50, null=True, verbose_name='Inside Pocket')),
                ('handSize', models.CharField(blank=True, max_length=50, null=True, verbose_name='Hand Size')),
                ('cufflink', models.CharField(choices=[('CL1', 'Cufflink1'), ('CL2', 'Cufflink2'), ('CL3', 'Cufflink3'), ('CL4', 'Cufflink4'), ('CL5', 'Cufflink5'), ('CL6', 'Cufflink6'), ('CL7', 'Cufflink7'), ('CL8', 'Cufflink8')], default='CL1', max_length=5)),
                ('insidepocketshape', models.CharField(choices=[('IPS1', 'InsidePocketShape1'), ('IPS2', 'InsidePocketShape2')], default='IPS1', max_length=5)),
                ('button', models.CharField(choices=[('BTN1', 'Button1'), ('BTN2', 'Button2')], default='BTN1', max_length=5)),
                ('finalstyle', models.CharField(choices=[('FS1', 'FinalStyle1'), ('FS2', 'FinalStyle2')], default='FS1', max_length=5)),
                ('width_collar', models.CharField(blank=True, max_length=50, null=True, verbose_name='Width Collar')),
                ('size_collar', models.CharField(blank=True, max_length=50, null=True, verbose_name='Size Collar')),
                ('shoulder', models.CharField(blank=True, max_length=50, null=True, verbose_name='Size Collar')),
                ('front_chest', models.CharField(blank=True, max_length=50, null=True, verbose_name='Front Chest')),
                ('bar', models.CharField(blank=True, max_length=50, null=True, verbose_name='Bar')),
                ('sleeve_length', models.CharField(blank=True, max_length=50, null=True, verbose_name='Sleeve Length')),
                ('front_pocket', models.CharField(blank=True, max_length=50, null=True, verbose_name='Front Pocket')),
                ('size_pocket', models.CharField(blank=True, max_length=50, null=True, verbose_name='Size Pocket')),
                ('big_pocket', models.CharField(blank=True, max_length=50, null=True, verbose_name='Big Pocket')),
                ('fold_width', models.CharField(blank=True, max_length=50, null=True, verbose_name='Fold Width')),
                ('fold_length', models.CharField(blank=True, max_length=50, null=True, verbose_name='Fold Length')),
                ('two_line', models.CharField(blank=True, max_length=50, null=True, verbose_name='Two Line')),
                ('length', models.CharField(blank=True, max_length=50, null=True, verbose_name='Length')),
                ('color', models.CharField(blank=True, max_length=50, null=True, verbose_name='Color')),
                ('total_meters', models.CharField(blank=True, max_length=50, null=True, verbose_name='Total Meters')),
                ('fb_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fbrc_typ', to='orders.fabrictype')),
            ],
            options={
                'verbose_name': 'Measurements',
                'verbose_name_plural': 'Measurement',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='OrderBook',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('order_id', models.CharField(blank=True, max_length=100, null=True, verbose_name='Order ID')),
                ('is_customer_own_fabric', models.BooleanField(default=True)),
                ('quantity', models.CharField(blank=True, max_length=50, null=True, verbose_name='Quantity')),
                ('deliver_at', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_branch', to='accounts.branch')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_customer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Order Book',
                'verbose_name_plural': 'Order Book',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='TailoringStyle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Tailoring Title')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Tailoring Style',
                'verbose_name_plural': 'Tailoring Style',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='PricingPlansFabricTyp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Single Order Amount')),
                ('country', django_countries.fields.CountryField(default='KW', max_length=2)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('fabr_typ', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fabr_type_payment', to='orders.fabrictype')),
            ],
            options={
                'verbose_name': 'Pricing Plans Fabric Type',
                'verbose_name_plural': 'Pricing Plans Fabric Type',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='PricingPlans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Single Order Amount')),
                ('country', django_countries.fields.CountryField(default='KW', max_length=2)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tailr_styl', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tailr_styl_payment', to='orders.tailoringstyle')),
            ],
            options={
                'verbose_name': 'Pricing plans',
                'verbose_name_plural': 'Pricing plans',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('order_id', models.CharField(blank=True, max_length=100, null=True, verbose_name='Order ID')),
                ('total_amnt_to_pay', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Total Amount to Pay')),
                ('total_paid_amount', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Total Amount Paid')),
                ('balance_amount', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Balance Amount')),
                ('order_status', models.CharField(choices=[('OS1', 'Ordered'), ('OS2', 'COMPLETED'), ('OS3', 'DELIVERED')], default='OS1', max_length=5)),
                ('payment_status', models.CharField(choices=[('PS1', 'NOT PAID'), ('PS2', 'PARTIALLY PAID'), ('PS3', 'FULLY PAID'), ('PS4', 'OVERPAID')], default='PS1', max_length=5)),
                ('payment_method', models.CharField(choices=[('PM1', 'CASH'), ('PM2', 'CREDIT CARD'), ('PM3', 'DEBIT CARD'), ('PM4', 'PAY LATER')], default='PM1', max_length=5)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_order_customer', to=settings.AUTH_USER_MODEL)),
                ('measurements', models.ManyToManyField(to='orders.Measurements')),
                ('orders', models.ManyToManyField(to='orders.OrderBook')),
            ],
            options={
                'verbose_name': 'Complete Order',
                'verbose_name_plural': 'Complete Order',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='measurements',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_measurement', to='orders.orderbook'),
        ),
        migrations.AddField(
            model_name='measurements',
            name='tailr_styl',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tailr_styl', to='orders.tailoringstyle'),
        ),
        migrations.CreateModel(
            name='HistoricalOrders',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('order_id', models.CharField(blank=True, max_length=100, null=True, verbose_name='Order ID')),
                ('total_amnt_to_pay', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Total Amount to Pay')),
                ('total_paid_amount', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Total Amount Paid')),
                ('balance_amount', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Balance Amount')),
                ('order_status', models.CharField(choices=[('OS1', 'Ordered'), ('OS2', 'COMPLETED'), ('OS3', 'DELIVERED')], default='OS1', max_length=5)),
                ('payment_status', models.CharField(choices=[('PS1', 'NOT PAID'), ('PS2', 'PARTIALLY PAID'), ('PS3', 'FULLY PAID'), ('PS4', 'OVERPAID')], default='PS1', max_length=5)),
                ('payment_method', models.CharField(choices=[('PM1', 'CASH'), ('PM2', 'CREDIT CARD'), ('PM3', 'DEBIT CARD'), ('PM4', 'PAY LATER')], default='PM1', max_length=5)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(blank=True, editable=False)),
                ('updated_at', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('customer', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Complete Order',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
