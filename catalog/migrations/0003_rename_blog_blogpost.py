# Generated by Django 4.2.3 on 2023-08-19 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_blog'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Blog',
            new_name='BlogPost',
        ),
    ]
