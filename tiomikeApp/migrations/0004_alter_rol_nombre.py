# Generated by Django 4.0.4 on 2022-06-01 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiomikeApp', '0003_rename_id_rol_idrol_rename_id_usuario_idusuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rol',
            name='nombre',
            field=models.CharField(max_length=30, unique=True, verbose_name='nombre'),
        ),
    ]