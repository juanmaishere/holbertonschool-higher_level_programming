#!/usr/bin/python3
import hidden_4

vari = dir(hidden_4)

for v in vari:
    if (vari[0:2] != "__"):
        print(vari)
