# !/usr/bin/env python3
# Created by: Jedidiah
# Created on: April 18 2022


def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


text = "anything"
colored_text = colored(255, 0, 0, text)
print(colored_text)
for r in range(200, 255, 1):
    for g in range(200, 255, 1):
        for b in range(200, 255, 1):
            text = ("RGB {},{},{}.".format(r, g, b))
            colored_text = colored(r, g, b, text)
            print(colored_text)
