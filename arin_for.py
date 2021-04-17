"""
friends = ['ahmet', 'mehmet', 'ebru', 'mahmut', 'ayşe']

x = 0
while (x < len(friends)):
    friend = friends[x]
    x = x + 1
    if friend == 'mahmut':
        continue
    print(friend)
    """
"""
minNum = int(input('Please min number: '))
maxNum = int(input('Please max number: '))

for evenNum in range(minNum, maxNum):
    if evenNum % 2 != 0:
        continue
    else:
        print(evenNum)
        """
"""        
import random
xnum = random.randint(1, 100)

num = int(input('Lütfen 1 ile 100 arasında bir sayı girin: '))

while num != xnum:
    if num < xnum:
        print(f'{num} daha büyük bir sayı giriniz')
        num = int(input())
    else:
        print(f'{num} daha küçük bir sayı giriniz')
        num = int(input())
        
print(f' Tebrikler {num} yakaladınız!')
"""
"""
celciuses = [20, 25, 30, 35]
kelvin = []
fahrenheit = []

for c in celciuses:
    k = c + 273
    kelvin.append(k)
    f = c * 9 / 5 + 32
    fahrenheit.append(f)
    
print(kelvin)
print(fahrenheit)
"""
"""
num = int(input('Lütfen bir sayı giriniz: '))

if num < 0:
    print('Negatif bir sayı girdiniz')
else:
    sum = 0
    while num > 0:
        sum += num
        num -= 1
    print('Tomlam sayı:', sum)"""
    
    #imports
import time
import random
import turtle

delay = 0.1

#scores
score = 0
high_score = 0

# set up screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor('yellow')
wn.setup(width=600, height=600)
wn.tracer(0)
 
#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"
 
#snake food 
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0,100)
 
segments = []
 
#scoreboards
 
sc = turtle.Turtle()
sc.speed(0)
sc.shape("square")
sc.color("black")
sc.penup()
sc.hideturtle()
sc.goto(0, 260)
sc.write("score: 0 High score: 0", align= "center", font=("ds-digital", 24, "normal"))

#Function
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction !="left":
        head.direction = "right"
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

#keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

#mainLoop
while True:
    wn.update()
    
    #check collision with border area
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        
        #hide the segments of body
        for segment in segments:
            segment.goto(1000,1000) #out of range
            
        #clear the segments
        segments.clear()
        
        #reset score
        score = 0
        
        #reset delay
        delay = 0.1
        sc.clear()
        st.write("score: {} High score: {}:" .format(score, high_score), align="center", font=("ds-digital", 24, "normal"))

#check collision with food
if head.distance(food) < 20:
    #move the food to random place 
    x = random.randint(-290,290)
    y = random.randint(-290,290)
    food.goto(x,y)
    
    #add a new segment to the head 
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.color("black")
    new_segment.penup()
    segments.append(new_segment)
    
    #shorten the delay
    delay -= 0.001
    #increase the score
    score += 10
    
    if score > high_score:
        high_score = score
sc.clear()
sc.write("score: {} High score: {}:" .format(score, high_score), align="center", font=("ds-digital", 24, "normal"))

#move the segments in reserve order 
for index in range(len(segments)-1,0,-1):
    x = head.xcor()
    y = head.ycor()
    segments[0].goto(x,y)

move()

#check for collision with body
for segment in segments:
    if segment.distance(head)<20:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        
        #hide segments
        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()
        score = 0
        delay = 0.1
        
        #update the score
        sc.clear()
        sc.write("score: {} High score: {}:" .format(score, high_score), align="center", font=("ds-digital", 24, "normal"))
    time.sleep(delay)
wn.mainloop()
 