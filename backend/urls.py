from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from backend.features.views import FeatureViewSet

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from accounts.views import RegisterView

from food.views import CategoryViewSet, RestaurantViewSet, MenuItemViewSet, OrderViewSet, CartView, AddToCartView, RemoveFromCartView
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'features', FeatureViewSet, basename='feature')
router.register(r'categories', CategoryViewSet)
router.register(r'restaurants', RestaurantViewSet)
router.register(r'menu', MenuItemViewSet)
router.register(r'orders', OrderViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    # Authentication endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),   # login
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # refresh token
    path('api/register/', RegisterView.as_view(), name='register'),  
    path("cart/", CartView.as_view(), name="cart"),
    path("cart/add/", AddToCartView.as_view(), name="add-to-cart"),
    path("cart/remove/<int:item_id>/", RemoveFromCartView.as_view(), name="remove-from-cart"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
