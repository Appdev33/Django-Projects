# Generated by Django 3.1.7 on 2021-04-04 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppExpenses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]