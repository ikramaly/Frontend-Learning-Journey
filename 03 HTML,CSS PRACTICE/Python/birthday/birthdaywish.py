# import time
# import os
# from colorama import Fore, Style, init
# import itertools

# # Initialize colorama
# init(autoreset=True)

# # List of birthday messages
# messages = [
#     f"{Fore.MAGENTA}🎂 Happy Birthday to the most amazing girl, Humaira! 🎉",
#     f"{Fore.CYAN}💖 You light up every room just by being in it!",
#     f"{Fore.YELLOW}🌟 May all your dreams come true, my star!",
#     f"{Fore.GREEN}🎁 Today is all about you, Humaira. Enjoy every second!",
#     f"{Fore.BLUE}💫 You’re not just special — you’re my everything 💕",
#     f"{Fore.RED}🌸 Smile more, laugh loud, and stay blessed always!",
#     f"{Fore.MAGENTA}🫶 Tere bina zindagi adhoori lagti hai Humaira ❤️",
#     f"{Fore.CYAN}🌹 You're not just my bestie — you're my heartbeat 💓",
#     f"{Fore.YELLOW}🎈 Happy wala Birthday meri Jaan Humaira 🎊",
#     f"{Fore.GREEN}🦋 Allah tumhe hamesha khush rakhe 💫 Ameen 🌙"
# ]

# # Infinite loop to display messages with animation
# for msg in itertools.cycle(messages):
#     os.system('cls' if os.name == 'nt' else 'clear')  # clear screen
#     print("\n" * 5)  # padding for center feel
#     print(msg.center(100))
#     time.sleep(2)  # wait before showing next message
# import os
# import time
# import itertools
# from colorama import init, Fore, Back, Style

# # Initialize colorama
# init(autoreset=True)

# # Heart pattern
# heart = """
#         {r}  ***     ***  
#       *******  *******
#      *******************
#      *******************
#       *****************
#         *************
#           *********
#             *****
#               *
# """

# # Messages with emojis
# messages = [
#     f"{Fore.MAGENTA}💖 Happy Birthday to the Queen of my Heart — Humaira! 💖",
#     f"{Fore.CYAN}🌹 Tera muskuraana meri pehchaan hai...",
#     f"{Fore.YELLOW}✨ Har dua mein tujhe maanga hai Humaira 🌙",
#     f"{Fore.GREEN}🎂 Aaj tera din hai, aur tu meri duniya hai 💫",
#     f"{Fore.BLUE}🫶 Teri har khushi meri duaon se judi hai 💌",
#     f"{Fore.RED}🎁 Tu zindagi ka woh hissa hai jisko main kabhi khona nahi chahta ❤️",
#     f"{Fore.MAGENTA}🌟 Allah tujhe lambi umar aur dher saari khushiyan de Ameen 🌸",
#     f"{Fore.CYAN}💓 Har saal yeh din aaye, aur tu yunhi muskuraati rahe 😊",
#     f"{Fore.YELLOW}🎈 Tu sirf meri bestie nahi, meri jaan bhi hai 💕",
#     f"{Fore.GREEN}🥳 Happy Birthday once again Humaira — from your Ibrahim 💝"
# ]

# # Emoji fireworks
# fireworks = [
#     "✨🎉✨      🎂      ✨🎉✨",
#     "🎆💖🎆   Happy Birthday   🎆💖🎆",
#     "🌟🌟🌟      Humaira      🌟🌟🌟",
#     "💫🫶💫     You’re Loved     💫🫶💫"
# ]

# # Infinite loop of glow and messages
# for msg, fire in itertools.cycle(zip(messages, fireworks)):
#     os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
#     print("\n" * 2)
    
#     # Show glowing heart
#     print(heart.format(r=Fore.RED))

#     # Print birthday message
#     print("\n" + msg.center(100))
    
#     # Fireworks
#     print("\n\n" + fire.center(100))
    
#     time.sleep(2)
import os
import time
import random
import itertools
from colorama import init, Fore, Back, Style
from shutil import get_terminal_size

# Initialize colorama
init(autoreset=True)

def get_terminal_dimensions():
    try:
        columns, lines = get_terminal_size()
        return columns, lines
    except:
        return 80, 24  # Default fallback size

# Romantic messages and poetry
romantic_lines = [
    "Humaira, you are the most beautiful person in my life ✨",
    "Your smile lights up my world like nothing else 💖",
    "In your eyes, I found my paradise 🌹",
    "Every moment with you feels like a dream come true 🌙",
    "Your love is the greatest gift I've ever received 🎁",
    "I fall in love with you more each day 🌟",
    "You're the missing piece to my puzzle 🧩",
    "My heart beats only for you 💓",
    "Forever isn't long enough with you ⏳",
    "You're my today and all of my tomorrows 📅"
]

birthday_wishes = [
    "🎂🎉 Happy Birthday to the most amazing woman! 🎉🎂",
    "✨🎁 May your day be as wonderful as you are! 🎁✨",
    "💝🌸 Wishing you endless joy and happiness! 🌸💝",
    "🎈🍰 Another year of incredible you! 🍰🎈",
    "🌠🎇 May all your dreams come true! 🎇🌠"
]

# ASCII Art
def get_heart(name):
    heart = [
        "  ******       ******  ",
        " ********** ********** ",
        "***********************",
        "***********************",
        " ********************* ",
        "  *******************  ",
        "   *****************   ",
        "    ***************    ",
        "     *************     ",
        "      ***********      ",
        "       *********       ",
        "        *******        ",
        "         *****         ",
        "          ***          ",
        "           *           "
    ]
    
    if len(name) > 0:
        mid = len(heart) // 2
        space = (len(heart[mid]) - len(name)) // 2
        if space > 0:
            heart[mid] = heart[mid][:space] + name + heart[mid][space+len(name):]
    
    return heart

couple_art = [
    "     O     O     ",
    "    /|\\   /|\\    ",
    "    / \\   / \\    ",
    "   ♥   ♥ ♥   ♥   ",
    "  *    * *    *  ",
    " *     * *     * ",
    "*****************"
]

# Color cycling
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
bg_colors = [Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE]

def get_random_color():
    return random.choice(colors)

def get_random_bg():
    return random.choice(bg_colors)

def center_text(text, width=None):
    cols, _ = get_terminal_dimensions()
    if width is None:
        width = cols
    return text.center(width)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_centered(text, color=Fore.WHITE, bg=Back.BLACK):
    print(color + bg + center_text(text) + Style.RESET_ALL)

def animate_emoji_line():
    emojis = ["✨", "🎂", "💖", "🎉", "🎁", "🌸", "🍰", "🎈", "🌹", "🌟"]
    base_text = " Happy Birthday Humaira "
    while True:
        for i in range(len(emojis)*2):
            left_emoji = emojis[i % len(emojis)]
            right_emoji = emojis[(i+3) % len(emojis)]
            yield f"{left_emoji}{base_text}{right_emoji}"

def display_fireworks():
    symbols = ["*", "+", ".", "o", "O", "°", "·"]
    positions = [(random.randint(0, cols-1), random.randint(0, rows//2)) for _ in range(20)] # type: ignore
    for _ in range(10):
        for x, y in positions:
            print(f"\033[{y};{x}H{random.choice(symbols)}", end="", flush=True)
        time.sleep(0.05)

def main():
    emoji_line_gen = animate_emoji_line()
    color_cycle = itertools.cycle(colors)
    bg_cycle = itertools.cycle(bg_colors)
    
    try:
        while True:
            cols, rows = get_terminal_dimensions()
            clear_screen()
            
            current_color = next(color_cycle)
            current_bg = next(bg_cycle)
            
            print("\n" * (rows // 8), end="")
            
            try:
                emoji_line = next(emoji_line_gen)
                print_centered(emoji_line, current_color, current_bg)
            except StopIteration:
                emoji_line_gen = animate_emoji_line()
                emoji_line = next(emoji_line_gen)
                print_centered(emoji_line, current_color, current_bg)
            
            print("\n" * 2, end="")
            
            heart = get_heart("Humaira")
            for line in heart:
                print_centered(line, get_random_color())
            
            print("\n" * 2, end="")
            
            print_centered(random.choice(romantic_lines), get_random_color())
            print_centered(random.choice(birthday_wishes), get_random_color())
            
            print("\n" * 2, end="")
            
            for line in couple_art:
                print_centered(line, get_random_color())
            
            print("\n" * (rows // 8), end="")
            
            if cols > 60 and rows > 30:  # Only show fireworks if terminal is large enough
                display_fireworks()
            
            time.sleep(1.5)
            
    except KeyboardInterrupt:
        clear_screen()
        cols, _ = get_terminal_dimensions()
        print("\n" * (rows // 3))
        print_centered("Happy Birthday Humaira! I Love You! 💖", Fore.RED)
        print_centered("Press Ctrl+C again to exit.", Fore.YELLOW)
        print("\n" * (rows // 3))
        time.sleep(3)

if __name__ == "__main__":
    main()