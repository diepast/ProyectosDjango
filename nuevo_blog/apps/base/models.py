from django.db import models
from ckeditor.fields import RichTextField


class ModeloBase(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.BooleanField('Estado', default=True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now_add=True)
    fecha_modificacion = models.DateField(
        'Fecha de Modificación', auto_now=True, auto_now_add=False)
    fecha_eliminacion = models.DateField(
        'Fecha de Eliminación', auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True


class Categoria(ModeloBase):
    nombre = models.CharField('Nombre de la Categoria',
                              max_length=100, unique=True)
    imagen_referencial = models.ImageField(
        'Imagen Referencial', upload_to='categoria/')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre


class Autor(ModeloBase):
    nombre = models.CharField('Nombre', max_length=100)
    apellido = models.CharField('Apellido', max_length=100)
    email = models.EmailField('E-mail', max_length=100)
    descripcion = models.TextField('Descripción')
    web = models.URLField('Web', null=True, blank=True)
    facebook = models.URLField('Facebook', null=True, blank=True)
    twitter = models.URLField('Twitter', null=True, blank=True)
    instagram = models.URLField('Instagram', null=True, blank=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return '{0}.{1}'.format(self.apellido, self.nombre)


class Post(ModeloBase):
    titulo = models.CharField('Titulo del Post', max_length=150, unique=True)
    slug = models.CharField('Slug', max_length=150, unique=True)
    descripcion = models.TextField('Descripción')
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    contenido = RichTextField()
    imagen_referencial = models.ImageField(
        'Imagen referencial', upload_to='imagenes/', max_length=200)
    publicado = models.BooleanField('Publicado / No Publicado', default=False)
    fecha_publicacion = models.DateField('Fecha de Publicación')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo


class web(ModeloBase):
    nosotros = models.TextField('Nosotros')
    email = models.EmailField('E-mail', max_length=100)
    web = models.URLField('Web', null=True, blank=True)

    class Meta:
        verbose_name = 'Web'
        verbose_name_plural = 'Webs'

    def __str__(self):
        return self.nosotros


class RedesSociales(ModeloBase):
    facebook = models.URLField('Facebook')
    twitter = models.URLField('Twitter')
    instagram = models.URLField('Instagram')

    class Meta:
        verbose_name = 'Red Social'
        verbose_name_plural = 'Redes Sociales'

    def __str__(self):
        return self.facebook


class Contacto(ModeloBase):
    nombre = models.CharField('Nombre', max_length=100)
    apellido = models.CharField('Apellido', max_length=100)
    email = models.EmailField('E-mail', max_length=100)
    asunto = models.CharField('Asunto', max_length=100)
    mensaje = models.TextField('Mensaje')

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

    def __str__(self):
        return self.asunto


class Subscriptor(ModeloBase):
    email = models.EmailField('E-mail', max_length=100)

    class Meta:
        verbose_name = 'Subscriptor'
        verbose_name_plural = 'Subscriptores'

    def __str__(self):
        return self.email
