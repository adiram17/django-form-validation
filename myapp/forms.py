from django import forms

class PersonalForm(forms.Form):
    
    firstname = forms.CharField(label='First Name', required=False,  widget = forms.TextInput(attrs={'class': 'form-control '}))
    lastname = forms.CharField(label='Last Name', required=False,  widget = forms.TextInput(attrs={'class': 'form-control '}))

    #clean validation
    def clean(self):
        super(PersonalForm, self).clean()
        
        firstname = self.cleaned_data.get('firstname')
        lastname = self.cleaned_data.get('lastname')

        if  not firstname:
            self._errors['firstname'] = self.error_class([
                'Please provide valid first name'])
            self.fields['firstname'].widget.attrs.update({'class': 'form-control is-invalid'})

        if  not lastname:
            self._errors['lastname'] = self.error_class([
                'Please provide valid last name'])
            self.fields['lastname'].widget.attrs.update({'class': 'form-control is-invalid'})

        return self.cleaned_data