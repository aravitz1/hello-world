# hello-world

## Signal Generator and Plotter

An interactive Python script that generates and plots various signal types with zoom capabilities.

### Features

- **Multiple signal types:**
  - Sinusoid
  - Sawtooth
  - Square Wave
  - Triangle Wave
  - Pulse Train

- **Customizable parameters:**
  - Frequency
  - Amplitude
  - Phase (for sinusoid)
  - Duty cycle (for square and pulse signals)
  - Duration
  - Sampling rate

- **Interactive plotting:**
  - Zoom horizontally and vertically
  - Pan across the signal
  - Reset view button

### Requirements

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Usage

Run the script:

```bash
python3 signal_generator.py
```

Follow the interactive prompts to:
1. Select a signal type (1-5)
2. Enter signal parameters (frequency, amplitude, etc.)
3. Set the duration and sampling rate
4. View the generated signal in an interactive plot

### Interactive Controls

- **Zoom:** Use the zoom button in the toolbar or draw a rectangle to zoom
- **Pan:** Use the pan button to move around the plot
- **Home:** Reset to the original view
- **Reset View button:** Quickly reset zoom to default
- Right-click and drag to zoom on both axes
