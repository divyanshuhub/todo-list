from django.db import models
from django.utils import timezone
TIME_ZONE = 'Asia/Kolkata'
USE_TZ = True

class Todo(models.Model):
	title=models.CharField(max_length=100)
	details=models.TextField()
	date=models.DateTimeField(default=timezone.localtime(timezone.now()),blank=True)
	#date=models.DateTimeField(default=lambda: timezone.localtime(timezone.now()))
	def __str__(self):
		return self.title