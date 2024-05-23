from django.forms.models import BaseModelForm
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Family, Word, WordFamily
from .forms import FamilyForm, WordForm, LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required



# Create your views here.
class FamilyCreateView(CreateView):
    model = Family
    form_class = FamilyForm
    template_name = 'vocabulary/family/create.html'
    success_url = reverse_lazy('vocabulary:index')

class FamilyListView(ListView):
    model = Family
    template_name = 'vocabulary/family/list.html'

class FamilyDetailView(DetailView):
    model = Family
    template_name = 'vocabulary/family/detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context['words'] = WordFamily.objects.filter(family=self.object)
        return self.render_to_response(context)

class FamilyUpdateView(UpdateView):
    model = Family
    form_class = FamilyForm
    template_name = 'vocabulary/family/update.html'
    success_url = reverse_lazy('vocabulary:index')

def index(request):
    return render(request, 'vocabulary/index.html')

class WordCreateView(CreateView):
    model = Word
    form_class = WordForm
    template_name = 'vocabulary/word/create.html'
    success_url = reverse_lazy('vocabulary:index')

    def form_valid(self, form: BaseModelForm):
        self.object = form.save()
        families = form.cleaned_data['family']
        for family in families:
            wordfamily = WordFamily.objects.create(family=family, word=self.object)
            wordfamily.save()
        return super().form_valid(form)
    
class WordListView(ListView):
    model = Word
    template_name = 'vocabulary/word/list.html'

class PositiveConnotationListView(ListView):
    model = WordFamily
    queryset = WordFamily.objects.filter(word__connotation='positive')
    template_name = 'vocabulary/word/connotation_list.html'

class NegativeConnotationListView(ListView):
    model = WordFamily
    queryset = WordFamily.objects.filter(word__connotation='negative')
    template_name = 'vocabulary/word/connotation_list.html'

class NeutralConnotationListView(ListView):
    model = WordFamily
    queryset = WordFamily.objects.filter(word__connotation='neutral')
    template_name = 'vocabulary/word/connotation_list.html'

def family_list_json(request):
    families = Family.objects.all()
    families_list = list()
    for family in families:
        family_id = family.id
        name = family.name
        family_dict = {
            'id': family_id,
            'name': name
        }
        families_list.append(family_dict)
    context = {
        'families': families_list
    }
    return JsonResponse(context)

@login_required
def register(request):  
    if request.POST == 'POST':  
        form = UserCreationForm()  
        if form.is_valid():  
            form.save()
            return redirect('vocabulary:index')  
    else:
        form = UserCreationForm()  
        context = {  
            'form':form  
        }  
    return render(request, 'user/create.html', context)

class VocabularyLoginView(LoginView):
    template_name = 'user/login.html'
    success_url = reverse_lazy('vocabulary:index')