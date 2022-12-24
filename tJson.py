# coding: UTF-8
import json


class Json(object):
    @staticmethod
    def readJson(fileName: str):
        with open(fileName) as f:
            data = json.load(f)

        return data

    @staticmethod
    def writeJson(fileName: str, content: dict):
        with open(fileName, "utf-8") as f:
            json.dump(content, f, ensure_ascii=False)
