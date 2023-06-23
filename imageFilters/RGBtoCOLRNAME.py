from scipy.spatial import KDTree

# Define a list of color names and their corresponding RGB values
colors = [
    ("red", (255, 0, 0)),
    ("green", (0, 255, 0)),
    ("blue", (0, 0, 255)),
    ("black", (0, 0, 0)),
    ("white", (255, 255, 255)),
    ("yellow", (255, 255, 0)),
    ("orange", (255, 165, 0)),
    ("purple", (128, 0, 128)),
    ("pink", (255, 192, 203)),
    ("gray", (128, 128, 128)),
    ("brown", (165, 42, 42)),
    ("gold", (255, 215, 0)),
    ("silver", (192, 192, 192)),
    ("navy", (0, 0, 128)),
    ("teal", (0, 128, 128)),
    ("olive", (128, 128, 0)),
    ("maroon", (128, 0, 0)),
    ("aquamarine", (127, 255, 212)),
    ("turquoise", (64, 224, 208)),
    ("indigo", (75, 0, 130))
]

# Create a KDTree for efficient nearest neighbor search
color_tree = KDTree([c[1] for c in colors])

# Open the text file containing RGB values
with open("rgb_values.txt", "r") as f:
    # Read the lines of the file and split the RGB values
    rgb_lines = f.readlines()
    rgb_values = [eval(line.strip()) for line in rgb_lines]
# Open a new file to write the results to
with open("rgb_color_names.txt", "w") as f:
    # Loop through each RGB value and find the nearest color
    for rgb in rgb_values:
        dist, idx = color_tree.query(rgb)
        color_name = colors[idx][0]
        # Write the RGB value and its corresponding color name to the file
        f.write("{}\n".format(color_name))