# Generated by Django 2.1.1 on 2019-09-15 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0003_auto_20190913_2221'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=255)),
                ('notes', models.CharField(max_length=255)),
            ],
        ),
    ]
