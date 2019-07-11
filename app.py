from flask import Flask, render_template, flash
from wtforms import SubmitField, StringField, validators, BooleanField
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
import os, math
import matplotlib.pyplot as plt


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
        flash(
            "You submitted name {a_side} via button {a_angle}".format(
                a_side=form.a_side.data,
                a_angle=form.a_angle.data
            )
        )

        return render_template('index.html', form=form)
    return render_template("index.html", form=form)


if __name__ == '__main__':
    app.run()

