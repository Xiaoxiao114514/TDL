# coding: UTF-8
"""
版本号 = 2.5.8

x = 正式版版本号
y = 正式版本发布时 公测版版本号（<10）
z = 正式版本发布时 内部测试版版本号（<10）
"""
import os
import sys

Version = "2.5.8"
WorkingDirectory = os.getcwd()
Path = sys.path

OwnPath = Path[0]
OneLevelDirectories = Path[1]
PyLibPath = sys.path[9]

UpdateLoger = """
Quick Facts:
[update] CLITool           (1.0.2) |^| (2.5.8)
[update] DesEncryptor      (1.0.2) |^| (2.5.8)
[update] Json              (1.0.2) |^| (2.5.8)
[update] Logger            (1.0.2) |^| (2.5.8)
[delete] LPVM                      |-|
[update] Tzip              (1.0.2) |^| (2.5.8)
[update] RSA               (1.0.2) |^| (2.5.8)
[update] DigitalProcessing (1.0.2) |^| (2.5.8)
[delete] Badl                      |-|
[delete] ErrorTypeTable            |-|


Log:
DC: DirectoryChanges

[    DC    ] 我们规整了 TDL 目录。
[    DC    ] 我们将所有的功能开头添加了 't' ，这样便于开发。
[    DC    ] 我们关闭了渠道提示。

[  Delete  ] 删除了 Badl(Basic Advanced Development Libraries) 功能。
[  Delete  ] 删除了 LPVM(Local Project Version Management) 功能。
[  Delete  ] 删除了 ETT(ErrorTypeTable) 表。

[  Revise  ] 修改了 Transwarp Development Library 使用条款

[  reName  ] CLITool 更名为 Shell Tool Box。

[   Next   ] 将会删除功能的定义类步骤，这样可以直接访问，这样便于开发。

[ Previews ] 我们已经结束了名为 Builder 计划。
[ Previews ] 我们已经启动了名为 Bridge 计划。


info:
Copyright Holder: Mr. Python / 萧啸
VersionName: Builder
"""
UOP = """
Use of Protocols: 
Transwarp Development Library 使用条款
1. 本运行库仅起到方便开发人员使用的作用，严禁以任何形式超范围使用本运行库的代码。
2. 本运行库仅有 Transwarp Development Library 发行版，与 TDL_耿博源发行版得到了认可，其他一切未经认可的发行版运行库不会得到任何服务。
3. 本运行库遵循 Apache 2.0 开源协议。
4. 最终解释权归 萧啸 所有。
5. 如果未遵守 Apache 2.0 开源协议，造成的一切后果由非法使用者承担。
6. 严禁以任何形式传播本运行库的修改代码。
8. 严禁使用本运行库去做任何非法行为。
"""
