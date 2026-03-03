from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price
        }


@api_view()
def index(request):
    person = {
        "name": "Andrey",
        "age": 22,
    }
    return Response(person)


products = [
    Product(1, "Pen", 1.2),
    Product(2, "Copybook", 2.2),
    Product(3, "Book", 3.2),
]


class ProductAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = [product.to_dict() for product in products]
        return Response(data)

    def post(self, request, *args, **kwargs):
        data = request.data

        last_product = products[-1]
        l_id = last_product.id


        new_product = Product(id=l_id + 1, **data)
        products.append(new_product)

        return Response(new_product.to_dict())


class ProductProcessAPIView(APIView):

    def get(self, request, *args, **kwargs):

        product = None
        product_id = kwargs.get("pk")
        for prod in products:
            if prod.id == product_id:
                product = prod
                break

        if product is None:
            return Response({'detail': "Product not found"},
                            status=status.HTTP_404_NOT_FOUND)
        return Response(product.to_dict())


    def put(self, request, *args, **kwargs):

        product = None
        product_id = kwargs.get("pk")
        for prod in products:
            if prod.id == product_id:
                product = prod
                break

        if product is None:
            return Response({'detail': "Product not found"},
                            status=status.HTTP_404_NOT_FOUND)

        for key, value in request.data.items():
            setattr(product, key, value)

        return Response(product.to_dict())


    def patch(self, request, *args, **kwargs):
        product = None
        product_id = kwargs.get("pk")
        for prod in products:
            if prod.id == product_id:
                product = prod
                break

        if product is None:
            return Response({'detail': "Product not found"},
                            status=status.HTTP_404_NOT_FOUND)

        for key, value in request.data.items():
            setattr(product, key, value)

        return Response(product.to_dict())


    def delete(self, request, *args, **kwargs):

        product_id = kwargs.get("pk")
        searching_index = None
        for index, prod in enumerate(products):
            if prod.id == product_id:
                searching_index = index
                break

        if searching_index is None:
            return Response({'detail': "Product not found"},
                            status=status.HTTP_404_NOT_FOUND)

        product = products.pop(searching_index)
        return Response({
            'detail': "Product deleted",
            'product': product.to_dict()
        }, status=status.HTTP_204_NO_CONTENT)


