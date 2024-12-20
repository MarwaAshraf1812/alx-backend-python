from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
  user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  first_name = models.CharField(max_length=50, null=False)
  last_name = models.CharField(max_length=50, null=False)
  email = models.EmailField(unique=True, null=False)
  password_hash = models.CharField(max_length=128, null=False)
  phone_number = models.CharField(max_length=15, unique=True)
  role = models.CharField(max_length=50, choices=[('guest', 'Guest'), ('host', 'Host'), ('admin', 'Admin')], default='guest', null=False)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.email

class Conversation(models.Model):
  conversation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  participants_id = models.ForeignKey(User, related_name='conversations')
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"Conversation {self.conversation_id}"


class Message(models.Model):
  message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  conversation_id = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
  sender_id = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
  message_body = models.TextField()
  sent_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"Message {self.message_id}"
