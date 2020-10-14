# Generated by Django 3.0.6 on 2020-10-10 16:51

from django.db import migrations, models
import phone_field.models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('mvp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente_representada',
            name='nivel_cliente',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F')], default=None, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente_representada',
            name='tipo_cliente',
            field=models.CharField(choices=[('AP', 'Almacén Papelería'), ('AR', 'Almacén Regalo'), ('AM', 'Almacén Multiprecio'), ('AA', 'Almacén Amarillo'), ('AJ', 'Almacén Juguetes'), ('SC', 'Suministrador Colegios'), ('SO', 'Suministrador de Oficinas'), ('DP', 'Detall Papeleria'), ('DB', 'Detall Bellas Artes'), ('DA', 'Detall Amarillo'), ('DR', 'Detall Regalo'), ('DJ', 'Detall Juguetes')], default=None, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='representada',
            name='logo',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='cliente_representada',
            name='telefono_corp_1',
            field=phone_field.models.PhoneField(blank=True, help_text='Teléfono cliente fijo 1', max_length=31),
        ),
        migrations.AlterField(
            model_name='cliente_representada',
            name='telefono_corp_2',
            field=phone_field.models.PhoneField(blank=True, help_text='Teléfono cliente fijo 2', max_length=31),
        ),
        migrations.AlterField(
            model_name='contacto_cliente_representada',
            name='telefono_movil',
            field=phone_field.models.PhoneField(blank=True, help_text='Móvil del contacto', max_length=31),
        ),
        migrations.AlterField(
            model_name='contacto_representada',
            name='telefono_movil',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Móvil del Contacto', max_length=9, region=None),
        ),
        migrations.AlterField(
            model_name='representada',
            name='telefono_corp_1',
            field=phone_field.models.PhoneField(blank=True, help_text='Teléfono fijo empresa 1', max_length=31),
        ),
        migrations.AlterField(
            model_name='representada',
            name='telefono_corp_2',
            field=phone_field.models.PhoneField(blank=True, help_text='Teléfono fijo empresa 2', max_length=31),
        ),
        migrations.AlterField(
            model_name='staff_ventas',
            name='telefono_movil',
            field=phone_field.models.PhoneField(blank=True, help_text='Móvil del contacto', max_length=31),
        ),
    ]