# Multi-thread Decorator
A Python decorator for executing "1 to 1" mappings in a paralleled way using multi-threading technique. It can be applied in many cases to increase efficiency greatly. I have tried using it to accelerate geocoding task by 20-30 times.

# Advantages
1. Multi-threading in the function enables you to do geocoding for large batch data much faster regardless of net speed.
2. The function will not be stopped by geocoding errors (timeout, no matched address etc) and will handle error terms by looping them over again and again until no improvement can be made. (all the errors cannot be geocoded anymore)

# Prerequisites
1. Library pandas & threading. (contained in Anaconda) 
2. The installation of geopy library. (compulsary)
3. Google Maps geocoding API key. (recommend)

Your requests for geocoding will be more stable and can go up to 100,000 times a day with an API key. Otherwise, the request limitation will be 2,500 times per day. Most importantly, the 300 dollar voucher for Google Cloud new user can already help you do a lot of geocoding! So have a try using the API key to do the geocoding.
Details of limitation and fee will be in https://developers.google.com/maps/documentation/geocoding/usage-limits.

# Function input
batch_geocode(address_df, thread_num = 20, key = "")

1. address_df: a list, array, series or one-dimension dataframe of address to do geocoding, will be better if no duplicates.
2. thread_num: the number of multi-threading line. Default is set to be 20. The larger the number, the faster the geocoding process. You can adjust the number according to your net speed, but please make sure it doesn't exceed the upper limit of 50 requests per second set by Google.
3. key: Google Maps Geocoding API key, default is no key.

# Function output
The batch_geocode function's output is a 3-dimension dataframe contains columns 'address', 'lat', 'lon'.

# Something else
1. There are totally 3 functions in the script, the third one (batch_geocode) should be the one you might directly use.
2. Output order will be the same as the input order if no duplicates in the input data.
