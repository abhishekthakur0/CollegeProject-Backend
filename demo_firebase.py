from firebase import firebase as fb

app = fb.FirebaseApplication('https://collegeproject-731cc.firebaseio.com/poles')
result = app.get('/pole1',name='None')
print(result)