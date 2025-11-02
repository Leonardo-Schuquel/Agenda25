from django import forms
from django.core.exceptions import ValidationError
from . import models


class ContactForm(forms.ModelForm):

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'clase_a clase_b',
            'placeholder': 'Escreva o primeiro nome aqui',
        }
        ),
        label='Primeiro Nome',
        help_text='Texto de ajuda para o usuario'
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'clase_a clase_b',
            'placeholder': 'Escreva o seu sobrenome aqui',
        }
        ),
        label='Segundo Nome',
    )

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        # self.fields['first_name'].widget.attrs.update({
        #     'class': 'clase_a clase_b',
        #     'placeholder': 'Escreva o primeiro nome aqui',
        # })

    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category',
        )

        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class': 'clase-a clase-b',
        #             'placeholder': 'Primeiro nome'
        #         }
        #     )
        # }

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError(
                'Primeiro nome não pode ser igual ao segundo',
                code='invalid',
            )
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            raise ValidationError(
                'Não digite ABC nesse campo',
                code='invalid'
            )

        return first_name
