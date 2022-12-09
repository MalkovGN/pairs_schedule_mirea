# Generated by Django 4.1.1 on 2022-12-09 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("schedule_app", "0003_pairmodel_remove_groupmodel_cabinet_number_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="daymodel", name="pair",),
        migrations.AddField(
            model_name="daymodel",
            name="pair",
            field=models.ManyToManyField(to="schedule_app.pairmodel"),
        ),
    ]