# Generated by Django 4.1.3 on 2023-02-24 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data_Interaction', '0033_categoryproduct_name_english_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Two_factor_authentication',
            field=models.CharField(blank=True, default='OFF', max_length=200, null=True),
        ),
    ]