#Program To Find the smallest number
arr = [25, 11, 7, 75, 56];   
    
min = arr[0];    
     
#Loop through the array    
for i in range(0, len(arr)):    
    #Compare elements of array with min    
   if(arr[i] < min):    
       min = arr[i];    
     
print("Smallest element present in given array: " + str(min));    




