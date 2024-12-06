from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect, HttpResponseForbidden, JsonResponse
from .forms import MachineForm, ErrorCodeForm, ErrorProtocolForm, CustomAuthenticationForm
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView, CreateView
from django.contrib import messages
from django.db.models import Q 
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
from .models import Machine, ErrorCode, ErrorProtocol

# Create your views here.

#@cache_page(60 * 5)
@csrf_protect
def home_page(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('home')  
    else:
        form = CustomAuthenticationForm()
       
    q = request.GET.get('q')
    if q:
        results = Machine.objects.filter(name__icontains=q)
    else:
        results = None

    machines = Machine.objects.all().only('name', 'description')
    context = {'form': form, 'all_machines': machines, 'results': results}
    return render(request, 'home.html', context)


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

@cache_page(60 * 10)
def error_protocol_details(request):
    search_query = request.GET.get('q', '').lower()
    page_number = request.GET.get('page', 1) 
    protocols = ErrorProtocol.objects.select_related('error_code', 'machine').only(
        'error_code__error_code', 'machine__name', 'timestamp')
    if search_query:
          protocols = protocols.filter(
            Q(error_code__error_code__icontains=search_query) | 
            Q(machine__name__icontains=search_query)             
        )
    paginator = Paginator(protocols, 5) 
    protocols_page = paginator.get_page(page_number)
    if request.method == "POST":
        form = ErrorProtocolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('error_protocol_details') 
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data = {
            'protocols': [
                {
                    'timestamp': protocol.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                    'machine': protocol.machine.name if protocol.machine else 'N/A',
                    'error_code': protocol.error_code.error_code,
                    'notes': protocol.notes,
                }
                for protocol in protocols_page
            ],
            'has_next': protocols_page.has_next(),
        }
        return JsonResponse(data)
    form = ErrorProtocolForm()  
   
    context = {
        'protocols': protocols_page, 
        'form': form,
        'search_query': search_query,
        'has_next': protocols_page.has_next() 
    }

    return render(request, 'error-protocol.html', context)

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

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Maschine wurde erfolgreich hinzugefügt!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home') 


class MachineEditView(UpdateView):
    model = Machine
    form_class = MachineForm
    template_name = 'edit_details.html'

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Maschine wurde erfolgreich bearbeitet!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('machine_detail', kwargs={'pk': self.object.pk}) 


def delete_machine(request, pk):
    if request.method == 'POST':
        machine = get_object_or_404(Machine, pk=pk)
        machine.delete()
        messages.success(request, "Maschine wurde erfolgreich gelöscht!")
        return redirect('home') 
    else:
        return HttpResponseForbidden("Ungültige Anfrage. Nur POST-Anfragen erlaubt.")



class ProtocollView(CreateView):
    model = ErrorProtocol
    form_class = ErrorProtocolForm
    template_name = 'error_protocoll.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Fehler wurde erfolgreich zum Protokoll hinzugefügt! ')
        return response
 

