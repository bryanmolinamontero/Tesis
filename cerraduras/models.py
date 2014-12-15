from django.contrib import admin
from django.db import models

# Create your models here.

class personal(models.Model):
    id_personal  = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=False, null=False)
    apellido = models.CharField(max_length=100, blank=False, null=False)
    username = models.CharField(max_length=100, blank=False, null=False)
    clave = models.CharField(max_length=100, blank=False, null=False)
    tipo = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        db_table = 'personal'

    def __unicode__(self):
        return '%d, %s, %s, %s, %s, %s ' % (self.id_personal, self.nombre, self.apellido, self.username, self.clave, self.tipo)

class personalAdmin(admin.ModelAdmin):
    list_display = ( 'id_personal', 'nombre' , 'apellido' , 'tipo')
    search_fields = ('nombre',)
admin.site.register(personal,personalAdmin)


class cerraduras(models.Model):
    id_cerradura = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=False, null=False)
    id_personal = models.ForeignKey('personal', db_column='id_personal')

    class Meta:
        db_table = 'cerraduras'

    def __unicode__(self):
        return '%d, %s, %s ' % (self.id_cerradura, self.nombre, self.id_personal)

class cerradurasAdmin(admin.ModelAdmin):
    list_display = ( 'id_cerradura', 'nombre' , 'id_personal')
    search_fields = ('nombre',)
admin.site.register(cerraduras,cerradurasAdmin)

class registros(models.Model):
    id_registro = models.AutoField(primary_key=True)
    puerta = models.CharField(max_length=100, blank=False, null=False)
    nombre_persona = models.CharField(max_length=100, blank=False, null=False)
    apellido_persona = models.CharField(max_length=100, blank=False, null=False)
    fecha  = models.DateTimeField(blank=False, null=False)


class registrosAdmin(admin.ModelAdmin):
    list_display = ( 'id_registro', 'puerta' , 'apellido_persona')
    search_fields = ('nombre_persona',)
admin.site.register(registros,registrosAdmin)
