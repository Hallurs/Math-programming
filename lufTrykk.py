import matplotlib.pyplot as plt
import numpy as np

m = 4.65e-26    #kg     (fordeling av atomer i atmosfÃ¦ren antas konstant)
T = 278         #K      (brukt gjennomsnittlig temperatur i Trondhjem)
k = 1.38e-23    #J/K
g = 9.81        #m/s^2  (antas konstant selv lengre ut i atmosfÃ¦ren)
p0 = 1013.25    #hPa    (lufttrykk ved havnivÃ¥)

def p(h):
    return p0 * np.exp(-(m*g*h)/(T*k))

h = np.linspace(0, 10000, 10000)



fig, ax = plt.subplots(dpi=200)

ax.plot(h,p(h))
ax.grid()
ax.set(xlabel="h [m]", ylabel="p [hPa]",title="Lufttrykk som funksjon av hÃ¸yde over havet")
ax.set_ylim(0,1100)
plt.savefig("lufttrykk")




print(p(6000), "hPa ved 6k moh")
print(p(16000), "hPa ved 16k moh")
print(p(50000), "hPa ved 50k moh")
# sammenlign med https://snl.no/lufttrykk