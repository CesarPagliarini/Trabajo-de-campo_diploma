# Generated by Django 3.0.8 on 2022-07-24 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('habitaciones', '0004_auto_20220724_1826'),
        ('mainapp', '0004_auto_20220724_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estadia',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.EstadoEstadia', verbose_name='estado'),
        ),
        migrations.AlterField(
            model_name='estadia',
            name='habitacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='habitaciones.Habitacion', verbose_name='habitacion'),
        ),
    ]
