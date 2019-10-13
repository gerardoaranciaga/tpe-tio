from django.db import models
import datetime
from django.db.models.signals import post_save, pre_save, post_delete, pre_delete
#import select2.fields
#import select2.models

from django.db.models import IntegerField, Case, Value, When, Sum, Max
from django.http import HttpResponseRedirect
from datetime import datetime
from django.dispatch import receiver

# Create your models here.
# Generar cambios en el Corredor
class Corredor(models.Model):
	numero_corredor = models.CharField(u'Numero Corredor', max_length=10,blank=True, default='')
	#numero_corredor = models.PositiveIntegerField( verbose_name='ID')
	apellido = models.CharField(u'Apellido', max_length=70)
	nombre = models.CharField(u'Nombre', max_length=70)
	provincia = models.CharField(u'Provincia', max_length=150, blank=True, default='')
	localidad = models.CharField(u'Localidad', max_length=150, blank=True, default='')
	direccion = models.CharField(u'Direccion', max_length=150, blank=True, default='')
	codigo_postal = models.IntegerField(u'Codigo Postal', blank=True, null=True)
	email = models.CharField(u'E-mail', max_length=100, blank=True, default='')
	telefono = models.CharField(u'Telefono', max_length=50, blank=True, default='')
	observaciones = models.TextField(u'Observaciones', blank=True, default=u'')

	def __unicode__(self):
		return u'{0}  {1} , ( {2} )'.format(self.apellido,self.nombre,self.numero_corredor)



def tiempo():
	now = datetime.now()
	return now

class Vuelta(models.Model):
	numero_corredor = models.ForeignKey(Corredor,blank=True, null=True) 
	vuelta = models.DateTimeField(u'Vuelta',default=tiempo)

	def __unicode__(self):	
		return u'{0} {1}'.format(self.numero_corredor,self.vuelta)

def actividad_en_progreso (num_corre):
	if Actividad.objects.filter(numero_corredor=num_corre).exists():
		act = Actividad.objects.filter(numero_corredor=num_corre)
		for ac in act:
			if ac.fin_actividad is None:
				return True

		return False

#  Preguntar si el corredor tiene una actividad en progreso
@receiver(pre_save,sender=Vuelta)
def vuelta_pre_save (sender,instance, *args, **kwargs):
	if not actividad_en_progreso(instance.numero_corredor):
		raise Exception('ESTE CORREDOR NO TIENE ACTIVDAD INICIADA')


@receiver(post_save,sender=Vuelta)	# Asignar la vuelta al corredor en su actividad
def vuelta_post_save(sender,instance, *args, **kwargs):
	act = Actividad.objects.filter(numero_corredor=instance.numero_corredor)
	for a in act:
			if a.fin_actividad is None :
				a.vuelta = instance
				#a.fin_actividad = tiempo
				a.save()
				#a.fin_actividad = None
				#a.save()





class Actividad(models.Model):
	inicio_actividad = models.DateTimeField(u'Inicio Actividad',default=tiempo)
	numero_corredor = models.ForeignKey(Corredor,blank=True, null=True)
	fin_actividad = models.DateTimeField(u'Fin Actividad',null=True, blank=True)
	#promedio = models.TimeField(u'Promedio Actividad',)
	vuelta = models.ForeignKey(Vuelta,blank=True, null=True)

	def __unicode__(self):	
		return u'{0} ,  tiempo {1}'.format(self.numero_corredor,self.inicio_actividad)


@receiver(pre_save,sender=Actividad)
def actividad_pre_save(sender, instance, **kwargs):
	
	if instance._state.adding is True:
		if Actividad.objects.filter(numero_corredor=instance.numero_corredor).exists() :
			act = Actividad.objects.filter(numero_corredor=instance.numero_corredor)
			for a in act:
				if a.fin_actividad is None : 
					if instance.fin_actividad is None :
						raise Exception('NO SE PUEDE GENERAR PORQUE NO TERMINO SU ACTIVIDAD ANTERIOR')

				else :
					print "El corredor TERMINO SU ACTIVIDAD PUEDE GUARDAR"

	
