from django.urls import reverse_lazy
from django.views import generic
from rest_framework.permissions import IsAuthenticated, BasePermission

from myinfo_auth.forms import MyInfoUserCreationForm
from myinfo_auth.models import User
from myinfo_auth.serializers import UserSerializer

from rest_framework import viewsets


class SignUp(generic.CreateView):
    form_class = MyInfoUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    user_lookup_kwarg = 'user'

    class IsOwnerOrAdmin(BasePermission):
        def has_object_permission(self, request, view, obj):
            try:
                return request.user.is_superuser or obj == request.user
            except AttributeError:
                return request.user.is_superuser

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [self.IsOwnerOrAdmin]

        return [permission() for permission in permission_classes]