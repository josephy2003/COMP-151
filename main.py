#for xloc in range(50 ,1000, 86):
#       print(f"I want to draw a line at xposition: {xloc}")
f = open("Project2.txt", 'r')

with open("Project2.txt","r") as f:
    for line in f:
        test = line.split(':')
        print(test[0], test[2])