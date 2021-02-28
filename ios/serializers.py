from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from ios.models import Os




class UserSerializers(serializers.ModelSerializer):
    #s - serializers.SlugRelatedField(queryset=Os.objects.all())

    class Meta:
        model = User
        fields = ('username','first_name')

class OsSerializers(serializers.ModelSerializer):
    #s - serializers.SlugRelatedField(queryset=Os.objects.all())
    user = UserSerializers(read_only=True)
    user_put = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),write_only=True,source='user')
    class Meta:
        model = Os
        fields = ('id','servico','descricao','valor','status','detalhes','prioridade',
                  'created_at','updated_at','user','user_put')
        #fields = '__all__'