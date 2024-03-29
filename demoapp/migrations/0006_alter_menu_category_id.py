# Generated by Django 4.1.7 on 2023-03-16 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("demoapp", "0005_menucategory_menu_category_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="menu",
            name="category_id",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="category_name",
                to="demoapp.menucategory",
            ),
        ),
    ]
