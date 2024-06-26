# Generated by Django 4.2.6 on 2024-01-31 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=30)),
                ('payroll', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mobile', models.BigIntegerField(blank=True, null=True)),
                ('password', models.CharField(max_length=20)),
                ('emp_joindate', models.DateField()),
                ('emp_skill', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=20)),
                ('price', models.BigIntegerField(blank=True, null=True)),
                ('weigth', models.BigIntegerField(max_length=20)),
                ('pro_img', models.ImageField(default='NULL', upload_to='pics')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
    ]
