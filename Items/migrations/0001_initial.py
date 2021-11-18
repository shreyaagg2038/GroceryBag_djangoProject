# Generated by Django 3.2.9 on 2021-11-17 15:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.TextField()),
                ('item_quantity', models.TextField()),
                ('item_added_on', models.DateTimeField(auto_now_add=True)),
                ('item_status', models.CharField(choices=[('PENDING', 'PENDING'), ('BOUGHT', 'BOUGHT'), ('NOT AVAILABLE', 'NOT AVAILABLE')], default='PENDING', max_length=100)),
                ('item_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
