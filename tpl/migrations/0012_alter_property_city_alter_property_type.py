# Generated by Django 4.1.2 on 2023-05-16 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tpl', '0011_alter_property_city_alter_property_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='city',
            field=models.CharField(choices=[('Brno', 'brno-czech_republic'), ('Prague', 'prague-czech_republic'), ('Tirana', 'tirana-albania'), ('Undefined', 'undefined')], default='Undefined', max_length=50),
        ),
        migrations.AlterField(
            model_name='property',
            name='type',
            field=models.CharField(choices=[('room', 'Room'), ('residence', 'Residence'), ('flat', 'Flat')], default='room', max_length=9),
        ),
    ]