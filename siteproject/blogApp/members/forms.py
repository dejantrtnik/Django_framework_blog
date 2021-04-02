from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from myblog.models import Profile

class SignUpForm(UserCreationForm):
      email             = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'autocomplete': 'off'}))
      first_name        = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name', 'autocomplete': 'off'}))
      last_name         = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name', 'autocomplete': 'off'}))

      class Meta:
            model = User
            fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2') 

      def __init__ (self, *args, **kwargs):
            super(SignUpForm, self).__init__(*args, **kwargs)

            self.fields['username'].widget.attrs['class'] = 'form-control'
            self.fields['first_name'].widget.attrs['class'] = 'form-control'
            self.fields['last_name'].widget.attrs['class'] = 'form-control'

class EditProfileForm(UserChangeForm):
      email             = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'autocomplete': 'off'}))
      first_name        = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name', 'autocomplete': 'off'}))
      last_name         = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name', 'autocomplete': 'off'}))

      username          = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'form-control'}))
      last_login        = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'form-control'}))
      # is_superuser      = forms.CharField(max_length=250, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
      # is_stuff          = forms.CharField(max_length=250, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
      # is_active         = forms.CharField(max_length=250, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
      # date_joined       = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'form-control'}))

      class Meta:
            model = User
            fields = ('username', 'first_name', 'last_name', 'email', 'password', 'last_login')


class ProfilePageForm(forms.ModelForm):
      class Meta:
            model = Profile
            fields = ('bio', 'profile_pic', 'web_url', 'facebook_url', 'twitter_url', 'instagram_url', 'pinterest_url', 'youtube_url', 'twitch_url')
            widgets = {
                  'bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write title', 'autocomplete': 'off'}),
                  #'profile_pic': forms.TextInput(attrs={'class': 'form-control'}),
                  'web_url': forms.TextInput(attrs={'class': 'form-group'}),
                  'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
                  'twitter_url': forms.TextInput(attrs={'class': 'form-control'}),
                  'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
                  'pinterest_url': forms.TextInput(attrs={'class': 'form-control'}),
                  'youtube_url': forms.TextInput(attrs={'class': 'form-control'}),
                  'twitch_url': forms.TextInput(attrs={'class': 'form-control'}),
            }



class PasswordChangingForm(PasswordChangeForm):
      old_password      = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
      new_password1     = forms.CharField(max_length=250, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
      new_password2     = forms.CharField(max_length=250, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

      class Meta:
            model = User
            # fields = ('old_password', 'new_password1', 'new_password2') 
            # labels = {
            # "Old password:": "embed",
            # "New password1:": "embed",
            # "New password2:": "embed",
            # }




