from django.shortcuts import render

# Create your views here.
from estore.models import products
from rest_framework.views import APIView
from rest_framework.response import Response


class ProductView(APIView):
    def get(self,request,*args,**kwargs):
        if "price" in request.query_params:
            id=int(request.query_params.get("price"))
            data=[product for product in products if product["price"]>100]
            return Response(data=data)
        return Response(data=products)
    def post(self,request,*args,**kwargs):
        data=request.data
        products.append(data)
        return Response(data=products)
class ProductDetailsView(APIView):
    def get(self,request,*args,**kwargs):
        pid=kwargs.get("pid")
        product=[product for product in products if product["id"]==pid].pop()
        return Response(data=product)

