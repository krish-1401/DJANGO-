# Generated by Django 4.2.3 on 2023-07-26 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT0oTZ787ETGsBQXUa0mAzoS3SR41X_rXdQnE2WqlP_&s', max_length=500),
        ),
    ]
