# Generated by Django 3.2.23 on 2023-12-05 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20231126_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='../profile_default_imagehome', upload_to='images/'),
        ),
    ]
