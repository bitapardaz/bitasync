from django import forms


class GetUserNameForm(forms.Form):
    username = forms.CharField(max_length=20)


class GenerateBulkLicenseForm(forms.Form):

    def __init__(self, all_usernames, *args, **kwargs):
        super(GenerateBulkLicenseForm, self).__init__(*args, **kwargs)

        self.fields['shop_id'].widget = forms.Select(choices=all_usernames)
        self.fields['shop_id'].widget.attrs.update({'class': 'selector'})


    shop_id = forms.CharField(required=True)
    license_type = forms.ChoiceField(choices=[('L1', 'L1'),
                                              ('L2', 'L2'),
                                              ('L5', 'L5'),
                                              ('U1', 'U1'),
                                              ('U3', 'U3'),
                                              ('U6', 'U6')
                                              ], required=True)
    copies = forms.IntegerField(required=True)
