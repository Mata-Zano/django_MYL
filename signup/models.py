from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class compra(models.Model):
    nombre_producto = models.CharField(max_length=200)
    cantidad = models.IntegerField()
    direccion = models.CharField(max_length=200)
    numero_telefono = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.DateTimeField(null=True)

    def __str__(self):
        return "Cliente : "+self.user.username +", Producto : "+ self.nombre_producto +", Cantidad : "+ str(self.cantidad)