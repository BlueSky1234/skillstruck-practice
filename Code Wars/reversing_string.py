def pig_it(text):
    x = (' '.join([x[::-1] + 'ay' for x in text.split()]))
    print(x)
    

pig_it("Hello World!")