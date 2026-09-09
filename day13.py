def robot_status(name, battery):
    print("Robot:", name)

    if battery >= 50:
        print("Status: Ready")
    elif battery >= 20:
        print("Status: Low")
    else:
        print("Status: Recharge")

robot_status("Nova", 85)
robot_status("Bot-X", 15)
robot_status("Robo-3", 35)
