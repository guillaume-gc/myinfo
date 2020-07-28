from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class MyInfoUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('email',)


class MyInfoUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email',)