# Generated by Django 2.0.7 on 2019-03-28 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_content_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
    ]