# Generated by Django 4.0.1 on 2022-01-31 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]