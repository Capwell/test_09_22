from django.db import models


class User(models.Model):
    emali = models.EmailField(max_length=250)
