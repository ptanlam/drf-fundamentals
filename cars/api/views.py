from rest_framework.response import Response
from rest_framework.request import Request

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated


@api_view()
@permission_classes([IsAuthenticated])
def first_api_view(request: Request):
    print(request.query_params.get('q'))
    return Response({'message': 'first api view'})
