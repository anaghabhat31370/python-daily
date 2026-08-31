battery = 80
obstacle = False

if battery > 20 and obstacle == False:
    print("Robot can move")
elif battery <= 20:
    print("Low battery - charge robot")
else:
    print("Obstacle detected - stop")
