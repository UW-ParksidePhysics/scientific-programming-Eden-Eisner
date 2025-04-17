from matplotlib.patches import FancyArrow
import matplotlib.pyplot as plt

plt.figure()
plt.axis([0, 10, 0, 10])
plt.arrow(1, 1, 4, 2, head_width=0.3, head_length=0.4, fc='blue', ec='black')
plt.grid(True)
plt.title('plt.arrow Example')
plt.show()



fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

arrow = FancyArrow(2, 2, 4, 3, width=0.2, head_width=0.5, head_length=0.6, length_includes_head=True, color='green')
ax.add_patch(arrow)

plt.grid(True)
plt.title('FancyArrow Example')
plt.show()
