# Generated by Django 5.0 on 2024-01-30 13:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0003_advocate_company"),
    ]

    operations = [
        migrations.AddField(
            model_name="advocate",
            name="name",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name="advocate",
            name="profile_pic",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="advocate",
            name="twitter",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="advocate",
            name="username",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]