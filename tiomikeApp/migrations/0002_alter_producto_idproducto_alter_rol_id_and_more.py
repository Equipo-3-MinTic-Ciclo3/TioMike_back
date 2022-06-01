# Generated by Django 4.0.4 on 2022-06-01 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiomikeApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='idProducto',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='id_producto'),
        ),
        migrations.AlterField(
            model_name='rol',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='id_rol'),
        ),
        migrations.AlterField(
            model_name='tamano',
            name='descripcion',
            field=models.CharField(max_length=30, verbose_name='descripcion'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False, verbose_name='id_usuario'),
        ),
    ]