def pig_it(text):
    x = (' '.join([x[::-1] + 'ay' for x in text.split()]))
    

pig_it("Hello World!")