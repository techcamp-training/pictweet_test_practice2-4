from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()  # カスタムユーザーモデルを取得
        fields = ('email', 'nickname',)  # 'email' と 'nickname' を追加