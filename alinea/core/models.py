from django.db import models

# Create your models here.

class CaruselLanding(models.Model):

    title = models.CharField(verbose_name="Título", max_length=200)
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    image = models.ImageField(verbose_name="Imagen", upload_to="Carrusel")
    text = models.CharField(verbose_name="Texto", max_length=200, blank=True)
    image_title = models.ImageField(verbose_name="Imagen de titulo", upload_to="Carrusel", blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Imagen del carrusel"
        verbose_name_plural = "Imagenes del carrusel"
        ordering = ['id']

    def __str__(self):
        return self.title

class Contact(models.Model):
   
    name= models.CharField(max_length=200, null=False, verbose_name="Nombre")
    mail= models.EmailField(max_length=200, null=False, verbose_name="Correo electrónico")
    phone= models.CharField(max_length=200, null=False, verbose_name="Número de teléfono")
    message= models.CharField(verbose_name="Mensaje", max_length=500)
    status=models.BooleanField(default=False, verbose_name="Contestado")
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"
        ordering = ["-created"]
        
                
    def __str__(self):
        return self.name

class what(models.Model):
   
    title= models.CharField(max_length=200, blank=True, verbose_name="Titulo")
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Que es"
        verbose_name_plural = "Que es"
        ordering = ["created"]
        
                
    def __str__(self):
        return self.title

class how(models.Model):
   
    title = models.CharField(verbose_name="Título", max_length=200, blank=True)
    text= models.TextField(max_length=200, blank=True, verbose_name="Información")
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Que hace"
        verbose_name_plural = "Que hace"
        ordering = ["-created"]
        
                
    def __str__(self):
        return self.title

class logos(models.Model):
   
    title = models.CharField(verbose_name="Título", max_length=200, blank=True)
    image = models.ImageField(verbose_name="Imagen", upload_to="Logo")
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Logo"
        verbose_name_plural = "Logo"
        ordering = ["created"]
        
                
    def __str__(self):
        return self.title


class Image(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='project_images/')

    class Meta:
        verbose_name = "Imagen"
        verbose_name_plural = "Imagenes"
        ordering = ["-title"]

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200, blank=True)
    images = models.ManyToManyField(Image, verbose_name="Imágenes")
    information = models.TextField(verbose_name="Información")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ["created"]

    def __str__(self):
        return self.title

