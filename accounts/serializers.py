from rest_framework import serializers
from accounts.models import member

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = member
        fields = ('reg_no', 'name', 'email', 'mob_no', 'dept', 'domain',  'password')
        extra_kwargs = {'password': {'write_only': True}}
        
        def create(self, validated_data):
            user = member.objects.create_user(validated_data['reg_no'], validated_data['name'], validated_data['email'],validated_data['mob_no'],validated_data['dept'], validated_data['domain'], validated_data['password'])
            return user