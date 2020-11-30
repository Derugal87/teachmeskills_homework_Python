# Generated by Django 3.1.2 on 2020-11-30 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='reward_date',
            new_name='order_date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='salary',
        ),
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='employee',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='position',
            name='salary',
            field=models.FloatField(default=0.0),
        ),
    ]
