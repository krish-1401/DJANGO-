# Generated by Django 4.2.3 on 2023-08-07 10:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('food', '0003_alter_item_item_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='user_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
