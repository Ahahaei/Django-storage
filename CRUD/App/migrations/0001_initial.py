# Generated by Django 4.2.1 on 2023-06-03 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poduct',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('product', models.CharField(max_length=40)),
                ('purchase', models.CharField(max_length=40)),
                ('sale', models.CharField(max_length=10)),
                ('qty', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=1)),
                ('note', models.TextField()),
                ('created_At', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
