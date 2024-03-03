from django import forms
from . constants import GENDERTYPE, ACCOUNTTYPE
from . models import UserAccount,UserAddress
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    birthDate = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    gender = forms.ChoiceField(choices=GENDERTYPE)
    accountType = forms.ChoiceField( choices=ACCOUNTTYPE)
    streetAddress = forms.CharField(max_length = 90)
    city = forms.CharField(max_length = 90)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length = 90)

    class Meta:
        model = User 
        fields = ['username', 'first_name', 'last_name','email','password1','password2','accountType','birthDate','gender','postal_code','city','streetAddress','country']
    
    def save(self,commit=True):
        user1 = super().save(commit=False)
        if commit == True:
            user1.save()
            accountType = self.cleaned_data.get('accountType')
            gender = self.cleaned_data.get('gender')
            postal_code = self.cleaned_data.get('postal_code')
            streetAddress = self.cleaned_data.get('streetAddress')
            birthDate = self.cleaned_data.get('birthDate')
            city = self.cleaned_data.get('city')
            country = self.cleaned_data.get('country')
            
            UserAccount.objects.create(
                user = user1,
                account_type = accountType,
                gender = gender,
                birth_date = birthDate,
                account_no = user1.id
            )

            UserAddress.objects.create(
                user = user1,
                postal_code = postal_code,
                country = country,
                city = city,
                street_address = streetAddress
            )
        return user1