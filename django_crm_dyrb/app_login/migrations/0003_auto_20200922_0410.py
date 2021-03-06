# Generated by Django 3.0.6 on 2020-09-22 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_login', '0002_auto_20200920_1115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='representacion',
            name='idstuff_ventas',
        ),
        migrations.AlterField(
            model_name='contacto_cliente_representada',
            name='idcliente_representada',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_login.Cliente_Representada'),
        ),
        migrations.AlterField(
            model_name='contacto_representada',
            name='idrepresentada',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_login.Representada'),
        ),
        migrations.AlterField(
            model_name='representacion',
            name='idcliente_representada',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_login.Cliente_Representada'),
        ),
        migrations.AlterField(
            model_name='representacion',
            name='idrepresentada',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_login.Representada'),
        ),
        migrations.DeleteModel(
            name='stuff_ventas',
        ),
    ]
