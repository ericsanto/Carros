from django import forms
from cars.models import *
from datetime import date
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class CarForms(forms.ModelForm):

  class Meta:
    model = Car
    fields = '__all__'


  def clean_value(self):
    value = self.cleaned_data.get('value') #---> busca o campo 'value' do formulário e atribui a value
    if value < 20000:
      self.add_error('value', 'Valor mínimo do carro deve ser de R$20.000')
    return value
  

  def clean_factory_year(self):
    ano = date.today().year
    factory_year = self.cleaned_data.get('factory_year')
    if factory_year > ano:
      self.add_error('factory_year', 'Não é possível cadastrar carros com o ano de fabricação maior que o ano atual')
    return factory_year
  


class UserForm(UserCreationForm):
  
  class Meta:
    model = User 
    fields = ['username', 'first_name', 'last_name', 'email']


  def clean_email(self):
    email = self.cleaned_data.get('email')
    if User.objects.filter(email=email).exists():
        raise ValidationError(f'O Email {email} já está cadastrado')
    return email
  


  def clean_username(self):
    username = self.cleaned_data.get('username')
    if User.objects.filter(username=username).exists():
        raise ValidationError(f'Nome {username} já existe. Por favor, tente outro username')
    return username

