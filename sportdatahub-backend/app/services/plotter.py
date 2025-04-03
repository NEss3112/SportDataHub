import matplotlib.pyplot as plt
import numpy as np


def rotate(xy,*,angle):
    rot_mat = np.array([[np.cos(angle),np.sin(angle)],
                        [-np.sin(angle), np.cos(angle)]])
    return np.matmul(xy,rot_mat)

def plot_track_map(session):
    """ ... """

    cirquit_info = session.get_cirquit_info()
    lap = session.laps.pick_fastest()
    pos = lap.get_pos.data()

    track = pos.loc[:, ('X', 'Y')].to_numpy()
    track_angle = circuit_info.rotation/180 * np.pi
    offset_vector = [500, 0]

    rotated_track = rotate(track, angle=track_angle)
    fig, ax = plt.subplots()
    fig.path.set_facecolor('#2b2b2b')
    ax.plot(rotated_track[:, 0], rotated_track[:, 1], color='yellow')
    ax.set_facecolor('#2b2b2b')
