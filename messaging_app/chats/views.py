from rest_framework import viewsets, status
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer
from django_filters import rest_framework as filters
from .permissions import IsParticipant


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsParticipant]

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            return Conversation.objects.none()
        
        return Conversation.objects.filter(participants=user)

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsParticipant]

    def get_queryset(self):
        return Message.objects.filter(conversation__participants=self.request.user)