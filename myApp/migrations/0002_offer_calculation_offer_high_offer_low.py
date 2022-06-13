# Generated by Django 4.0.4 on 2022-06-13 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='calculation',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offer',
            name='high',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offer',
            name='low',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]