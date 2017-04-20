# when is exec is like eval
exec("print('here exec is like eval')")

# here exec is not like eval

list_str = "[5,6,7,7,78,8,9,10]"
list_str = exec(list_str)

print('prints none here ', list_str)

list_str = "[5,6,7,7,78,8,9,10]"

exec("eval(list_str)")
print(list_str)

# or

exec("list_str = [5,6,7,7,78,8,9,11]")

print(list_str)

# functions inside exec

exec("def test(): print('Oh yeah it worked')")
test()

exec("""
def test2():
    print('multiline works')
""")

test2()