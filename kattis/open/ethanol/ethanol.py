out = ["  ",
       "  ",
       "H-",
       "  ",
       "  "]

mid = ["H ",
       "| ",
       "C-",
       "| ",
       "H "]

end = ["",
       "",
       "OH",
       "",
       ""]

mult = int(input())
for i in range(5):
    print(out[i] + mid[i]*mult + end[i])
