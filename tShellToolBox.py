# coding: UTF-8
import tJson
import sys


class ShellToolBox(object):
    @staticmethod
    def instPars(inst: str):
        return inst.split(" ")

    @staticmethod
    def comLine(beginningPrompt: str = "",
                body: str = "Undefined",
                endPrompt: str = ">",
                end: str = " ",
                wtu: bool = False):
        if not wtu:
            bp = beginningPrompt
            ep = endPrompt
            return bp + body + ep + end
        else:
            bp = "[italic green]" + beginningPrompt + "[/italic green]"
            ep = "[italic yellow]" + endPrompt + "[/italic yellow]"
            return bp + " " + body + ep + end

    @staticmethod
    def welcomeWords():
        til_json = tJson.Json
        info = til_json.readJson("appData.json")["info"]

        welcomeWords = "欢迎使用 " + "PowerTools" + "！  [版本："
        if info["UpdateChannel"] == "OFFICIAL":
            welcomeWords = welcomeWords + info["version"]
        else:
            welcomeWords = welcomeWords + info["UpdateChannel"] + info["version"]

        welcomeWords = welcomeWords + "]\n开发者：萧啸 保留所有权利\n"
        return welcomeWords

    @staticmethod
    def quitMain(userInput: str):
        if userInput == "exit" or userInput == "quit" or userInput == "e" or userInput == "q":
            sys.exit(0)

    @staticmethod
    def error(ET: str = None, OLI: str = None, NOR: str = None, AIE: str = None, SGP: str = None):
        jsons = tJson.Json
        WSG = jsons.readJson("appData.json")["PTS"]["wsg"]
        WSG = ", ".join(WSG)
        print(f"""
ERROR:
  + Error Entered
      - [{NOR}] {OLI}
      - [{AIE}]

  + What The Shell Gets
      - {WSG}

  + Error Type
      - {ET}

  + Shell Get Path
      - [List] {SGP}
        """)

    @staticmethod
    def errorHelp():
        helping = """
        OLI : Original line input               : 原行输入 -
        NOR : The number of original rows       : 原行数 -
        WSG : What the shell gets               : Shell 获取到的
        ET  : Error type                        : 错误类型
        AIE : Approximate location of the error : 错误大致位置
        SGP : Shell Get Path                    : Shell 获取路径 : List

        ERROR:
          + Error Entered
                - [{NOR}] {OLI}
                - [{AIE}]

          + What The Shell Gets
                - {WSG}

          + Error Type
                - {ET}
          + Shell Get Path
                - [List] {SGP}
        """
        print(helping)

    @staticmethod
    def backtracking(UILB, UIB, GoBackTo: int = 1):
        pass
