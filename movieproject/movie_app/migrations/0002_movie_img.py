# Generated by Django 5.0.1 on 2024-01-31 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='ddeg', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
