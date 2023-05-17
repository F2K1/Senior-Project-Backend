# Generated by Django 4.1.2 on 2023-05-16 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tpl', '0005_alter_property_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='city',
            field=models.CharField(choices=[('tirana', 'Tirana'), ('brno', 'Brno'), ('undefined', 'Undefined'), ('prague', 'Prague')], default='Undefined', max_length=12),
        ),
        migrations.AlterField(
            model_name='property',
            name='type',
            field=models.CharField(choices=[('flat', 'Flat'), ('residence', 'Residence'), ('room', 'Room')], default='room', max_length=9),
        ),
    ]