from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published') # 'date_published' não é obrigatorio

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # 'Question' referencia a classe 'Question', que será a tabela no sqlite
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) # 'default=0' começa sempre no zero