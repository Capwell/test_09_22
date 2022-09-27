import imp
from django.views.generic.edit import CreateView

from .models import User


class UserCreateView(CreateView):
    model = User
    template_name = 'user/index.html'
    fields = ('email',)
