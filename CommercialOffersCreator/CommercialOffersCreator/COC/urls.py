from django.urls import path
from .views import *

urlpatterns = [
    path('customers', customers_list, name='customers_list_url'),
    path('customer/create/', CustomerCreate.as_view(), name='customer_create_url'),
    path('customer/<str:id>/', CustomerDetail.as_view(), name='customer_ditail_url'),
    path('customer/<str:id>/update', CustomerUpdate.as_view(), name='customer_update_url'),
    path('customer/<str:id>/delete', CustomerDelete.as_view(), name='customer_delete_url'),

    path('products', products_list, name='products_list_url'),
    path('product/create/', ProductCreate.as_view(), name='product_create_url'),
    path('product/<str:id>/', ProductDetail.as_view(), name='product_ditail_url'),
    path('product/<str:id>/update', ProductUpdate.as_view(), name='product_update_url'),
    path('product/<str:id>/delete', ProductDelete.as_view(), name='product_delete_url'),

    path('price_groups', price_groups_list, name='price_groups_list_url'),
    path('price_group/create/', PriceGroupCreate.as_view(), name='price_group_create_url'),
    path('price_group/<str:id>/', PriceGroupDetail.as_view(), name='price_group_ditail_url'),
    path('price_group/<str:id>/update', PriceGroupUpdate.as_view(), name='price_group_update_url'),
    path('price_group/<str:id>/delete', PriceGroupDelete.as_view(), name='price_group_delete_url'),

    path('price_group_discounts', price_group_discounts, name='price_group_discounts_list_url'),
    path('price_group_discount/create/', PriceGroupDiscountCreate.as_view(), name='price_group_discount_create_url'),
    path('price_group_discount/<str:id>/', PriceGroupDiscountDetail.as_view(), name='price_group_discount_ditail_url'),
    path('price_group_discount/<str:id>/update', PriceGroupDiscountUpdate.as_view(), name='price_group_discount_update_url'),
    path('price_group_discount/<str:id>/delete', PriceGroupDiscountDelete.as_view(), name='price_group_discount_delete_url'),

    path('', commercial_offers, name='commercial_offers_list_url'),
    path('commercial_offer/create/', CommercialOfferCreate.as_view(), name='commercial_offer_create_url'),
    path('commercial_offer/<str:id>/', CommercialOfferDetail.as_view(), name='commercial_offer_ditail_url'),
    path('commercial_offer/<str:id>/update', CommercialOfferUpdate.as_view(), name='commercial_offer_update_url'),
    path('commercial_offer/<str:id>/delete', CommercialOfferDelete.as_view(), name='commercial_offer_delete_url'),

    path('index/<str:id>/', index, name='get_pdf_url'),
    path('pdf_view/<str:id>/', ViewPDF.as_view(), name="pdf_view"),
    path('pdf_download/<str:id>/', DownloadPDF.as_view(), name="pdf_download"),
]
