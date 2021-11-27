# Generated by Django 3.2.7 on 2021-11-27 01:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=15, unique=True, verbose_name='Username')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=20, verbose_name='Apellido')),
                ('password', models.CharField(max_length=256, verbose_name='Contraseña')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Email')),
                ('telefono', models.BigIntegerField(verbose_name='Telefono')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=25, verbose_name='Nombre')),
                ('caracteristica', models.TextField(verbose_name='Caracteristica')),
                ('precio', models.FloatField(verbose_name='precio')),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('cantidad', models.IntegerField()),
                ('total', models.FloatField()),
                ('productoFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='compra', to='aComprarApp.producto')),
                ('usuarioFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='compra', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
