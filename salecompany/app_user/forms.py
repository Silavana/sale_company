from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

# модель формы регистрации, взаимствуем из стандартной
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)


# модель формы входа, взаимствуем из стандартной 
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email',)