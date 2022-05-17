from abc import ABCMeta, abstractclassmethod
from mailbox import FormatError
from typing import List


class AbstractMarkdownService(metaclass=ABCMeta):
    """
    マークダウンのサービスを提供する抽象クラス
    """

    @abstractclassmethod
    def stdout_table(self, headers: List[str], rows: List[List[str]]) -> None:
        """
        マークダウン形式の表を標準出力する
        """

        pass


class MarkdownService(AbstractMarkdownService):
    def __init__(self) -> None:
        return

    def stdout_table(self, headers, rows):
        header_length = len(headers)
        for i, row in enumerate(rows, 1):
            row_length = len(row)
            if header_length is not row_length:
                raise FormatError("ヘッダーと内容の項目数が一致しません。ヘッダー数: {0}, {1}行目の数: {2}".format(header_length, i, row_length))

        # ヘッダーを出力
        header = "| " + " | ".join(headers) + " |"
        print(header)

        # ヘッダーとデータ行の分離線を出力
        diver = "| " + " | ".join(["---"] * header_length) + " |"
        print(diver)

        # データ行を出力
        for row in rows:
            line = "| " + " | ".join(row) + " |"
            print(line)
            pass

        return


class MarkdownServiceMock(AbstractMarkdownService):
    def __init__(self) -> None:
        return

    def stdout_table(self, headers, rows):
        print("| カラムA | カラムB | カラムC |")
        print("| --- | --- | --- |")
        print("| データ1-A | データ1-B | データ1-C |")
        print("| データ2-A | データ2-B | データ2-C |")
        print("| データ3-A | データ3-B | データ3-C |")
        print("| データ4-A | データ4-B | データ4-C |")
        return
