import pandas as pd
import numpy as np
import plotly.express as px


url="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
data=pd.read_csv(url)
data_format=data.groupby('Country/Region', as_index=False).sum().drop(['Lat','Long'],axis=1)
#columns={i:data_format[i][0] for i in range(np.shape(data_format)[1])}
#data_format=data_format.rename(columns=columns)

#tidy_data=data_format.melt(id_vars='Country/Region')
#fig=px.line(tidy_data,x='variable', y='value', color='Country/Region')
#fig.show()

fig = go.Figure()
for row in data_format.iterrows():
    to_keep=row[1][1:].values!=0
    if any(to_keep):
        fig.add_trace(go.Scatter(x=np.array(range(-1,to_keep.sum())), y=np.append([0],row[1][1:].values[to_keep]),
                        mode='lines',
                        name=row[1][0]))
    else :
        print(row[1][0])
fig.update_layout(title='Number of deaths per Country',
                   xaxis_title='Days after the first death',
                   yaxis_title='Number of deaths')
fig.show()
