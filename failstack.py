# generates enhancement success percentages for Black Desert Online
# does math for failstacker.py

def stackMath(stack, base, softcap):
    if(softcap>0 and stack>softcap):
        return (float)(stack-softcap) * (base/50) + (base/10) * softcap + base
    else:
        return (float)(stack) * (base/10) + base

def getStack(stack, enhance):
    stackInfo = [(.02,-1),(.1176,50),(.0769,82),(.062,102),(.02,-1),(.003,-1)]
    return stackMath(stack,stackInfo[enhance][0],stackInfo[enhance][1])
