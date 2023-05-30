from typing import List
import tkinter
import tkinter.font
from ttkbootstrap import Style
from manager import QStyle, FONT
from base_frame import BaseNoteBook, BaseBanner
from banner_tools import BaseBarTool
from notebook_tools import BaseNotebookTool
from base_tools import check_callable


class CreateQGUI:
    """
    创建最基础的QGUI程序

    :param title: 主程序标题
    :param style: 皮肤，需通过QStyle来确定
    :param stout: 标准输出流
    :param tab_names: List[str] 功能区Tab页面，默认为“主程序控制台”
    :param banner: QGUI的Banner对象
    :param notebook: QGUI的notebook对象
    :param bind_func: 全局事件绑定
    """

    def __init__(self,
                 title="未命名应用",
                 style: dict = None,
                 stout=None,
                 tab_names: List[str] = None,
                 banner: BaseBanner = None,
                 notebook: BaseNoteBook = None,
                 bind_func=None):
        super().__init__()
        self.title = title
        self.style = style

        self.root = tkinter.Tk()
        if bind_func:
            check_callable(bind_func=bind_func)
            self.root.bind_all("<1>", bind_func)
        if self.style:
            self.root.style = Style(**self.style)
        else:
            self.root.style = Style(**QStyle.default)
        self.root.style.configure('bg.TFrame', background=self.root.style.colors.inputbg)
        self.root.style.configure('bg.TLabel', background=self.root.style.colors.inputbg)
        default_font = tkinter.font.nametofont("TkDefaultFont")
        default_font.configure(family=FONT, size=10)
        self.root.option_add("*Font", "TkDefaultFont")
        self.root.geometry('780x560')
        # self.root.update()
        self.root.wm_resizable(False, False)
        self.root.title(self.title)

        # 初始化组件
        self.banner = banner if banner else BaseBanner(title=self.title)
        self.notebook = notebook if notebook else BaseNoteBook(tab_names=tab_names, stdout=stout)

        self.banner.build(self.root, self.get_global_info)
        self.notebook.build(self.root, self.get_global_info)

    @property
    def get_global_info(self):
        # ToDo 做个 global_info管理器，目前信息只从Notebook中流出
        return self.notebook.global_info

    def add_banner_tool(self, tool: BaseBarTool):
        """
        在程序最上方添加小组件
        :param tool: 继承于BaseBarTool的组件对象

        Example
            from qgui.banner_tools import GitHub
            q_gui = CreateQGUI()
            q_gui.add_banner_tool(GitHub())
        """
        self.banner.add_tool(tool)

    abt = add_banner_tool

    def add_notebook_tool(self, tool: BaseNotebookTool):
        """
        在程序中央功能区添加小组件
        :param tool: 继承于BaseNotebookTool的组件对象

        Example
            from qgui.notebook_tools import RunButton
            q_gui.add_notebook_tool(RunButton())
        """
        self.notebook.add_tool(tool)

    ant = add_notebook_tool


    def print_tool(self, tool: BaseNotebookTool):
        """
        在终端中打印组件
        :param tool: 继承于BaseNotebookTool的组件对象
        """
        self.notebook.print_tool(tool)

    def print_image(self, image):
        """
        在终端中打印图像
        :param image: 图像所在路径 or pillow图片对象
        """
        self.notebook.print_image(image)

    def run(self):
        """
        展示GUI界面
        """
        self.root.mainloop()


if __name__ == '__main__':
    from banner_tools import BaseBarTool
    from notebook_tools import BaseChooseFileTextButton

    _tmp = CreateQGUI()
    _tmp.add_banner_tool(BaseBarTool(lambda: print(0)))
    _tmp.add_notebook_tool(BaseChooseFileTextButton(lambda: print(1)))
    _tmp.run()
