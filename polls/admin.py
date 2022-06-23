from django.contrib import admin

# Register your models here.

from .models import Question

# Registra na interface de admin o Question
admin.site.register(Question)