import pandas as pd 
import plotly.express as px
df=pd.read_csv(r"C:\Users\a2z\Downloads\Data-visualization-master\Data-visualization-master\csv files\abc1.csv")
fig=px.bar(df,x="date",y="cases",color="country",title="Covid data for different countries")
fig.show()