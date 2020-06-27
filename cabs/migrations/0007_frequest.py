# Generated by Django 3.0.5 on 2020-04-23 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabs', '0006_post_pickup_from'),
    ]

    operations = [
        migrations.CreateModel(
            name='Frequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('by', models.CharField(max_length=100)),
                ('to', models.CharField(max_length=100)),
                ('accepted', models.BooleanField(default=False)),
                ('booking_id', models.IntegerField(default=0)),
            ],
        ),
    ]
