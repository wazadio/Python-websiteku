from django.db import models

# Create your models here.
class Tugas(models.Model):
	matakuliah = models.CharField(max_length=20)
	deskripsi = models.TextField()
	deadline = models.DateField()
	jam = models.CharField(max_length=10)

	def __str__(self):
		return self.matakuliah