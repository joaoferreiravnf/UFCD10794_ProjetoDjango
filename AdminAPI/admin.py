from django.contrib import admin

# Register your models here.
from AdminAPI.models import Aluno, Encarregadoeducacao, Local

admin.site.register(Aluno)
admin.site.register(Local)
admin.site.register(Encarregadoeducacao)