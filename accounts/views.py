from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User

from food.models import Cart, CartItem, MenuItem
from food.serializers import CartSerializer
from rest_framework.serializers import ModelSerializer


# -------- USER REGISTER --------
class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


# -------- CART ENDPOINTS --------
class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)


class AddToCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, menu_item_id):
        cart, created = Cart.objects.get_or_create(user=request.user)
        menu_item = MenuItem.objects.get(id=menu_item_id)

        cart_item, created = CartItem.objects.get_or_create(cart=cart, menu_item=menu_item)
        if not created:
            cart_item.quantity += 1
            cart_item.save()

        return Response({"message": f"{menu_item.name} added to cart"})


class RemoveFromCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, menu_item_id):
        cart = Cart.objects.get(user=request.user)
        try:
            cart_item = CartItem.objects.get(cart=cart, menu_item_id=menu_item_id)
            cart_item.delete()
            return Response({"message": "Item removed from cart"})
        except CartItem.DoesNotExist:
            return Response({"error": "Item not found in cart"}, status=status.HTTP_404_NOT_FOUND)
