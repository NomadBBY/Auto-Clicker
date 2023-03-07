# Auto-Clicker
This code imports the necessary modules and defines a class called ClickMouse, which is a subclass of threading.Thread. This class is used to create a separate thread for mouse clicking functionality.

The __init__ method of the ClickMouse class initializes the delay and button parameters, as well as the running and program_running variables, which are used to determine whether or not the thread is currently running and whether or not the entire program is still running.

The start_clicking and stop_clicking methods are used to start and stop the mouse clicking functionality by setting the running variable accordingly.

The exit method stops the mouse clicking functionality and sets the program_running variable to False, indicating that the program should exit.

The run method is the main method of the ClickMouse class, and it contains the code that is executed when the thread is started. This code loops indefinitely while the program_running variable is True. Inside the loop, the running variable is checked to see if the mouse clicking functionality should be executed. If running is True, the mouse.click method is called with the button parameter and a delay specified by the delay parameter. The loop then sleeps for 2 seconds before starting the next iteration.

The main part of the program starts by creating a Controller object from the pynput.mouse module and a ClickMouse object with the delay and button parameters. The ClickMouse thread is then started.

The on_press function is used to define what happens when a key is pressed. If the start_stop_key is pressed, the running variable of the ClickMouse object is toggled to start or stop the mouse clicking functionality. If the stop_key is pressed, the ClickMouse thread is stopped and the Listener is stopped. If the move_key is pressed, the mouse position is set to a specific coordinate. If the position_key is pressed, the current mouse position is printed.

Finally, the Listener object is created with the on_press function and the join method is called, which waits for the listener to finish processing events
