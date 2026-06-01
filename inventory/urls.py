from django.urls import path

from .views import (
    inventory_list,
  
    add_stock,
    remove_stock,
    stock_history,shopping_list,expiry_alerts,analytics_dashboard
    ,ai_predictions,inventory_api,shopping_list_api,admin_inventory_api
)


urlpatterns = [

    path('',inventory_list,name='inventory_list'),
   
    path('add/<int:pk>/',add_stock,name='add_stock'),
    path( 'remove/<int:pk>/', remove_stock, name='remove_stock'),
    path('history/',stock_history,name='stock_history'),
    path('shopping-list/',shopping_list,name='shopping_list'),
    path( 'expiry-alerts/', expiry_alerts, name='expiry_alerts'),
    path('analytics/',analytics_dashboard,name='analytics_dashboard'),
    path( 'ai-predictions/', ai_predictions, name='ai_predictions'),
   
    
    path('api/inventory/',inventory_api,name='inventory_api'),
    path( 'api/shopping-list/', shopping_list_api, name='shopping_list_api'),
    path('api/admin-inventory/',admin_inventory_api,name='admin_inventory_api'),
]