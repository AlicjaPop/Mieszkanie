import numpy as np
import numpy_financial as npf

prop_price_init=120000
prop_rate=0.05
dep_rate=0.12/12
time=5
dep_nper=12*time
prop_nper=1*time

dep_periods=np.arange(1,dep_nper+1,dtype=int)
prop_periods=np.arange(1,prop_nper+1,dtype=int)

prop_price_future=np.around(-npf.fv(prop_rate, prop_nper, 0, 120000),2)

#Przyszła wartość mieszkania to 153 153.79 zł

pmt=np.around(npf.pmt(dep_rate,dep_nper,0,-prop_price_future),2)

#Co miesiąc należy wpłacać ok. 1875,28 zł, aby uzbierać na mieszkanie w ciągu 5 lat