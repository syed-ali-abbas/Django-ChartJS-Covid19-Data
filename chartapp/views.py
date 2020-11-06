from django.shortcuts import render
import pandas as pd

def ChartJS(request):
    data = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
    total_count = data[data.columns[-1]].sum()
    temp = data[['Country/Region', data.columns[-1]]].groupby('Country/Region').sum()
    temp = temp.reset_index()
    temp.columns = ['Country/Region', 'Values']
    temp = temp.sort_values(by='Values', ascending=False)
    country_names = temp['Country/Region'].tolist()
    people_effected = temp['Values'].tolist()
    context = {
        'total_count':total_count,
         'country_names':country_names,
        'people_effected':people_effected
    }



    return render(request,'index.html', context)