"""
核心目标：
- 不用函数和类
- 逻辑简单直观
- 让孩子快速有成就感
"""

import random
from colorama import Fore, init

# 初始化 colorama，使每次打印后自动重置颜色
init(autoreset=True)

number = random.randint(1, 100)  # 1~100 的随机数
tries = 0

print(Fore.CYAN + "🎈 小朋友，数字猜猜乐小游戏开始啦！(1~100)")

while True:
    guess = input(Fore.YELLOW + "请猜一个数字哦：")
    tries += 1

    if not guess.isdigit():
        print(Fore.RED + "⚠️ 请输入一个数字哦，小朋友！")
        continue

    guess = int(guess)

    if guess < 1 or guess > 100:
        print(Fore.RED + "小朋友，要在 1~100 之间哦！")
        continue

    if guess == number:
        print(Fore.GREEN + f"🎉 太棒啦！你猜对了！一共用了 {tries} 次哦！")
        break
    elif guess < number:
        print("这个数字有点小哦，再试一次吧！")
    else:
        print("这个数字有点大哦，再试一次吧！")