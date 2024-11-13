from django.db import models

# Create your models here.

class Utility(models.Model):
	name = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = "Utilities"
	
	def __str__(self):
		return self.name

class HostelMedia(models.Model):
	hostel = models.ForeignKey('Hostel', on_delete=models.CASCADE)
	video = models.FileField(upload_to='hostel_videos/')
	picture = models.ImageField(upload_to='hostel_pictures/')

	def __str__(self):
		return self.hostel.name + ' media.'


class Hostel(models.Model):
	name = models.CharField(max_length=200)
	property_size = models.CharField(max_length=200)
	distance_to_junction = models.CharField(max_length=500)
	utilities = models.ForeignKey('Utility', on_delete=models.CASCADE)
	picture1 = models.ImageField(upload_to='hostel_pictures/')
	picture2 = models.ImageField(upload_to='hostel_pictures/')
	picture3 = models.ImageField(upload_to='hostel_pictures/')
	picture4 = models.ImageField(upload_to='hostel_pictures/')
	picture5 = models.ImageField(upload_to='hostel_pictures/')
	more_media = models.ForeignKey('HostelMedia', related_name='get_hostels',  on_delete=models.CASCADE)

	
	def __str__(self):
		return self.name + ' hostel'