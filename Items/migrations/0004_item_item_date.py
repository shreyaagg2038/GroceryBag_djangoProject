# Generated by Django 3.2.9 on 2021-11-18 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Items', '0003_remove_item_item_added_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_date',
            field=models.DateField(null=True),
        ),
    ]
