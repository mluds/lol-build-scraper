import requests as reqs
import os
import json
import tkinter as tk

class App(tk.Frame):
  def __init__(self, master):
    tk.Frame.__init__(self, master)
    self.pack()
    self.createWidgets()

  def createWidgets(self):
    tk.Button(self, text="Browse").pack()

def download(dir):
  domain = 'http://www.lolflavor.com'
  response = reqs.get(domain + '/data/champion.json').json()
  champions = [c for c in response['data']]
  roles = ['lane', 'jungle', 'support', 'aram']

  for c in champions:
    for r in roles:
      response = reqs.get(domain + '/champions/' + c + '/Recommended/' +
        c + '_' + r + '_scrape.json').text

      try:
        json.loads(response)
      except ValueError:
        continue

      file = dir + '/Config/Champions/' + c + '/Recommended/' + r + '.json'

      if not os.path.exists(os.path.dirname(file)):
        os.makedirs(os.path.dirname(file))

      with open(file, 'w') as f:
        f.write(response)

if __name__ == '__main__':
  #download('C:/Riot Games/League of Legends')
  App(tk.Tk()).mainloop()
