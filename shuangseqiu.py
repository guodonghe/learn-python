import random

def select_ball(self):
    red_balls = list(range(1,34))
    blue_balls = list(range(1,17))
    select_red = []
    select_blue = []
    
    for i in range(6):
        red = random.choice(red_balls)
        select_red.append(red)
        red_balls.remove(red)
    print ('选择的红球为',end=" ")
    print (select_red,end=" ")

    for j in range(1):
        blue = random.choice(blue_balls)
        select_blue.append(blue)
    print ('选择的蓝球为',end=" ")
    print (select_blue)

if __name__ == "__main__":
    number = int(input('你需要几注随机双色球? \n'))
    for i in range(number):
        select_ball(i)
        
