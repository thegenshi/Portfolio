# Generated by Django 4.1.5 on 2023-01-06 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('og', '0002_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('discription', models.TextField()),
                ('image', models.ImageField(upload_to='static')),
                ('link', models.URLField()),
            ],
        ),
    ]
