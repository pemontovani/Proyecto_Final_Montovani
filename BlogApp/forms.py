from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import BooleanField, EmailField, CharField, PasswordInput, ModelForm, ImageField, FileInput, Textarea, TextInput
from BlogApp.models import Bio

class UserEditForm(UserCreationForm):
    email = EmailField()
    password1 = CharField(label='Contraseña', widget=PasswordInput)
    password2 = CharField(label='Repetir Contraseña', widget=PasswordInput)
    last_name = CharField()
    first_name = CharField()
    is_staff = BooleanField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name', 'is_staff']
        help_texts = {k:'' for k in fields}
        
class UpdateUserForm(ModelForm):
    username = CharField(max_length=100,
                               required=True,
                               widget=TextInput(attrs={'class': 'form-control'}))
    email = EmailField(required=True,
                             widget=TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']
        
class UpdateProfileForm(ModelForm):
    biografia = CharField(widget=Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Bio
        fields = ['biografia']