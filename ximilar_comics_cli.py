#!/usr/bin/env python3
"""Ximilar Comics CLI実行用ラッパースクリプト"""
import sys
import os
import importlib.util
import types

# プロジェクトルートをパスに追加
project_root = os.path.dirname(os.path.abspath(__file__))
ximilar_comics_path = os.path.join(project_root, "ximilar-comics")
sys.path.insert(0, project_root)
sys.path.insert(0, ximilar_comics_path)

# 親モジュールを作成（相対インポート用）
def create_module(name):
    """モジュールを作成してsys.modulesに登録"""
    module = types.ModuleType(name)
    sys.modules[name] = module
    return module

# 必要な親モジュールをすべて作成
create_module("ximilar_comics")
create_module("ximilar_comics.domain")
create_module("ximilar_comics.domain.entities")
create_module("ximilar_comics.domain.repositories")
create_module("ximilar_comics.usecase")
create_module("ximilar_comics.infrastructure")
create_module("ximilar_comics.infrastructure.ximilar")
create_module("ximilar_comics.interface")

# モジュールを順番に読み込む（依存関係の順序）
def load_module(module_name, file_path):
    """モジュールを読み込む"""
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

# Domain層を読み込み
load_module("ximilar_comics.domain.entities.comic_result", 
            os.path.join(ximilar_comics_path, "domain", "entities", "comic_result.py"))
load_module("ximilar_comics.domain.repositories.comic_search_repository",
            os.path.join(ximilar_comics_path, "domain", "repositories", "comic_search_repository.py"))

# Usecase層を読み込み
load_module("ximilar_comics.usecase.search_comic_usecase",
            os.path.join(ximilar_comics_path, "usecase", "search_comic_usecase.py"))

# Infrastructure層を読み込み
load_module("ximilar_comics.infrastructure.ximilar.ximilar_repository",
            os.path.join(ximilar_comics_path, "infrastructure", "ximilar", "ximilar_repository.py"))

# Interface層を読み込み
cli_module = load_module("ximilar_comics.interface.cli",
                         os.path.join(ximilar_comics_path, "interface", "cli.py"))

if __name__ == "__main__":
    cli_module.main()

