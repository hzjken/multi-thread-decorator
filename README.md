# Multi-thread Decorator
A simple Python decorator function for executing "1 to 1" mappings in a paralleled way using multi-threading technique. It can be applied in many cases to increase efficiency greatly. I have tried using it to **accelerate geocoding task by 20-30 times**.

## Function Arguments
```python
multiThread(func, List, threadNum = 20)
```
**1. func:** <br>the function to be decorated. It should have one main input argument.<br>
**2. List:** <br>the input data to be mapped by the function. It should be an iterable variable.(list, array, series etc.) <br>
**3. threadNum:** <br>The number of threads to be used in the function, default 20. It should be adjusted according to different tasks and CPU capacities. Default 20 is set for geocoding task.

## Function output
The list of outputs of the original function in **the same order as the input data**.

## Use Example (Geocoding)
1. There are totally 3 functions in the script, the third one (batch_geocode) should be the one you might directly use.
2. Output order will be the same as the input order if no duplicates in the input data.
