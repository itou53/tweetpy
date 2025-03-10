import subprocess

today_event = input("今日の出来事を入力してください")

result = subprocess.run(["python", "main.py", today_event], capture_output=True, text=True, shell=True)

diary_entry = result.stdout.strip()

print(diary_entry)

with open("diary.txt", "a", encoding="utf-8") as f:
    f.write(diary_entry + "\n")

print("完了")