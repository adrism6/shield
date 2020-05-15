# Generated by Django 3.0.6 on 2020-05-06 15:22

from django.db import migrations
from django.utils.text import slugify


def update_slugs(apps, schema_editor):
    Team = apps.get_model("metahumans", "Team")

    for team in Team.objects.all():
        team.slug = slugify(team.name)
        team.save()


def undo_update_slugs(apps, schema_editor):
    Team = apps.get_model("metahumans", "Team")

    for team in Team.objects.all():
        team.slug = None
        team.save()

class Migration(migrations.Migration):

    dependencies = [
        ('metahumans', '0008_team_slug'),
    ]

    operations = [
        migrations.RunPython(update_slugs, undo_update_slugs)
    ]
