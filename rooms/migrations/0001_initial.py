# Generated by Django 5.1.3 on 2024-12-10 05:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('houses', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(default='대한민국', max_length=50)),
                ('city', models.CharField(default='서울', max_length=50)),
                ('price', models.PositiveIntegerField()),
                ('address', models.CharField(max_length=140)),
                ('bathrooms', models.FloatField()),
                ('bedrooms', models.PositiveIntegerField()),
                ('room_type', models.CharField(choices=[('Entire', '건물 전체'), ('Private', '개인실'), ('Shared', '다인실'), ('Hotel', 'Hotel')], max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='houses.house')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
