
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

video_file = "myvid.mp4"
fps = 15
number_of_timesteps = 30
boarding_method = 'random'
labels = ['A','B','C',None,'D','E','F']
aircraft = np.zeros((30,7))
aircraft[:,3]=1

# Output video writer
FFMpegWriter = animation.writers['ffmpeg']
metadata = dict(title='Movie Test', artist='Matplotlib', comment='Movie support!') # kanske överflödig
writer = FFMpegWriter(fps=fps, metadata=metadata)

fig = plt.figure(figsize=(15,15))
ax = fig.gca()
plt.rcParams.update({'font.size': 22})

cmap = mpl.colors.ListedColormap(['silver','black','black'])
bounds=[-1,5]
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

with writer.saving(fig, video_file, 100):
    for i in range(number_of_timesteps):

        fig.clear()
        plt.title(f'Boarding method: {boarding_method}. Timestep: {number_of_timesteps} ')
       
        img = plt.imshow( aircraft,interpolation='nearest',cmap=cmap) #
        plt.scatter(x=np.random.randint(0,6, 10), y=np.random.randint(0,29, 10), c='r', s=150) # passengers positions
        ax = plt.gca();

        # Major ticks
        ax.set_xticks(np.arange(0, 7, 1));
        ax.set_yticks(np.arange(0, 29, 1));

        # Labels for major ticks
        ax.set_xticklabels(labels);
        ax.set_yticklabels(np.arange(1, 30, 1));

        # Minor ticks
        ax.set_xticks(np.arange(-.5, 7, 1), minor=True);
        ax.set_yticks(np.arange(-.5, 29, 1), minor=True);

        # Gridlines based on minor ticks
        ax.grid(which='minor', color='black', linestyle='-', linewidth=2)
        
        writer.grab_frame()


# In[ ]:




