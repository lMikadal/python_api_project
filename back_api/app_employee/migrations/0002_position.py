# Generated by Django 4.2 on 2023-04-15 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=100)),
            ],
        ),
    ]