# Generated by Django 4.1.2 on 2023-05-16 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tpl', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='imgs',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]