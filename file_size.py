import os

def process_file(filepath):
    """
    ファイルサイズをチェックして、10MBを超える場合はスキップ。
    """
    max_size = 10 * 1024 * 1024  # 10MB
    try:
        # ファイルサイズを取得
        file_size = os.path.getsize(filepath)
        
        if file_size > max_size:
            print(f"スキップ: ファイルサイズが10MBを超えています ({file_size / (1024 * 1024):.2f} MB): {filepath}")
            return None  # 処理をスキップ
        
        # ファイル処理をここに記述
        print(f"処理中: {filepath} ({file_size / (1024 * 1024):.2f} MB)")
        # 例: ファイル内容を読み取る
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            # 処理内容を記述（例: 要旨抽出やクレンジングなど）
            print("ファイル処理完了")
            return content  # 必要に応じて結果を返す

    except Exception as e:
        print(f"エラー: ファイル {filepath} の処理中に問題が発生しました: {str(e)}")
        return None


# ファイルリストの例
file_list = [
    "sample1.txt",  # ファイル1
    "sample2.txt",  # ファイル2
    "large_file.txt"  # 10MB超のファイル
]

# ファイルごとに処理
for file_path in file_list:
    if os.path.exists(file_path):
        result = process_file(file_path)
    else:
        print(f"ファイルが見つかりません: {file_path}")
