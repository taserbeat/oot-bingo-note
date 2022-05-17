from typing import Union


class BingoTask:
    """
    ビンゴタスクのデータモデル
    """

    def __init__(self, internal_id: Union[int, None], obj: dict) -> None:
        self.__internal_id = 0 if internal_id is None else internal_id
        self.__name = obj.get('name', "")
        self.__jp = obj.get('jp', "")
        self.__difficulty = obj.get('difficulty', 0)
        return

    @property
    def internal_id(self) -> int:
        return self.__internal_id

    @internal_id.setter
    def internal_id(self, internal_id: int) -> None:
        self.__internal_id = internal_id
        return

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name
        return

    @property
    def jp(self) -> str:
        return self.__jp

    @jp.setter
    def jp(self, jp: str) -> None:
        self.__jp = jp
        return

    @property
    def difficulty(self) -> str:
        return self.__difficulty

    @difficulty.setter
    def difficulty(self, difficulty: str) -> None:
        self.__difficulty = difficulty
        return
