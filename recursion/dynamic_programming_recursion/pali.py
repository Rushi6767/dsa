def pali(text):
    if len(text) <= 1:
        return "Palidrome"
    else:
        if text[0] == text[-1]:
            pali(text[1:-1])
        else:
            return "Not palidram"


text = "mada"
print(pali(text))