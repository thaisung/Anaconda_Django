# Generated by Django 4.1.3 on 2023-02-05 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data_Interaction', '0031_alter_user_options_user_total_amount_deducted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Avatar',
            field=models.ImageField(blank=True, null=True, upload_to='upload/User'),
        ),
    ]
