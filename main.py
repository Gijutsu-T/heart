import turtle
import math

# Function to calculate heart shape points based on a parametric equation 😭
def heart_coordinates(t):
    x = 16 * math.sin(t)**3
    y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
    return x * 20, y * 20  # Scale up to fit in the screen

# Function to draw the intricate string art inside the heart
def draw_prism_heart(artist, points):
    total_points = len(points)
    for i in range(total_points):
        for j in range(i + 5, total_points, 10):  # Step and density control
            artist.penup()
            artist.goto(points[i])
            artist.pendown()
            artist.goto(points[j])

# Main function to set up and draw the heart
def main():
    # Screen setup
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("black")
    screen.title("Prism-Like Heart Design")

    # Turtle setup
    artist = turtle.Turtle()
    artist.speed(0)  # Maximum speed
    artist.hideturtle()
    artist.pencolor("#eb7ce0")  # pink color for the lines

    # Generate high-resolution heart points
    points = []
    for angle in range(0, 360, 1):  # High resolution for smooth curves
        radians = math.radians(angle)
        points.append(heart_coordinates(radians))

    # Draw string art with overlapping connections
    draw_prism_heart(artist, points)

    # Keep the window open
    screen.mainloop()


# Run the program
if __name__ == "__main__":
    main()
