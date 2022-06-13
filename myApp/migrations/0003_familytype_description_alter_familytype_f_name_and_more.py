# Generated by Django 4.0.4 on 2022-06-13 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_offer_calculation_offer_high_offer_low'),
    ]

    operations = [
        migrations.AddField(
            model_name='familytype',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='familytype',
            name='f_name',
            field=models.CharField(choices=[('1', 'Single Parent'), ('2', 'Couple')], default=1, max_length=200),
        ),
        migrations.AlterField(
            model_name='offer',
            name='calculation',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='offer',
            name='high',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='offer',
            name='low',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='progressstate',
            name='state_name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
