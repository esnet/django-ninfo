from ninfo import Ninfo
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class PluginViewSet(viewsets.ViewSet):
    """
    A simple ViewSet that for listing plugins
    """
    permission_classes=[IsAuthenticated]
    def list(self, request):
        P = Ninfo()
        data = plugins = [p.as_json() for p in P.plugins]
        data = {"plugins": plugins}
        return Response(data)
