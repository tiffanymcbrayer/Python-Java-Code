# Tiffany McBrayer 
# Eulers method

import math
    
def method(function, step, initalT, initalTofY , findTofY):
    # function stuff
    Ypower, Tpower = 1, 1
    negY, negT = 1, 1
    multY, multT = 1, 1
    fY, fT = function.split(",")
    fY = fY.split("|")
    fT = fT.split("|")
    if fY[-1] != Ypower:
        Ypower = fY[-1]
    if fT[-1] != Tpower:
        Tpower = fT[-1] 
    if fY[0] == "-":
        negY = -1
    if fT[0] == "-":
        negT = -1
    if fY[1] != multY:
        multY = fY[1]
    if fT[1] != multT:
        multT = fT[1]
    stepSize = (findTofY - initalT)/step
    tMult = 0
    Y = initalTofY
    y0 = initalTofY
    Ypower, Tpower = eval(Ypower), eval(Tpower)
    multY, multT = eval(multY), eval(multT)
    # multiples of y0
    for n in range(step):
        to = initalT + stepSize* tMult
        #y0 = y0 + (stepSize*((negY*(pow(y0,2))) + (negT*(pow(to,2)))))
        y0 = y0 + (stepSize*((negY*(pow((multY*y0),Ypower)))) + (negT*(pow((multT*to),Tpower))))
        print(y0)
        tMult = tMult + 1
    
y = "+|1|y|2,-|1|t|2", 3, 1, 2, 4
 
                
