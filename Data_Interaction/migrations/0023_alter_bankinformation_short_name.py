# Generated by Django 4.1.3 on 2023-01-05 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data_Interaction', '0022_alter_bankinformation_api_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankinformation',
            name='Short_Name',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
    ]
