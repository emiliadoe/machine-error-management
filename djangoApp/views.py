from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect, HttpResponseForbidden
from .forms import MachineForm, ErrorCodeForm, ErrorProtocolForm
from .models import Machine, ErrorCode, ErrorProtocol
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView
from django.contrib import messages

# Create your views here.

def home_page(request):
    q = request.GET.get('q')
    if q:
        results = Machine.objects.filter(name__icontains=q)
    else:
        results = None
    
    return render(request, 'home.html', {'results': results})


def overview_list(request):
    machines = Machine.objects.all().only('name', 'description')
    context = {'all_machines': machines}
    return render(request, 'overview.html', context)

def privatepolicy(request):
    return render(request, 'policy.html')

def machine_detail(request, pk=None):
    if pk is None:
        pk = request.GET.get('pk')
    
    current_machine = get_object_or_404(Machine, id=pk)
    all_error_codes = ErrorCode.objects.filter(machine=current_machine).order_by('-id')
    search_query = request.GET.get('q', '').lower()
    filtered_error_codes = all_error_codes.filter(error_code__icontains=search_query) if search_query else all_error_codes
    context = {
        'single_machine': current_machine,
        'error_codes': filtered_error_codes,
        'search_query': search_query,
    }
    
    return render(request, 'machine_detail.html', context)


def error_protocol_details(request):
    protocols = ErrorProtocol.objects.all().order_by('-timestamp')
    return render(request, 'protocol-content.html', {'protocols': protocols}) 


class MyLoginView(LoginView):
    template_name = 'registration/login.html'
    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())


class ErrorAddView(CreateView):
    model = ErrorCode
    form_class = ErrorCodeForm
    template_name = 'add_error.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Error Code wurde erfolgreich hinzugefügt! ')
        return response

class MachineAddView(CreateView):
    model = Machine
    form_class = MachineForm
    template_name = 'add_machine.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Maschine wurde erfolgreich hinzugefügt! ')
        return response

class ProtocollView(CreateView):
    model = ErrorProtocol
    form_class = ErrorProtocolForm
    template_name = 'error_protocoll.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Fehler wurde erfolgreich zum Protokoll hinzugefügt! ')
        return response

class MachineEditView(UpdateView):
    model = Machine
    form_class = MachineForm
    template_name = 'edit_details.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Maschine wurde erfolgreich bearbeitet! ')
        return response
    
def delete_machine(request, pk):
    print(pk)
    if request.method == 'POST': 
        machine = get_object_or_404(Machine, pk=pk)
        machine.delete()  
        messages.success(request, "Maschine wurde erfolgreich gelöscht!")
        return redirect('home') 
    else:
        return HttpResponseForbidden("Ungültige Anfrage. Nur POST-Anfragen erlaubt.")

