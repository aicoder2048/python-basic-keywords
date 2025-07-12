"""
核心目标：
- 用 class 组织代码
- 用 def 定义方法
- 让孩子理解封装和模块化的好处
"""
import random
from colorama import Fore, init

init(autoreset=True)

class GuessGame:
    def __init__(self):
        self.number = random.randint(1, 100)
        self.tries = 0

    def check_guess(self, guess):
        if guess == self.number:
            return True
        else:
            return False

    def play(self):
        print(Fore.CYAN + "🎈 数字猜猜乐（进阶版）开始啦！(1~100)")

        while True:
            guess_input = input(Fore.YELLOW + "请猜一个数字：")
            self.tries += 1

            if not guess_input.isdigit():
                print(Fore.RED + "⚠️ 请输入数字！")
                continue

            guess = int(guess_input)

            if guess < 1 or guess > 100:
                print(Fore.RED + "要在 1~100 之间哦！")
                continue

            if self.check_guess(guess):
                print(Fore.GREEN + f"🎉 太棒了！你用了 {self.tries} 次猜对！")
                break
            elif guess < self.number:
                print("太小了！再试试～")
            else:
                print("太大了！再试试～")

def main():
    game = GuessGame()
    game.play()

if __name__ == "__main__":
    main()
