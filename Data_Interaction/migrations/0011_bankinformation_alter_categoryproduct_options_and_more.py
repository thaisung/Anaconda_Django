# Generated by Django 4.1.3 on 2023-01-02 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data_Interaction', '0010_alter_personaltransactionhistory_codeorders'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AccountName', models.CharField(blank=True, max_length=100, unique=True)),
                ('AccountNumber', models.IntegerField(blank=True, default=0, unique=True)),
                ('BankName', models.CharField(blank=True, max_length=100, unique=True)),
                ('QRCodeLink', models.CharField(blank=True, max_length=100, unique=True)),
                ('MainColor', models.CharField(blank=True, max_length=100, unique=True)),
                ('Active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='categoryproduct',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='listproduct',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='personaltransactionhistory',
            options={'ordering': ['-id']},
        ),
    ]