"""
Matplotlib has a number of predefined styles available, with good
starting settings that will make your visualizations appealing without
requiring much customization.
This code displays all styles available on the system
"""
import matplotlib.pyplot as plt

styles = plt.style.available

for style in styles:
    print(style)
    