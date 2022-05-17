import os
from typing import List
from injector import Binder, Injector, Module

from obn.providers.file_system_provider import AbstractFileSystemProvider, FileSystemProvider, FileSystemProviderMock
from obn.services.markdown_system import AbstractMarkdownService, MarkdownService, MarkdownServiceMock
from obn.services.task_parser import AbstractBingoTaskParser, BingoTaskParser, BingoTaskParserMock


GOAL_LIST_JSON_PATH = "./target_version/goal-list.json"


class ProductionDIModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(AbstractFileSystemProvider, FileSystemProvider)
        binder.bind(FileSystemProvider, to=FileSystemProvider)

        binder.bind(AbstractBingoTaskParser, BingoTaskParser)
        binder.bind(BingoTaskParser, to=BingoTaskParser)

        binder.bind(AbstractMarkdownService, MarkdownService)
        binder.bind(MarkdownService, to=MarkdownService)
        return


class TestDIModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(AbstractFileSystemProvider, FileSystemProviderMock)
        binder.bind(FileSystemProvider, to=FileSystemProviderMock)

        binder.bind(AbstractBingoTaskParser, BingoTaskParserMock)
        binder.bind(BingoTaskParser, BingoTaskParserMock)

        binder.bind(AbstractMarkdownService, MarkdownServiceMock)
        binder.bind(MarkdownService, to=MarkdownService)
        return


# 環境変数で実行環境を指定する
# production: 実際のjsonファイルを読み込む (規定値)
# test: 決め打ちで用意したモックデータを読み込む
exe_env = os.environ.get('OBN_ENV', 'production').lower()

di_module: Module = TestDIModule() if exe_env == 'test' else ProductionDIModule()
di_container = Injector(di_module)

parser = di_container.get(BingoTaskParser)

bingo_tasks = parser.parse(GOAL_LIST_JSON_PATH)

md_service = di_container.get(MarkdownService)

headers = ["通し番号", "タスク名", "タスク名(日本語)", "難しさ"]
rows = []
for bingo_task in bingo_tasks:
    row: List[str] = [
        str(bingo_task.internal_id),
        str(bingo_task.name),
        str(bingo_task.jp),
        str(bingo_task.difficulty)
    ]
    rows.append(row)

md_service.stdout_table(headers=headers, rows=rows)
