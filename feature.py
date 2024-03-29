from flask import Flask,request,render_template
from flask_wtf import Form
from wtforms import StringField,SubmitField

FAI=Flask(__name__)


@FAI.route('/htmlforms',methods=['GET','POST'])
def htmlforms():

    if request.method=='POST':
        fd=request.form
        return fd['un']
    return render_template('htmlforms.html')


class NameForm(Form):
    name=StringField()
    submit=SubmitField()


@FAI.route('/webforms',methods=['GET','POST'])
def webforms():
    NFO=NameForm()

    if request.method=='POST':
        NFDO=NameForm(request.form)
        if NFDO.validate():
            return NFDO.name.data
    return render_template('webforms.html',NFO=NFO)




if __name__=='__main__':
    FAI.run(debug=True)