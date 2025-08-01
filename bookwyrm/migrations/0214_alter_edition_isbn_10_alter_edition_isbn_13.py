# Generated by Django 4.2.20 on 2025-05-02 18:17

import bookwyrm.models.book
import bookwyrm.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bookwyrm", "0213_alter_user_preferred_timezone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="edition",
            name="isbn_10",
            field=bookwyrm.models.fields.CharField(
                blank=True,
                max_length=255,
                null=True,
                validators=[bookwyrm.models.book.validate_isbn10],
            ),
        ),
        migrations.AlterField(
            model_name="edition",
            name="isbn_13",
            field=bookwyrm.models.fields.CharField(
                blank=True,
                max_length=255,
                null=True,
                validators=[bookwyrm.models.book.validate_isbn13],
            ),
        ),
    ]
