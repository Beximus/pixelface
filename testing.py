from matplotlib import image as img
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
from scipy.cluster.vq import whiten
from scipy.cluster.vq import kmeans

image = img.imread('faceTest.jpg')

r = []
g = []
b = []
# print(image)

for line in image:
    for pixel in line:
        temp_r, temp_g, temp_b = pixel
        r.append(temp_r)
        g.append(temp_g)
        b.append(temp_b)

df = pd.DataFrame({'red': r,'blue': b,'green': g})

df['scaled_red'] = whiten(df['red'])
df['scaled_blue'] = whiten(df['blue'])
df['scaled_green'] = whiten(df['green'])

df.sample(n = 10)

cluster_centers, distortion= kmeans(df[['scaled_red', 'scaled_green', 'scaled_blue']], 5)
print(cluster_centers)

colors = []
r_std, g_std, b_std = df[['red', 'green', 'blue']].std()

print(r_std)
print(g_std)
print(b_std)

for cluster_center in cluster_centers:
    scaled_r, scaled_g, scaled_b = cluster_center
    colors.append((scaled_r*r_std/255,scaled_g*g_std/255,scaled_b*b_std/255))
plt.imshow([colors])
plt.show()