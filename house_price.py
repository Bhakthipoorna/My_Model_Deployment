from flask import Flask, render_template, request,url_for,request
import pickle
import numpy as np
import joblib


model = pickle.load(open('house_price.pkl', 'rb'))

app=Flask(__name__)


@app.route('/')
def hp_home():
    return render_template('hp_home.html')

@app.route('/hp_prediction',methods=['POST'])
def hp_predict():
    data1=request.form['MSSubClass']
    data2=request.form['MSZoning']
    data3=request.form['LotFrontage']
    data4=request.form['LotArea']
    data5=request.form['LotShape']
    data6=request.form['LandContour']
    data7=request.form['LotConfig']
    data8=request.form['LandSlope']
    data9=request.form['Neighborhood']
    data10=request.form['Condition1']
    data11=request.form['HouseStyle']
    data12=request.form['OverallQual']
    data13=request.form['OverallCond']
    data14=request.form['YearBuilt']
    data15=request.form['YearRemodAdd']
    data16=request.form['RoofStyle']
    data17=request.form['Exterior1st']
    data18=request.form['ExterQual']
    data19=request.form['Foundation']
    data20=request.form['BsmtCond']
    data21=request.form['BsmtExposure']
    data22=request.form['BsmtFinType1']
    data23=request.form['BsmtFinSF1']
    data24=request.form['BsmtUnfSF']
    data25=request.form['TotalBsmtSF']
    data26=request.form['HeatingQC']
    data27=request.form['CentralAir']
    data28=request.form['Electrical']
    data29=request.form['GrLivArea']
    data30=request.form['FullBath']
    data31=request.form['BedroomAbvGr']
    data32=request.form['KitchenAbvGr']
    data33=request.form['KitchenQual']
    data34=request.form['Fireplaces']
    data35=request.form['GarageType']
    data36=request.form['GarageFinish']
    data37=request.form['GarageCars']
    data38=request.form['GarageQual']
    data39=request.form['PavedDrive']
    data40=request.form['MoSold']
    data41=request.form['YrSold']
    data42=request.form['SaleType']
    data43=request.form['SaleCondition']

    array=np.array([[data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12,data13,data14,
         data15,data16,data17,data18,data19,data20,data21,data22,data23,data24,data25,data26,data27,data28,data29,data30,
         data31,data32,data33,data34,data35,data36,data37,data38,data39,data40,data41,data42,data43]])
    predict=model.predict(array)
    return render_template('hp_predict.html',output=predict)  
          

if __name__=='__main__':
    app.run(debug=True)
