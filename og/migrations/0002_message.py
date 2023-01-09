# Generated by Django 4.1.5 on 2023-01-06 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('og', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('text', models.TextField(verbose_name='Сообщение')),
            ],
        ),
    ]