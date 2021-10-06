from datetime import datetime
now_method = datetime.now()
currentTime = now_method.strftime("%H:%M:%S")
print("Current Time =", currentTime)
