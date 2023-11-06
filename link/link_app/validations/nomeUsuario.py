from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from models import Usuario

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ('nome do usuário')

    def clean(self):
        cleaned_data = super(CustomUserCreationForm, self).clean()
        Usuario.nomeUsuario = cleaned_data.get('nome de usuário')
        if ('@', '.', '-', '+') in Usuario.nomeUsuario:
            self.add_error('nome de usuário', 'Os símbolos @/./-/+ não são permitidos.')
        return cleaned_data

# caso o usuario queira mudar o usuário
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        fields = ('nome de usuario')

    def clean(self):
        cleaned_data = super(CustomUserChangeForm, self).clean()
        username = cleaned_data.get('nome de usuario')
        if ('@', '.', '-', '+') in username:
            self.add_error('username', 'Symbols @/./-/+ are not allowed in username.')
        return cleaned_data