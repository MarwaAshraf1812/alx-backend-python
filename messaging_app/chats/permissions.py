from rest_framework.permissions import BasePermission

class IsParticipant(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'participants'):
            # Check if the user is part of the participants in the conversation
            return request.user in obj.participants.all()

        if hasattr(obj, 'conversation'):
            # If the object has a 'conversation', check if the user is part of the conversation's participants
            return request.user in obj.conversation.participants.all()

        return False
