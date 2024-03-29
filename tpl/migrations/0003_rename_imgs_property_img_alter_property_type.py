# Generated by Django 4.1.2 on 2023-05-16 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tpl', '0002_property_imgs_alter_property_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='imgs',
            new_name='img',
        ),
        migrations.AlterField(
            model_name='property',
            name='type',
            field=models.CharField(choices=[('re', 'Residence'), ('ro', 'Room'), ('fl', 'Flat')], default='ro', max_length=2),
        ),
    ]
