import numpy as np
import matplotlib.pyplot as plt
def set_axes_equal(ax):
    '''Make axes of 3D plot have equal scale so that spheres appear as spheres,
    cubes as cubes, etc..  This is one possible solution to Matplotlib's
    ax.set_aspect('equal') and ax.axis('equal') not working for 3D.

    Input
      ax: a matplotlib axis, e.g., as output from plt.gca().
    '''
    x_limits = ax.get_xlim3d()
    y_limits = ax.get_ylim3d()
    z_limits = ax.get_zlim3d()
    x_middle = np.mean(x_limits)
    y_middle = np.mean(y_limits)
    z_middle = np.mean(z_limits)
    plot_radius = 0.5*max([abs(x_limits[1] - x_limits[0]), abs(y_limits[1] - y_limits[0]), abs(z_limits[1] - z_limits[0])])
    ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
    ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
    ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])


def graphIt(pts,hull,index_for_winner,center):
    fig = plt.figure(dpi=300)# start  a graph
    ax = fig.add_subplot(111, projection="3d")# add 3d sub plot
    ax.plot(pts.T[0], pts.T[1], pts.T[2], "k,")# plot all the points in a cloud
    ax.plot(pts[index_for_winner,0],pts[index_for_winner,1],pts[index_for_winner,2],"go")#plot the winner
    ax.plot(center[0],center[1],center[2],"bo")#plot the center
    for i in ["x", "y", "z"]:# lable the axis
        eval("ax.set_{:s}label('{:s}')".format(i, i))
    for s in hull.simplices:#draw the hull
        ss = np.append(s, s[0]) 
        ax.plot(pts[s, 0], pts[s, 1], pts[s, 2], "r-")
    set_axes_equal(ax)
    plt.show()#graph!