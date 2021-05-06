def pos_arg(a, b) :
    print(a, "is the first arg")
    print(b, "is the second arg")
pos_arg("one", "second")
pos_arg([1,2, "1"], {2,44})

def concat(a, b) :
    print(a + b)

concat("İstanbul ", "Ankara")


def default(a = "ali", b = 33) :
    print(a, "is", b, "years old.")

default("sefa", 9)