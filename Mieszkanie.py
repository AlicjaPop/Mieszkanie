import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as plt

prop_price_init=120000
prop_rate=0.05/12
dep_rate=0.12/12
time=5
nper=12*time


periods=np.arange(1,nper+1,dtype=int)
prop_price_future=np.around(-npf.fv(prop_rate, nper, 0, prop_price_init),2)

dep_pmt=np.around(npf.pmt(dep_rate,nper,0,-prop_price_future),2)

dep_value_in_time=np.around(npf.fv(dep_rate, periods, -dep_pmt, 0),2)
prop_value_in_time=np.around(prop_price_init*(1+prop_rate)**(periods),2)

plt.plot(dep_value_in_time,label='wartość lokaty')
plt.plot(prop_value_in_time,label='wartość mieszkania')
plt.legend()
plt.xlabel('Liczba okresów')
plt.ylabel('Wartość')