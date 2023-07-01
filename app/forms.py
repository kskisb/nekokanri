from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput

class PostForm(forms.Form):
    name = forms.CharField(label='名前', max_length=30)
    birthday = forms.DateField(
        label="生年月日",
        widget=DatePickerInput(format='%Y-%m-%d')
    )
    sex = forms.ChoiceField(
        label="性別",
        choices=(('男の子', '男の子'), ('女の子', '女の子')),
        required=True,
        widget=forms.widgets.Select
    )
    image = forms.ImageField(label="写真", required=False)
    mated_at = forms.DateField(
        label="交配日(無入力可)",
        widget=DatePickerInput(format='%Y-%m-%d'),
        required=False,
    )
    days_to_conceive = forms.IntegerField(label="妊娠するまでの日数(無入力可)", initial=63, required=False)