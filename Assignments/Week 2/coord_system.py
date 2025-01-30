import pygame
from pygame.locals import *
import math


if __name__ == "__main__":
    # initializing all the imported
    # pygame modules
    (numpass,numfail) = pygame.init()

    # printing the number of modules 
    # initialized successfully 
    print('Number of modules initialized successfully:',
        numpass)
    
    # Define window width & height
    WINDOW_WIDTH = 960
    WINDOW_HEIGHT = 540

    window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    
    pygame.display.set_caption('Coordinate System Demo')

    x_offset = WINDOW_WIDTH // 2
    y_offset = WINDOW_HEIGHT // 2
    angle = 0
   

    # Define the color of the axis
    axis_color = (0, 0, 0)

    # Define a scalar for the axis length
    axis_scalar = 10

    def draw_coordinate_system(x_offset, y_offset, angle):
        # Flush the screen with white color
        window.fill((255, 255, 255))  

        radians = math.radians(angle)
        cos_angle = math.cos(angle)
        sin_angle = math.sin(angle)

        scaled_width = WINDOW_WIDTH * axis_scalar
        scaled_height = WINDOW_HEIGHT * axis_scalar

        # Draw the X axis
        x_axis_start = (
            x_offset - scaled_width * cos_angle,
            y_offset - scaled_width * sin_angle
        )
        x_axis_end = (
            x_offset + scaled_width * cos_angle,
            y_offset + scaled_width * sin_angle
        )
        pygame.draw.line(window, axis_color, x_axis_start, x_axis_end, 2)

        # Draw the y-axis
        y_axis_start = (
            x_offset + scaled_height * sin_angle,
            y_offset - scaled_height * cos_angle
        )
        y_axis_end = (
            x_offset - scaled_height * sin_angle,
            y_offset + scaled_height * cos_angle
        )
        pygame.draw.line(window, axis_color, y_axis_start, y_axis_end, 2)

        # Draw indicators for the x-axis
        for x in range(-int(scaled_width // 2), int(scaled_width // 2), 10):
            indicator_x = x_offset + x * cos_angle
            indicator_y = y_offset + x * sin_angle
            indicator_start = (
                indicator_x - 4 * sin_angle,
                indicator_y + 4 * cos_angle
            )
            indicator_end = (
                indicator_x + 4 * sin_angle,
                indicator_y - 4 * cos_angle
            )
            pygame.draw.aaline(window, axis_color, indicator_start, indicator_end)

            # Draw indicators for the y-axis
        for y in range(-int(scaled_height // 2), int(scaled_height // 2), 10):
            indicator_x = x_offset - y * sin_angle
            indicator_y = y_offset + y * cos_angle
            indicator_start = (
                indicator_x - 4 * cos_angle,
                indicator_y - 4 * sin_angle
            )
            indicator_end = (
                indicator_x + 4 * cos_angle,
                indicator_y + 4 * sin_angle
            )
            pygame.draw.aaline(window, axis_color, indicator_start, indicator_end)
      
    running  = True

    while running:      
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                running = False

         # Handle keyboard input
        keys = pygame.key.get_pressed()
        if keys[K_w]:  # Move up
            y_offset -= 10
        if keys[K_s]:  # Move down
            y_offset += 10
        if keys[K_a]:  # Move left
            x_offset -= 10
        if keys[K_d]:  # Move right
            x_offset += 10
        if keys[K_q]:  # Rotate left (counter-clockwise)
            angle -= 0.05
        if keys[K_e]:  # Rotate right (clockwise)
            angle += 0.05

        # Keep the angle within 0-360 degrees
        angle = angle % 360

        # Draw the coordinate system
        draw_coordinate_system(x_offset,y_offset,angle)
        

        # Update our window
        pygame.display.flip()
        clock.tick(30)