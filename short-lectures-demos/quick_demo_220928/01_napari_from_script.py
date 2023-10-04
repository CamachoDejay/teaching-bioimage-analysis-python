# super simple example of runing napari from a python
# script. date: 2022-sep
# github: camachodejay
from skimage import data
import napari

# start the viewer and add the image data
viewer = napari.view_image(data.astronaut(), rgb=True)
napari.run()  # start the event loop and show viewer