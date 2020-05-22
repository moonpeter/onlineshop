from django.urls import path

from shop.views import product_in_category, product_detail

app_name = 'shop'

urlpatterns = [
    # 카테고리 선택이 없는 경우, 전체 제품을 노출
    path('', product_in_category, name='product_all'),
    # 카테고리 선택이 있는 경우, 해당 카테고리의 제품을 노출
    path('<slug:category_slug>/', product_in_category, name='product_in_category'),
    # 특정(id)의 상품의 상세페이
    path('<int:id>/<product_slug>/', product_detail, name='product_detail'),
]
