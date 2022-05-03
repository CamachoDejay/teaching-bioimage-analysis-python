import napari
from skimage.data import astronaut

# create the viewer and display the image
viewer = napari.Viewer()
new_layer = viewer.add_image(astronaut(), rgb=True)
napari.run()