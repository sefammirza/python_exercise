def brothers(bro1, bro2, bro3):
    print('Here are the names of brothers :')
    print(bro1, bro2, bro3, sep='\n')
family = ['tom', 'sue', 'tim']
brothers(*family)

def merger(par1, par2, par3, par4) :
    print(f"For me, {par1} {par4} and {par3} {par2} are geniuses.")
genius = ("Bill", "Rossum", "Guido van", "Gates")
merger(*genius)

def önceki(**parametre) :
    for x, y in parametre.items() :
        print(x, y)
önceki(a = "ahmet", b = "mehmet", c = "selamet")

def gene(x='Solomon', y='David'):  # defined by kwargs (default values assigned to x and y)
    print(x, "belongs to Generation X")
    print(y, "belongs to Generation Y")
dict_gene = {"y" : "Marry", 'x' : "Fred"}
gene(**dict_gene)   
gene()