# Generated by Django 4.1.5 on 2023-01-05 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0005_alter_aluno_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='celular',
            field=models.CharField(default='', max_length=13),
        ),
    ]
