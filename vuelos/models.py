from django.db import models


class Areopuerto(models.Model):
    codigo = models.CharField(max_length=3)
    ciudad = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.ciudad} ({self.codigo})"


class Vuelo(models.Model):
    origen = models.ForeignKey(
        Areopuerto, on_delete=models.CASCADE, related_name="salida")
    destino = models.ForeignKey(
        Areopuerto, on_delete=models.CASCADE, related_name="llegadas")
    # origen = models.CharField(max_length=64)
    # destino = models.CharField(max_length=64)
    duracion = models.IntegerField(null=True)

    def __str__(self):
        return f" {self.origen} hasta {self.destino}"


class Pasajero(models.Model):
    nombre = models.CharField(max_length=64)
    apellidos = models.CharField(max_length=64)
    vuelo = models.ManyToManyField(Vuelo, blank=True, related_name="pasajeros")
    
    def __str__(self):
        return f"{self.nombre} ({self.apellidos})"
