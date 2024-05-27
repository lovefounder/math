import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def logistic_map(b, x0, num_iterations):
    """根据b的取值,x0的初始值,迭代次数，计算出差分方程的收敛点。

    Args:
        b (_floatList_): 差分方程参数b的初始值,取[2.5,3.5],步长0.01。
        x0 (_float_): 差分方程迭代时的初始值,取0.02。
        num_iterations (_intList_): 差分方程的迭代次数,取1000。

    Returns:
        _float_: 差分方程收敛点。
    """
    x = x0
    for _ in range(num_iterations):
        x = b * x * (1 - x)
    return x


b_values = np.arange(2.5, 3.51, 0.01)  # 生成b的列表
x0 = 0.2  # 初始值
num_iterations = 1000  # 迭代次数
num_last_points = 100  # 生成的点的个数

converged_points = {}  # 创建一个字典，用来存储生成的收敛点坐标

for b in b_values:
    # 调用函数进行收敛点计算，这里的计算结果只有一个收敛点，但是实际上可能有多个，后续进行剔除。
    x = logistic_map(b, x0, num_iterations)

    # 创建一个列表收集生成的收敛点。
    last_points = []
    # 找到达到稳定状态后的100个点。
    for _ in range(num_last_points):
        x = b * x * (1 - x)
        last_points.append(x)

    # 删除这100个点中的重复的点，留下的即为全部收敛点。
    unique_points = np.unique(np.round(last_points, decimals=4))
    converged_points[b] = unique_points


# 调用pandas进行收敛点表的生成
# data = []
# for b, points in converged_points.items():
#     for point in points:
#         data.append([b, point])
# df = pd.DataFrame(data, columns=['b', 'Converged Points'])
# df.to_excel('converged_points.xlsx', index=False)


# 调用matplotlib.pyplot进行点的绘制。
plt.figure(figsize=(10, 7))
for b, points in converged_points.items():
    plt.plot([b] * len(points), points, 'k.', markersize=2)

plt.title("Bifurcation diagram of the logistic map")
plt.xlabel("b")
plt.ylabel("x")
plt.grid(True)
plt.show()
