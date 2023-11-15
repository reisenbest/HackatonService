# Generated by Django 4.2.6 on 2023-11-15 15:21

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PointCondition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Условие для изменения количества очков Score')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='PointConditionUserID', to=settings.AUTH_USER_MODEL, verbose_name='user_id')),
            ],
            options={
                'verbose_name': 'Условие начисления очков Score',
                'verbose_name_plural': 'Условие начисления очков Score',
            },
        ),
        migrations.CreateModel(
            name='HistoryPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='Количество очков')),
                ('created', models.DateTimeField(default=datetime.datetime.now, null=True, verbose_name='Время создания записи')),
                ('condition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conditionID', to='Score.pointcondition', unique=True, verbose_name='condition_id')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='HistoryPointUserID', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Запись об изменении очков у пользователя',
                'verbose_name_plural': 'Запись об изменении очков у пользователя',
            },
        ),
    ]
