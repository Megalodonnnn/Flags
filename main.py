class bcolors: # Color Text Code
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    WHITE = '\033[97m'
    RED = '\033[91m'
print("1 = Sweden | 2 = Israel | 3 = France | 4 = Spain") # Detecting Which Choice
Flag = input("Input Number:")
intFlag = int(Flag)
if intFlag == 1: # Swedish Flag Code
    print(bcolors.BLUE + "000000" + bcolors.YELLOW + "111" + bcolors.BLUE + "000000000000")
    print(bcolors.BLUE + "000000" + bcolors.YELLOW + "111" + bcolors.BLUE + "000000000000")
    print(bcolors.YELLOW + "111111111111111111111")
    print(bcolors.YELLOW + "111111111111111111111")
    print(bcolors.BLUE + "000000" + bcolors.YELLOW + "111" + bcolors.BLUE + "000000000000")
    print(bcolors.BLUE + "000000" + bcolors.YELLOW + "111" + bcolors.BLUE + "000000000000")
if intFlag == 2:
    print(bcolors.WHITE + "000000000000000000000")
    print(bcolors.BLUE + "111111111111111111111")
    print(bcolors.WHITE + "000000000000000000000")
    print(bcolors.WHITE + "0000000000" + bcolors.BLUE + "1" + bcolors.WHITE + "0000000000")
    print(bcolors.WHITE + "000000000000000000000")
    print(bcolors.BLUE + "111111111111111111111")
    print(bcolors.WHITE + "000000000000000000000")
if intFlag == 3:
    print(bcolors.BLUE + "1111111" + bcolors.WHITE + "0000000" + bcolors.RED + "2222222")
    print(bcolors.BLUE + "1111111" + bcolors.WHITE + "0000000" + bcolors.RED + "2222222")
    print(bcolors.BLUE + "1111111" + bcolors.WHITE + "0000000" + bcolors.RED + "2222222")
    print(bcolors.BLUE + "1111111" + bcolors.WHITE + "0000000" + bcolors.RED + "2222222")
    print(bcolors.BLUE + "1111111" + bcolors.WHITE + "0000000" + bcolors.RED + "2222222")
    print(bcolors.BLUE + "1111111" + bcolors.WHITE + "0000000" + bcolors.RED + "2222222")
if intFlag == 4:
    print(bcolors.RED + "111111111111111111111")
    print(bcolors.YELLOW + "000000000000000000000")
    print(bcolors.YELLOW + "0000" + bcolors.RED + "11" + bcolors.YELLOW + "000000000000000")
    print(bcolors.YELLOW + "0000" + bcolors.RED + "11" + bcolors.YELLOW + "000000000000000")
    print(bcolors.YELLOW + "000000000000000000000") # 4 Yello Zeros
    print(bcolors.RED + "111111111111111111111")

