# Generated by Django 4.2.19 on 2025-02-23 16:52

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ImageFile",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("file", models.FileField(upload_to="images/")),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
