# Generated by Django 3.2.14 on 2022-08-01 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_estadia_penalizacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reglamento',
            name='retiro_anticipado',
            field=models.DecimalField(decimal_places=2, max_digits=2, verbose_name='tasa'),
        ),
    ]
