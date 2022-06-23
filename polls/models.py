from datetime import datetime, timezone
from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published') # 'date_published' não é obrigatorio

    # Para poder apresentar as 'Question' de forma mais específica
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # 'Question' referencia a classe 'Question', que será a tabela no sqlite
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) # 'default=0' começa sempre no zero

    def __str__(self):
        return self.choice_text