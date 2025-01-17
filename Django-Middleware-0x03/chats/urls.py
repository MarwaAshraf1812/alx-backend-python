from django.urls import path, include
from rest_framework_nested import routers
from .views import ConversationViewSet, MessageViewSet

router = routers.DefaultRouter()

router.register(r'conversations', ConversationViewSet, basename='conversation')
'''
This feature allows you to structure URLs in a hierarchy
such as:
/api/conversations/
/api/conversations/<conversation_id>/messages/
'''
nested_router = routers.NestedDefaultRouter(router, r'conversations', lookup='conversation')
nested_router.register(r'messages', MessageViewSet, basename='conversation-messages')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(nested_router.urls)),
]
