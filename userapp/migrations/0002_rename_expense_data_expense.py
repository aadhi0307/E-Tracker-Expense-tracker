# Generated by Django 3.2.10 on 2023-10-25 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='expense_data',
            new_name='expense',
        ),
    ]