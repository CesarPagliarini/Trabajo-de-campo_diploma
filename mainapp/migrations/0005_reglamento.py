# Generated by Django 3.2.14 on 2022-08-01 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20220726_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reglamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('retiro_anticipado', models.IntegerField()),
            ],
        ),
    ]
