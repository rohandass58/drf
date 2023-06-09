# Generated by Django 4.1.7 on 2023-04-05 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                ("name", models.CharField(max_length=50)),
                ("mobile", models.IntegerField(max_length=12)),
                ("email", models.EmailField(max_length=254)),
                ("address", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("pid", models.IntegerField(primary_key=True, serialize=False)),
                ("pname", models.CharField(max_length=50)),
                ("stock", models.IntegerField()),
                ("quantity", models.IntegerField()),
                ("mrp", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="api.customer",
                    ),
                ),
                ("address", models.CharField(max_length=100)),
                ("amount", models.PositiveIntegerField()),
                ("date", models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name="customer",
            name="c_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="api.product"
            ),
        ),
        migrations.CreateModel(
            name="OrderDetails",
            fields=[
                (
                    "id",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="api.order",
                    ),
                ),
                ("order_id", models.CharField(max_length=100)),
                ("price", models.IntegerField()),
                ("quantity", models.IntegerField()),
            ],
        ),
    ]
