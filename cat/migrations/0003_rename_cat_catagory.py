# Generated by Django 5.0.3 on 2024-03-19 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cat', '0002_alter_cat_slug'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cat',
            new_name='Catagory',
        ),
    ]