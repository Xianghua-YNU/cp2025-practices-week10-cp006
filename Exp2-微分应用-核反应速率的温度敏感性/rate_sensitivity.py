import numpy as np
import matplotlib.pyplot as plt

def q3a(T):
    """
    计算 3-alpha 反应速率中与温度相关的部分 q / (rho^2 Y^3)
    输入: T - 温度 (K)
    返回: 速率因子 (erg * cm^6 / (g^3 * s))
    """
    T8 = T / 1.0e8  # 以 10^8 K 为单位的温度
    # 避免 T8 过小导致除零或溢出错误 (虽然在此问题中 T 的范围较大，一般不会遇到)
    if T8 <= 0:  
        return 0.0  # 如果 T8 小于等于 0，返回 0.0
    rate_factor = 5.09e11 * T8**(-3.0) * np.exp(-44.027 / T8)  # 计算速率因子
    return rate_factor  # 返回计算得到的速率因子
    # TODO: 在此实现3-α反应速率计算
    # 提示：
    # 1. 将温度转换为以 10^8 K 为单位
    # 2. 注意处理温度为零的特殊情况
    # 3. 使用公式：q_{3α} = 5.09×10^11 ρ^2 Y^3 T_8^(-3) exp(-44.027/T_8)
    pass

def plot_rate(filename="rate_vs_temp.png"):
    """绘制速率因子随温度变化的 log-log 图"""
    T_values = np.logspace(np.log10(3.0e8), np.log10(5.0e9), 100) # 生成在 3e8 K 到 5e9 K 之间的 100 个对数间距的温度值
    q_values = [q3a(T) for T in T_values]  # 对每个温度值计算对应的速率因子
    
    fig, ax = plt.subplots()  # 创建一个新的图形和轴对象
    ax.loglog(T_values, q_values)  # 绘制对数-对数图
    ax.set_xlabel("Temperature T (K)")  # 设置 x 轴标签
    ax.set_ylabel(r"$q_{3\alpha}/(\rho^2 Y^3)$  (erg cm$^6$ g$^{-3}$ s$^{-1}$)")  # 设置 y 轴标签
    ax.set_title("3-α Reaction Rate Factor vs Temperature")  # 设置图表标题
    ax.grid(True, which="both", ls=":") # 显示主要和次要网格线
    #plt.savefig(filename)
    #print(f"图表已保存至 {filename}")
    plt.show() # 如果希望在运行时显示图表，取消此行注释

    # TODO: 在此实现绘图函数
    # 提示：
    # 1. 使用 np.logspace 生成温度数据点
    # 2. 计算对应的速率值
    # 3. 使用 plt.loglog 绘制双对数图
    # 4. 添加适当的标签和标题
    pass

if __name__ == "__main__":
    # 计算并打印 nu 值
    print("   温度 T (K)    :   ν (敏感性指数)")
    print("--------------------------------------")

    temperatures_K = [1.0e8, 2.5e8, 5.0e8, 1.0e9, 2.5e9, 5.0e9]
    h = 1.0e-8  # 扰动因子
    for T0 in temperatures_K:
        q_T0 = q3a(T0)
        if q_T0 == 0: # 避免除以零
            nu = np.nan # Not a Number
        else:
            delta_T = h * T0
            q_T0_plus_deltaT = q3a(T0 + delta_T)
            
            # 使用前向差分计算 dq/dT
            dq_dT_approx = (q_T0_plus_deltaT - q_T0) / delta_T
            
            # 计算 nu
            nu = (T0 / q_T0) * dq_dT_approx
            
        # 格式化输出
        print(f"  {T0:10.3e} K : {nu:8.3f}")

    # (可选) 调用绘图函数
    plot_rate()

    # TODO: 实现温度敏感性指数的计算
    # 提示：
    # 1. 对每个温度点计算 q3a
    # 2. 使用前向差分计算导数
    # 3. 计算敏感性指数 nu
    # 4. 注意处理特殊情况（如 q = 0）

    # TODO: 调用绘图函数展示结果
