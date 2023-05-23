from rest_framework.views import APIView
from rest_framework.response import Response

class CustomApiRootView(APIView):
    def get(self, request, format=None):
        # Custom logic to return your own API root
        data = {
            'message': 'Welcome to my API!',
            'endpoints': [
                '/my-endpoint/',
                '/another-endpoint/',
            ]
        }
        return Response(data)

