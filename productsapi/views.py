from django.contrib.auth import authenticate
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.forms import UserCreationForm
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.authtoken.models import Token
from products.forms import CreateRecordForm, UpdateRecordForm
from rest_framework import serializers
from products.models import Record


# Register a User

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    form = UserCreationForm(data=request.data)
    if form.is_valid():
        user = form.save()
        return Response("Account created successfully", status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


# Login a User

@api_view(["POST"])
@permission_classes([AllowAny])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},status=status.HTTP_200_OK)


# User Logout

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response({'Message': 'You are logged out'},status=status.HTTP_200_OK)


# Create Record
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_product(request):
    form = CreateRecordForm(request.POST)
    if form.is_valid():
        product = form.save()
        return Response({'id': product.id}, status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


# Read Record

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_products(request):
    products = Record.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


# Update Record

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_product(request, pk):
    product = get_object_or_404(Record, pk=pk)
    form = UpdateRecordForm(request.data, instance=product)
    if form.is_valid():
        form.save()
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    else:
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    

# Delete Record
    
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_product(request, pk):
    try:
        product = Record.objects.get(pk=pk)
    except Record.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    product.delete()
    return Response("deleted successfully")


# Search

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_product(request):
    query = request.GET.get('find', '')
    products = Record.objects.filter(name__istartswith=query)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)