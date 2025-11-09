#!/usr/bin/env python3
"""trace.moe CLI実行用ラッパースクリプト"""
import sys
import os
import importlib.util
import types

# プロジェクトルートをパスに追加
project_root = os.path.dirname(os.path.abspath(__file__))
trace_moe_path = os.path.join(project_root, "trace-moe")
sys.path.insert(0, project_root)
sys.path.insert(0, trace_moe_path)

# 親モジュールを作成（相対インポート用）
def create_module(name):
    """モジュールを作成してsys.modulesに登録"""
    module = types.ModuleType(name)
    sys.modules[name] = module
    return module

# 必要な親モジュールをすべて作成
create_module("trace_moe")
create_module("trace_moe.domain")
create_module("trace_moe.domain.entities")
create_module("trace_moe.domain.repositories")
create_module("trace_moe.usecase")
create_module("trace_moe.infrastructure")
create_module("trace_moe.infrastructure.tracemoe")
create_module("trace_moe.interface")

# モジュールを順番に読み込む（依存関係の順序）
def load_module(module_name, file_path):
    """モジュールを読み込む"""
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

# Domain層を読み込み
load_module("trace_moe.domain.entities.anime_result", 
            os.path.join(trace_moe_path, "domain", "entities", "anime_result.py"))
load_module("trace_moe.domain.repositories.anime_search_repository",
            os.path.join(trace_moe_path, "domain", "repositories", "anime_search_repository.py"))

# Usecase層を読み込み
load_module("trace_moe.usecase.search_anime_usecase",
            os.path.join(trace_moe_path, "usecase", "search_anime_usecase.py"))

# Infrastructure層を読み込み
load_module("trace_moe.infrastructure.tracemoe.tracemoe_repository",
            os.path.join(trace_moe_path, "infrastructure", "tracemoe", "tracemoe_repository.py"))

# Interface層を読み込み
cli_module = load_module("trace_moe.interface.cli",
                         os.path.join(trace_moe_path, "interface", "cli.py"))

if __name__ == "__main__":
    cli_module.main()

