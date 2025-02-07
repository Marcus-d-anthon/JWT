from rest_framework import serializers
from .models import Productos

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'

class ProductosSerializerDTO(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = ['Nombre', 'Categoria','Marca']