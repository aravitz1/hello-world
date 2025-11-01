#!/usr/bin/env python3
"""
Signal Generator and Plotter
Generates various signal types and plots them with interactive zoom capabilities.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button


def get_float_input(prompt, default=None):
    """Get float input from user with optional default value."""
    while True:
        try:
            if default is not None:
                value = input(f"{prompt} (default: {default}): ").strip()
                if not value:
                    return default
                return float(value)
            else:
                return float(input(f"{prompt}: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def generate_sinusoid(t, frequency, amplitude, phase):
    """Generate a sinusoidal signal."""
    return amplitude * np.sin(2 * np.pi * frequency * t + phase)


def generate_sawtooth(t, frequency, amplitude):
    """Generate a sawtooth wave signal."""
    period = 1.0 / frequency
    return amplitude * 2 * ((t / period) - np.floor(0.5 + t / period))


def generate_square(t, frequency, amplitude, duty_cycle):
    """Generate a square wave signal."""
    period = 1.0 / frequency
    phase = (t % period) / period
    return amplitude * np.where(phase < duty_cycle, 1, -1)


def generate_triangle(t, frequency, amplitude):
    """Generate a triangle wave signal."""
    period = 1.0 / frequency
    phase = (t % period) / period
    return amplitude * (4 * np.abs(phase - 0.5) - 1)


def generate_pulse(t, frequency, amplitude, duty_cycle):
    """Generate a pulse train signal."""
    period = 1.0 / frequency
    phase = (t % period) / period
    return amplitude * np.where(phase < duty_cycle, 1, 0)


def main():
    print("=" * 60)
    print("Signal Generator and Plotter")
    print("=" * 60)

    # Signal type selection
    print("\nAvailable signal types:")
    print("1. Sinusoid")
    print("2. Sawtooth")
    print("3. Square Wave")
    print("4. Triangle Wave")
    print("5. Pulse Train")

    while True:
        try:
            choice = int(input("\nSelect signal type (1-5): "))
            if 1 <= choice <= 5:
                break
            print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    signal_types = {
        1: "Sinusoid",
        2: "Sawtooth",
        3: "Square Wave",
        4: "Triangle Wave",
        5: "Pulse Train"
    }

    signal_name = signal_types[choice]
    print(f"\nSelected: {signal_name}")

    # Get common parameters
    print("\n" + "=" * 60)
    print("Signal Parameters")
    print("=" * 60)

    frequency = get_float_input("Enter frequency (Hz)", default=1.0)
    amplitude = get_float_input("Enter amplitude", default=1.0)

    # Get signal-specific parameters
    phase = 0
    duty_cycle = 0.5

    if choice == 1:  # Sinusoid
        phase = get_float_input("Enter phase (radians)", default=0.0)
    elif choice in [3, 5]:  # Square or Pulse
        duty_cycle = get_float_input("Enter duty cycle (0-1)", default=0.5)
        while not 0 < duty_cycle <= 1:
            print("Duty cycle must be between 0 and 1.")
            duty_cycle = get_float_input("Enter duty cycle (0-1)", default=0.5)

    # Get time parameters
    print("\n" + "=" * 60)
    print("Time Parameters")
    print("=" * 60)

    duration = get_float_input("Enter signal duration (seconds)", default=2.0)
    sampling_rate = get_float_input("Enter sampling rate (Hz)", default=1000.0)

    # Generate time array
    num_samples = int(duration * sampling_rate)
    t = np.linspace(0, duration, num_samples)

    # Generate signal
    print("\nGenerating signal...")

    if choice == 1:
        signal = generate_sinusoid(t, frequency, amplitude, phase)
    elif choice == 2:
        signal = generate_sawtooth(t, frequency, amplitude)
    elif choice == 3:
        signal = generate_square(t, frequency, amplitude, duty_cycle)
    elif choice == 4:
        signal = generate_triangle(t, frequency, amplitude)
    elif choice == 5:
        signal = generate_pulse(t, frequency, amplitude, duty_cycle)

    # Plot signal
    print("Plotting signal...")
    print("\nInteractive controls:")
    print("  - Use the zoom button or rectangle zoom tool to zoom in")
    print("  - Use the pan button to move around")
    print("  - Use the home button to reset view")
    print("  - Right-click and drag to zoom on both axes")
    print("  - Close the window to exit")

    fig, ax = plt.subplots(figsize=(12, 6))
    plt.subplots_adjust(bottom=0.15)

    ax.plot(t, signal, linewidth=1.5, label=signal_name)
    ax.grid(True, alpha=0.3)
    ax.set_xlabel('Time (seconds)', fontsize=12)
    ax.set_ylabel('Amplitude', fontsize=12)
    ax.set_title(f'{signal_name} Signal (f={frequency} Hz, A={amplitude})', fontsize=14)
    ax.legend()

    # Add reset button
    reset_ax = plt.axes([0.8, 0.025, 0.1, 0.04])
    reset_button = Button(reset_ax, 'Reset View', hovercolor='0.975')

    def reset_view(event):
        ax.set_xlim(t[0], t[-1])
        ax.set_ylim(signal.min() * 1.1, signal.max() * 1.1)
        plt.draw()

    reset_button.on_clicked(reset_view)

    # Set initial view limits
    ax.set_xlim(t[0], t[-1])
    ax.set_ylim(signal.min() * 1.1, signal.max() * 1.1)

    plt.show()

    print("\nDone!")


if __name__ == "__main__":
    main()
