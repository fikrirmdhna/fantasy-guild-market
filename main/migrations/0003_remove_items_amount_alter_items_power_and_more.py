# Generated by Django 4.2.5 on 2023-09-13 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_items_delete_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='amount',
        ),
        migrations.AlterField(
            model_name='items',
            name='power',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='price',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
