
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from sklearn.datasets import make_blobs
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# Generate simple 2D data with labels
X_simple, y_simple = make_blobs(n_samples=30, centers=2, n_features=2, cluster_std=2.2, random_state=42) # type: ignore


# Use sklearn's KNeighborsClassifier for prediction and neighbor selection

# Fit KNN once and update n_neighbors as needed
class ResponsiveKNN:
    def __init__(self, X_train, y_train, k=3):
        self.X_train = X_train
        self.y_train = y_train
        self.knn = KNeighborsClassifier(n_neighbors=k)
        self.knn.fit(X_train, y_train)
        self.k = k

    def update_k(self, k):
        if k != self.k:
            self.knn = KNeighborsClassifier(n_neighbors=k)
            self.knn.fit(self.X_train, self.y_train)
            self.k = k

    def predict(self, new_point):
        new_point_2d = np.array(new_point).reshape(1, -1)
        pred_class = self.knn.predict(new_point_2d)[0]
        distances, indices = self.knn.kneighbors(new_point_2d)
        nearest_idx = indices[0]
        return pred_class, nearest_idx

# Colors for plotting
C = {0: 'red', 1: 'blue', 2: 'green', 3: 'magenta'}


# Responsive plot update using artists
def setup_responsive_plot(ax, knn_model, x, y, k):
    pred_class, idxs = knn_model.predict([x, y])
    # Data points
    scatter_data = ax.scatter(X_simple[:,0], X_simple[:,1], c=[C[int(label)] for label in y_simple], edgecolor='k', s=80, label='Data points')
    # Nearest neighbors
    scatter_neighbors = ax.scatter(X_simple[idxs,0], X_simple[idxs,1], facecolors='none', edgecolors='lime', s=200, linewidths=2, label='Nearest neighbors')
    # New point
    scatter_new = ax.scatter(x, y, c=C[int(pred_class)], edgecolor='black', s=120, marker='*', label='New point')
    ax.set_title(f"K-NN iteration k={k}")
    ax.set_xlabel("Feature 1")
    ax.set_ylabel("Feature 2")
    legend = ax.legend()
    return scatter_data, scatter_neighbors, scatter_new, legend

def update_responsive_plot(scatter_neighbors, scatter_new, legend, knn_model, x, y, k, ax):
    knn_model.update_k(k)
    pred_class, idxs = knn_model.predict([x, y])
    # Update neighbors
    scatter_neighbors.set_offsets(X_simple[idxs])
    # Update new point
    scatter_new.set_offsets([[x, y]])
    scatter_new.set_facecolor(C[int(pred_class)])
    # Update title
    ax.set_title(f"K-NN iteration k={k}")
    # Remove and redraw legend
    legend.remove()
    legend = ax.legend()
    ax.figure.canvas.draw_idle()
    return legend

def main():
    x_min, x_max = X_simple[:,0].min()-1, X_simple[:,0].max()+1
    y_min, y_max = X_simple[:,1].min()-1, X_simple[:,1].max()+1

    # Initial values
    x0 = (x_min + x_max) / 2
    y0 = (y_min + y_max) / 2
    k0 = 2

    fig, ax = plt.subplots(figsize=(7,5))
    plt.subplots_adjust(left=0.1, bottom=0.3)

    # Fit KNN once
    knn_model = ResponsiveKNN(X_simple, y_simple, k=k0)
    scatter_data, scatter_neighbors, scatter_new, legend = setup_responsive_plot(ax, knn_model, x0, y0, k0)

    # Slider axes
    axcolor = 'lightgoldenrodyellow'
    ax_x = plt.axes((0.1, 0.2, 0.8, 0.03), facecolor=axcolor)
    ax_y = plt.axes((0.1, 0.15, 0.8, 0.03), facecolor=axcolor)
    ax_k = plt.axes((0.1, 0.1, 0.8, 0.03), facecolor=axcolor)

    s_x = Slider(ax_x, 'x', x_min, x_max, valinit=x0)
    s_y = Slider(ax_y, 'y', y_min, y_max, valinit=y0)
    s_k = Slider(ax_k, 'k', 1, 10, valinit=k0, valstep=1)

    def update(val):
        nonlocal legend
        legend = update_responsive_plot(scatter_neighbors, scatter_new, legend, knn_model, s_x.val, s_y.val, int(s_k.val), ax)

    s_x.on_changed(update)
    s_y.on_changed(update)
    s_k.on_changed(update)

    # Reset button
    resetax = plt.axes((0.8, 0.025, 0.1, 0.04))
    button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

    def reset(event):
        s_x.reset()
        s_y.reset()
        s_k.reset()
    button.on_clicked(reset)

    plt.show()


if __name__ == "__main__":
    main()