# Generated by Django 4.1.3 on 2023-01-03 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Data_Interaction', '0015_admininformation_avatar_admininformation_brandname_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bankinformation',
            old_name='AccountName',
            new_name='Account_Name',
        ),
    ]
