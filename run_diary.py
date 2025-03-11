import sys
import subprocess

# ファイルパスを取得
if len(sys.argv) < 2:
    print("ファイルを入力して")
    sys.exit(1)

file_path = sys.argv[1]

# today_event = input("今日の出来事を入力してください")
# ファイルの内容を読み込む
try:
    with open(file_path, "r", encoding="utf-8") as file:
        today_event = file.read().strip()
except FileNotFoundError:
    print("指定されたファイルが見つかりません")
    sys.exit(1)

result = subprocess.run(["python", "main.py", today_event], capture_output=True, text=True, shell=True)

diary_entry = result.stdout.strip()

print(diary_entry)

with open("diary.txt", "a", encoding="utf-8") as f:
    f.write(diary_entry + "\n")

print("完了")