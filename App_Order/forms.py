from django import forms


class CouponForm(forms.Form):
    couponCode = forms.CharField(label='Coupon code', max_length=100, required=False)