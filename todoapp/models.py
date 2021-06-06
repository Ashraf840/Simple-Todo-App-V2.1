# from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


# Create your models here.
class MyTodo(models.Model):
    task = models.CharField(max_length=50, blank=False, null=False)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True) 
    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True, null=True)
    last_updated_on = models.DateTimeField(verbose_name="Last modified on", auto_now=True, null=True)
    class Meta:
        db_table = "Todo List"      # Viewed the db table as subsequent from any db (sqlite3. mysql, postgresql)
        verbose_name_plural = "todo"    # Viewed from the django administration page

    def __str__(self):
        return self.task
