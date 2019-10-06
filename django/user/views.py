from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView


class RegisterView(CreateView):
    template_name = 'templates/user/register.html'
    form_class = UserCreationForm
