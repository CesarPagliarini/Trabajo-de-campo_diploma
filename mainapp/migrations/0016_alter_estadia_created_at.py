# Generated by Django 3.2.14 on 2022-08-08 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_estadia_user_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estadia',
            name='created_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Creado'),
        ),
    ]
