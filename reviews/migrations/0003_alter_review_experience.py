# Generated by Django 5.1.3 on 2024-12-19 04:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0004_alter_experience_category'),
        ('reviews', '0002_remove_review_payload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='experience',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to='experiences.experience'),
        ),
    ]