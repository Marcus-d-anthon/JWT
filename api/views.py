from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Productos
from .serializer import ProductosSerializer, ProductosSerializerDTO

# Create your views here.
"""
Métodos HTTP en viewsets.ModelViewSet
    La clase ModelViewSet ya implementa los siguientes métodos:

    list() → Maneja GET para listar todos los registros.
    retrieve() → Maneja GET para obtener un solo registro por ID.
    create() → Maneja POST para crear un nuevo registro.
    update() → Maneja PUT para actualizar un registro completo.
    partial_update() → Maneja PATCH para actualizar parcialmente un registro.
    destroy() → Maneja DELETE para eliminar un registro.
"""
class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()

    def get_serializer_class(self):
        """
        Define qué serializador se usa dependiendo del método HTTP o la acción.
        """
        if self.action in ['list', 'destroy', 'update']:  # GET /productos/
            return ProductosSerializerDTO  # Muestra solo ciertos campos
        elif self.action == 'create':  # POST, PUT, PATCH
            return ProductosSerializer  # Muestra todos los campos
        return ProductosSerializer  # Por defecto, usa el serializador completo
    

    def list(self, request):
        productos = Productos.objects.all()
        serializer = ProductosSerializerDTO(productos, many= True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = ProductosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.erros, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None): #pk: es la clave primaria (id) del producto que se quiere actualizar.
        try:
            producto = Productos.objects.get(pk=pk)
            serializer = ProductosSerializer(producto, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Productos.DoesNotExist:
            return Response({"error": "Producto no Encontrado"}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        try:
            productos = Productos.objects.get(pk=pk)
            productos.delete()
            return Response({"Mensaje": "Producto ha sido eliminado"}, status=status.HTTP_200_OK)
        except Productos.DoesNotExist:
            return Response({"Error" : "El producto no existe"}, status=status.HTTP_400_BAD_REQUEST)