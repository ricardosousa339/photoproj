from skimage import io
from sklearn.cluster import KMeans
import numpy as np
from matplotlib.colors import rgb2hex

def extract_main_color(image_path, n_colors=1):
    image = io.imread(image_path)
    image = image.reshape(-1, 3)

    kmeans = KMeans(n_clusters=n_colors)
    kmeans.fit(image)

    main_color = kmeans.cluster_centers_[0]
    main_color_hex = rgb2hex(main_color / 255)
    return main_color_hex
