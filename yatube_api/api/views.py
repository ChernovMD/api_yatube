# api/views.py — ИСПРАВЛЕННАЯ ВЕРСИЯ ДЛЯ ПРОХОЖДЕНИЯ ТЕСТОВ

from rest_framework import viewsets, permissions

from posts.models import Post, Group, Comment
from .serializers import PostSerializer, CommentSerializer, GroupSerializer
from .permissions import IsOwnerOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # ❗ Только авторизованные могут что-то делать, включая GET
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    # ❗ То же самое
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post_id=post_id)

    def perform_create(self, serializer):
        post_id = self.kwargs['post_id']
        serializer.save(author=self.request.user, post_id=post_id)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # Группы тоже только для авторизованных
    permission_classes = [permissions.IsAuthenticated]
