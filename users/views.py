from django.shortcuts import render
from django.views import View
from users.forms import LoginForm
from django.contrib.auth import login
from django.shortcuts import redirect 

from django.urls import reverse_lazy


from django.contrib.auth.views import LoginView


# class LoginUserView(View):
#     def get(self, request):
#         form = LoginForm(request)
#         return render(request, 'users/login.html', {'form': form})

#     def post(self, request):
#         form = LoginForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('/admin/')
#         return render(request, 'users/login.html', {'form': form})


class LoginUserView(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'