from rest_framework import serializers
from .models import User, Conversation, Message


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name', read_only=True)
    class Meta:
        model = User
        fields = ['user_id', 'email', 'first_name',
                  'last_name', 'full_name', 'phone_number', 'role']
        read_only_fields = ['user_id', 'created_at']

class MessageSerializer(serializers.ModelSerializer):
    # Nested UserSerializer to include sender information
    sender = UserSerializer()
    formatted_sent_at = serializers.SerializerMethodField()
    class Meta:
        model = Message
        fields = ['message_id', 'sender', 'message_body',
                  'sent_at', 'formatted_sent_at']
        read_only_fields = ['message_id','sent_at']

    def get_formatted_sent_at(self, obj):
        return obj.sent_at.strftime("%Y-%m-%d %H:%M:%S")
    
    def validate(self, data):
        if 'message_body' not in data or data['message_body'] == '':
            raise serializers.ValidationError("Message body cannot be empty")
        return data

class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)
    # participants_count = serializers.SerializerMethodField()
    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'messages', 'created_at']
    
    # def get_participants(self, obj):
    #   return obj.participants.count()