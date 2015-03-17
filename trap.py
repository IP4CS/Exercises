def Trapezoidal(p, k, x0, xn, step):
    '''Use trapezoidal algorithm to calculate the integral of wave fuction product 
    phi(p, x)*phi(k, x) over x
    
    x0 and xn are integral arange 
    
    number of integral steps: n*2^step
    
    Trapezoidal algoirthm: I = h*[ 0.5[f(a)+f(b)] + sum(f(x), x from a to b) ]
    ''' 
    #integral step size h
    h = (xn-x0)/float(step)
    xpoints = np.linspace(x0, xn, step) #points from x0 to xn (included) at step size h
    
    #number of x points 
    num_points= len(xpoints)

    #trap: sum of the interal with trapezoidal method
    trap = 0.5*( Wavefunc(p, xpoints[0])*Wavefunc(k, xpoints[0]) + \
    Wavefunc(p, xpoints[-1])*Wavefunc(k, xpoints[-1]) )#the first and last point
    #sum ove middle points
    for i in range(1, num_points-1):
        trap += Wavefunc(p,xpoints[i])*Wavefunc(k,xpoints[i])
       
    return trap*h   
