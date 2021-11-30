import requests
import json
import plotly.graph_objects as go
import time

class Bitcoin:
	def __init__(self):
		self.requests = requests.Session()
		
	def get_response(self):
		response = self.requests.get('https://crypto.cnyes.com/BTC/24h', 
									headers = {
									'Host': 'crypto.cnyes.com',
									'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
									'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
									'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3',
									'Accept-Encoding': 'gzip, deflate',
										}).text
		return response
  
	def response_filter_to_json(self):
		response = self.get_response()
		data = json.loads(response.split('__NEXT_DATA__ = ')[1].split('module=')[0])
		return data
  
	def get_bitcoin(self):
		response = self.response_filter_to_json()
		bitcoin = response['props']['initialState']['coinHistory']['BTC-24h']['items']['c']
		bitcoin_time = response['props']['initialState']['coinHistory']['BTC-24h']['items']['t']
		bitcoin_time = [time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time_stamp)) for time_stamp in bitcoin_time]
		return bitcoin, bitcoin_time

	def output_fig(self):
		bitcoin_dict = {}
		bitcoin_list, bitcoin_time_list = self.get_bitcoin()
		for time, bitcoin in zip(bitcoin_time_list, bitcoin_list):
			bitcoin_dict[time] = bitcoin
		scatter = go.Scatter(x=list(bitcoin_dict.keys()), y=list(bitcoin_dict.values()), mode='lines', name='比特幣幅度折線圖')
		fig = go.Figure(scatter)
		fig.update_layout(title = '比特幣幅度折線圖',
				xaxis_title = 'time',
				yaxis_title = 'gold')
		fig.show()

if __name__ == '__main__':
    bitcoin = Bitcoin()
    print(bitcoin.get_bitcoin())
    bitcoin.output_fig()
