def f(t):
    c = list(t)
    for i in range(len(t)):
        print(f"i : {str(i)}")
        for j in range(len(t) - 1, len(t) - i - 1, -1):
            print(f"\tj : {str(j)}")
            c[j], c[j-1] = c[j-1], c[j]
    return "".join(c)

if __name__ == "__main__":
    ciphertext = open("ciphertext", "r").read()
    print(f(ciphertext))
