# Generated by Django 4.0.4 on 2022-06-14 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0008_progressstatestransalation_transalations_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='progressstate',
            old_name='languages',
            new_name='specifications',
        ),
    ]