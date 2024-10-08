from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Category, Product
from products.serializers import CategorySerializer, ProductSerializer

@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all().order_by('popularity')
    # print(categories.query)
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)



@api_view(['GET', 'POST'])
def product_list(request):
    """
    List all  products, or create a new product.
    """
    if request.method == 'GET':
        category_id = request.GET.get('category_id')
        if category_id:
            # Get the category object
            category = Category.objects.get(id=category_id)        
            # Filter products that belong to the selected category
            products = Product.objects.filter(category=category)
        else:
            products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, id):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        products = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(products)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductSerializer(products, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        products.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# @api_view(['GET', 'POST'])
# def category_list(request):
#     """
#     List all categories, or create a new category.
#     """
#     if request.method == 'GET':
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, id):
    """
    Retrieve, update or delete a category.
    """
    try:
        category = Category.objects.get(pk=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)