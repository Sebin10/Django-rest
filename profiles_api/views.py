from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    def get(self,request,format=None):
        an_apiview=['Uses HTTP method as function(get,post,patch,put,update,delete)','Is similar to traditional Django view',
        'Gives you the most Control','Is mapped manually',]


        return Response({'message':'Hello','an_apiview':an_apiview})
