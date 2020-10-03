from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect, reverse
from .models import Post
from .serializers import PostSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, \
    HTTP_201_CREATED, HTTP_200_OK, HTTP_400_BAD_REQUEST



class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def list(self, request):
        queryset = Post.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=HTTP_201_CREATED, headers=headers)

    def update(self, request, pk):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, pk):
        instance = self.get_object()
        instance.delete()
        return Response(HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['post', 'put'])
    def upvote(self, request, pk=None):
        post = self.get_object()
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            post.upvote()
            post.save()
            return Response({'status':'Post Upvoted'})
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post', 'put'])
    def downvote(self, request, pk=None):
        post = self.get_object()
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            post.downvote()
            post.save()
            return Response({'status': 'Post Downvoted'})
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @action(detail=False)
    def boasts(self, request):
        boasts = Post.objects.filter(post_type='Boast')
        serializer = self.get_serializer(boasts, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def roasts(self, request):
        roasts = Post.objects.filter(post_type='Roast')
        serializer = self.get_serializer(roasts, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def popular(self, request):
        popular = Post.objects.all().order_by("-total_votes")
        serializer = self.get_serializer(popular, many=True)
        return Response(serializer.data)
