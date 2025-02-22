from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from .import models
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
#from friendship.models import Friendship
from extra_fruction import problem_solver
from django.contrib.auth import get_user_model
User = get_user_model()



class my_Profile_data(APIView):  
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            profile = request.user.profile
            serializer = serializers.myProfileSerializer(profile, many=False)
            return Response({'profile': serializer.data})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class my_Profile_data_update(APIView):  
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.myProfileUpdateSerializer
    def post(self, request, *args, **kwargs):
        try:
            user = request.user
            print("hello inside")
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            profile = request.user.profile
            first_name = serializer.validated_data['first_name']
            last_name = serializer.validated_data['last_name']
            image_url = serializer.validated_data['image_url']

            print(first_name,last_name,image_url)

            profile.profile_picture=image_url
            user.first_name=first_name
            user.last_name=last_name
            user.save()
            profile.save()
            
            return Response({'status':1})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

















# class Profile_data_1(APIView):  # small data
#     def get(self, request, *args, **kwargs):
#         posts = models.UserProfile.objects.all()[:50]
#         serializer = serializers.UserProfileSerializer_1(posts, many=True)
#         return Response({'all_posts': serializer.data})


# class user_Profile_data(APIView):   # mid
#     def get(self, request, id, *args, **kwargs):
#         try:
#             if models.UserProfile.objects.filter(id=id).exists():
#                 profile = models.UserProfile.objects.get(id=id)
#                 serializer = serializers.userProfileSerializer_2(
#                     profile, many=False)
#                 return Response({'profile': serializer.data})
#             return Response({"error": "no data found for the given request", "status": 0}, status=status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)









# class Add_profile_pic_during_register(APIView):   # high
#     authentication_classes = [JWTAuthentication, SessionAuthentication]
#     permission_classes = [IsAuthenticated]
#     serializer_class = serializers.addProfilePicSerializer_during_register

#     def post(self, request, *args, **kwargs):
#         print("hello auth")
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         try:
#             profile = request.user.profile
#             profile_pic = serializer.validated_data['profile_pic']
#             if profile_pic:
#                 profile.profile_picture = profile_pic
#                 profile.save()
#                 return Response({"message": "profile pic added", "status": 1}, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
