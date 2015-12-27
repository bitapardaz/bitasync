from django import forms


class GetUserNameForm(forms.Form):
    username = forms.CharField(max_length=20)


class GenerateBulkLicenseForm(forms.Form):

    def __init__(self, choices, *args, **kwargs):
        super(GenerateBulkLicenseForm, self).__init__(*args, **kwargs)
        self.fields['shop_id'] = forms.ChoiceField(choices=choices)
        self.fields['shop_id'].widget.attrs.update({'class': 'selector'})

    shop_id = forms.ChoiceField(required=True)
    license_type = forms.ChoiceField(choices=[('L1', 'L1'),
                                              ('L2', 'L2'),
                                              ('L5', 'L5'),
                                              ('U1', 'U1'),
                                              ('U2', 'U2'),
                                              ('U5', 'U5')
                                              ], required=True)
    copies = forms.IntegerField(required=True)
