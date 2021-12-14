from django.contrib import admin
from Menú.models import Producto, CafePreparado, CafeGranel, Comida, Postres
from Inventario.models import Articulos
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nom_producto" , "precio_producto")
    search_fields = ("nom_producto" , "precio_producto")
admin.site.register(Producto, ProductoAdmin)

class CafePreparadoAdmin(admin.ModelAdmin):
    list_display = ("nom_cafe", "descripcion_cafe", "tipo_cafe")
admin.site.register(CafePreparado, CafePreparadoAdmin)


admin.site.register(CafeGranel)
admin.site.register(Comida)
admin.site.register(Postres)

