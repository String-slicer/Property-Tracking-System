import json
from flask import Flask,request,render_template,jsonify
from web3 import Web3,HTTPProvider
import urllib3

blockchain="http://127.0.0.1:7545"

def connect():
    web3=Web3(HTTPProvider(blockchain))
    web3.eth.defaultAccount=web3.eth.accounts[0]
    artifact="../build/contracts/PropertyTrackingSystem.json"
    
    with open(artifact) as f:
        artifact_json=json.load(f)
        contract_abi=artifact_json['abi']
        contract_address=artifact_json['networks']['5777']['address']
    contract=web3.eth.contract(
        abi=contract_abi,
        address=contract_address
    )
    return contract,web3

app=Flask(__name__)

@app.route('/registerProperty',methods=['GET','POST'])
def registerProperty():
    id=int(request.args.get('id'))
    location=request.args.get('location')
    size=int(request.args.get('size'))
    contract,web3=connect()
    try:
        tx_hash=contract.functions.registerProperty(id,location,size).transact()
        web3.eth.waitForTransactionReceipt(tx_hash)
        return 'Property Registered'
    except:
        return 'Already registered'

@app.route('/transferOwnership',methods=['GET','POST'])
def transferOwnership():
    id=int(request.args.get('id'))
    address=request.args.get('address')
    contract,web3=connect()
    try:
        tx_hash=contract.functions.transferOwnership(id,address).transact()
        web3.eth.waitForTransactionReceipt(tx_hash)
        return 'ownership of the property is transformed successfully'
    except:
        return 'failed in transformation of ownership'

@app.route('/getPropertyDetails',methods=['GET','POST'])
def getPropertyDetails():
    id=int(request.args.get('id'))
    contract,Web3=connect()
    data=contract.functions.getPropertyDetails(id).call()
    return (jsonify(data))

@app.route('/',methods=['GET','POST'])
def registerpropertypage():
    return render_template('registerproperty.html')
@app.route('/a',methods=['GET','POST'])
def a():
    return render_template('index.html')

@app.route('/transferownershippage',methods=['GET','POST'])
def transferownershippage():
    return render_template('transferownership.html')

@app.route('/getpropertydetailspage',methods=['GET','POST'])
def getpropertydetailspage():
    return render_template('getpropertydetails.html')

@app.route('/registerpropertyform',methods=['GET','POST'])
def registerpropertyform():
    id=request.form['id']
    location=request.form['location']
    size=request.form['size']
    pipe=urllib3.PoolManager()
    response=pipe.request('get','http://127.0.0.1:4000/registerProperty?id='+id+'&location='+location+'&size='+size)
    response=response.data
    response=response.decode('utf-8')
    return render_template('registerproperty.html',response=response)

@app.route('/transferownershipform',methods=['GET','POST'])
def transferownershipform():
    id=request.form['id']
    address=request.form['address']
    pipe=urllib3.PoolManager()
    response=pipe.request('get','http://127.0.0.1:4000/transferOwnership?id='+id+'&address='+address)
    response=response.data
    response=response.decode('utf-8')
    return render_template('transferownership.html',response=response)

@app.route('/getpropertydetailsform',methods=['GET','POST'])
def getpropertydetailsform():
    id=request.form['id']
    pipe=urllib3.PoolManager()
    response=pipe.request('get','http://127.0.0.1:4000/getPropertyDetails?id='+id)
    response=response.data
    response=response.decode('utf-8')
    return render_template('getpropertydetails.html',response=response)

if __name__=="__main__":
    app.run(
        host='0.0.0.0',
        port=4000
    )
