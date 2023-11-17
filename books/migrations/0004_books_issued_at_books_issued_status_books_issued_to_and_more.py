# Generated by Django 4.1.1 on 2022-09-20 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("books", "0003_issued_books_issued_at_issued_books_issued_status")]

    operations = [
        migrations.AddField(
            model_name="books",
            name="issued_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="books",
            name="issued_status",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name="books",
            name="issued_to",
            field=models.CharField(blank=True, default=None, max_length=60, null=True),
        ),
        migrations.DeleteModel(name="issued_books"),
    ]
