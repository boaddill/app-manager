from django.db import models

class Quote(models.Model):
	"""docstring for invoice:"""
	quote_number  = models.CharField(max_length=200, blank=True)
