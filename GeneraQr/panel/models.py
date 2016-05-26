from django.db import models


class Lista ( models.Model ) :
  nombre = models.CharField ( max_length=255 , help_text='Nombre Docente' )
  curso = models.CharField ( max_length=255 , help_text='Nombre Curso' )
  fecha = models.DateTimeField ( auto_now=True )
  status = models.IntegerField ( default=1 )

  def __unicode__ ( self ) :
    return self.nombre + ' - ' + self.curso
