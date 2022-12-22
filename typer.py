from pynput import keyboard as pynput_keyboard
import time


# Type the given string
def type_string(string):
    time.sleep(3)
    keyboard = pynput_keyboard.Controller()
    commands = string.split("\n")
    for command in commands:
        if command == "sleep":
            time.sleep(1)
            continue
        type_command(command, keyboard)
        time.sleep(1)
    # Press ctrl-d to exit the shell
    keyboard.press(pynput_keyboard.Key.ctrl)
    keyboard.press('d')
    keyboard.release(pynput_keyboard.Key.ctrl)
    keyboard.release('d')


# Type the given string and press enter
def type_command(command, keyboard):
    for character in command:
        if character == "_" or character == ":":
            # Shift
            keyboard.press(pynput_keyboard.Key.shift)
            keyboard.press(character)
            keyboard.release(pynput_keyboard.Key.shift)
            keyboard.release(character)
            continue
        keyboard.press(character)
        keyboard.release(character)
        time.sleep(0.1)
    keyboard.press(pynput_keyboard.Key.enter)
    keyboard.release(pynput_keyboard.Key.enter)


if __name__ == "__main__":
    # type_string("""counter = count()
# [next(counter) for i in range(10)]
# sleep
# counter = count(10, 3)
# [next(counter) for i in range(10)]""")
    # type_string("""cycler = cycle([1, 2, 3])
# [next(cycler) for i in range(10)]
# sleep
# cycler = cycle("Hello")
# [next(cycler) for i in range(10)]""")
    # type_string("""repeater = repeat(10)
# [next(repeater) for i in range(10)]
# sleep
# list(repeat("Hello World", 4))""")
    # type_string("""list(product([1, 2], [4, 5, 6]))
# sleep
# list(product([2, 3], [4], ["a", "b"]))
# sleep
# list(product([1, 2], [4, 3], repeat_obj=2))[:4]""")
    # type_string("""list(permutations([1, 2, 3]))
# sleep
# list(permutations([1, "2", [3]], 2))
# sleep""")
    # type_string("""list(combinations([1, 2, 3, 4], 2))
# sleep
# list(combinations([1, "a", 3, [2]], 3))""")
    # type_string("""list(combinations_with_replacement([1, 2, 3, 4], 2))
# sleep
# list(combinations_with_replacement([1, "a", [2]], 2))""")
