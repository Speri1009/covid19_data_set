import pandas as pd


url_confirmed  = "https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_confirmed_global.csv&filename=time_series_covid19_confirmed_global.csv"
url_death = "https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_deaths_global.csv&filename=time_series_covid19_deaths_global.csv"
url_recovered = "https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_recovered_global.csv&filename=time_series_covid19_recovered_global.csv"
df_confirmed = pd.read_csv(url_confirmed)
df_confirmed['Case Type']="Confirmed"
df_confirmed= pd.DataFrame(df_confirmed)
df_death = pd.read_csv(url_death)
df_death['Case Type']="Death"
df_death = pd.DataFrame(df_death)
df_recovered = pd.read_csv(url_recovered)
df_recovered['Case Type']="Recovered"
df_recovered=pd.DataFrame(df_recovered)
#print (df_confirmed.shape,df_death.shape,df_recovered.shape)
Covid_19 = pd.concat([df_confirmed,df_death,df_recovered])
#print (Covid_19)

Covid_19_data =Covid_19.melt(id_vars=['Province/State','Country/Region','Lat','Long','Case Type'])
Covid_19_data.columns = ['Province/State','Country/Region','Lat','Long','Case Type','Date','Case Count']
Covid_19_data['Date']= pd.to_datetime(Covid_19_data['Date']) 
print((Covid_19_data['Date']))
Covid_19_data.to_csv(r'C:\Users\Lenovo\Desktop\Data set\Covid 19\Covid_19.csv', index = False)
