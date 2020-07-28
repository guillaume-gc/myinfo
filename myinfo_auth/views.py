from django.urls import reverse_lazy
from django.views import generic

from myinfo_auth.forms import MyInfoUserCreationForm


class SignUp(generic.CreateView):
    form_class = MyInfoUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
