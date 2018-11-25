from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tables(models.Model):
	tabel_name = models.CharField(max_length=250, null=True, blank=True)
	tabel_capacity = models.IntegerField(null=True, blank=True)
	activeStatus = (
        (0, "created"),
        (1, "approved"),
    )
	status = models.IntegerField( choices= activeStatus, default=0, blank=True)
	image = models.ImageField(upload_to='profile_image', blank=True)
	def __unicode__(self):
		return self.tabel_name
	class Meta:
		verbose_name = "Table"
        verbose_name_plural = "Table"

class Reservations(models.Model):
	user_id = models.ForeignKey(User,null=True,blank=True)
	table_id = 	models.ForeignKey(Tables,null=True,blank=True)
	start_time = models.DateTimeField(auto_now_add=True)
	end_time = models.DateTimeField(auto_now_add=True)
	activeStatus = (
        (0, "created"),
        (1, "pending"),
        (2, "approved"),
    )
	reservation_status = models.IntegerField( choices= activeStatus, default=0, blank=True)
	def __unicode__(self):
		return self.table_id.tabel_name
	class Meta:
		verbose_name = "Reservation"
        verbose_name_plural = "Reservation"