# Generated by Django 3.2.14 on 2022-08-01 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_alter_reglamento_retiro_anticipado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estadia',
            name='penalizacion',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=2, null=True, verbose_name='penalizacion'),
        ),
    ]
