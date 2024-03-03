from django.shortcuts import redirect,get_object_or_404, render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView,DetailView
from user.models import UserAccount
from . import forms 
from . import models
from . models import Enroll,courses
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
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
def enrollCourse(request, id):
    course1 = models.courses.objects.get(id=id)
    coursess = models.courses.objects.all()
    user_account = request.user
    if models.Enroll.objects.filter(user=request.user, course=course1).exists():
        messages.success(request, "You are already enrolled in this course.")
    else:
        course2=models.Enroll.objects.create(user=request.user, course=course1)
        user_account.save()
        user_id = request.user.id
        course2.save()
        messages.success(request, 'Enroll Successfully')
    return redirect('profile')



    
   

    # if book.quantity > 0:
    #         if user_profile.balance > 100:
    #             borrow = Enroll.objects.create(user=request.user, book=book)
    #             borrow.save()
    #             book.quantity -= 1
    #             book.save()
    #             useraccount = user_profile[0] if created else user_profile
    #             useraccount.balance -= book.price
    #             useraccount.save()
    #             messages.success(request, 'You borrowed book Successfully!!!!!')
    #             return redirect('profile')
    #         else:
    #             messages.error(request, 'You donot have sufficient balance to borrow this book')
    #             return redirect('deposit')
    # else:
    #     messages.success(request, 'This book out of stock')
    #     return redirect('home_page')
    # return redirect('profile')

# def returnBook(request, id):
#     borrow = get_object_or_404(Enroll, pk=id)
#     book = borrow.book
#     user_profile = UserAccount.objects.get_or_create(user=request.user)[0]
#     if borrow.user == request.user:
#         borrow.delete() 
#         book.quantity += 1
#         book.save()
#         user_profile.balance += book.price 
#         user_profile.save()
#         messages.success(request, 'You have returned the book successfully!!!')
#     else:
#         messages.error(request, 'You arenot authorize for return book')
#     return redirect('profile')