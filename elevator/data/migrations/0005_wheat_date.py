# Generated by Django 4.1.2 on 2022-12-02 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_alter_wheat_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='wheat',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
