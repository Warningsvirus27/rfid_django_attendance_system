# Generated by Django 3.2.4 on 2021-06-09 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_alter_register_tag_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='area',
            field=models.CharField(choices=[('Computer Lab 1-a', 'Computer Lab 1-a'), ('Computer Lab 1-b', 'Computer Lab 1-b'), ('Computer Lab 2-a', 'Computer Lab 2-a'), ('Computer Lab 2-b', 'Computer Lab 2-b'), ('Computer Lab 3-a', 'Computer Lab 3-a'), ('Computer Lab 3-b', 'Computer Lab 3-b'), ('Computer Lab 4-a', 'Computer Lab 4-a'), ('Computer Lab 4-b', 'Computer Lab 4-b'), ('Electronics lab', 'Electronics lab'), ('Sports Room', 'Sports Room'), ('Library', 'Library')], max_length=40),
        ),
    ]
