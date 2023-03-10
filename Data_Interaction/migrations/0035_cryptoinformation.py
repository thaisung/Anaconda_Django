# Generated by Django 4.1.3 on 2023-02-25 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data_Interaction', '0034_user_two_factor_authentication'),
    ]

    operations = [
        migrations.CreateModel(
            name='CryptoInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Crytop_Name', models.CharField(blank=True, max_length=100)),
                ('Wallet_Address', models.CharField(blank=True, max_length=100, unique=True)),
                ('Exchanges', models.CharField(blank=True, max_length=100, unique=True)),
                ('Avatar_QR_Code', models.ImageField(blank=True, null=True, upload_to='upload/Bank')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
