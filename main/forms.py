from django import forms

class FormEvent(forms.Form):
    name = forms.CharField(
        max_length=100,
        label = 'Event Name',
    )
    type = forms.CharField(
        max_length=20,
        label = 'Event Type',
    )
    date = forms.DateField(
        label = 'D-Day',
        widget=forms.DateInput(attrs={
            'class' : 'date',
            'type' : 'date'
        })
    )
    reg = forms.CharField(
        max_length = 30,
        label = 'Registration Link'
    )
    desc = forms.CharField(
        label = 'Description',
        max_length=100
    )
    img = forms.CharField(
        label = 'Poster / Image link',
        max_length=100
    )

class FormItems(forms.Form):
    name = forms.CharField(
        label = 'Item Name ',
        max_length=100
    )
    penerima = forms.CharField(
        label = 'barang diterima oleh ',
        max_length=20
    )
    type = forms.CharField(
        label = 'Tipe barang ',
        max_length=30
    )
    amount = forms.IntegerField(
        label = 'Jumlah barang ',
    )
    owner = forms.CharField(
        label = 'Owner ',
        max_length = '20'
    )
    dateIn = forms.DateField(
        label = 'Tanggal masuk ',
        widget=forms.DateInput(attrs={
            'class' : 'date',
            'type' : 'date'
        })
    )
    desc = forms.CharField(
        label = 'Detail lainnya ',
        max_length=100,
    )
    location = forms.CharField(
        label = 'tempat disimpan/diletakan ',
        max_length=30
    )