from django.db import models

# Create your models here.

class ToDo(models.Model):
	Task = models.CharField(max_length=30)
	Description = models.CharField(max_length=100)


class MOVIESinfo(models.Model):
	title       = models.CharField(max_length = 120)  # max_length = required
	year        = models.DecimalField(decimal_places = 0, max_digits=2025)
	runtime_min = models.DecimalField(decimal_places = 2, max_digits=10000)
	genres      = models.TextField(default=True)
	language    = models.TextField(default = True)  # null=True, default=True
	imdb_rating = models.DecimalField(decimal_places = 1, max_digits=10)
	actors      = models.TextField(default = True)




