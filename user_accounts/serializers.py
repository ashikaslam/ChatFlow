


from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError  # Correct import
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name',]
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
        


class otp_taker(serializers.Serializer):  
    email = serializers.EmailField()
    otp = serializers.IntegerField()
    token1 =serializers.CharField()
    token2 =serializers.CharField()
    

class LoginSerializer(serializers.Serializer):  # 4
    email = serializers.EmailField(required=True)
    

class logoutSerializer(serializers.Serializer):  # 8
    refresh_token = serializers.CharField(write_only=True, required=True)
    