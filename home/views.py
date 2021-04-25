from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, About
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.core import serializers
from django.views.generic import View, TemplateView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from . import forms
from .forms import ContactForm
# from prolens.settings import EMAIL_HOST_USER

# Create your views here.

# def home(request):
#   posts = Post.objects.filter(published=True).order_by('-pub_date')[0:6]
#   paginator = Paginator(posts, 4)
#   page = request.GET.get('page')

#   context = {
#     'title': 'Pro LENS',
#     'posts': posts,
#     'page': page
#   }
#   return render(request, 'home/home.html', context)


class MainView(TemplateView):
    template_name = 'home/home.html'

class PostJsonListView(View):
    # def get(self, *args, **kwargs):
    #     upper = kwarges.get('num_posts') #3
    #     lower = upper - 3 #0
    #     posts = list(Post.objects.values()[lower:upper])
    #     print(kwargs)
    #     posts_size = len(Post.objects.all())
    #     max_size = True if upper >= posts_size else False
    #     return JsonResponse({'data': posts, 'max': max_size}, safe=False)
    #     # return JsonResponse({'data': posts}, safe=False)

    def get(self, *args, **kwargs):
        print(kwargs)
        upper = kwargs.get('num_posts') #3
        lower = upper - 15 #0
        posts = list(Post.objects.values()[lower:upper])
        posts_size = len(Post.objects.all())
        max_size = True if upper >= posts_size else False
        return JsonResponse({'data': posts, 'max': max_size}, safe=False)    


def about(request):
  content = About.objects.all()
  context = {
    'title': 'Pro LENS',
    'abouts': content,
  }
  return render(request, 'home/about.html', context)


# def connect(request):
#     # create a form instance and populate it with data from the request:
#   form = forms.ContactForm()
#   # if this is a POST request we need to process the form data
#   if request.method == 'POST':
#     # check whether it's valid:
#     form = forms.ContactForm(request.POST)

#     subject = 'Welcome to DataFlair'
#     message = 'Hope you are enjoying your Django Tutorials'
#     recepint = str(form['Email'].value())
    
#     send_mail(
#       subject,
#       message,
#       EMAIL_HOST_USER,
#       [recepint],
#       fail_silently = False
#     )
#     return render(request, 'home/connect.html', {'recepint': recepint})
#   return render(request, 'home/connect.html', {'form': form})

def connect(request):
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      subject = "Pro lens"
      recepint = str(form['email'].value())
      print(recepint)
      body = {
        'client_name': form.cleaned_data['client_name'],
			  'client_number': form.cleaned_data['client_number'], 
			  'email': form.cleaned_data['email'], 
			  'message':form.cleaned_data['message'], 
      }
      message = "\n".join(body.values())

      try:
        send_mail(subject, message, recepint, ['abdallahhaboharba@gmail.com'], fail_silently = False)
      except BadHeaderError:
        return HttpResponse('Invalid Header Found.')
      return redirect ('/')
  form = ContactForm()
  return render(request, 'home/connect.html', {'form': form})
  