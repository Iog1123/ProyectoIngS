from django.db import models


class AdminBodega(models.Model):
    id_admin = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'admin_bodega'


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    e_mail = models.CharField(db_column='e-mail', unique=True, max_length=70)  # Field renamed to remove unsuitable characters.
    nomb_user = models.CharField(unique=True, max_length=20)
    contraseña = models.CharField(max_length=10)
    fecha_registro = models.DateField()

    class Meta:
        managed = False
        db_table = 'cliente'


class FormaPago(models.Model):
    id_pago = models.CharField(primary_key=True, max_length=3)
    tipo_pago = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'forma_pago'


class Oferta(models.Model):
    id_oferta = models.AutoField(primary_key=True)
    nombre_ofert = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'oferta'


class Pedido(models.Model):
    cod_pedido = models.AutoField(primary_key=True)
    fecha_compra = models.DateField()
    fecha_entrega = models.DateField()
    cliente_id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente_id_cliente')
    forma_pago_id_pago = models.ForeignKey(FormaPago, models.DO_NOTHING, db_column='forma_pago_id_pago')

    class Meta:
        managed = False
        db_table = 'pedido'


class PedidoProducto(models.Model):
    pedido_cod_pedido = models.OneToOneField(Pedido, models.DO_NOTHING, db_column='pedido_cod_pedido', primary_key=True)
    producto_cod_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='producto_cod_producto')
    cant_producto = models.BigIntegerField()
    fecha_entrega = models.DateField()

    class Meta:
        managed = False
        db_table = 'pedido_producto'
        unique_together = (('pedido_cod_pedido', 'producto_cod_producto'),)


class Producto(models.Model):
    cod_prod = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    precio = models.BigIntegerField()
    categoria = models.CharField(max_length=40)
    marca = models.CharField(max_length=50, blank=True, null=True)
    stock = models.BigIntegerField()
    fech_registro = models.DateField()
    admin_bodega_id_admin = models.ForeignKey(AdminBodega, models.DO_NOTHING, db_column='admin_bodega_id_admin')

    class Meta:
        managed = False
        db_table = 'producto'


class ProductoOferta(models.Model):
    producto_cod_producto = models.OneToOneField(Producto, models.DO_NOTHING, db_column='producto_cod_producto', primary_key=True)
    oferta_id_oferta = models.ForeignKey(Oferta, models.DO_NOTHING, db_column='oferta_id_oferta')

    class Meta:
        managed = False
        db_table = 'producto_oferta'
        unique_together = (('producto_cod_producto', 'oferta_id_oferta'),)


class ProvProd(models.Model):
    producto_cod_prod = models.OneToOneField(Producto, models.DO_NOTHING, db_column='producto_cod_prod', primary_key=True)
    proveedor_id_prove = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='proveedor_id_prove')

    class Meta:
        managed = False
        db_table = 'prov_prod'
        unique_together = (('producto_cod_prod', 'proveedor_id_prove'),)


class Proveedor(models.Model):
    id_prove = models.AutoField(primary_key=True)
    razon_social = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'proveedor'


class SugCliente(models.Model):
    cliente_id_cliente = models.OneToOneField(Cliente, models.DO_NOTHING, db_column='cliente_id_cliente', primary_key=True)
    sugerencia_id_sugerencia = models.ForeignKey('Sugerencia', models.DO_NOTHING, db_column='sugerencia_id_sugerencia')
    nombre_producto = models.CharField(max_length=30)
    categoria_producto = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'sug_cliente'
        unique_together = (('cliente_id_cliente', 'sugerencia_id_sugerencia'),)


class Sugerencia(models.Model):
    id_sugerencia = models.AutoField(primary_key=True)
    fecha_registro = models.DateField()

    class Meta:
        managed = False
        db_table = 'sugerencia'
