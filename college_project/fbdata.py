from firebase import Firebase
import urllib.request
import json


config = {
    "apiKey": "AIzaSyAaCMZTYvOOaHioUYUn7vgjDgWjJJOQw5g",
    "authDomain": "collegeproject-731cc.firebaseapp.com",
    "databaseURL": "https://collegeproject-731cc.firebaseio.com",
    "projectId": "collegeproject-731cc",
    "storageBucket": "collegeproject-731cc.appspot.com",
    "messagingSenderId": "486317977578",
    "appId": "1:486317977578:web:bcfb982546f6e6871dcc93",
    "measurementId": "G-VXMEM3XYFD"
  }

data ={
          "poles":{"cheerlights":False,  "pole1":{"switchStatus":True, "faultStatus": True},
            "pole2":{"switchStatus":False, "faultStatus": False},
            "pole3":{"switchStatus":False, "faultStatus": False},
            "pole4":{"switchStatus":False, "faultStatus": False},
            "pole5":{"switchStatus":False, "faultStatus": False},
            "pole6":{"switchStatus":False, "faultStatus": False},
            "pole7":{"switchStatus":False, "faultStatus": False}}}

def checkNetwork (host = 'https://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        with open('data.json', 'w') as json_file:
            json.dump(data, json_file)
        print("No Internet")
        print("Data locally saved")
        return False


def updateOnCloud():
    if checkNetwork():
        try:
            firebase = Firebase(config)
            db = firebase.database()
            db.update(data)
            print("Data Pushed")
        except:
            print("Firebase Error")


def syncWithCloud():
    if checkNetwork():
        try:
            firebase = Firebase(config)
            db = firebase.database()
            poles = db.child("poles").child("pole1").child("switchStatus").get()
            #print(poles.val())

            #for pole in poles.each():
                #print(pole.key())
               # print(pole.val())
            #print("Data Pulled")
            return poles.val()
        except:
            print("Firebase Error")
            return False



#updateOnCloud()
#syncWithCloud()