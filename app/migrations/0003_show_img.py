# Generated by Django 3.2.4 on 2021-06-22 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_show_release'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
    ]