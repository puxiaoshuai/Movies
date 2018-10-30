
from  flask_wtf import FlaskForm
from  wtforms import StringField,PasswordField,SubmitField
from  wtforms.validators import DataRequired,EqualTo

class RegistForm(FlaskForm):
    #DataRequired: must input
    username=StringField(label=u"用户名",validators=[DataRequired(u"必须填写")])
    password=PasswordField(label=u"密码",validators=[DataRequired(u"必须填写")])
    password2=PasswordField(label=u"确认密码",validators=[DataRequired(u"必须填些密码"),EqualTo('password',u"两次输入不一致")])
    submit=SubmitField(u"注册")
    def validata_phone(self,field):
        pass
        return True
    #sure phone