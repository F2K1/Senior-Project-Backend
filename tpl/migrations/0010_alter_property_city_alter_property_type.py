# Generated by Django 4.1.2 on 2023-05-16 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tpl', '0009_alter_property_city_alter_property_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='city',
            field=models.CharField(choices=[('brno-czech_republic', 'Brno'), ('prague-czech_republic', 'Prague'), ('tirana-albania', 'Tirana'), ('undefined', 'Undefined')], default='undefined', max_length=50),
        ),
        migrations.AlterField(
            model_name='property',
            name='type',
            field=models.CharField(choices=[('flat', 'Flat'), ('residence', 'Residence'), ('room', 'Room')], default='room', max_length=9),
        ),
    ]
