from django.contrib import admin

# Register your models here.
from .models.usuario import Usuario
from .models.barrio import Barrio
from .models.departamento import Departamento
from .models.detalleFactura import DetalleFactura
from .models.proveedor import Proveedor
from .models.cita import Cita
from .models.estado import Estado
from .models.mascota import Mascota
from .models.tipoIdentificacion import TipoIdentificacion
from .models.raza import Raza
from .models.detalleCita import DetalleCita
from .models.producto import Producto
from .models.tipoProducto import TipoProducto
from .models.ciudad import Ciudad
from .models.cliente import Cliente
from .models.detalleMascota import DetalleMascota
from .models.factura import Factura
from .models.tamano import Tamano
from .models.genero import Genero
from .models.rol import Rol


admin.site.register(Usuario)
admin.site.register(Barrio)
admin.site.register(Departamento)
admin.site.register(DetalleFactura)
admin.site.register(Proveedor)
admin.site.register(Cita)
admin.site.register(Estado)
admin.site.register(Mascota)
admin.site.register(TipoIdentificacion)
admin.site.register(Raza)
admin.site.register(DetalleCita)
admin.site.register(Producto)
admin.site.register(TipoProducto)
admin.site.register(Ciudad)
admin.site.register(Cliente)
admin.site.register(DetalleMascota)
admin.site.register(Factura)
admin.site.register(Tamano)
admin.site.register(Genero)
admin.site.register(Rol)


