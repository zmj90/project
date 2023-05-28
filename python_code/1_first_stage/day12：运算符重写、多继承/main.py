"""
    入口
"""
# import usl
#
# view = usl.EpidemicInformationView()
# view.main()
from usl import EpidemicInformationView

# 入口代码,当前模块只有是主模块,才满足条件。
if __name__ == '__main__':
    view = EpidemicInformationView()
    view.main()