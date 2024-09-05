names = input().split()
partners = []

def assign_partners(names):
    ST = 0
    SP = len(names) - 1
    names.sort()

    while ST < SP:
        partners.append((names[ST], names[SP]))
        ST += 1
        SP -= 1

assign_partners(names)
print(partners)

