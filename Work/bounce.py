# bounce.py
#
# Exercise 1.5

# a rubber ball dropped from a height of 100 meters and and each time it hits the ground, i
#t bounces back up to 3/5 the height it fell. 
#Write a program bounce.py that prints a table showing the height of the first 10 bounces.
hitNo=0
height=100
rebounce = height
while hitNo<10:
    rebounce = rebounce * 3/5
    print(hitNo + 1, round(rebounce,4))
    hitNo = hitNo +1
