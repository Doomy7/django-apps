# Generated by Django 3.0.4 on 2020-03-18 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='toDoListItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listItem', models.CharField(max_length=30)),
                ('time_limit', models.TimeField(verbose_name='Until when')),
            ],
        ),
    ]