"""CLIエントリーポイント"""
import sys
from ..usecase.search_comic_usecase import SearchComicUseCase
from ..infrastructure.ximilar.ximilar_repository import XimilarRepository


def main():
    """CLIメイン関数"""
    if len(sys.argv) != 2:
        print("使用方法: python -m ximilar-comics.interface.cli <画像ファイルパス>")
        print("または: python ximilar-comics/interface/cli.py <画像ファイルパス>")
        sys.exit(1)
    
    image_path = sys.argv[1]
    
    try:
        # リポジトリとユースケースの初期化
        repository = XimilarRepository()
        use_case = SearchComicUseCase(repository)
        
        # 検索実行
        results = use_case.execute(image_path)
        
        if not results:
            print("検索結果が見つかりませんでした。")
            sys.exit(0)
        
        # 上位3件のみ表示
        top_results = results[:3]
        
        # 結果を表示
        print(f"\n検索結果 (上位{len(top_results)}件 / 全{len(results)}件):\n")
        print("=" * 50)
        
        for i, result in enumerate(top_results, 1):
            print(f"\n[{i}]")
            print(result)
            if i < len(top_results):
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

