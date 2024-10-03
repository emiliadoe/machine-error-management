from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect
from django.db.models import Q
from .forms import SearchForm, MachineForm
from .models import Machine
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView



# Create your views here.


def home_page(request):
    q = request.GET.get('q')
    if q:
        results = Machine.objects.filter(name__icontains=q)
    else:
        results = None
    
    return render(request, 'home.html', {'results': results})

    if request.method == 'POST':

        search_name = request.POST['name']
        search_description = request.POST['description']
        machines_found = Machine.objects.filter(
            Q(title__contains=search_name)
            & Q(description__contains=search_description)
        )
        form_in_function_based_view = SearchForm()
        context = {
            'show_search_results': True,
            'form': form_in_function_based_view,
            'machines_found': machines_found
        }
    else:  # GET
        form_in_function_based_view = SearchForm()
        context = {
            'show_search_results': False,
            'form': form_in_function_based_view,
        }
    return render(request, 'home.html', context)

def overview_list(request):
    machines = Machine.objects.all()
    context = {'all_machines': machines}
    return render(request, 'overview.html', context)


def machine_detail(request, **kwargs):
    product_id = kwargs['pk']  
    current_machine = get_object_or_404(Machine, id=product_id)
    current_user = request.user

    context = {
        'single_machine': current_machine,
    }

    return render(request, 'machine_detail.html', context)


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


class MachineEditView(UpdateView):
    model = Machine
    form_class = MachineForm
    template_name = 'edit_details.html'
    success_url = reverse_lazy('home')

class MachineAddView(CreateView):
    model = Machine
    form_class = MachineForm
    template_name = 'add_machine.html'
    success_url = reverse_lazy('home')
