# Generated by Django 3.0.3 on 2020-05-13 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_item_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='Item_Type',
            field=models.CharField(default='Veg', max_length=50),
        ),
    ]
