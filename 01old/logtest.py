import numpy as np
import pylab as plt
np.random.seed(100)
data  = np.random.normal(1,1,1000)
log_data = np.random.lognormal(3,1,1000)
log_data_1000 = log_data/1000
log_log_data =np.log(log_data)
log_log_data_1000 = np.log(log_data_1000)
#average
ave_log_log_data = np.average(log_log_data)
ave_log_log_data_1000 = np.average(log_log_data_1000)

#std
std_log_log_data = np.std(log_log_data)
std_log_log_data_1000 = np.std(log_log_data_1000)

print(ave_log_log_data,std_log_log_data)
print(ave_log_log_data_1000,std_log_log_data_1000)

#plt.hist(log_data,bins=100)
#plt.hist(data,bins=100)
#plt.show()
