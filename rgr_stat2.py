import matplotlib.pyplot as plt
import numpy as np


def core():
    global omega
    global altitude
    global radius_earth
    global density
    global mu
    global velocity
    global deltaQ

    mu = 398602
    altitude= 400
    radius_earth=6371

    omega = np.sqrt(mu/(radius_earth+altitude)**3)
    velocity=np.sqrt(mu/(radius_earth+altitude))
    density=5.934*10**(-12)
    deltaQ=0.02#*10**(-6)

    vars = np.zeros(20)
    vars[0] =100#*10**(-6)
    vars[1] = 0.5
    vars[2]= 0.2
    vars[5] =0.01#*10**(-6)
    vars[9] =100#*10**(-6)
    vars[10] = 0.5
    vars[12] =0.01#*10**(-6)
    vars[13] = density
    vars[14] =3.518*10**(-18)
    vars[15] =5#*10**(-7)
    vars[18] =0.5*omega*vars[15]
    vars[19] =3.518 * pow(10, -19)


    t = 0
    h = 50

    k = np.zeros((20,4))

    results = vars

    time = list()
    time.append(0)
    while t <= 5400:


        k[:, 0] = diffs(vars)
        k[:, 1] = diffs(vars + k[:, 0] / 2)*2
        k[:, 2] = diffs(vars + k[:, 1] / 2)*2
        k[:, 3] = diffs(vars + k[:, 2])

        k *= h/6
        dvars = [sum(elem) for elem in k]
        vars += dvars

        results = np.vstack([results, vars])
        time.append(t)

        t += h



    plt.plot(time, results[:,0]/10e6)
    plt.xlabel('Время (секунда)')
    plt.ylabel('Dx(t), км^2')
    plt.grid()
    plt.show()

    plt.plot(time, results[:, 5]*10**(-6))
    plt.xlabel('Время (секунда)')
    plt.ylabel('D_Vx(t), км^2/с^2')
    plt.grid()
    plt.show()

    plt.plot(time, results[:, 9]*10**(-6))
    plt.xlabel('Время (секунда)')
    plt.ylabel('Dy(t), км^2')
    plt.grid()
    plt.show()

    plt.plot(time, results[:, 12]*10**(-6))
    plt.xlabel('Время (секунда)')
    plt.ylabel('D_Vy(t), км^2/c^2')
    plt.grid()
    plt.show()

    plt.plot(time, results[:, 14])
    plt.xlabel('Время (секунда)')
    plt.ylabel('Dax(t)')
    plt.grid()
    plt.show()

    #Correlation graph

    r_xy = results[:,2]/np.sqrt(results[:,0]*results[:,9])
'''
    r_xVx = results[:,1]/np.sqrt(results[:,0]*results[:,5])

    r_yVy = results[:,10]/np.sqrt(results[:,9]*results[:,12])

    r_xVy = results[:,3]/np.sqrt(results[:,0]*results[:,12])

    r_yVx = results[:,6]/np.sqrt(results[:,9]*results[:,5])

    r_VxVy = results[:,7]/np.sqrt(results[:,5]*results[:,12])

    r_xax = results[:,4]/np.sqrt(results[:,0]*results[:,14])

    r_yax = results[:,11]/np.sqrt(results[:,9]*results[:,14])

    r_Vxax = results[:,8]/np.sqrt(results[:,5]*results[:,14])

    r_Vyax = results[:,13]/np.sqrt(results[:,12]*results[:,14])
'''
    plt.plot(time, results[:, 2])
    plt.xlabel('Время (секунда)')
    plt.ylabel('rxy')
    plt.grid()
    plt.show()

    plt.plot(time, results[:, 1])
    plt.xlabel('Время (секунда)')
    plt.ylabel('r_xVx')
    plt.grid()
    plt.show()

    plt.plot(time, results[:, 10])
    plt.xlabel('Время (секунда)')
    plt.ylabel('r_yVy')
    plt.grid()
    plt.show()

    plt.plot(time, results[:, 3])
    plt.xlabel('Время (секунда)')
    plt.ylabel('r_xVy')
    plt.grid()
    plt.show()

    plt.plot(time, results[:, 6])
    plt.xlabel('Время (секунда)')
    plt.ylabel('D_yVx')
    plt.grid()
    plt.show()

    plt.plot(time, results[:, 7])
    plt.xlabel('Время (секунда)')
    plt.ylabel('r_xVy')
    plt.grid()
    plt.show()

    plt.plot(time, results[:, 4])
    plt.xlabel('Время (секунда)')
    plt.ylabel('r_xax')
    plt.grid()
    plt.show()

    plt.plot(time, results[:, 11])
    plt.xlabel('Время (секунда)')
    plt.ylabel('r_yax')
    plt.grid()
    plt.show()

    plt.plot(time, results[:, 8])
    plt.xlabel('Время (секунда)')
    plt.ylabel('r_Vxax')
    plt.grid()
    plt.show()

    plt.plot(time, results[:, 13])
    plt.xlabel('Время (секунда)')
    plt.ylabel('r_Vyax')
    plt.grid()
    plt.show()







'''
    plt.plot(time, results[:, 2])
    plt.xlabel('Время (секунда)')
    plt.ylabel('rxy')
    plt.grid()
    plt.show()

    plt.plot(time, results[:, 1])
    plt.xlabel('Время (секунда)')
    plt.ylabel('r_xVx')
    plt.grid()
    plt.show()

    plt.plot(time, results[:, 10])
    plt.xlabel('Время (секунда)')
    plt.ylabel('r_yVy')
    plt.grid()
    plt.show()

    plt.plot(time, results[:, 3])
    plt.xlabel('Время (секунда)')
    plt.ylabel('r_xVy')
    plt.grid()
    plt.show()

    plt.plot(time, results[:, 6])
    plt.xlabel('Время (секунда)')
    plt.ylabel('D_yVx')
    plt.grid()
    plt.show()

    plt.plot(time, results[:, 7])
    plt.xlabel('Время (секунда)')
    plt.ylabel('r_xVy')
    plt.grid()
    plt.show()

    plt.plot(time, results[:, 4])
    plt.xlabel('Время (секунда)')
    plt.ylabel('r_xax')
    plt.grid()
    plt.show()

    plt.plot(time, results[:, 11])
    plt.xlabel('Время (секунда)')
    plt.ylabel('r_yax')
    plt.grid()
    plt.show()

    plt.plot(time, results[:, 8])
    plt.xlabel('Время (секунда)')
    plt.ylabel('r_Vxax')
    plt.grid()
    plt.show()

    plt.plot(time, results[:, 13])
    plt.xlabel('Время (секунда)')
    plt.ylabel('r_Vyax')
    plt.grid()
    plt.show()

'''

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





