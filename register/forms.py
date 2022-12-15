from django import forms
from allauth.account.forms import SignupForm as _SignupForm


class SignupForm(_SignupForm):
    # ユーザー登録時に、プロフ画像も含めるためにフィールド追加とメソッド上書き
    image = forms.ImageField(label='画像', required=False)
    
    def save(self, request):
        user = super().save(request)
        user.image = self.cleaned_data['image']
        user.save()
        return user
