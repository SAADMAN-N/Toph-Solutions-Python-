H , M = map(int , input().split())


hour_angle = (H*60 + M)*0.5
minute_angle = 6 * M
angle = hour_angle - minute_angle
    
angle = min(360 - angle , angle)
print(angle)

 