# Generated by Django 4.1.3 on 2023-02-24 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data_Interaction', '0032_alter_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoryproduct',
            name='Name_English',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='listproduct',
            name='Name_English',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='Password_Level_2',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
