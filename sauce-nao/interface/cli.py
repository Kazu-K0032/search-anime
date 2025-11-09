"""CLIエントリーポイント"""
import sys
from ..usecase.search_image_usecase import SearchImageUseCase
from ..infrastructure.saucenao.saucenao_repository import SauceNAORepository


def main():
    """CLIメイン関数"""
    if len(sys.argv) != 2:
        print("使用方法: python -m sauce-nao.interface.cli <画像ファイルパス>")
        print("または: python sauce-nao/interface/cli.py <画像ファイルパス>")
        sys.exit(1)
    
    image_path = sys.argv[1]
    
    try:
        # リポジトリとユースケースの初期化
        repository = SauceNAORepository()
        use_case = SearchImageUseCase(repository)
        
        # 検索実行
        results = use_case.execute(image_path)
        
        if not results:
            print("検索結果が見つかりませんでした。")
            sys.exit(0)
        
        # 結果を表示
        print(f"\n検索結果 ({len(results)}件):\n")
        print("=" * 50)
        
        for i, result in enumerate(results, 1):
            print(f"\n[{i}]")
            print(result)
            if i < len(results):
                print("-" * 50)
        
        print("\n" + "=" * 50)
    
    except FileNotFoundError as e:
        print(f"エラー: {e}", file=sys.stderr)
        sys.exit(1)
    
    except ValueError as e:
        print(f"エラー: {e}", file=sys.stderr)
        sys.exit(1)
    
    except Exception as e:
        print(f"エラー: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

