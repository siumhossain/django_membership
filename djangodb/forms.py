from django import forms
from . models import Home


class MemberFrom(forms.ModelForm):
	class Meta:
		model = Home
		fields = ['f_name','l_name','email','age','passwd']