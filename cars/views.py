from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import *
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import UserPassesTestMixin
    



class HomeListView(ListView):
    model = Car
    template_name = 'home.html'
    context_object_name = 'cars'

    def get_queryset(self):
      cars = super().get_queryset()
      search = self.request.GET.get('search')
      if search:
        cars = cars.filter(model__icontains=search)
      return cars




class CreateCarView(CreateView):
  model = Car
  template_name = 'addcar.html'
  form_class = CarForms
  success_url = reverse_lazy('home')






'''def create_user(request):
  if str(request.method) == 'POST':
    form = UserForm(request.POST)
    if form.is_valid():
      form.save()
      form = UserForm()
      return redirect('login')
  else:
    messages.error(request, 'Não foi possível cadastrar usuário')
    form = UserForm()
  context = {
    'form': form
  }
  return render(request, 'create-user.html', context)'''



class CreateUserView(CreateView):
  model = UserCreationForm
  form_class = UserForm
  template_name = 'create-user.html'
  success_url = reverse_lazy('login')



class CarDetailView(DetailView):
  model = Car
  template_name = 'car_detail.html'


@method_decorator(login_required, name='dispatch')
class UpdateCarView(UpdateView):
  model = Car
  form_class = CarForms
  template_name = 'update_car.html'
  
  def get_success_url(self):
    return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})




class DeleteCarView(DeleteView):
  model = Car
  template_name = 'delete_car.html'
  success_url = reverse_lazy('home')