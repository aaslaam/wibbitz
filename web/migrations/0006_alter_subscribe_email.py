# Generated by Django 5.0.1 on 2024-01-17 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_rename_email_subscribe_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribe',
            name='Email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
    ]
