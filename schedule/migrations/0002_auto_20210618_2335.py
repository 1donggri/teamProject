# Generated by Django 3.2.2 on 2021-06-18 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterModelTable(
            name='post',
            table='schedule',
        ),
    ]
