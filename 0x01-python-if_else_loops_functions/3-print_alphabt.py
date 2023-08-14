#!/usr/bin/python3
for alph in range(ord('a'), ord('z')):
    if (alph == ord('e') or (alph == ord('q'))):
        continue
    print(chr(alph).format(), end="")
