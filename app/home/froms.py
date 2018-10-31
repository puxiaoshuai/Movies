from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, Form, IntegerField
from wtforms.validators import DataRequired, EqualTo, length,NumberRange
"""
验证层
"""
class RegistForm(Form):
    # DataRequired: must input
    username = StringField("用户名", validators=[DataRequired("不能为空"), length(min=5, max=6)])
    password = PasswordField("密码", validators=[DataRequired("请填写")])
    password2 = PasswordField("确认密码", validators=[DataRequired("请填写"), EqualTo('password',"两次输入不一致")])


    def validata_phone(self, field):
        pass
        return True
    # sure phone


class SearchForm(Form):
    q = StringField(validators=[DataRequired(),length(min=2, max=10)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
