from django import forms
from django.conf import settings
from django.contrib.auth import authenticate, login,logout,get_user_model
from polls.models import Entry,Files_Upload_Model
from django.forms import ModelForm

User=get_user_model()

class ContactForm(forms.Form):
    name = forms.CharField(label='Name')
    age = forms.CharField(label='Age')
    location=forms.CharField(label='Location')

class ContactEmailForm(forms.Form):
    name=forms.CharField(label='Name')
    email=forms.EmailField(label='Email')
    message=forms.CharField(widget=forms.Textarea)

    def clean(self, *args,**kwargs):
        name=self.cleaned_data.get('username')
        email=self.cleaned_data.get('email')
        message=self.cleaned_data.get('message')
        return super(ContactEmailForm, self).clean(*args,**kwargs)


class UserLogin(forms.Form):
    name=forms.CharField(label='Name')
    email=forms.EmailField(label='Email')
    password=forms.CharField(widget=forms.PasswordInput)

class Uday_Login_form(forms.Form):
    name=forms.CharField(label='Name')
    password=forms.CharField(widget=forms.PasswordInput)
    def clean_user(self):
        uday=Entry.objects.get(name=self.cleaned_data.get('name'))
        if not uday:
            raise forms.ValidationError('this user does not exist')
        if not uday.check_password(password=self.cleaned_data.get('password')):
            raise forms.ValidationError()

class EntryForm(forms.Form):
    name=forms.CharField(label='Name')
    password=forms.CharField(label='Password')
    age=forms.IntegerField(label='Age')
    email=forms.EmailField(label='Email')
    phone_number=forms.CharField(label='Phone Number')


class User_Login_Form(forms.Form):
    username=forms.CharField(label='Name')
    password=forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args,**kwargs):
        username=self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')
        user=authenticate(username=username,password=password)


        if not user:
            raise forms.ValidationError('This user does not exist')
        if not user.check_password(password):
            raise forms.ValidationError('Incorrect password')
        if not user.is_active:
            raise forms.ValidationError('This user no longer active.')
        return super(User_Login_Form, self).clean(*args,**kwargs)



class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(label='Email address')
    email2=forms.EmailField(label='Conform Email')
    class Meta:
        model = User
        fields=['username',
                'email',
                'email2',
                'password']
    # def clean_email(self):
    #     email=self.cleaned_data.get('email')
    #     email2 = self.cleaned_data.get('email2')
    #     if email != email2:
    #         raise forms.ValidationError('Email must match')
    #     email_qs=User.objects.filter(email=email)
    #     if email_qs.exists():
    #         raise  forms.ValidationError('This Email has already been registered')
    #     return email


    def clean(self, *args,**kwargs):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError('Email must match')
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError('This Email has already been registered')
        return super (UserRegistrationForm,self).clean(*args,**kwargs)


class File_Upload_Form(forms.Form):
    files=forms.FileField(label='Select a File',help_text='max. 1000 megabytes')

class File_Upload_Form(ModelForm):
    class Meta:
        model = Files_Upload_Model
        fields='__all__'

class Audio_Video_Form(forms.Form):
    audio=forms.FileField(label='Audio')
    video=forms.FileField(label='Video')


    def clean (self,*args,**kwargs):
        audio=self.cleaned_data.get('audio')
        video=self.cleaned_data.get('video')
        content_type = ["audio/mpeg", "audio/..."]
        # audio_ext=('.mp3')
        # video_ext=('.mp4')

        # if audio and video is None:
        #     raise forms.ValidationError("Please Select File First...")
        # if audio not in content_type:
        #     raise forms.ValidationError('Audio accepted only in: %s' % ''.join(content_type))
        #
        # if video not in content_type:
        #     raise forms.ValidationError('Video accepted only in: %s' % ''.join(content_type))
        # return super (Audio_Video_Form,self).clean(*args,**kwargs)
        #























