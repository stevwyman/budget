# Generated by Django 5.1.7 on 2025-03-10 13:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("vmb", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="expenditureitem",
            name="project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="vmb.project"
            ),
        ),
    ]
