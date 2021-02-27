from django.db.models.signals import pre_save
from django.dispatch import Signal

from ios.models import Os

#mesma coisa que eventos mas se chama signals
def prioridade_up(sender,instance,**kwargs):
        os =instance
        os.prioridade = '3'


pre_save.connect(prioridade_up,sender=Os)
sinal_novo = Signal()