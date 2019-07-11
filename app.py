from flask import Flask, render_template, flash
from wtforms import SubmitField, StringField, validators, BooleanField
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
import os
import triangleCreator


class GenerationForm(FlaskForm):
    a_side = StringField('a', [validators.DataRequired()],render_kw={"placeholder": "Side a"})
    a_side_var = BooleanField(label="Is variable?")
    b_side = StringField('b', [validators.DataRequired()],render_kw={"placeholder": "Side b"})
    b_side_var = BooleanField(label="Is variable?")
    c_side = StringField('c', [validators.DataRequired()],render_kw={"placeholder": "Side c"})
    c_side_var = BooleanField(label="Is variable?")

    a_angle = StringField('A', [validators.DataRequired()],render_kw={"placeholder": "Angle A"})
    a_angle_var = BooleanField(label="Is variable?")
    b_angle = StringField('B', [validators.DataRequired()],render_kw={"placeholder": "Angle B"})
    b_angle_var = BooleanField(label="Is variable?")
    c_angle = StringField('C', [validators.DataRequired()],render_kw={"placeholder": "Angle C"})
    c_angle_var = BooleanField(label="Is variable?")

    generate = SubmitField(label='Generate')


app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
csrf = CSRFProtect(app)


@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    form = GenerationForm()
    if form.validate_on_submit():
        data_nums =[form.a_angle.data, form.a_side.data, form.b_angle.data, form.b_side.data, form.c_angle.data, form.c_side.data]
        data =[0,0,0,0,0,0]
        if form.a_angle_var.data == True:
            data[0] = "A"
        if form.b_angle_var.data == True:
            data[2] = "B"
        if form.c_angle_var.data == True:
            data[4] = "C"
        if form.a_side_var.data == True:
            data[1] = "a"
        if form.b_side_var.data == True:
            data[3] = "b"
        if form.c_side_var.data == True:
            data[5] = "c"
        file = triangleCreator.createTriangle(data_nums, data)
        #use annotate() to create labels
        return render_template('triangle.html', user_image=file.name)
    return render_template("index.html", form=form)


if __name__ == '__main__':
    app.run()

