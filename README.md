# Multi-thread Decorator
A simple Python decorator function for executing "1 to 1" mappings in a paralleled way using multi-threading technique. It can be applied in many cases to increase efficiency greatly. I have tried using it to **accelerate geocoding task by 20-30 times**.

## Function Arguments
```python
multiThread(func, List, threadNum = 20)
```
**1. func:** <br>the function to be decorated. It should have one main input argument.<br><br>
**2. List:** <br>the input data to be mapped by the function. It should be an iterable variable.(list, array, series etc.) <br><br>
**3. threadNum:** <br>The number of threads to be used in the function, default 20. It should be adjusted according to different tasks and CPU capacities. Default 20 is set for geocoding task.

## Function output
The list of outputs of the original function in **the same order as the input data**. Although multi-threading sometimes processes data in a random order, the passing of order number into local thread in the code solves this problem. 
```python
def square(x):
    return x**2
    
multiThread(square, [0,1,2,3,4,5], threadNum = 2)
#output will be [0,1,4,9,16,25]
```

## Use Example (Geocoding)
Here is an example of how the function can be used to do geocoding with data in [geocode data.csv](https://github.com/hzjken/multi-thread-decorator/blob/master/geocode%20data.csv).
<br><br>**Preparation Work**
```python
import pandas as pd
import geopy

data = pd.read_csv("geocode data.csv")
addressList = data['address']
latLonList = list(zip(data['lat'],data['lon']))
```
**Multi-threaded geocoding with ArcGIS API**
```python
g = geopy.geocoders.ArcGIS()
geoResult = multiThread(g.geocode, addressList, threadNum = 10)
geoResult = [(i,x[-1]) for i,x in enumerate(geoResult) if x != None]
```
**Multi-threaded reverse-geocoding**
```python
revGeoFunc = lambda x:g.reverse(x,timeout=5) #longer timeout helps to reduce error when thread number is big
revGeoResult = multiThread(revGeoFunc, latLonList, threadNum = 10)
revGeoResult = [(i,x[0]) for i,x in enumerate(revGeoResult) if x != None]
```
With multi-threading, the processing speed for geocoding can be increased roughly by **20 times**. Theoretically, as long as the number of threads doesn't exceed the limit of processor and geocoding server, the higher the thread number, the faster the geocoding will be. However, more threads will bring heavier burden to the server, which might lead to higher error rate in the geocoding. Therefore, you will need to choose a proper thread number for a specific task.<br>

In short, when dealing with large list mapping, this multi-thread decorator can be used to accelerate the process, especially when an external API needs to be called or internet services are required. 

**Hope this function helps!**
