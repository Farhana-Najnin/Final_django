
from django import forms
from .models import UserAccount
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . constants import GENDERTYPE, ACCOUNTTYPE

class SignupForm(UserCreationForm):
    account_type = forms.ChoiceField(choices=ACCOUNTTYPE)

    class Meta:
        model = User
        fields = ['username', 'email', 'account_type', 'password1', 'password2']

    def save(self, commit=True):
        our_user = super().save(commit=False)
        if commit:
            our_user.save()
            account_type = self.cleaned_data.get('account_type')

            UserAccount.objects.create(
                user=our_user,
                account_type=account_type,
            )
        # print(account_type)
        return our_user

    def init(self, *args, **kwargs):
        super().init(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].widget.attrs.update({     
                'class' : (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                ) 
            })