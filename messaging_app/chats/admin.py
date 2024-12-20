from django.contrib import admin
from .models import Conversation, Message, User

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ['conversation_id', 'created_at']

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['message_id', 'get_conversation', 'get_sender', 'sent_at']
    
    def get_conversation(self, obj):
        return obj.conversation.conversation_id
    
    def get_sender(self, obj):
        return f"{obj.sender.first_name} {obj.sender.last_name}"

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'email', 'first_name', 'last_name', 'role']
