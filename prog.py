# number buttons
btn7=7;
btn8=8;
btn9=9;
btn4=4;
btn5=5;
btn6=6;
btn1=1;
btn2=2;
btn3=3;
btn0=0;

# button to make a number a float
btnPeriod=".";

#button to delete the entire input
btnDel="#";

#button to delete one unit of the input
btnClr="#";

#operational buttons
btnMply="*";
btnDivi="/";
btnAdd="+";
btnMinus="-";

#button to display the result
btnEqual="#";

#button to refer to the last result stored
btnAns="#";

print("Welcome to Roosiez Calculator! ");
print("Let's begin.");

# get problem
num1 = int(input("Enter num1: "));
operator= input("Enter operator (e.g. /): ");
num2 = int(input("Enter num2: "));

if (operator == "*"):
    res = num1 * num2;
    print(f"That's {res}");
elif (operator == "/"):
    res = num1/num2;
    print(f"That's {res}");
elif (operator == "+"):
    res = num1+num2;
    print(f"That's {res}");
elif (operator == "-"):
    res = num1-num2;
    print(f"That's {res}");
else:
    print("TRY AGAIN");
    