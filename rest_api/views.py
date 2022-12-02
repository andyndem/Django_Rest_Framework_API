# from django.shortcuts import render

# # Create your views here.
# # FUNCTION BASED API VIEWS 


# from rest_api.models import Post
# from rest_api.serializers import PostSerializer
# # below for MODEL SERIALIZERS
# # from django.http import JsonResponse, HttpResponse
# # from rest_framework.parsers import JSONParser
# # from django.views.decorators.csrf import csrf_exempt

# # using Function Based API_view with decorators
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status


# # @csrf_exempt
# @api_view(['GET'])
# def postView(request):

#   if request.method == 'GET':
#     posts = Post.objects.all() # queryset
#     serializer = PostSerializer(posts, many=True)
#     # return JsonResponse(serializer.data, safe=False)
#     return Response(serializer.data)

  

# @api_view(['POST'])
# def createView(request):
#   serializer = PostSerializer(data=request.data)
#   if serializer.is_valid():
#     serializer.save()
#     # return JsonResponse(serializer.data, status=201) 
#     #return JsonResponse(serializer.errors, status=400)  
#     return Response(serializer.data, status=status.HTTP_201_CREATED) 
#   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # @csrf_exempt
# @api_view(['GET', 'PUT', 'DELETE'])
# def post_details(request, pk):
  
#   try:
#     post = Post.objects.get(pk=pk)
#   except:
#       return Response({
#         'error': 'Page Does Not Exist'
#       }, status=status.HTTP_404_NOT_FOUND)


#   if request.method =='GET':
#     serializer =  PostSerializer(post)
#     #return JsonResponse(serializer.data)
#     return Response(serializer.data)
    
#   if request.method == 'PUT': 
#     #data = JSONParser().parse(request)
#     serializer = PostSerializer(post, data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       # return JsonResponse(serializer.data)
#       return Response(serializer.data)
#       # return JsonResponse(serializer.errors, status=400)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#   if request.method == 'DELETE':
#     post.delete()
#     return Response({'Info': 'Page Deleted'}, status=status.HTTP_204_NO_CONTENT)





# # ===========================================================

# using Class Based Views

from rest_framework.views import APIView
from rest_api.models import Post
from rest_api.serializers import PostSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class PostView(APIView):
  def get(self, request):
    posts = Post.objects.all() # queryset complex Data
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

# add quick test functionality to end point to perform post request
# def post(self, request):
#   return Response({
#     'hello': 'Welcome to Employee API'
#   })

class CreateView(APIView):
  def post(self, request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED) 
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PostDetails(APIView):

  def get_book_by_pk(self, pk):
    try:
      return Post.objects.get(pk=pk)
    except Post.DoesNotExist:
      raise Http404


  def get(self, request, pk, format=None):
    post = self.get_book_by_pk(pk)
    serializer =  PostSerializer(post)
    return Response(serializer.data)

      
  def put(self, request, pk, format=None):
    post = self.get_book_by_pk(pk)
    serializer = PostSerializer(post, data=request.data)
    if serializer.is_valid():
      serializer.save() 
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

  def delete(self, request, pk, format=None):
    post = self.get_book_by_pk(pk)
    post.delete()
    return Response({'Info': 'Page Deleted'}, status=status.HTTP_204_NO_CONTENT)

