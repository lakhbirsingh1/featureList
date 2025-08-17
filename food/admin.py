from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Restaurant, MenuItem, Order, OrderItem, Cart, CartItem

# -------------------------
# Category
# -------------------------
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "image_preview")

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 50px; height: 50px; object-fit: cover;" />',
                obj.image.url,
            )
        return "No Image"

    image_preview.short_description = "Image"


# -------------------------
# Restaurant
# -------------------------
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "image_preview")
    list_filter = ("category",)
    search_fields = ("name",)

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 50px; height: 50px; object-fit: cover;" />',
                obj.image.url,
            )
        return "No Image"

    image_preview.short_description = "Image"


# -------------------------
# Menu Item
# -------------------------
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("name", "restaurant", "price", "image_preview")
    list_filter = ("restaurant",)
    search_fields = ("name",)

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 50px; height: 50px; object-fit: cover;" />',
                obj.image.url,
            )
        return "No Image"

    image_preview.short_description = "Image"


# -------------------------
# Order
# -------------------------
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "restaurant", "status", "total_price", "created_at")
    list_filter = ("status", "restaurant")
    search_fields = ("user__username",)
    inlines = [OrderItemInline]


# -------------------------
# Cart
# -------------------------
class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1


class CartAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "total_price")
    inlines = [CartItemInline]


# -------------------------
# Register Models
# -------------------------
admin.site.register(Category, CategoryAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Cart, CartAdmin)
