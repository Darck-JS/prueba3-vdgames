# Generated by Django 4.1.2 on 2024-06-28 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_registro_colaborador_id_indie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='indie',
            name='id_indie',
        ),
        migrations.RemoveField(
            model_name='registro_colaborador',
            name='id_indie',
        ),
        migrations.AddField(
            model_name='indie',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='indie',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.registro_colaborador'),
            preserve_default=False,
        ),
    ]
