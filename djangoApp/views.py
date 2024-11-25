from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect, HttpResponseForbidden
from .forms import MachineForm, ErrorCodeForm, ErrorProtocolForm
from .models import Machine, ErrorCode, ErrorProtocol
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView, CreateView
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def home_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('home')  
    else:
        form = AuthenticationForm()
       
    q = request.GET.get('q')
    if q:
        results = Machine.objects.filter(name__icontains=q)
    else:
        results = None

    machines = Machine.objects.all().only('name', 'description')
    context = {'form': form, 'all_machines': machines, 'results': results}
    return render(request, 'home.html', context)


def overview_list(request):
    machines = Machine.objects.all().only('name', 'description')
    context = {'all_machines': machines}
    return render(request, 'overview.html', context)

def privatepolicy(request):
    return render(request, 'policy.html')

def about(request):
    return render(request, 'about.html')

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
    def get_success_url(self):
        return reverse('machine_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Maschine wurde erfolgreich bearbeitet! ')
        return response
    
def delete_machine(request, pk):
    if request.method == 'POST': 
        machine = get_object_or_404(Machine, pk=pk)
        machine.delete()  
        messages.success(request, "Maschine wurde erfolgreich gelöscht!")
        return redirect('home') 
    else:
        return HttpResponseForbidden("Ungültige Anfrage. Nur POST-Anfragen erlaubt.")

