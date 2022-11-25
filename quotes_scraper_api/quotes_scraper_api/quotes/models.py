from django.db import models

class Quote(models.Model):
    quote_text = models.CharField()
    quote_author = models.CharField(max_length = 100)
