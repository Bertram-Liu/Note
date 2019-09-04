#导入django提供的froms
from django import forms

LEVEL_CHOICE = (
    ('1','好评'),
    ('2','中评'),
    ('3','差评'),
)
#创建class
class RemarkForm(forms.Form):
    title = forms.CharField(max_length=10,label='评论标题')
    email = forms.EmailField(label='电子邮箱')
    #单独的input无法满足需求 需要添加控件
    #forms.Textarea将当前的控件变为多行文本域textarea
    content = forms.CharField(
        label='评论内容',widget=forms.Textarea
    )
    #ChoiceField需要提供选项
    level = forms.ChoiceField(label='评论级别',choices=LEVEL_CHOICE)
    isSaved = forms.BooleanField(label='是否保存',required=False)