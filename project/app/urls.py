from django.urls import path
from . import views

urlpatterns = [
    path('sales/', views.add_sale, name='add_sale'),
    path('sales/report/<report_date>/', views.sales_report, name='sales_report')

]