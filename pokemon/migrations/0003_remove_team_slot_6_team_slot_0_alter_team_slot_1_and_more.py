# Generated by Django 4.1 on 2022-08-10 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0002_alter_team_slot_1_alter_team_slot_2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='slot_6',
        ),
        migrations.AddField(
            model_name='team',
            name='slot_0',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='team',
            name='slot_1',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='team',
            name='slot_2',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='team',
            name='slot_3',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='team',
            name='slot_4',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='team',
            name='slot_5',
            field=models.IntegerField(default=25),
        ),
    ]