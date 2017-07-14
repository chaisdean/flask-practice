from flask import Flask,render_template, redirect, request

message=Flask(__name__)

@message.route('/')

def index():
    print "Did this work!?"
    return render_template('index.html')

@message.route('/ninjas')
def ninja():
    print 'This is Ninja'
    return render_template('ninjas.html')

@message.route('/form', methods=['POST'])
def form():
    print 'something'
    print request.form
    return redirect('/')
message.run(debug=True)
