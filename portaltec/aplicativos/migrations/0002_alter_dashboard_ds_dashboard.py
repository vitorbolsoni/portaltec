# Generated by Django 4.1.1 on 2022-10-08 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicativos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard',
            name='ds_dashboard',
            field=models.CharField(max_length=40),
        ),
    ]
