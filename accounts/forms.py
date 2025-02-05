from django import forms
from .models import User


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password != password_confirm:
            self.add_error('password_confirm', 'Passwords do not match')
        
        return cleaned_data


class ConsentForm(forms.ModelForm):

    # Consent consists of multiple questions. Add each here.
    widget = forms.CheckboxInput(attrs={'class': 'form-check-input'})
    field_1 = forms.BooleanField(
        required=True,
        error_messages={'required': 'Check this box to acknowledge you consent.'},
        widget=widget
    )
    field_2 = forms.BooleanField(
        required=True,
        error_messages={'required': 'Check this box to acknowledge you consent.'},
        widget=widget
    )
    field_3 = forms.BooleanField(
        required=True,
        error_messages={'required': 'Check this box to acknowledge you consent.'},
        widget=widget
    )
    field_4 = forms.BooleanField(
        required=True,
        error_messages={'required': 'Check this box to acknowledge you consent.'},
        widget=widget
    )
    field_5 = forms.BooleanField(
        required=True,
        error_messages={'required': 'Check this box to acknowledge you consent.'},
        widget=widget
    )
    field_6 = forms.BooleanField(
        required=True,
        error_messages={'required': 'Check this box to acknowledge you consent.'},
        widget=widget
    )

    class Meta:
        model = User
        fields = ['consent']

    def clean(self):
        ''' If the form gets submitted, the user has consented to all the
            items. We can just set consent to true. '''
        cleaned_data = super().clean()
        cleaned_data['consent'] = True
        return cleaned_data


class ConsentWithdrawForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['consent']
    
    def clean(self):
        ''' If the form gets submitted, the user has withdrawn consent. '''
        cleaned_data = super().clean()
        cleaned_data['consent'] = False
        return cleaned_data


class GoogleTakeoutUploadForm(forms.Form):
    file = forms.FileField()
