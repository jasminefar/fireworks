import turtle
import random
import threading

class ScreenManager:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.bgcolor("black")
        self.screen.title("Fireworks Display with Turtle Graphics")
        self.colors = ["red", "yellow", "blue", "green", "orange", "purple", "pink", "cyan", "white"]

class Firework:
    def __init__(self, x, y, size, color):
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.color(color)
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.pendown()
        self.size = size
        self.color = color

    def explode(self):
        for _ in range(36):
            self.turtle.forward(self.size)
            self.turtle.right(170)

    def reset(self):
        self.turtle.clear()
        self.turtle.penup()
        self.turtle.goto(random.randint(-200, 200), random.randint(-200, 200))
        self.turtle.pendown()

class FireworkManager:
    def __init__(self, num_fireworks, colors):
        self.fireworks = [Firework(random.randint(-200, 200), random.randint(-200, 200), random.randint(50, 100), random.choice(colors)) for _ in range(num_fireworks)]
        self.colors = colors

    def launch_fireworks(self):
        for firework in self.fireworks:
            firework.explode()

    def reset_fireworks(self):
        for firework in self.fireworks:
            firework.reset()

def main():
    screen_manager = ScreenManager()
    num_fireworks = 10
    firework_manager = FireworkManager(num_fireworks, screen_manager.colors)
    
    firework_manager.launch_fireworks()

    screen_manager.screen.ontimer(firework_manager.reset_fireworks, 5000)
    screen_manager.screen.ontimer(firework_manager.launch_fireworks, 6000)
    
    turtle.done()

if __name__ == "__main__":
    main()
