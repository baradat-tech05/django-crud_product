from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..model.serializers import ProductSerializer
from product.service.product_service import ProductService


class ProductListCreateView(APIView):
    def get(self, request):
        products = ProductService.list_products()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        product = ProductService.create_product(**serializer.validated_data)
        return Response(ProductSerializer(product).data, status=status.HTTP_201_CREATED)
    
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..model.models import Product
from ..model.serializers import ProductSerializer

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    # UPDATE (Actualizar)
    if request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    # DELETE (Eliminar)
    elif request.method == 'DELETE':
        product.delete()
        return Response({'message': 'Producto eliminado correctamente'}, status=200)
    
    # GET individual
    elif request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)