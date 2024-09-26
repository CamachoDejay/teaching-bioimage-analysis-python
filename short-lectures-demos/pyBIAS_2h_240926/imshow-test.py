# based on a question by a students that uses Matplotlib and Seaborn
# 
# simple code that shows how to leave matplotlib and seaborn figures open
# while running a script.

import skimage.io as skio
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# loading the file into memory
script_path = Path(__file__)
tif_path = script_path.parents[1].joinpath("data","rice.tif")
print(tif_path)
img = skio.imread(tif_path, plugin="tifffile")

# check image size
print(img.shape)

# create figure using Matplotlib
plt.figure(figsize=(4, 4), dpi=300)
plt.imshow(img, cmap="gray")
plt.colorbar()
plt.title('Rice image')
plt.axis('off')
# this creates the figure and continues running the script
plt.draw()

# seaborn example using data from their examples
sns.set_theme(style="ticks")

# Load the example dataset for Anscombe's quartet
df = sns.load_dataset("anscombe")

# Show the results of a linear regression within each dataset
sns.lmplot(
    data=df, x="x", y="y", col="dataset", hue="dataset",
    col_wrap=2, palette="muted", ci=None,
    height=4, scatter_kws={"s": 50, "alpha": 1}
)
# this shows the image and keep them open, for the script 
# to continue you have to close the iamges
plt.show()