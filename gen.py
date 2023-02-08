import base64

print("IBSGH v1.1")
print("coded by: off#0165\nREAD THE CREDITS.MD FILE\n")

print("What level do you want to be on? (Dont make it more than 999999)")
level = input()

print("What amount of money would you like to have")
money = input()

print("How much gold do you want")
gold = input()

print("How many Black Boxes?")
bb = input()

print("How many skillpoints")
sp = input()

print("How many Basic Balls?")
bbs = input()

print("How many Plasma Balls?")
pb = input()

print("How many Sniper Balls?")
sb = input()

print("How many Scatter Balls?")
scb = input()

print("How many Cannon Balls?")
cb = input()

print("How many Poison Balls?")
pob = input()

print("What boss brick level?")
bbl = input()

s = f"{level},{money},{gold},2,0,0,0,0,0,0,0,1,1,0,43595.78,999999,0,0,0,0,0,0,0,0,0,0,0,0,{bbs},{pb},{sb},{scb},{cb},{pob},0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,{bb},0,0,0,{bbl},{sp},1,0,0,"



b = s.encode("UTF-8")
e = base64.b64encode(b)
print("Encoding....")
print("Your result is....")
print(e)
print("\nCopy whats INSIDE the quotes\n")
end = 1
while end == 1:
    print("Once copied you may exit the console")
    input()
