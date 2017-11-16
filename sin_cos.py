import numpy as np
import pylab as plt

def sin_draw():
    # num = np.arange(1,5,0.001)*np.pi
    # sin = np.sin(num)
    # cos = np.cos(num)
    # plt.plot(sin)
    # plt.plot(cos)
    # plt.plot(sin/2)
    # plt.show()

    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib.font_manager import FontProperties
    fp = FontProperties(fname='C:\WINDOWS\Fonts\msgothic.ttc', size=14)

    x = np.linspace(0, np.pi * 2.1, 100)
    # plt.plot(x, np.cos(x) * 0.8, "r")
    # plt.plot(x, np.sin(x) * 0.8, "olive")
    plt.plot(x, np.sin(x), "b")
    plt.plot(x, np.sin(x) * 0.8 + np.cos(x)*0.4, "black")

    #plt.legend([u'粘性100%',"弾性100%", "入力", '測定結果'], prop=fp, loc='lower left')
    plt.legend(["入力", '測定結果'], prop=fp, loc='lower left')

    #plt.legend([u'粘性100%', "弾性100%", "入力"], prop=fp, loc='lower left')
    plt.title("弾性と粘性", loc="center", fontproperties=fp)

    plt.xlim(xmin=0)
    plt.ylim(-1.1, 1.1)
    xtick = np.array(["0", "1/2π", "π","3/2π","2π"])
    locs = np.linspace(0, np.pi*2, 5)
    plt.xticks(locs, xtick, color="black", fontsize=14, rotation=0)
    plt.yticks([-1, 0, 1])

    ax = plt.gca()  # get current axis
    ax.spines["right"].set_color("none")  # 右枠消し
    ax.spines["top"].set_color("none")  # 上枠消し
    ax.spines["left"].set_color("b")
    ax.spines["bottom"].set_color("b")

    plt.vlines(np.linspace(0, np.pi*2, 5),
               -1.1, 1.1, "c", linestyle=":", lw=1)
    plt.hlines([0], -np.pi, np.pi * 2.1, "m", linestyle=":", lw=1)

    plt.legend()  # 凡例の表示
    plt.show()


if __name__ == '__main__':
    sin_draw()