import random
import time
import sys
from colorama import init, Fore, Back, Style
import pygame

init(autoreset=True)
pygame.mixer.init()

try:
    shot_sound = pygame.mixer.Sound("shot.wav")
    click_sound = pygame.mixer.Sound("click.wav")
except:
    print(Fore.YELLOW + "Звуковые эффекты не найдены, игра продолжится без них")


class Revolver:
    def __init__(self, chambers=6):
        self.chambers = chambers
        self.bullet_position = random.randint(1, chambers)
        self.current_position = 1

    def spin(self):
        self.bullet_position = random.randint(1, self.chambers)
        self.current_position = 1
        print(Fore.CYAN + "\nБарабан крутится...")
        time.sleep(2)
        print(Fore.GREEN + "Барабан остановился. Готов к выстрелу.")
        return self

    def trigger_pull(self):
        print(Fore.WHITE + Back.RED + "\nПалец на спусковом крючке...")
        time.sleep(1.5)

        if self.current_position == self.bullet_position:
            print(Fore.RED + Back.WHITE + "БАХ!!!")
            try:
                pygame.mixer.Sound.play(shot_sound)
            except:
                pass
            time.sleep(1)
            print(Fore.RED + "Ты проиграл. Игра окончена.")
            self._show_bloody_animation()
            return False
        else:
            print(Fore.GREEN + "*Щелк*")
            try:
                pygame.mixer.Sound.play(click_sound)
            except:
                pass
            time.sleep(1)
            print(Fore.YELLOW + "Повезло... на этот раз.")
            self.current_position += 1
            if self.current_position > self.chambers:
                self.current_position = 1
            return True

    def _show_bloody_animation(self):
        blood = [Fore.RED + "✖", Fore.RED + "✗", Fore.RED + "✘", Fore.RED + "💀"]
        for _ in range(15):
            print(random.choice(blood), end=" ")
            sys.stdout.flush()
            time.sleep(0.1)
        print("\n")


def get_player_choice():
    print("\n" + Fore.MAGENTA + "Выбери действие:")
    print(Fore.BLUE + "1. Крутить барабан")
    print(Fore.BLUE + "2. Нажать курок")
    print(Fore.RED + "3. Выйти")

    while True:
        choice = input(Fore.WHITE + "> ")
        if choice in ("1", "2", "3"):
            return int(choice)
        print(Fore.RED + "Неверный выбор. Попробуй еще раз.")


def show_intro():
    print(Fore.RED + """
    ██████╗ ██╗   ██╗███████╗███████╗██╗ █████╗ ██╗   ██╗    ██████╗ ██╗   ██╗██╗     ███████╗████████╗
    ██╔══██╗██║   ██║██╔════╝██╔════╝██║██╔══██╗██║   ██║    ██╔══██╗██║   ██║██║     ██╔════╝╚══██╔══╝
    ██████╔╝██║   ██║███████╗███████╗██║███████║██║   ██║    ██████╔╝██║   ██║██║     █████╗     ██║   
    ██╔══██╗██║   ██║╚════██║╚════██║██║██╔══██║╚██╗ ██╔╝    ██╔══██╗██║   ██║██║     ██╔══╝     ██║   
    ██║  ██║╚██████╔╝███████║███████║██║██║  ██║ ╚████╔╝     ██║  ██║╚██████╔╝███████╗███████╗   ██║   
    ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝╚═╝╚═╝  ╚═╝  ╚═══╝      ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝   ╚═╝   
    """)
    time.sleep(2)
    print(Fore.WHITE + "Добро пожаловать в русскую рулетку!")
    print(Fore.YELLOW + "Ты готов испытать судьбу?")
    time.sleep(1)


def main():
    show_intro()
    revolver = Revolver()
    alive = True

    while alive:
        choice = get_player_choice()

        if choice == 1:
            revolver.spin()
        elif choice == 2:
            alive = revolver.trigger_pull()
        elif choice == 3:
            print(Fore.GREEN + "Ты выбрал жизнь. До свидания!")
            break

    print(Fore.RED + "\nИгра завершена. Спасибо за игру!")


if __name__ == "__main__":
    main()
