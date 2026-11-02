from django.shortcuts import render
from django.views import View
from users.forms import LoginForm, RegistrationForm
from django.contrib.auth import login
from django.shortcuts import redirect 

from django.urls import reverse_lazy


from django.contrib.auth.views import LoginView


# class LoginUserView(View):
#     def get(self, request):
#         form = LoginForm()
#         return render(request, 'users/login.html', {'form': form})

#     def post(self, request):
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('/admin/')
#         return render(request, 'users/login.html', {'form': form})


class LoginUserView(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'


class RegistrationUserView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'users/registration.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/admin/')
        return render(request, 'users/registration.html', {'form': form})