# Generated by Django 3.2.11 on 2022-03-09 20:54

from django.db import migrations

import poc_django.users.managers


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_user_id"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="user",
            managers=[
                ("objects", poc_django.users.managers.UserManager()),
            ],
        ),
    ]