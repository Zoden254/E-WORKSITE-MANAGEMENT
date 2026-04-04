from rest_framework import serializers
from management.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username','ID_number','phone_no', 'position', 'password', 'profile_pic')
        extra_kwargs = {
            'password' : {'write_only': True}
        }
    def create(self, validated_data):
        # This handles hashing automatically
        return User.objects.create_user(**validated_data)

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('department_name', 'HOD', 'job')

class PositionSerializer(serializers.ModelSerializer):
    foreman = UserSerializer(read_only=True)
    class Meta:
        model = Position
        fields = ['job_title', 'foreman', 'payment_basis', 'payment_amount']