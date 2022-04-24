from django import forms
from .models import Rooms,Roombookings,Payments

class DateInput(forms.DateInput):
    input_type = 'date'

class RoomForm(forms.ModelForm):
    class Meta:
        model = Rooms
        fields = ['roomid','roomnumber','roomprice','roomtype','roomcapacity']
        labels = {'roomid':'roomid','roomnumber': "roomnumber", "roomprice": "Price",
                  'roomtype':'Type','roomcapacity':'Capacity'}
    # roomnumber = forms.IntegerField()
    # roomprice = forms.IntegerField()
    # roomtype = forms.CharField(max_length=255)
    # roomcapacity = forms.IntegerField()

class RoombookingsForm(forms.ModelForm):
    class Meta:
        model = Roombookings
        fields = ['bookingid', 'customername', 'customeraddress', 'bookingfrom', 'bookingto',
                  'assignroomid','noofguests']

        widgets = {
            'bookingfrom': DateInput(),
            'bookingto' : DateInput()
        }
        # labels = {'roomid': 'roomid', 'roomnumber': "roomnumber", "roomprice": "Price",
        #           'roomtype': 'Type', 'roomcapacity': 'Capacity'}

class PaymentsForm(forms.ModelForm):
    class Meta:
        model = Payments
        fields = ['paymentid','bookingid','paymenttype','paymentamount']