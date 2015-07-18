from django.db import models
from django.contrib.auth.models import User

class WebUser(models.Model):
	user = models.OneToOneField(User)

	justATestString = models.CharField(max_length=128)

	def __unicode__(self):
		self.user.username