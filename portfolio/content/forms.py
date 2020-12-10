from django import forms
from . import models

class MessageForm(forms.ModelForm):
    class Meta:
        model = models.SendMessage
        fields = ['name','email','subject','message']

        widgets = {
            'name' : forms.TextInput(attrs={
                "name":"name",
                "class":"form-control",
                "id":"name",
                "placeholder":"Your Name",
                "minlength":"4",
                "data-rule":"minlen:4",
                "data-msg":"Please enter at least 4 chars"
            }),
            'email' : forms.EmailInput(attrs={
                "name":"email",
                "class":"form-control",
                "id":"email",
                "placeholder":"Your Email",
                "data-rule":"email",
                "data-msg":"Please enter a valid email"
            }),
            'subject' : forms.TextInput(attrs={
                "name":"subject",
                "class":"form-control",
                "id":"subject",
                "placeholder":"Subject",
                "data-rule":"subject",
                "minlength":"8",
                "data-msg":"Please enter at least 8 chars"
            }),

            'message' : forms.Textarea(attrs={
                "class":"form-control",
                "name":"message",
                "rows":"5",
                "placeholder":"Your Email",
                "data-rule":"required",
                "minlength":"2",
                "data-msg":"Please write something for me",
                "placeholder": "Message"
            }),

        }