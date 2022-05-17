from abc import ABCMeta, abstractclassmethod
from typing import List
from injector import inject
import json

from obn.models.task import BingoTask
from obn.providers.file_system_provider import AbstractFileSystemProvider


class AbstractBingoTaskParser(metaclass=ABCMeta):
    """
    ビンゴタスクをパースするインターフェースを表す抽象クラス
    """

    @abstractclassmethod
    def parse(self, target_file_path: str) -> List[BingoTask]:
        """
        指定したjsonファイルパスのビンゴタスクを読み込む

        Parameters
        ----------
        target_file_path: 対象のビンゴタスクデータが格納されているjsonファイルパス

        Returns
        -------
        ビンゴタスクデータモデルのリスト
        """

        pass

    @abstractclassmethod
    def is_task_model(self, obj: dict) -> bool:
        """
        dictオブジェクトがビンゴのタスクモデル型であるかを判定する
        """

        pass


class BingoTaskParser(AbstractBingoTaskParser):
    @inject
    def __init__(self, fsp: AbstractFileSystemProvider) -> None:
        self.__fsp = fsp

        return

    def parse(self, target_file_path):
        if not self.__fsp.exist_file(target_file_path):
            raise FileNotFoundError("`{0}`は存在しません".format(target_file_path))

        raw_json = {}
        with open(target_file_path, 'r', encoding='utf-8') as fr:
            raw_json: dict[str, list[dict]] = json.load(fr)
            fr.close()
            pass

        internal_id = 1
        bingo_tasks: List[BingoTask] = []
        for _, v_diff_tasks in raw_json.items():
            if type(v_diff_tasks) is not list:
                # ここでリスト型ではない場合、タスクデータではないので無視する
                continue
            for task_dict in v_diff_tasks:
                if not self.is_task_model(task_dict):
                    continue
                bingo_task = BingoTask(internal_id=internal_id, obj=task_dict)
                bingo_tasks.append(bingo_task)
                internal_id += 1
                pass
            pass

        return bingo_tasks

    def is_task_model(self, obj):
        if type(obj) is not dict:
            return False

        if 'name' not in obj:
            return False

        if 'jp' not in obj:
            return False

        if 'difficulty' not in obj:
            return False

        return True


class BingoTaskParserMock(AbstractBingoTaskParser):
    @inject
    def __init__(self, fsp: AbstractFileSystemProvider) -> None:
        self.__fsp = fsp

        return

    def parse(self, target_file_path):
        bingo_tasks: List[BingoTask] = [
            BingoTask(None, {
                "name": "MockTaskName_1",
                "jp": "モックタスク_1",
                "difficulty": 1
            }),
            BingoTask(None, {
                "name": "MockTaskName_2",
                "jp": "モックタスク_2",
                "difficulty": 2
            }),
            BingoTask(None, {
                "name": "MockTaskName_3",
                "jp": "モックタスク_3",
                "difficulty": 3
            }),
        ]

        for i, bingo_task in enumerate(bingo_tasks, 1):
            bingo_task.internal_id = i

        return bingo_tasks

    def is_task_model(self, obj):
        return True
