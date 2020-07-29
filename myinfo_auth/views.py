from django.http import Http404
from django.urls import reverse_lazy
from django.views import generic

from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.response import Response
from rest_framework.views import APIView

from myinfo_auth.forms import MyInfoUserCreationForm
from myinfo_auth.models import User
from myinfo_auth.serializers import UserSerializer

from rest_framework import viewsets, status


class SignUp(generic.CreateView):
    form_class = MyInfoUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        try:
            return request.user.is_superuser or obj == request.user
        except AttributeError:
            return request.user.is_superuser


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    user_lookup_kwarg = 'user'

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsOwnerOrAdmin]

        return [permission() for permission in permission_classes]

    # @action(detail=False)
    # def me(self, request, pk=None):
    #     user = User.objects.get(email=request.user.email)
    #
    #     serializer = self.get_serializer(user, many=False)
    #     return Response(serializer.data)
    #
    # @me.mapping.put
    # def me_put(self, request, pk=None):
    #     user = self.get_object()
    #     serializer = UserSerializer(data=request.data)
    #
    #     if serializer.is_valid():
    #         user.save()
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors,
    #                         status=status.HTTP_400_BAD_REQUEST)


class MeView(APIView):
    """
       Retrieve or update user own info
    """

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        permission_classes = [IsOwnerOrAdmin]

        return [permission() for permission in permission_classes]

    @staticmethod
    def get_object(request):
        try:
            return User.objects.get(email=request.user.email)
        except User.DoesNotExist:
            raise Http404

    def get(self, request):
        user = self.get_object(request)
        serializer = UserSerializer(user, context={'request': request})

        return Response(serializer.data)

    def put(self, request):
        user = self.get_object(request)
        serializer = UserSerializer(user, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
