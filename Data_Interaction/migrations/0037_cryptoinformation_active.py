# Generated by Django 4.1.3 on 2023-02-25 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data_Interaction', '0036_cryptoinformation_avatar_logo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cryptoinformation',
            name='Active',
            field=models.BooleanField(default=True),
        ),
    ]
