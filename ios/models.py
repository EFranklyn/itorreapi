from django.db import models
from django.db.models.signals import post_save,pre_save

PRIORIDADE = (
        ('1', 'Baixa'),
        ('2', 'Média'),
        ('3', 'Alta')
    )

class ControletempMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    class Meta:
        abstract = True


class Os(ControletempMixin,models.Model):
    servico    = models.CharField(max_length=10)
    descricao  = models.CharField(max_length=50)
    detalhes   =  models.CharField(max_length=255)
    prioridade = models.CharField(max_length=2, choices=PRIORIDADE)  # usar choices
    user = models.ForeignKey('auth.User',on_delete = models.PROTECT)
'''
    @classmethod
    def prioridade_up(self,sender,instance,**kwargs):
        os =instance
        os.prioridade = '3'


pre_save.connect(Os.prioridade_up,sender=Os)'''