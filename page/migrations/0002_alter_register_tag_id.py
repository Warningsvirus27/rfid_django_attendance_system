# Generated by Django 3.2.4 on 2021-06-09 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='tag_id',
            field=models.CharField(max_length=15, primary_key=True, serialize=False, unique=True),
        ),
    ]
