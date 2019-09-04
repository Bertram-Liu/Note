from django import  forms
from .models import  *
'''练习自定义注册表单 RegisterForm
uname 
upwd
uemial
uphone
isActive
'''
class RegisterForm(forms.Form):
    uname = forms.CharField(label='用户名')
    upwd = forms.CharField(label='密码')
    uemail = forms.EmailField(label='邮箱')
    uphone = forms.CharField(label='手机')
    isActive = forms.BooleanField(label='状态')

class LoginForm(forms.ModelForm):
    class Meta:
        model = Users
        # fields = '__all__'
        fields = ['uphone','upwd']
        labels = {
            'uphone':'登录账号',
            'upwd':'登录密码'
        }
        widgets = {
            'upwd':forms.PasswordInput(
                attrs={
                    'placeholder': "请输入密码",
                    'class':'form-control'
                }
            ),
            #为uphone添加小控件TextInput
            #设置HTML属性placeholder
            'uphone': forms.TextInput(
                attrs={
                    'placeholder': "请输入手机号/邮箱/账号",
                    #指定css样式
                    'class': 'form-control'
                }

            )
        }