from datetime import date
from django.db.models import Sum
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Sale
from .serializers import SaleSerializer

@api_view(['POST'])
def add_sale(request):
    serializer = SaleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def sales_report(request, report_date):
    report_date = date.fromisoformat(report_date)
    sales = Sale.objects.filter(date=report_date)
    total_sales = sum(s.product.price * s.quantity for s in sales)
    total_items_sold = sales.aggregate(total=Sum('quantity'))['total']

    top_product_data = (
        sales.values('product__name')
        .annotate(total_qty=Sum('quantity'))
        .order_by('-total_qty')
        .first()
    )
    top_product = top_product_data['product__name']
    report = {
        "date": str(report_date),
        "total_sales": total_sales,
        "total_items_sold": total_items_sold,
        "top_product": top_product
    }
    return Response(report)