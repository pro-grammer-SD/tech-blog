# Generated by Django 5.1.7 on 2025-03-13 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='Enter title here...')),
                ('desc', models.TextField(default='Enter description here...')),
                ('price', models.FloatField()),
            ],
        ),
    ]
