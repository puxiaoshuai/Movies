
from  flask_wtf import FlaskForm
from  wtforms import StringField,PasswordField,SubmitField
from  wtforms.validators import DataRequired,EqualTo,length

class RegistForm(FlaskForm):
    #DataRequired: must input
    username=StringField("用户名",validators=[DataRequired(),length(min=5,max=6)])
    password=PasswordField("密码",validators=[DataRequired()])
    password2=PasswordField("确认密码",validators=[DataRequired(),EqualTo('password',u"两次输入不一致")])
    sumit=SubmitField("提交")
    def validata_phone(self,field):
        pass
        return True
    #sure phone