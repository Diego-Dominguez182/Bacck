from django.db import models

class Build(models.Model):
    champion_name = models.CharField(max_length=100)
    item_1 = models.CharField(max_length=100)
    item_2 = models.CharField(max_length=100)
    item_3 = models.CharField(max_length=100)
    item_4 = models.CharField(max_length=100)
    item_5 = models.CharField(max_length=100)
    item_6 = models.CharField(max_length=100)

    class Meta:
        db_table = 'builds'  

