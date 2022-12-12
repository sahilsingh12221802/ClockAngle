# Function to compute the angle between the hour and minute hand
def findAngle(hh, mm):
 
    # handle 24-hour notation
    hh = hh % 12
 
    # find the position of the hour's hand
    h = (hh * 360) // 12 + (mm * 360) // (12 * 60)
 
    # find the position of the minute's hand
    m = (mm * 360) // (60)
 
    # calculate the angle difference
    angle = abs(h - m)
 
    # consider the shorter angle and return it
    if angle > 180:
        angle = 360 - angle
 
    return angle
 
 
# Clock Angle Problem
if __name__ == '__main__':
 
    hh = int(input())
    mm = int(input())
 
    print("The angle between Hour hand and Minute hand is",findAngle(hh, mm) )
    
#Made by 
#Name:- Sahil Singh, Lakshay Malia, PN Venkata Sai
#Roll No:- 55,53,54
#Registration No:- 12221802,12222319,12220225