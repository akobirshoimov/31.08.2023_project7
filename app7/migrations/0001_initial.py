# Generated by Django 3.2.20 on 2023-08-30 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ichimliklar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='coca cola', max_length=120)),
                ('hajmi', models.CharField(max_length=50)),
                ('narhi', models.IntegerField(default=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Korxona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=' ', max_length=140)),
                ('build_in', models.DateField(default='29-08-2023')),
            ],
        ),
    ]