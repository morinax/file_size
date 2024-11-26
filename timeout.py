import threading
import time

def process_file(filepath):
    """
    ファイルを処理する（長時間かかる可能性あり）。
    実際の処理内容をこの関数に記述。
    """
    print(f"処理開始: {filepath}")
    time.sleep(5)  # ダミー処理（5秒かかる）
    print(f"処理完了: {filepath}")
    return f"Processed {filepath}"


def process_with_timeout(filepath, timeout=3):
    """
    ファイル処理をタイムアウト付きで実行。
    timeout秒以内に処理が完了しない場合はスキップ。
    """
    result = None
    thread = threading.Thread(target=lambda: process_file(filepath))
    thread.start()
    thread.join(timeout=timeout)  # 指定したタイムアウト時間で待つ

    if thread.is_alive():
        print(f"タイムアウト: {filepath} の処理をスキップしました")
        thread.join()  # スレッドを終了
    else:
        result = f"{filepath} の処理が完了しました"

    return result


# ファイルリストの例
file_list = ["file1.txt", "file2.txt", "file3.txt"]

# 各ファイルを処理
for file in file_list:
    print(process_with_timeout(file, timeout=4))  # タイムアウトは4秒
