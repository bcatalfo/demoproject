# Generated by Django 4.1.7 on 2023-03-16 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("demoapp", "0004_person_age"),
    ]

    operations = [
        migrations.CreateModel(
            name="MenuCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("menu_category_name", models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name="menu",
            name="category_id",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.PROTECT,
                to="demoapp.menucategory",
            ),
        ),
    ]