import os


file_path = "kleuren/rgb_color_names.txt"

color_freq = {}

with open(file_path, "r") as f:
    for line in f:
  
        color = line.strip().lower()
       
        if color in color_freq:
            color_freq[color] += 1

        else:
            color_freq[color] = 1


sorted_colors = sorted(color_freq.items(), key=lambda x: x[1], reverse=True)


print("Top 5 most frequent colors:")
for i in range(5):
    print(f"{i+1}. {sorted_colors[i][0].capitalize()}: {sorted_colors[i][1]}")
