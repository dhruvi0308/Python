import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns

def simulate_coin_flips(num_flips):
    # Generate random coin flips: 1 for heads, 2 for tails
    flips = np.random.randint(1, 3, size=num_flips)  # 1s and 2s
    return flips

# Number of flips for different simulations
flip_counts = [200, 20000, 200000]

# Set Seaborn style
sns.set_style('whitegrid')

for count in flip_counts:
    flips = simulate_coin_flips(count)

    # Calculate frequencies of heads (1s) and tails (2s)
    values = [1, 2]
    frequencies = [np.count_nonzero(flips == face) for face in values]

    # Create and display the bar plot without text above the bars
    title = f'Coin Flips: {count} Simulations'
    axes = sns.barplot(x=values, y=frequencies, palette='bright')

    # Set the title and label the axes
    axes.set_title(title)
    axes.set(xlabel='Coin Side (1=Heads, 2=Tails)', ylabel='Frequency')  
    axes.set_ylim(top=max(frequencies) * 1.10)

    plt.xticks([1, 2], ['Heads', 'Tails'])
    plt.show()

for count in flip_counts:
    flips = simulate_coin_flips(count)

    # Calculate frequencies of heads (1s) and tails (2s)
    values = [1, 2]
    frequencies = [np.count_nonzero(flips == face) for face in values]

    # Create and display the bar plot with text above the bars
    title = f'Coin Flips: {count} Simulations'
    axes = sns.barplot(x=values, y=frequencies, palette='bright')

    # Set the title and label the axes
    axes.set_title(title)
    axes.set(xlabel='Coin Side (1=Heads, 2=Tails)', ylabel='Frequency')  
    axes.set_ylim(top=max(frequencies) * 1.10)

    plt.xticks([1, 2], ['Heads', 'Tails'])

    # Add text annotations for frequencies and percentages
    for bar, frequency in zip(axes.patches, frequencies):
        text_x = bar.get_x() + bar.get_width() / 2.0  
        text_y = bar.get_height() 
        percentage = frequency / count * 100
        text = f'{frequency}\n{percentage:.1f}%'
        axes.text(text_x, text_y, text, fontsize=11, ha='center', va='bottom')

    plt.show()