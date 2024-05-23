from django.urls import path
from .views import FamilyCreateView, index, WordCreateView, FamilyListView, FamilyDetailView, FamilyUpdateView, WordListView, PositiveConnotationListView, NegativeConnotationListView, NeutralConnotationListView, register
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", index, name='index'),
    path('family/create/', login_required(FamilyCreateView.as_view(), login_url= reverse_lazy('vocabulary:login')), name='family-create'),
    # path('family/list-json/', family_list_json, name='family-list-json'),
    path('family/list/', login_required(FamilyListView.as_view(),login_url= reverse_lazy('vocabulary:login')), name='family-list'),
    path('family/detail/<int:pk>/', login_required(FamilyDetailView.as_view(), login_url=reverse_lazy('vocabulary:login')), name='family-detail'),
    path('family/update/<int:pk>/', login_required(FamilyUpdateView.as_view(), login_url=reverse_lazy('vocabulary:login')), name='family-update'),
    path('word/create/', login_required(WordCreateView.as_view(), login_url=reverse_lazy('vocabulary:login')), name='word-create'),
    path('word/list/', login_required(WordListView.as_view(),login_url= reverse_lazy('vocabulary:login')), name='word-list'),
    path('connotation/positive/', login_required( PositiveConnotationListView.as_view(), login_url=reverse_lazy('vocabulary:login')), name='positive-connotation-list'),
    path('connotation/negative/', login_required(NegativeConnotationListView.as_view(), login_url=reverse_lazy('vocabulary:login')), name='negative-connotation-list'),
    path('connotation/neutral/', login_required(NeutralConnotationListView.as_view(), login_url=reverse_lazy('vocabulary:login')), name='neutral-connotation-list'),
    path('user/register/', register, name='register'),
    path('user/login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('user/logout/', LogoutView.as_view(next_page=reverse_lazy('vocabulary:index')), name='logout'),
]