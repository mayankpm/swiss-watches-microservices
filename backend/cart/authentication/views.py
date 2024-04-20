# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Cart, Address
from .serializer import CartSerializer, AddressSerializer
from rest_framework import permissions, status
from decimal import Decimal


class CartList(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        cart_items = Cart.objects.all()
        serializer = CartSerializer(cart_items, many=True)

        total_price = sum(Decimal(item['price']) for item in serializer.data)
        for item in serializer.data:
            item['final_price'] = total_price

        return Response(serializer.data)

    def post(self, request):
        print(request.data)
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            # Extract product_id, brand, name, and price from the request data
            product_id = request.data.get('product_id')
            brand = request.data.get('brand')
            name = request.data.get('name')
            price = request.data.get('price')
            
            # Create the Cart instance with the product_id, brand, name, and price
            cart_item = Cart.objects.create(
                quantity=serializer.validated_data.get('quantity', 1),
                total_price=serializer.validated_data.get('total_price', Decimal('0.00')),
                user_id=serializer.validated_data.get('user_id', 1),
                product_id=product_id, # Use the product_id from the request data
                brand=brand,
                name=name,
                price=price
            )
            
            # Serialize the created cart item
            serializer = CartSerializer(cart_item)
            
            # Calculate final_price after the instance has been created
            total_price = Decimal(serializer.instance.total_price)
            final_price = total_price # Assuming final_price is the same as total_price for simplicity
            
            # Add final_price to the serialized data
            serializer.data['final_price'] = final_price

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddressList(APIView):
    def get(self, request):
        addresses = Address.objects.all()
        serializer = AddressSerializer(addresses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
