from django.shortcuts import render,redirect
from django.views.generic import CreateView,View
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import FormView, RedirectView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout, update_session_auth_hash
from .forms import SignupForm
from django.contrib import messages
from Courses.models import courses,Enroll 
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.forms import PasswordChangeForm
from django.template.loader import render_to_string
from Category.models import Categori
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from .models import UserAccount


# Create your views here.

# class SignUpFormView(CreateView):
#     template_name = 'signup.html'
#     form_class = SignupForm
#     success_url=reverse_lazy('login.html')

#     def form_valid(self,form):
#         print(form.cleaned_data)
#         user = form.save()
#         login(self.request, user)
#         print(user)
#         return super().form_valid(form) # form_valid function call hobe jodi sob thik thake
   
# class SignUpFormView(CreateView):
#     template_name = 'signup.html'
#     form_class = SignupForm

#     def form_valid(self, form):
#         user = form.save(commit=False)
#         user.is_active = False  # User is inactive until email verification
#         user.save()

#         current_site = get_current_site(self.request)
#         subject = 'Activate your account'
#         message = render_to_string('activation_email.html', {
#             'user': user,
#             'domain': current_site.domain,
#             'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#             'token': default_token_generator.make_token(user),
#             })

#         user.email_user(subject, message)

#         messages.success(self.request, 'Account created successfully. Please check your email to activate your account.')
#         return redirect('login')
class SignUpFormView(CreateView):
    template_name = 'signup.html'
    form_class = SignupForm

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False  # User is inactive until email verification
        user.save()

    
        token = default_token_generator.make_token(user)
    
        uid = urlsafe_base64_encode(force_bytes(user.pk))
       
        confirm_link = f"http://127.0.0.1:8000//user/activate/{uid}/{token}"
        email_subject = "Confirm Your Email"
        email_body = render_to_string('activation_email.html', {'confirm_link' : confirm_link})
            
        email = EmailMultiAlternatives(email_subject , '', to=[user.email])
        email.attach_alternative(email_body, "text/html")
        email.send()
        messages.success(self.request, 'Account created successfully. Please check your email to activate your account.')
        return redirect('login')
class ActivationView(View):
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = get_user_model().objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, 'Your account has been activated. You can now login.')
            return redirect('login')
        else:
            return HttpResponseBadRequest('Activation link is invalid or has expired.')
# class LoginView(FormView):
#     template_name = 'login.html'
#     form_class = LoginForm

#     def form_valid(self, form):
#         username = form.cleaned_data['username']
#         password = form.cleaned_data['password']
#         user = authenticate(self.request, username=username, password=password)
#         if user is not None:
#             login(self.request, user)
#             return super().form_valid(form)
#         else:
#             form.add_error(None, 'Invalid username or password')
#             return self.form_invalid(form)


class LoginFormView(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm

    def get(self, request):
        LoginForm = self.form_class()
        return render(request,self.template_name,{'form':LoginForm})
    
    def post(self,request):
        LoginForm = self.form_class(request, data=request.POST)
        if LoginForm.is_valid():
            self.form_valid(LoginForm)
            messages.success(request,'Logged in successfully')

            return redirect('home_page')
        else:
            messages.warning(request,'Invalid Information')
            return render(request,self.template_name,{'form':LoginForm})   


# class LogoutFormView(LogoutView):
#     def get_success_url(self):
#         if self.request.user.is_authenticated:
#             logout(self.request)
#         return reverse_lazy('home_page')
        
    
def LogoutFormView(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect(reverse_lazy('home_page'))

def ProfileView(request,category_slug = None):
    data = courses.objects.all()
    categoryCourse = Categori.objects.all()
    enroll = Enroll.objects.all()
    
    if category_slug is not None:
        user_id = request.user.id
        category = Categori.objects.get(slug = category_slug)
        data = courses.objects.filter(Category = category)
        enroll = Enroll.objects.filter(id = user_id)

    return render(request, 'profile.html', {'data': data,'Enroll': enroll, 'categoryCourse': categoryCourse})

class PasswordUpdateView(View):
    template_name = 'password_change.html'

    def get(self, request):
        if request.user.is_authenticated:
            form = PasswordChangeForm(user = request.user)
            return render(request, self.template_name, {'form': form})
        else:
            return redirect('login')
        
    def post(self, request):
        if request.user.is_authenticated:
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
            return render(request, self.template_name,{'form': form})
        else:
            return redirect('login')