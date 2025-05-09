# Generated by Django 5.0.1 on 2024-01-18 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_alter_subscribe_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Logo', models.FileField(upload_to='Features/images')),
                ('Icon', models.FileField(upload_to='Features/icons')),
                ('icon_background', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('testimonial_description', models.TextField(max_length=255)),
                ('testimonial_author', models.CharField(max_length=255)),
                ('author_designation', models.CharField(max_length=255)),
                ('testimonial_logo', models.FileField(upload_to='Features/logos')),
            ],
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='image',
            new_name='Logo',
        ),
    ]
