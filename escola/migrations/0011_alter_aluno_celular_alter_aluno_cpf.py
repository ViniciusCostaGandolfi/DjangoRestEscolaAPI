# Generated by Django 4.1.5 on 2023-01-05 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0010_alter_aluno_celular'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='celular',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='cpf',
            field=models.CharField(max_length=14, unique=True),
        ),
    ]