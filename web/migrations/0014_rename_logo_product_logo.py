# Generated by Django 5.0.1 on 2024-02-01 00:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_alter_blog_title_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Logo',
            new_name='logo',
        ),
    ]
