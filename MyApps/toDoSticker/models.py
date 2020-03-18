from django.db import models
from datetime import datetime
# Create your models here.
# The todolistitems consists of a char var (listItem) and a time object (time_limit)
class toDoListItems(models.Model):
    listItem = models.CharField(max_length=30)
    time_limit = models.TimeField('Until when')
    def __str__(self):
        return self.listItem + ' ' + self.time_limit.strftime('%H:%M')