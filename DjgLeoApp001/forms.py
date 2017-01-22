from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    address = forms.CharField()
    phone = forms.CharField()
    mail = forms.EmailField(required=False)
    tk = forms.CharField()
    text = forms.CharField()
    #hospital = forms.NullBooleanField(db_column='Hospital')  # Field name made lowercase.
    #medicalcenter = models.NullBooleanField(db_column='MedicalCenter')  # Field name made lowercase.
    #eopyy = models.NullBooleanField(db_column='EOPYY')  # Field name made lowercase.
    contact = forms.CharField()
    #countryid = forms.ForeignKey(Country, db_column='CountryId')  # Field name made lowercase.

#Crispy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

class ExampleForm(forms.Form):
    like_website = forms.TypedChoiceField(
        label = "Do you like this website?",
        choices = ((1, "Yes"), (0, "No")),
        coerce = lambda x: bool(int(x)),
        widget = forms.RadioSelect,
        initial = '1',
        required = True,
    )

    favorite_food = forms.CharField(
        label = "What is your favorite food?",
        max_length = 80,
        required = True,
    )

    favorite_color = forms.CharField(
        label = "What is your favorite color?",
        max_length = 80,
        required = True,
    )

    favorite_number = forms.IntegerField(
        label = "Favorite number",
        required = False,
    )

    notes = forms.CharField(
        label = "Additional notes or feedback",
        required = False,
    )

    def __init__(self, *args, **kwargs):
        super(ExampleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'

        self.helper.add_input(Submit('submit', 'Submit'))

from django.shortcuts import render

from  django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    example_form = ExampleForm()
    return render_to_response("example_form.html",
                              {"form": example_form,"example_form": example_form},)
    
