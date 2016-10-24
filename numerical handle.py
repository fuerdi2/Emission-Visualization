import json
import schedule
import random
import time
import math
Roadfuyang = [{'lat':31.879041,'lng':117.293976},{'lat':31.877964,'lng':117.293743},{'lat':31.877025,'lng':117.293563},{'lat':31.875807,'lng':117.293257},{'lat':31.874204,'lng':117.292912},{'lat':31.87335,'lng':117.292647},{'lat':31.872023,'lng':117.292328},{'lat':31.871253,'lng':117.29217}];
Roadshouchun = [{'lat':31.871859,'lng':117.299415},{'lat':31.872123,'lng':117.297947},{'lat':31.872437,'lng':117.296375},{'lat':31.873307,'lng':117.292552},{'lat':31.874116,'lng':117.289202},{'lat':31.874833,'lng':117.285451}];
def export():
   print ("I am generating json!")
   HeatData={'data':[]}
   kv={}
   for i in range (len(Roadfuyang)-1):
       k = (Roadfuyang[i+1]['lat']-Roadfuyang[i]['lat'])/(Roadfuyang[i+1]['lng']-Roadfuyang[i]['lng']);
       l=(Roadfuyang[i+1]['lng']-Roadfuyang[i]['lng'])/100;
       for m in range(1,100):
         X=Roadfuyang[i]['lng']+m*l;
         Y=Roadfuyang[i]['lat']+m*l*k;
         kv['lat'] = Y;
         kv['lng']=X;
         kv['count']=m*random.random();
         HeatData['data'].append(kv.copy());
   for j in range (len(Roadshouchun)-1):
       k = (Roadshouchun[j+1]['lat']-Roadshouchun[j]['lat'])/(Roadshouchun[j+1]['lng']-Roadshouchun[j]['lng']);
       l=(Roadshouchun[j+1]['lng']-Roadshouchun[j]['lng'])/100;
       for n in range(1,100):
         X=Roadshouchun[j]['lng']+n*l;
         Y=Roadshouchun[j]['lat']+n*l*k;
         kv['lat'] = Y;
         kv['lng']=X;
         kv['count']=m*random.random();
         HeatData['data'].append(kv.copy());
         
   HeatData['NoX']=math.sin(random.random())**2*30;
       
   with open('D:/xampp/htdocs/Googlemap/baidudata.json','w') as f:
     json.dump(HeatData,f);
     
schedule.every(4).seconds.do(export)
while True:
   schedule.run_pending()
   time.sleep(1)
