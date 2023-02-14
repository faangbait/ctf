#!/usr/bin/env python

ciphertext = "μσζ'ι ργσκ ιηγτ. οσμιδ{ς_ενγθθ_νθςζε_τσζω_εργγα_μησρσμιγρθ_κςκζ'ι_θιπψ_ωπν._λγοο_ψοσωγκ_ς_τνθι_θσω.μπζερσιθ!}"

g = {
    959: "l",
    963: "a",
    956: "c",
    953: "t",
    948: "f",
    950: "n",
    # 952: "e",
    962: "i",
    954: "d",
    961: "r",
    947: "e",
    951: "h",
    955: "w",
    968: "p",
    969: "y",
    952: "s",
    949: "g",
    957: "u",
    945: "k",
    960: "o",
    964: "m",
    
}

known = []

for char in ciphertext:

    k = g.get(ord(char), None);

    if ord(char) < 500:
        k = char

    if k is None:
        known.append(".")
        print(f"{char} = {ord(char)}")
    else:
        known.append(k)

print("".join(known))

    # if ord(char) > 500:
    #     print(chr(ord(char)-880))
    # else:
    #     print(char)
