# Generated by Django 4.1.3 on 2023-01-02 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data_Interaction', '0013_alter_bankinformation_accountname'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankinformation',
            name='Avatar',
            field=models.ImageField(blank=True, null=True, upload_to='upload/Bank'),
        ),
    ]
