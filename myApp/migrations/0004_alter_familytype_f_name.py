# Generated by Django 4.0.4 on 2022-06-13 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_familytype_description_alter_familytype_f_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familytype',
            name='f_name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
