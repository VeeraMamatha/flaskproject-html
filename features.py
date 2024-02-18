from flask import Flask,render_template
FAI=Flask(__name__)

@FAI.route('/sendhtml')
def sendhtml():
    return render_template('send_html.html',name='AlluArjun')

@FAI.route('/properties')
def properties():
    return render_template('properties_html.html')
if__name__='__main__'
FAI.run(debug=True)   
