####################################################################
#####	Creating Graph using latitude and Logitude Dataset	########
#####	Artificial Intelligence (CS F407)					########
##### 	@author: Saurabh,Akhil					`			########
####################################################################	


import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import vincenty
import pickle
import numpy as np
print ('Importing Libraries')
df=pd.read_csv("cordinates.csv")

list_of_places = []

class Node():
	def __init__(self,name,nodeid):
		self.children = dict()
		self.node_child = dict()
		self.name = name
		self.time = 0
		self.latitude = 0
		self.longitude = 0
		self.nodeid = nodeid
		
	def add_children(self,new_location,distance):
	'''Function to add Children'''	
		if len(self.children)<5:
			#print('1')
			self.children[new_location] = distance
			self.node_child[new_location] = root.node_child[new_location]
		else:
			temp=str(max(self.children,key=self.children.get))
			#print('2')
			if self.children[temp]>distance:
			#	print('3')
				del(self.children[temp])
				del(self.node_child[temp])
				self.children[new_location] = distance
				self.node_child[new_location] = root.node_child[new_location]
			else:
				pass;
			
			
		
	def add_root_child(self,new_location,nodeid):
	'''Function to add children to root node'''
		self.children[new_location] = (0,0)
		#Child Node is created
		self.node_child[new_location] = Node(new_location,nodeid)#Node Constructor Called
		
root = Node('Root',-1)#Dummy Node

for i in range(len(df)):
	list_of_places.append(df.loc[i]['location'])
	#print (df.loc[i]['location'])
	root.add_root_child(df.loc[i]['location'],i)

for i in list_of_places:
	print(i)
	for j in list_of_places:
		if i==j:
			pass
		else:

			lat_i = df[df['location']==i]['latitude']
			long_i = df[df['location']==i]['longitude']
			
			lat_j = df[df['location']==j]['latitude']
			long_j = df[df['location']==j]['longitude']
			
			lon_i  = long_i.tolist()
			lon_j = long_j.tolist()
			
			lati = lat_i.tolist()
			latj = lat_j.tolist()
			
			
			x=(lati[0],lon_i[0])
			y=(latj[0],lon_j[0])
			#print (x,':',y)
			dis=vincenty(x,y).miles
			
			root.node_child[i].add_children(j,dis)
			
	#print(root.node_child[i].children)
					

	
adj_mat = []

for i in range(len(list_of_places)):
	X = root.node_child[list_of_places[i]].children
	y = np.zeros(len(list_of_places)).tolist()
	
	for keys,value in X.iteritems():
		key_id = list_of_places.index(keys)
		y[key_id] = value
	adj_mat.append(y)


for i in range(len(adj_mat)):
	for j in range(len(adj_mat)):
		if adj_mat[i][j] > 0:
			adj_mat[j][i] = adj_mat[i][j]
			

print ('Saving the adjancy matrix........')				
import pickle
with open('adj_mat.pkl','wb') as fp:
	pickle.dump(adj_mat,fp,-1)
	

	
		
		
			
 			
#root.node_child[j].add_children(i,dis,10)
			
	


			
		
	

