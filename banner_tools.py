# 导航栏按钮模块
import os
import webbrowser
import tkinter
from tkinter import ttk
from manager import ICON_PATH, ConcurrencyModeFlag
from base_tools import ArgInfo, BaseTool

RUN_ICON = os.path.join(ICON_PATH, "play_w.png")
GITHUB_ICON = os.path.join(ICON_PATH, "github.png")
WIKI_ICON =  os.path.join(ICON_PATH, "up_cloud.png")

"""
    基础Banner工具集
    需注意的是，如需增加异步等操作，请为函数添加_callback
"""
class BaseBarTool(BaseTool):
    def __init__(self, bind_func, name="未命名组件", icon=None, style=None, async_run: bool = True, concurrency_mode=ConcurrencyModeFlag.SAFE_CONCURRENCY_MODE_FLAG):
        super().__init__(bind_func=bind_func, name=name, style=style, async_run=async_run, concurrency_mode=concurrency_mode)

        if icon and not os.path.exists(icon):
            raise f"请确认{os.path.abspath(icon)}是否存在"
        if not icon:
            icon = RUN_ICON
        self.icon = icon

    def build(self, *args, **kwargs):
        super().build(*args, **kwargs)
        self.img = tkinter.PhotoImage(file=self.icon)
        btn = ttk.Button(self.master, text=self.name, image=self.img, compound="left", command=self._callback(self.bind_func) if self.async_run else self.bind_func, style=self.style + "TButton")
        btn.pack(side="left", ipadx=5, ipady=5, padx=0, pady=1)



# GitHub模块
class GitHub(BaseBarTool):
    def __init__(self, url, name="GitHub项目", style="primary"):
        icon = GITHUB_ICON
        bind_func = self.github_callback
        super().__init__(bind_func, name=name, icon=icon, style=style)
        self.github_url = url

    # 点击链接执行函数
    def github_callback(self, args):
        webbrowser.open_new(self.github_url)


# wiki模块
class wiki(BaseBarTool):
    def __init__(self, url, name="云存储安全WIKI", style="primary"):
        icon = WIKI_ICON
        bind_func = self.wiki_callback
        super().__init__(bind_func, name=name, icon=icon, style=style)
        self.wiki_url = url

    # 点击链接执行函数
    def wiki_callback(self, args):
        webbrowser.open_new(self.wiki_url)
