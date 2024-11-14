from matplotlib import animation
import matplotlib.pyplot as plt
import random
import seaborn as sns

def update(frame_number, rolls, sums, frequencies):
    """Configures bar plot contents for each animation frame."""
    # Roll two dice and update frequencies for the sum of the results
    for _ in range(rolls):
        roll_sum = random.randint(1, 6) + random.randint(1, 6)
        frequencies[roll_sum - 2] += 1  # Adjust for index (sum starts at 2)

    # Clear the previous plot
    plt.cla()

    # Plot new frequency distribution
    axes = sns.barplot(x=sums, y=frequencies, palette='bright')
    axes.set_title(f'Sum Frequencies for {sum(frequencies):,} Rolls')
    axes.set(xlabel='Sum of Two Dice', ylabel='Frequency')
    axes.set_ylim(top=max(frequencies) * 1.10)  # Scale y-axis

    # Display frequency & percentage above each bar
    for bar, frequency in zip(axes.patches, frequencies):
        text_x = bar.get_x() + bar.get_width() / 2.0
        text_y = bar.get_height()
        text = f'{frequency:,}\n{frequency / sum(frequencies):.2%}'
        axes.text(text_x, text_y, text, ha='center', va='bottom')

# Set parameters for the animation
number_of_frames = 100
rolls_per_frame = 100
sns.set_style('whitegrid')  # White background with gray grid lines
figure = plt.figure('Rolling Two Six-Sided Dice')  # Figure for animation

# Define possible sums (from 2 to 12)
sums = list(range(2, 13))
frequencies = [0] * 11  # Frequency list for sums from 2 to 12

# Configure and start the animation
sum_animation = animation.FuncAnimation(
    figure, update, repeat=False, frames=number_of_frames, interval=100,
    fargs=(rolls_per_frame, sums, frequencies))

plt.show()  # Display the animation window