from rest_framework import viewsets,  status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Category, Restaurant, MenuItem, Order, Cart, CartItem
from .serializers import CategorySerializer, RestaurantSerializer, MenuItemSerializer, OrderSerializer, CartSerializer, CartItemSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# Get or create cart
class CartView(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart


# Add item to cart
class AddToCartView(generics.CreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        menu_item_id = request.data.get("menu_item")
        quantity = int(request.data.get("quantity", 1))
        cart, _ = Cart.objects.get_or_create(user=request.user)

        try:
            menu_item = MenuItem.objects.get(id=menu_item_id)
        except MenuItem.DoesNotExist:
            return Response({"error": "Menu item not found"}, status=404)

        # If item already in cart → update quantity
        cart_item, created = CartItem.objects.get_or_create(cart=cart, menu_item=menu_item)
        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity
        cart_item.save()

        return Response(CartSerializer(cart).data, status=200)


# Remove item from cart
class RemoveFromCartView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        item_id = kwargs.get("item_id")
        try:
            cart_item = CartItem.objects.get(id=item_id, cart__user=request.user)
            cart_item.delete()
            return Response({"message": "Item removed"}, status=200)
        except CartItem.DoesNotExist:
            return Response({"error": "Item not found"}, status=404)
