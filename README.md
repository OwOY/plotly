<p align='center'>
  <img src="https://images.prismic.io/plotly-marketing-website/b91638ab-80b7-446d-8a83-b6d911bd1519_Plotly_logo.png?auto=compress,format"/>
</p>



- 長條圖
```
import plotly.graph_objects as go
test = {'a':123, 'b':400, 'c':789, 'd':753, 'e':532}
bar = go.Bar(x=list(test.keys()), y=list(test.values()), text = list(test.values()), textposition = 'outside')
fig = go.Figure(scatter)
fig.update_layout(title = f'{折線圖名稱}',
                  xaxis_title = f'{x軸name}',
                  yaxis_title = f'{y軸name}')
fig.show()
```
![image](https://user-images.githubusercontent.com/63274030/144008722-b32fb44f-5c2f-4ae2-894f-8fadad794cae.png)  

----  
- 餅狀圖         
```
import plotly.graph_objects as go  
test = {'a':123, 'b':400, 'c':789, 'd':753, 'e':532}
pie = go.Pie(labels=list(test.keys()), values=list(test.values()))
fig = go.Figure(pie)	
fig.update_layout(title='測試')
fig.show()
```
![image](https://user-images.githubusercontent.com/63274030/144010610-ce57948e-d7d8-491a-add1-8df65232a233.png)  

----
- 環形餅狀圖
```
import plotly.graph_objects as go  
test = {'a':123, 'b':400, 'c':789, 'd':753, 'e':532}
pie = go.Pie(labels=list(test.keys()), values=list(test.values()), hole=0.6)
fig = go.Figure(pie)	
fig.update_layout(title='測試')
fig.show()
```
![image](https://user-images.githubusercontent.com/63274030/144011012-7607e2c4-570f-432a-a9a7-da40d03a2dd7.png)  

----  
- 折線圖
```
import plotly.graph_objects as go  
test = {'a':123, 'b':400, 'c':789, 'd':753, 'e':532}
scatter = go.Scatter(x=list(test.keys()), y=list(test.values()), mode='lines', name='testline')
fig = go.Figure(scatter)
fig.update_layout(title = f'{折線圖名稱}',
                  xaxis_title = f'{x軸name}',
                  yaxis_title = f'{y軸name}')
fig.show()
```
![image](https://user-images.githubusercontent.com/63274030/144008974-bb72e03c-3553-4db7-95d3-cc494c92add0.png)  

----  
