#!/usr/bin/env python3
"""SauceNAO CLI実行用ラッパースクリプト"""
import sys
import os
import importlib.util
import types

# プロジェクトルートをパスに追加
project_root = os.path.dirname(os.path.abspath(__file__))
sauce_nao_path = os.path.join(project_root, "sauce-nao")
sys.path.insert(0, project_root)
sys.path.insert(0, sauce_nao_path)

# 親モジュールを作成（相対インポート用）
def create_module(name):
    """モジュールを作成してsys.modulesに登録"""
    module = types.ModuleType(name)
    sys.modules[name] = module
    return module

# 必要な親モジュールをすべて作成
create_module("sauce_nao")
create_module("sauce_nao.domain")
create_module("sauce_nao.domain.entities")
create_module("sauce_nao.domain.repositories")
create_module("sauce_nao.usecase")
create_module("sauce_nao.infrastructure")
create_module("sauce_nao.infrastructure.saucenao")
create_module("sauce_nao.interface")

# モジュールを順番に読み込む（依存関係の順序）
def load_module(module_name, file_path):
    """モジュールを読み込む"""
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

# Domain層を読み込み
load_module("sauce_nao.domain.entities.search_result", 
            os.path.join(sauce_nao_path, "domain", "entities", "search_result.py"))
load_module("sauce_nao.domain.repositories.image_search_repository",
            os.path.join(sauce_nao_path, "domain", "repositories", "image_search_repository.py"))

# Usecase層を読み込み
load_module("sauce_nao.usecase.search_image_usecase",
            os.path.join(sauce_nao_path, "usecase", "search_image_usecase.py"))

# Infrastructure層を読み込み
load_module("sauce_nao.infrastructure.saucenao.saucenao_repository",
            os.path.join(sauce_nao_path, "infrastructure", "saucenao", "saucenao_repository.py"))

# Interface層を読み込み
cli_module = load_module("sauce_nao.interface.cli",
                         os.path.join(sauce_nao_path, "interface", "cli.py"))

if __name__ == "__main__":
    cli_module.main()
