# Generated by Django 3.2.3 on 2021-06-16 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminBodega',
            fields=[
                ('id_admin', models.AutoField(primary_key=True, serialize=False)),
                ('rut', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'admin_bodega',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('e_mail', models.CharField(db_column='e-mail', max_length=70, unique=True)),
                ('nomb_user', models.CharField(max_length=20, unique=True)),
                ('contraseña', models.CharField(max_length=10)),
                ('fecha_registro', models.DateField()),
            ],
            options={
                'db_table': 'cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FormaPago',
            fields=[
                ('id_pago', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('tipo_pago', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'forma_pago',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id_oferta', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_ofert', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'oferta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('cod_pedido', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_compra', models.DateField()),
                ('fecha_entrega', models.DateField()),
            ],
            options={
                'db_table': 'pedido',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('cod_prod', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('precio', models.BigIntegerField()),
                ('categoria', models.CharField(max_length=40)),
                ('marca', models.CharField(blank=True, max_length=50, null=True)),
                ('stock', models.BigIntegerField()),
                ('fech_registro', models.DateField()),
            ],
            options={
                'db_table': 'producto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id_prove', models.AutoField(primary_key=True, serialize=False)),
                ('razon_social', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'proveedor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sugerencia',
            fields=[
                ('id_sugerencia', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_registro', models.DateField()),
            ],
            options={
                'db_table': 'sugerencia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PedidoProducto',
            fields=[
                ('pedido_cod_pedido', models.OneToOneField(db_column='pedido_cod_pedido', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='core.pedido')),
                ('cant_producto', models.BigIntegerField()),
                ('fecha_entrega', models.DateField()),
            ],
            options={
                'db_table': 'pedido_producto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductoOferta',
            fields=[
                ('producto_cod_producto', models.OneToOneField(db_column='producto_cod_producto', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='core.producto')),
            ],
            options={
                'db_table': 'producto_oferta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProvProd',
            fields=[
                ('producto_cod_prod', models.OneToOneField(db_column='producto_cod_prod', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='core.producto')),
            ],
            options={
                'db_table': 'prov_prod',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SugCliente',
            fields=[
                ('cliente_id_cliente', models.OneToOneField(db_column='cliente_id_cliente', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='core.cliente')),
                ('nombre_producto', models.CharField(max_length=30)),
                ('categoria_producto', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'sug_cliente',
                'managed': False,
            },
        ),
    ]
