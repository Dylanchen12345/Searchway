import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Algorithm': ['SpiralSearch_A', 'SpiralSearch_B', 'SpiralSearch_C', 'SpiralSearch_D', 'SpiralSearch_E',
                  'RandomWalk_A', 'RandomWalk_B', 'RandomWalk_C', 'RandomWalk_D', 'RandomWalk_E',
                  'GridSearch_A', 'GridSearch_B', 'GridSearch_C'],
    'ReactionTime': [11, 12, 13, 10, 12, 24, 26, 25, 23, 27, 17, 18, 19],
    'SuccessRate': [90.7, 93.1, 92.4, 94.1, 91.5, 72.1, 74.6, 73.7, 75.1, 71.3, 87.5, 89.3, 88.7],
    'CoverageRate': [95.2, 96.2, 94.8, 97.3, 96.9, 84.7, 85.3, 83.2, 86.8, 82.3, 93.1, 95.6, 94.2]
}

df = pd.DataFrame(data)
plt.figure(figsize=(12, 6))
plt.bar(df['Algorithm'], df['ReactionTime'], color='blue')
plt.xlabel('Algorithm')
plt.ylabel('Reaction Time (min)')
plt.title('Reaction Time of Different Algorithms')
plt.xticks(rotation=45)
plt.show()
plt.figure(figsize=(12, 6))
bar_width = 0.4
index = df.index

# Plotting Success Rate
plt.bar(index, df['SuccessRate'], bar_width, color='green', alpha=0.6, label='Success Rate')
# Plotting Coverage Rate with an offset
plt.bar(index + bar_width, df['CoverageRate'], bar_width, color='red', alpha=0.6, label='Coverage Rate')

plt.xlabel('Algorithm')
plt.ylabel('Percentage (%)')
plt.title('Success Rate and Coverage Rate of Different Algorithms')
plt.xticks(index + bar_width / 2, df['Algorithm'], rotation=45)
plt.legend()
plt.show()
