from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect

# Create your views here.


def home_page(request):
    return render(request, 'home.html')



class MyLoginView(LoginView):

    template_name = 'registration/login.html'

    def form_valid(self, form):
        """
        At this point the security check complete.
        The user gets logged in here the user in
        and custom code gets performed.
        """
        auth_login(self.request, form.get_user())

        return HttpResponseRedirect(self.get_success_url())

