import pandas as pd
import plotly.graph_objects as go
import csv

df=pd.read_csv("student1.csv")
stud_df=df.loc[df["student_id"]=="TRL_zet"]
print(stud_df.groupby("level")["attempt"].mean())

a=go.Figure(go.Bar(
    x=stud_df.groupby("level")["attempt"].mean(),
    y=["level1","level2","level3","level4"],
    orientation='h'))
a.show()



 
