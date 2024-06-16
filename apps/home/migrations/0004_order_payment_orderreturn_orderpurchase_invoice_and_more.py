# Generated by Django 4.2.6 on 2024-02-28 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_customer_id_alter_employee_id_alter_product_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20)),
                ('amuont', models.DecimalField(decimal_places=2, max_digits=10)),
                ('custid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.customer')),
                ('proid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.product')),
            ],
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(default='COD', max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('orderid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.order')),
            ],
        ),
        migrations.CreateModel(
            name='orderreturn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('orderid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.order')),
            ],
        ),
        migrations.CreateModel(
            name='orderpurchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('proid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.product')),
            ],
        ),
        migrations.CreateModel(
            name='invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(default='COD', max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('custid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.customer')),
                ('orderid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.order')),
            ],
        ),
        migrations.CreateModel(
            name='inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mfgdate', models.DateField()),
                ('qty', models.BigIntegerField(blank=True, null=True)),
                ('batchno', models.BigIntegerField(blank=True, null=True)),
                ('proid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.product')),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=100)),
                ('custid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.customer')),
            ],
        ),
    ]
