# Generated by Django 4.0.4 on 2022-05-29 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_remove_cadeira_docente_pratica_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadeira',
            name='docente_pratica',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='portfolio.professorpratica'),
        ),
        migrations.AddField(
            model_name='cadeira',
            name='docente_teorica',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='portfolio.professorteorica'),
        ),
    ]
