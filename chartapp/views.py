from django.shortcuts import render
import pandas as pd

json_data = pd.read_json('https://cdn.jsdelivr.net/gh/highcharts/highcharts@v7.0.0/samples/data/world-population-density.json')

def ChartJS(request):
    data = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
    total_count = data[data.columns[-1]].sum()
    temp = data[['Country/Region', data.columns[-1]]].groupby('Country/Region').sum()
    temp = temp.reset_index()
    temp.columns = ['Country/Region', 'Values']
    temp = temp.sort_values(by='Values', ascending=False)
    country_names = temp['Country/Region'].tolist()
    people_effected = temp['Values'].tolist()
    map_data=WorldMap(country_names,temp)
    context = {
        'total_count':total_count,
         'country_names':country_names,
        'people_effected':people_effected,
        'map_data':map_data
    }
    return render(request,'index.html', context)



def WorldMap(country_names,temp):
    dataForMap = []
    for i in country_names:
        try:
            temp_map = json_data[json_data['name'] == i]
            t = {}
            t["code3"] = list(temp_map['code3'].values)[0]
            t["name"] = i
            t["value"] = temp[temp['Country/Region'] == i]['Values'].sum()
            t["code"] = list(temp_map['code'].values)[0]
            dataForMap.append(t)
        except:
            pass
    return dataForMap

