from flask import Flask, render_template
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from bs4 import BeautifulSoup 
import requests

#don't change this
matplotlib.use('Agg')
app = Flask(__name__) #do not change this

#insert the scrapping here
url_get = requests.get('https://www.exchange-rates.org/exchange-rate-history/usd-idr')
soup = BeautifulSoup(url_get.content,"html.parser")

#find your right key here
table = soup.find('table',attrs={'class':'history-rates-data'})
data1 = table.find_all('tr',attrs={'class':'odd'})

row_length = len(data1)

temp = [] #initiating a list 

for i in range(1, row_length):
#insert the scrapping process here
    Tanggal = table.find_all('a',attrs={'class':'n'})[i].text
    change_rate = table.find_all('span',attrs={'class':'n'})[i].text
    change_rate = change_rate.strip()
    temp.append((Tanggal,change_rate))
temp = temp[::-1]

#change into dataframe
data = pd.DataFrame(temp,columns=('Tanggal','ChangeRate'))

#insert data wrangling here
data['Tanggal']=pd.to_datetime(data['Tanggal'])
data['ChangeRate']=data['ChangeRate'].replace("IDR","",regex=True)
data['ChangeRate']=data['ChangeRate'].replace("1 USD =","",regex=True)
data['ChangeRate']=data['ChangeRate'].replace(",","",regex=True)
data['ChangeRate']=data['ChangeRate'].astype('int64')
#end of data wranggling 

@app.route("/")
def index(): 
	
	card_data = f'{data["ChangeRate"].mean().round(2)}' #be careful with the " and ' 

	# generate plot
	#ax = data.plot(figsize = (20,9)) 
	
	# Rendering plot
	data.plot(kind='line',y = 'ChangeRate', title='Nilai Tukar Rupiah Terhadap USD'
         ,ylabel="IDR", xlabel='Tanggal')
	# Do not change this
	figfile = BytesIO()
	plt.savefig(figfile, format='png', transparent=True)
	figfile.seek(0)
	figdata_png = base64.b64encode(figfile.getvalue())
	plot_result = str(figdata_png)[2:-1]

	# render to html
	return render_template('index.html',
		card_data = card_data, 
		plot_result=plot_result
		)


if __name__ == "__main__": 
    app.run(debug=True)