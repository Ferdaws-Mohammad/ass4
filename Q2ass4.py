n1=input('enter the first number')
if n1.isdecimal():

    print('\n 1_+','\n 2_-''\n 3_*','\n 4_/','\n 5_^','\n 6_%')
    proces=input('enter the proces')
    n2= input('enter the second number')
    if n2.isdecimal():
        n1 = float(n1)
        n2=float(n2)
        if '+' ==proces or '1' in proces:
           result=n1+n2
           print('result=',result)
           print('1- normal rounding of a number = ',result.__round__(),'\n 2- the result without a decimal point=',result.__floor__(),'\n 3-exit')
        elif  '-' ==proces or '2' in proces:
           result=n1-n2
           print('result=', result)
           print('1- normal rounding of a number = ',result.__round__(),'\n 2- the result without a decimal point=',result.__floor__(),'\n 3-exit')
        elif '*' == proces or '3' in proces:
           result=n1*n2
           print('result=', result)
           print('1- normal rounding of a number = ',result.__round__(),'\n 2- the result without a decimal point=',result.__floor__(),'\n 3-exit')
        elif '/' == proces or '4' in proces:
           result=n1 / n2
           print('result=', result)
           print('1- normal rounding of a number = ',result.__round__(),'\n 2- the result without a decimal point=',result.__floor__(),'\n 3-exit')
        elif '^' == proces or '5' in proces:
           result=n1 ** n2
           print('result=', result)
           print('1- normal rounding of a number = ',result.__round__(),'\n 2- the result without a decimal point=',result.__floor__(),'\n 3-exit')
        elif '%' == proces or '6' in proces:
           result=n1 %n2
           print('result=', result)
           print('1- normal rounding of a number = ',result.__round__(),'\n 2- the result without a decimal point=',result.__floor__(),'\n 3-exit')
    else:print('invalid value, try again')
else:print('invalid value, try again')



