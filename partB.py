import numpy as np
import matplotlib.pyplot as plt

# Constants
c = 3e8  # speed of light in m/s (used for distance-based signal calculation)

# Function to calculate the signal in either time or distance domain
def generate_signal(A, f, phi, fixed_value, is_time_fixed, points):
    """
    This function generates a signal based on the input parameters.
    It calculates the signal either over time (if is_time_fixed is True) 
    or over distance (if is_time_fixed is False).

    Parameters:
    - A: Amplitude of the signal
    - f: Frequency of the signal
    - phi: Phase of the signal
    - fixed_value: The fixed value (time or distance depending on is_time_fixed)
    - is_time_fixed: A boolean indicating whether the fixed value is time (True) or distance (False)
    - points: The number of points in the generated signal

    Returns:
    - A list of signal values over the specified domain (time or distance)
    """
    
    omega = 2 * np.pi * f  # Angular frequency (rad/s)
    k = 2 * np.pi / (c / f)  # Wave number (1/m), related to frequency and speed of light
    delta = (1 / f) / points if is_time_fixed else (c / f) / points  # Spacing between points, either in time or distance

    signal = []  # List to store the signal values

    # Loop over the points to generate the signal
    for i in range(points):
        variable = i * delta  # Variable that progresses with each point
        if is_time_fixed:
            # Signal calculated based on fixed time (sin(ω(t + fixed_value)))
            signal.append(A * np.sin(omega * (fixed_value + variable) + phi))  
        else:
            # Signal calculated based on fixed distance (sin(k(x + fixed_value)))
            signal.append(A * np.sin(k * (fixed_value + variable) + phi))  

    return signal

# Function to plot the signals and their sum
def plot_signals(signal1, signal2, sum_signal, title):
    """
    This function plots three signals: Signal 1, Signal 2, and their sum.

    Parameters:
    - signal1: The first signal to plot
    - signal2: The second signal to plot
    - sum_signal: The sum of signal1 and signal2 to plot
    - title: The title of the plot (indicates if the signals are over time or distance)
    """
    # Create a new figure for the plot
    plt.figure(figsize=(10, 6))

    # Plot the three signals with labels
    plt.plot(signal1, label="Signal 1", color='r')  # Signal 1 in red
    plt.plot(signal2, label="Signal 2", color='b')  # Signal 2 in blue
    plt.plot(sum_signal, label="Sum of Signals", color='g')  # Sum in green

    # Add title, labels, and a legend to the plot
    plt.title(title)
    plt.xlabel("Index")  # X-axis represents the index (time or distance)
    plt.ylabel("Amplitude")  # Y-axis represents the amplitude of the signal
    plt.legend()  # Display the legend to label each curve
    plt.grid(True)  # Add grid lines to the plot for better visibility

    # Display the plot
    plt.show()

# Main function to handle user inputs and execution
def main():
    """
    The main function of the program. It handles user input, generates signals,
    calculates their sum, and calls the plotting function.
    """
    points = 100  # Number of points to plot (resolution of the signals)

    # Take user input for the parameters of Signal 1
    A1, f1, phi1 = map(float, input("Enter amplitude, frequency, and phase for Signal 1 (A1, f1, phi1): ").split())

    # Take user input for the parameters of Signal 2
    A2, f2, phi2 = map(float, input("Enter amplitude, frequency, and phase for Signal 2 (A2, f2, phi2): ").split())

    # Take user input for the fixed value (either time or distance)
    fixed_value = float(input("Enter the fixed value (time or distance): "))

    # Take user input to specify whether the fixed value refers to time (1) or distance (0)
    is_time_fixed = int(input("Is this a fixed time (1) or fixed distance (0)? "))

    # Generate the two signals based on the user input
    signal1 = generate_signal(A1, f1, phi1, fixed_value, is_time_fixed, points)
    signal2 = generate_signal(A2, f2, phi2, fixed_value, is_time_fixed, points)

    # Calculate the sum of the two signals
    sum_signal = [signal1[i] + signal2[i] for i in range(points)]

    # Plot the signals and their sum
    if is_time_fixed:
        # If it's a time-fixed signal, label the plot accordingly
        plot_signals(signal1, signal2, sum_signal, "Sum of Signals over Time")
    else:
        # If it's a distance-fixed signal, label the plot accordingly
        plot_signals(signal1, signal2, sum_signal, "Sum of Signals over Distance")

# Run the program
if __name__ == "__main__":
    main()
