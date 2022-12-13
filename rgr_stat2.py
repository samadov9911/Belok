import numpy as np


def core():
    global omega
    global altitude
    global radius_earth
    global density
    global mu
    global velocity
    global deltaQ


    '''
    0 - radius
    1 - time
    2 - radial speed
    3 - angular speed
    4 - mass
    '''

    mu = 398.6e12
    radius_earth=6371*10**3
    altitude=400*10**3
    omega = np.sqrt(mu/(radius_earth+altitude)**3)
    velocity=np.sqrt(mu/(radius_earth+altitude))
    density=5.934
    deltaQ=0.02*10**(-6)

    vars = np.zeros(20)
    vars[0] = 100*10**(-6)
    vars[1] = 0.5
    vars[2]= 0.2
    vars[5] = 0.01*10**(-6)
    vars[9] = 100*10**(-6)
    vars[10] = 0.5
    vars[12] =0.01*10**(-6)
    vars[14] =3.518*10**(-19)
    vars[15] =5000
    vars[18] =0.5*omega*5000
    vars[19] =3.518*10**(-18)


    t= 0
    h = 50

    k = np.zeros((20, 4))

    while t <= 5400:

        k[:, 0] = diffs(vars)
        k[:, 1] = diffs(vars + k[:, 0] / 2)*2
        k[:, 2] = diffs(vars + k[:, 1] / 2)*2
        k[:, 3] = diffs(vars + k[:, 2])

        k *= h/6
        dvars = [sum(elem) for elem in k]
        vars += dvars

        t += h




def diffs(args):

    out = np.zeros(20)

    out[0] = 2*args[1]
    out[1] = -2*omega*args[3]+args[4]+args[5]
    out[2] = args[3]+args[6]
    out[3] = 2*omega*args[1]+3*omega*omega*args[2]+args[7]
    out[4] = args[8]
    out[5] = -2*(2*omega*args[7]-args[8])
    out[6] = -2*omega*args[10]+args[11]+args[7]
    out[7] = 2*omega*args[5]+3 * omega * omega *args[6]-2*omega*args[12]+args[13]
    out[8] = -2*omega*args[13]+args[14]
    out[9] = 2*args[10]
    out[10] = 2*omega*args[6]+3*omega*omega*args[9]+args[12]
    out[11] = args[13]
    out[12] = 2*(2*omega*args[7]+3*omega*omega*args[10])
    out[13] = 2*omega*args[8]+3*omega*omega*args[11]
    out[14] = 0
    out[15] = args[16]
    out[16] = -2*omega*args[18]+args[19]
    out[17] = args[18]
    out[18] = 2-omega*args[16]+3*omega*omega*args[17]
    out[19] = 0


    return out





core()





