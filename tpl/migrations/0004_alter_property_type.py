# Generated by Django 4.1.2 on 2023-05-16 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tpl', '0003_rename_imgs_property_img_alter_property_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='type',
            field=models.CharField(choices=[('ro', 'Room'), ('re', 'Residence'), ('fl', 'Flat')], default='ro', max_length=2),
        ),
    ]
