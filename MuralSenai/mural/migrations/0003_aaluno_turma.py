# Generated by Django 5.1.3 on 2024-11-14 13:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mural', '0002_aturma_curso'),
    ]

    operations = [
        migrations.AddField(
            model_name='aaluno',
            name='turma',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mural.aturma'),
            preserve_default=False,
        ),
    ]