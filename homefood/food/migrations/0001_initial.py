# Generated by Django 3.0.3 on 2020-05-09 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item_name', models.CharField(max_length=200)),
                ('Item_desc', models.CharField(max_length=200)),
                ('Item_price', models.IntegerField()),
                ('Item_image', models.CharField(default='https://www.google.com/url?sa=i&url=http%3A%2F%2Fchaysendo.com%2Fthuc-uong-162&psig=AOvVaw0svv7irjRzq-nhIkbJkkUz&ust=1589142336011000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCMiFn9XOp-kCFQAAAAAdAAAAABAI', max_length=500)),
            ],
        ),
    ]
