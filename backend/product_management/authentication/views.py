from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Watch
from .producer import publish
from .serializer import WatchSerializer

class WatchList(APIView):
    def get(self, request):
        watches = Watch.objects.all()
        serializer = WatchSerializer(watches, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = WatchSerializer(data=request.data)
        publish()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddToCart(APIView):
    def post(self, request):
        watch_id = request.data.get('watch_id')
        if not watch_id:
            return Response({"error": "Watch ID is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            watch = Watch.objects.get(id=watch_id)
        except Watch.DoesNotExist:
            return Response({"error": "Watch not found."}, status=status.HTTP_404_NOT_FOUND)
        
        # Trigger the publish function with the watch ID
        publish(watch_id)
        
        return Response({"message": f"Watch {watch_id} added to cart."}, status=status.HTTP_200_OK)