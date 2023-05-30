from factory import CreateQGUI
from banner_tools import GitHub, wiki
from notebook_tools import *
from manager import QStyle, HORIZONTAL
from script.secret_scan import secret_scan
from script.bucket_discovery import bucket_discovery
from script.config_scan import config_scan
from script.policy_scan import policy_scan
from script.bucket_takeover import bucket_takeover
from script.about import about


# 创建主界面
q_gui = CreateQGUI(title="云存储漏洞挖掘工具", tab_names=["密钥泄露检测", "存储桶发现", "存储桶权限检测", "存储桶策略检测", "存储桶接管", "工具相关"], style=QStyle.default)  # 界面标题，界面中心部分的分页标题，皮肤
# 在界面最上方添加一个按钮，链接到GitHub主页
q_gui.add_banner_tool(GitHub(url="https://github.com/huacheng1122/Cloud-storage-service-vul-scanner"))
# 云存储安全wiki
q_gui.add_banner_tool(wiki(url="https://docs.qq.com/doc/DU2t6RUdQRW92d2FC"))

# 【密钥泄露检测】
global frame1_url_input
frame1_url_input=InputBox(name="目标url输入框", label_info="相关目标站点URL", default="加载了存储服务的站点url")
q_gui.add_notebook_tool(frame1_url_input)
global frame1_keys_input
frame1_keys_input=InputBox(name="目标关键字输入框", label_info="目标相关关键字", default="如域名、公司名、存储桶地址，以英文逗号间隔")
q_gui.add_notebook_tool(frame1_keys_input)
# HorizontalToolsCombine，它可以接受一组工具并将其进行水平排列
frame1_cloud = Label(text="目前支持检测的云存储服务厂商：阿里云OSS、腾讯云COS、百度云COS", alignment=LEFT, tab_index=0)
run_menu = HorizontalFrameCombine([frame1_cloud, RunButton(bind_func=secret_scan, padx=50)])
q_gui.add_notebook_tool(run_menu)


# 【存储桶发现】
global frame2_url_input
frame2_url_input=InputBox(name="目标url输入框", label_info="相关目标站点URL", default="加载了存储服务的站点url或相关资产的url", tab_index=1)
q_gui.add_notebook_tool(frame2_url_input)
# HorizontalToolsCombine，它可以接受一组工具并将其进行水平排列
frame2_cloud = Label(text="目前支持检测的云存储服务厂商：阿里云OSS、腾讯云COS、百度云COS", alignment=LEFT, tab_index=1)
run_menu2 = HorizontalFrameCombine([frame2_cloud, RunButton(bind_func=bucket_discovery, padx=50)])
q_gui.add_notebook_tool(run_menu2)

# 【存储桶权限检测】
global frame3_url_input
frame3_url_input=InputBox(name="目标url输入框", label_info="存储桶域名地址", default="存储桶域名地址", tab_index=2)
q_gui.add_notebook_tool(frame3_url_input)
# HorizontalToolsCombine，它可以接受一组工具并将其进行水平排列
frame3_cloud = Label(text="目前支持检测的云存储服务厂商：阿里云OSS、腾讯云COS、百度云COS", alignment=LEFT, tab_index=2)
run_menu3 = HorizontalFrameCombine([frame3_cloud, RunButton(bind_func=config_scan, padx=50)])
q_gui.add_notebook_tool(run_menu3)

# 【存储桶策略检测】
global frame4_url_input
frame4_url_input=InputBox(name="目标url输入框", label_info="存储桶域名地址", default="存储桶域名地址", tab_index=3)
q_gui.add_notebook_tool(frame4_url_input)
# HorizontalToolsCombine，它可以接受一组工具并将其进行水平排列
frame4_cloud = Label(text="目前支持检测的云存储服务厂商：阿里云OSS、腾讯云COS、百度云COS", alignment=LEFT, tab_index=3)
run_menu4 = HorizontalFrameCombine([frame4_cloud, RunButton(bind_func=policy_scan, padx=50)])
q_gui.add_notebook_tool(run_menu4)

# 【存储桶接管】
global frame5_url_input
frame5_url_input=InputBox(name="目标url输入框", label_info="存储桶域名地址", default="存储桶域名地址", tab_index=4)
q_gui.add_notebook_tool(frame5_url_input)
# HorizontalToolsCombine，它可以接受一组工具并将其进行水平排列
frame5_cloud = Label(text="目前支持检测的云存储服务厂商：阿里云OSS、腾讯云COS、百度云COS", alignment=LEFT, tab_index=4)
run_menu5 = HorizontalFrameCombine([frame5_cloud, RunButton(bind_func=bucket_takeover, padx=50)])
q_gui.add_notebook_tool(run_menu5)

# 【工具相关】
combine_left = VerticalFrameCombine([BaseButton(bind_func=about, text="功能简介", padx=50, pady=3, tab_index=2)], tab_index=5,
                                    text="关于：\n" \
                                        "\n" \
                                        "本工具是为白帽子以及企业相关人员提供了关于主流云存储服务安全漏洞的自动化挖掘以及检测。   作者：花城\n" \
                                        "\n" \
                                        "坚决反对利用该工具进行非法测试或恶意攻击行为，一切后果自行承担，推荐大家在了解技术原理的前提下，共同维护\n" \
                                        "\n" \
                                        "信息安全、网络安全！！！\n" \
                                        "")
q_gui.add_notebook_tool(combine_left)

# 运行
q_gui.run()



