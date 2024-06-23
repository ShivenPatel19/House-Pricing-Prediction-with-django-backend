from django.shortcuts import render
import pandas as pd
from sklearn import linear_model

def index(request):
    if request.method == 'POST':
        bedroom = request.POST['Bedrooms']
        bathroom = request.POST['Bathrooms']
        floors = request.POST['Floors']
        sq_feet = request.POST['SQ_FEET']

        df = pd.read_csv('csv/data.csv')
        reg = linear_model.LinearRegression()
        reg.fit(df[['bedrooms','bathrooms','sqft_living','floors']],df.price)
        price = reg.predict([[int(bedroom),int(bathroom),int(sq_feet),int(floors)]])

        context = {
            'bedroom':bedroom,
            'bathroom':bathroom,
            'floors':floors,
            'sq_feet':sq_feet,
            'price':price,
        }
        return render(request,'index.html',context)
    else:
        return render(request,'index.html')