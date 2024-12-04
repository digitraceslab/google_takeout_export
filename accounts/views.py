from .models import User
from django.views.generic import DetailView

class UserProfileDetailView(DetailView):
    model = User
    template_name = 'accounts/profile.html'

    def get_object(self):
        return self.request.user
