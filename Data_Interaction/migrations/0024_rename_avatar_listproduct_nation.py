# Generated by Django 4.1.3 on 2023-01-06 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Data_Interaction', '0023_alter_bankinformation_short_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listproduct',
            old_name='Avatar',
            new_name='Nation',
        ),
    ]
