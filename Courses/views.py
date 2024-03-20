from django.shortcuts import redirect,get_object_or_404, render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView,DetailView,UpdateView,DeleteView,ListView
from user.models import UserAccount
from django.template.loader import render_to_string
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from Category.models import Categori
from . import forms 
from . import models
from . models import Enroll,courses
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from .choice import ENROLL,COMPLETE
from django.http import HttpResponse
from django.utils import timezone

def enroll_user_in_course(user_account, course, enrollment_type):
    enroll = Enroll.objects.create(
        user1=user_account,
        course=course,
        enrollment_type=enrollment_type,
        enroll_date=timezone.now()
    )
    return enroll
class CoursePost(CreateView):
    model = courses
    form_class = forms.CourseForm
    template_name = 'home.html'
    success_url = reverse_lazy('home.html')
    def form_valid(self, form):
        return super().form_valid(form)

class CourseDetailsPost(DetailView):
    model = courses
    template_name = 'course_details.html'
    pk_url_kwarg = 'id'

    # def post(self, *args, **kwargs):
    #         commentform = forms.CommentForm(data=self.request.POST)
    #         post = self.get_object()
    #         if commentform.is_valid():
    #             new_comment = commentform.save(commit=False)
    #             new_comment.post = post 
    #             new_comment.save()
    #         return self.get(self, *args, **kwargs)
    # def get_context_data(self,**kwargs):
    #     context = super().get_context_data(**kwargs)
    #     post = self.object 
    #     comments = post.comment.all()
    #     commentform = forms.CommentForm()
        
@method_decorator(login_required, name='dispatch')
class CourseDetailsView(DetailView):
    model = courses
    template_name = 'course_details.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = courses.objects.all()
        context['category'] = Categori.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        course = self.get_object()
        user = request.user
        useraccount = UserAccount.objects.filter(user=user).first()
        
        if 'borrow' in request.POST:
            Enroll.objects.create(
                user=useraccount,
                enrollment_type=ENROLL
            )
            course.borrowers.add(user)
            messages.success(request, 'You Enrolled in the course successfully!!!')
        elif 'return' in request.POST:
            Enroll.objects.create(
                user=useraccount,
                enrollment_type=COMPLETE
            )
            course.borrowers.remove(user)
            messages.success(request, 'Congratulations!!! You successfully completed the course!!!!')
        
        return redirect('course_details', id=course.id) 
    
# def enrollCourse(request,id):
#     course = get_object_or_404(courses, id=id)
#     user_profile, created = UserAccount.objects.get_or_create(user=request.user)
#     # enroll = Enroll.objects.create(user=request.user, courses=courses)
#     # enroll.save()
#     # courses.save()
#     # useraccount = user_profile[0] if created else user_profile
#     # useraccount.save()
#     # messages.success(request, 'You enrolled courses Successfully!!!!!')
    
#     # return redirect('profile')
#     enroll = Enroll.objects.create(user=request.user, courses=course)
#     enroll.save()
    
#     courses.save()
#     useraccount = user_profile[0] if created else user_profile
#     useraccount.save()
#     messages.success(request, 'You enrolled Successfully!!!!!')
#     return redirect('profile')
@login_required
def CourseDetails(request, id, category_slug = None):
    course1 = courses.objects.get(id=id)
    data1 = courses.objects.all()
    if category_slug is not None:
        category = Categori.objects.get(slug = category_slug)
        data1 = courses.objects.filter(category = category)
    categories = Categori.objects.all()
    User = request.user
    useraccount = UserAccount.objects.filter(user=User).first()
    borrowerslist = []
    returnlist = []

    if request.method == 'POST':
        
        if 'borrow' in request.POST:
            Enroll.objects.create(
                user=useraccount,
                enrollment_type=ENROLL
            )
            course1.borrowers.add(User)
            borrowerslist.append(course1)
            # print(borrowerslist)
            
            
        elif 'return' in request.POST:
            Enroll.objects.create(
                user=useraccount,
                enrollment_type=COMPLETE
            )
            course1.borrowers.remove(User)
            returnlist.append(User)
            # print(returnlist)
            
        return redirect('course_details', id=course1.id)
      
    
    return render(request, 'course_details.html', {'course': course1, 'data': data1, 'category': categories})



@login_required
def enrollCourse(request, id):
    # print("line 2")
    # print(id)
    course1 = models.courses.objects.get(pk=id)
    # print(course1)
    user_account = request.user
    # print(user_account)
    borrowers_list = []
    return_list = []
    try:
        # print('user account exist')
        useraccount = user_account.account 
    except UserAccount.DoesNotExist:
        # print('user account doesnt exist')
        useraccount = UserAccount.objects.create(user=user_account)
        


    if models.Enroll.objects.filter(user1=useraccount, course=course1).exists():
        
        # print('enroll created')
        # print(' course completed')
        course1.borrowers.remove(user_account)
        return_list.append(user_account)
        
        # print('return_list')
        # print(return_list)
        messages.success(request, 'Congratulations!!! You successfully completed the course!!!!')
    else:
        
        models.Enroll.objects.create(user1=useraccount, course=course1)
        # print('enroll course')
        course1.borrowers.add(user_account)
        # print(course1.borrowers)
        print('append course to the borrowerlist')
        # borrowers_list.append(course1)
        # print('borrowerlist')
        # print(borrowers_list)
        messages.success(request, 'Enrolled successfully')
    
    return redirect('profile')
@login_required
def completeCourse(request, id):
    print("line 2")
    print(id)
    course1 = models.courses.objects.get(pk=id)
    print(course1)
    user_account = request.user
    print(user_account)
    return_list = []
    try:
        print('user account exist')
        useraccount = user_account.account 
    except UserAccount.DoesNotExist:
        print('user account doesnt exist')
        useraccount = UserAccount.objects.create(user=user_account)
        


    if models.Enroll.objects.filter(user1=useraccount, course=course1).exists():
        print(' course completed')
        course1.borrowers.remove(user_account)
        return_list.append(user_account)
        
        print('return_list')
        print(return_list)
        messages.success(request, 'Congratulations!!! You successfully completed the course!!!!')
        
    else:
        
        models.Enroll.objects.create(user1=useraccount, course=course1)
        print('enroll course')
        messages.success(request, 'Enrolled successfully')
    
    return redirect('profile')

@method_decorator(login_required, name='dispatch')
class AddCourse(CreateView):
    template_name = 'add_course.html'
    form_class = forms.CourseForm
    model = models.courses
    success_url = reverse_lazy('home_page')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context
    

class AddPostView(CreateView):
    template_name = 'add_course.html'
    form_class = forms.CourseForm
    success_url = reverse_lazy('home_page') 

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context


@method_decorator(login_required, name='dispatch')  
class EditCourse(UpdateView):
    template_name = 'add_course.html'
    form_class = forms.CourseForm
    model = models.courses
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('add_course')
    
    
def edit_post(request, id):
    post = models.courses.objects.get(pk=id) 
    post_form = forms.CourseForm(instance=post)
    print(post.title)
    if request.method == 'POST': 
        post_form = forms.CourseForm(request.POST, instance=post) 
        if post_form.is_valid(): 
            post_form.save()
            return redirect('home_page') 
    
    return render(request, 'add_course.html', {'form' : post_form})

@method_decorator(login_required, name='dispatch')
class DeleteCourse(DeleteView):
    template_name = 'delete_course.html'
    model = models.courses
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('manage_course')
    
 