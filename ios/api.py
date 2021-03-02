from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets

from ios.models import Os
from ios.serializers import OsSerializers
from itorre.settings import STATIC_ROOT


class OsViewSet(viewsets.ModelViewSet):
    #permission_classes = () para caso queira liberar da segurança JWT
    print(str(STATIC_ROOT))
    print('tew')
    serializer_class = OsSerializers
    queryset = Os.objects.all()