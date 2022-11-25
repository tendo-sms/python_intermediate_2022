"""
figsetting.py
概要:ARIM事業におけるfigureの初期設定
"""

__author__      = "National Institute for Materials Science"
__contact__     = "Matsunami.shigeyuki@nims.go.jp"
__license__     = "ARIM Confidential"
__copyright__   = "National Institute for Materials Science, Japan"
__date__        = "2022/10/31"
__revised__     = "2022/11/08"
__version__     = "1.2"

from matplotlib import font_manager

# フォント指定（Google FontのNoto_Sansをデフォルトとする）
FONTPROPERTIY = font_manager.FontProperties(
    fname="NotoSansJP-Medium.otf"
)

# 作図用のフォント
FONT_LABEL = {
    "fontproperties": FONTPROPERTIY,
    "fontsize": 18,
}  # 軸ラベルのフォント設定。デフォルトでは文字サイズ18
FONT_TITLE = {
    "fontproperties": FONTPROPERTIY,
    "fontsize": 16,
}  # タイトルのフォント設定。デフォルトでは文字サイズ16

# 作図初期設定
FIGSIZE = (16, 9)  # グラフサイズ 16:9
LINE_COLOR = "black"  # グラフの線色 黒色
LINE_COLOR2 = 'red'   # グラフの線色 赤色

# see https://matplotlib.org/stable/tutorials/introductory/customizing.html
CONFIG = {
    "lines.linestyle": "solid",  # 線種　実線
    "lines.linewidth": 1,  # 線幅 （points単位）
    "xtick.labelsize": 16,  # font size of the tick labels
    "xtick.direction": "in",  # direction: {in, out, inout}
    "xtick.major.size": 5,  # major tick size in points
    "xtick.minor.size": 3.5,  # minor tick size in points
    "ytick.labelsize": 16,  # font size of the tick labels
    "ytick.direction": "in",  # direction: {in, out, inout}
    "ytick.major.size": 5,  # major tick size in points
    "ytick.minor.size": 3.5,  # minor tick size in points
    "axes.grid.axis": "both",  # which axis the grid should apply to
    "axes.grid.which": "major",  # grid lines at {major, minor, both} ticks
    "grid.color": "gray",  # グリッドの線色
    "grid.linestyle": "--",  # グリッドの線設定　破線
    "grid.linewidth": 0.6,  # グリッド線幅　（points単位）
    "savefig.dpi": 600,  # 図の解像度（dpi単位）
    "savefig.format": "png",  # 図の出力フォーマット　{png, ps, pdf, svg}
}
