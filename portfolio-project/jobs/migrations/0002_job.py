# Generated by Django 3.2.8 on 2023-07-11 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hobbies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('summary', models.CharField(max_length=200)),
            ],
        ),
    ]