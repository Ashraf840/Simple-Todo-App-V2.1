from django.db import models


# Create your models here.
class MyTodo(models.Model):
    task = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        db_table = "Todo List"      # Viewed the db table as aforementioned from any db (sqlite3. mysql, postgresql)
        verbose_name_plural = "todo"    # Viewed from the django administration page

    def __str__(self):
        return self.task
