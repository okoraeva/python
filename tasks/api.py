import numpy as np
from matplotlib.patches import Rectangle
import itertools
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib as mpl
from matplotlib.patches import Polygon


class Polygon:

    def gen_polygon(self, *tuple):
        tuples = itertools.cycle(tuple)
        fig, axs = plt.subplots(1, len(tuple), figsize=(9, 3))
        for _ in range(len(tuple)):
            tup = next(tuples)
            x = []
            y = []
            for i in tup:
                x.append(i[0])
                y.append(i[1])
            x.append(tup[0][0])
            y.append(tup[0][1])
            axs[_].set_xlim([-1, 10])
            axs[_].set_ylim([-1, 10])
            axs[_].plot(x, y)
        plt.show()

    def gen_rectangle(self, x, y, w, h):  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
        fig, ax = plt.subplots()
        ax.set_xlim([0, 5])
        ax.set_ylim([0, 1])
        for i, j in zip(x, y):
            ax.add_patch(Rectangle((i, j), w, h))
        plt.show()

    def gen_triangle(self, x, y):
        x = 1.5
        y = 1.7
        z = 1.6
        ax = plt.gca()
        for i in range(18):
            pts = np.array([[x, 4], [y, 4], [z, 4.3]])
            x += 0.3
            y += 0.3
            z += 0.3
            ax.add_patch(patches.Polygon(pts))
        ax.set_xlim([1, 7])
        ax.set_ylim([1, 8])
        plt.show()
        # plt.plot(x, y, '^')
        # plt.show()

    def gen_hexagon(self, x, y):
        plt.plot(x, y, 'H')
        plt.show()

    def gen_mixed(self):
        fig, axs = plt.subplots(1, 1)
        axs.scatter(4 * np.random.rand(2), 0.9 * np.random.rand(2), s=300, c=np.random.rand(2), marker='^')
        axs.scatter(4 * np.random.rand(3), 0.9 * np.random.rand(3), s=300, c=np.random.rand(3), marker='H')
        axs.set_xlim([-1, 4.5])
        axs.set_ylim([-1, 1])
        for i, j in zip(5 * np.random.rand(2), 0.9 * np.random.rand(2)):
            axs.add_patch(Rectangle((i, j), 0.3, 0.1))
        plt.show()

    def tr_translate(self, figure, x, y):
        if figure == 'hexagon':
            count = 1
            marker = 'H'
        elif figure == 'triangle':
            count = 1
            marker = '^'
        elif figure == 'rectangle':
            count = 0
        else:
            count = 1
            marker = ''
        fig, axs = plt.subplots(1, 1)
        axs.set_xlim([-0.2, 5])
        axs.set_ylim([0, 1])
        if count == 1:
            axs.plot(x, y, marker)
        else:
            for i, j in zip(x, y):
                axs.add_patch(Rectangle((i, j), 0.1, 0.02))
        for i in range(len(y)):
            y[i] = y[i] - 0.1
        if count == 1:
            axs.plot(x, y, marker)
        else:
            for i, j in zip(x, y):
                axs.add_patch(Rectangle((i, j), 0.1, 0.02))
        plt.show()

    def tr_rotate(self, figure, x, y, degree):
        if figure == 'hexagon':
            marker = 'H'
        elif figure == 'triangle':
            marker = '^'
        else:
            marker = ''
        fig, ax = plt.subplots()
        ax.set_xlim([0, 5])
        ax.set_ylim([0, 1])
        tr = mpl.transforms.Affine2D().rotate_deg(degree) + ax.transData
        arr = []
        if figure == 'rectangle':
            for i, j in zip(x, y):
                arr.append(patches.Rectangle((i, j), 0.1, 0.02))
            counter = 0
            for i in arr:
                counter += 1
                if counter % 2 == 0:
                    i.set_transform(tr)
                ax.add_patch(i)
        else:
            ax.plot(x, y, marker)
        plt.show()

    def tr_symmetry(self, figure, x, y):
        if figure == 'hexagon':
            count = 1
            marker = 'H'
        elif figure == 'triangle':
            count = 1
            marker = '^'
        elif figure == 'rectangle':
            count = 0
        else:
            count = 1
            marker = ''
        fig, axs = plt.subplots(1, 1)
        axs.set_xlim([-0.2, 5])
        axs.set_ylim([0, 1])
        if count == 1:
            axs.plot(x, y, marker)
        else:
            for i, j in zip(x, y):
                axs.add_patch(Rectangle((i, j), 0.1, 0.02))
        for i in range(len(y)):
            y[i] = y[i] - 0.1
        if count == 1:

            axs.plot(x, y, 'v')
        else:
            for i, j in zip(x, y):
                axs.add_patch(Rectangle((i, j), 0.1, 0.02))
        plt.show()

    def one_fich(self, x, y):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.set_xlim([0, 5])
        ax.set_ylim([0, 1])
        tr = mpl.transforms.Affine2D().rotate_deg(10) + ax.transData
        times = 0
        while times < 3:
            arr = []
            for i, j in zip(x, y):
                arr.append(patches.Rectangle((i, j), 0.1, 0.02))
            counter = 0
            for i in arr:
                counter += 1
                if counter % 2 == 0:
                    i.set_transform(tr)
                    ax.add_patch(i)
            for i in range(len(y)):
                y[i] = y[i] - 0.1
            times += 1
        plt.show()

    def sec_fich(self, x, y):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.set_xlim([0, 5])
        ax.set_ylim([0, 1])
        arr = []
        tr = mpl.transforms.Affine2D().rotate_deg(10) + ax.transData
        for i, j in zip(x, y):
            arr.append(patches.Rectangle((i, j), 0.1, 0.02))
        counter = 0
        for i in arr:
            counter += 1
            if counter % 2 == 0:
                i.set_transform(tr)
                ax.add_patch(i)
        tr = mpl.transforms.Affine2D().rotate_deg(-15) + ax.transData
        for i in range(len(y)):
            y[i] = y[i] + 1
        arr = []
        for i, j in zip(x, y):
            arr.append(patches.Rectangle((i, j), 0.1, 0.02))
        counter = 0
        for i in arr:
            counter += 1
            if counter % 2 == 0:
                i.set_transform(tr)
                ax.add_patch(i)
        plt.show()


    # def tr_homothety(self, figure):
    #     if figure == 'hexagon':
    #         count = 1
    #         marker = 'H'
    #     elif figure == 'triangle':
    #         count = 1
    #         marker = '^'
    #     elif figure == 'rectangle':
    #         count = 0
    #     else:
    #         count = 1
    #         marker = ''
    #     fig, ax = plt.subplots()
    #     ax.set_xlim([1, 7])
    #     ax.set_ylim([1, 8])
    #     plt.show()
    #     if figure == 'S':
    #         x = np.array([2, 2, 3, 3, 2])
    #         y = np.array([0, 1, 1, 0, 0])
    #     elif figure == 'H':
    #         x = np.array([1, 2, 4, 5, 4, 2, 1])
    #         y = np.array([2, 4, 4, 2, 0, 0, 2])
    #     elif figure == 'T':
    #         x = np.array([2, 3, 4, 2])
    #         y = np.array([0, 2, 0, 0])
    #     arr_x = []
    #     arr_y = []
    #     for i, j in zip(x, y):
    #     arr_x = list(map(lambda x, z: x*(2 ** z), self.hx, range(len(self.x)+1)))
    #     arr_y = list(map(lambda y, z: y*(2 ** z), self.hy, range(len(self.y)+1)))
    #     for coords in range(len(arr_x)):
    #         ax.plot(self.hx[coords], self.hy[coords])
    #         ax.plot(-self.hx[coords], -self.hy[coords])
    #     plt.show()

square = ((0, 0), (0, 1), (1, 1), (1, 0))
rect = ((0, 0), (0.5, 1), (1, 0))

polygon = Polygon()
# polygon.gen_polygon(rect, square)
polygon.gen_rectangle(np.arange(0.15, 4.85, 0.2), [0.5]*25, 0.1, 0.02)
polygon.gen_rectangle(np.arange(0.15, 4.85, 0.2), [0.5]*25, 0.15, 0.025)
# polygon.gen_triangle(np.arange(0., 5., 0.2), [0.5]*25)
# polygon.gen_hexagon(np.arange(0., 5., 0.2), [0.5]*25)
# polygon.gen_mixed()
# polygon.tr_translate('triangle', np.arange(0., 5., 0.2), [0.5]*25)
# polygon.tr_rotate('rectangle', np.arange(0.15, 4.85, 0.2), [0.3]*24, 7)
# polygon.tr_symmetry('triangle', np.arange(0.15, 4.85, 0.2), [0.3]*24)
# polygon.one_fich(np.arange(0., 5., 0.2), [0.2]*25)
# polygon.sec_fich(np.arange(0., 5., 0.2), [0.2]*25)
# polygon.tr_homothety('S')