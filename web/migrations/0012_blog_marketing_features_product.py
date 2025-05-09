# Generated by Django 5.0.1 on 2024-01-30 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_rename_is_featured_testimonial_is_featured'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.FileField(upload_to='blog/images')),
                ('Title', models.TextField(max_length=255)),
                ('Content_type', models.CharField(choices=[('webinar', 'Webinar'), ('report', 'Report'), ('blog_post', 'Blog_Post')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Marketing_features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='Marketing_features/')),
                ('title', models.TextField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='products/images')),
                ('title', models.TextField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('Logo', models.FileField(upload_to='products/logos')),
            ],
        ),
    ]
