# Generated by Django 3.0.8 on 2022-06-26 23:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('huespedes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='huesped',
            name='user',
            field=models.ForeignKey(default=2, editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]
