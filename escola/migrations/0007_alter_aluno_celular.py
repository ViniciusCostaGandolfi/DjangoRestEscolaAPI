# Generated by Django 4.1.5 on 2023-01-05 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0006_aluno_celular'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='celular',
            field=models.CharField(max_length=13),
        ),
    ]