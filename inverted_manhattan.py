import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
mpl.rcParams['axes.color_cycle'] = ['r', 'k', 'b']

data_fem = np.genfromtxt('female_data', dtype=None, names=True)
data_mal = np.genfromtxt('male_data', dtype=None, names=True)

shift=np.array([0])
plt.clf()
for i in range(1,23):
    plt.subplot(2,1,1)
    print i 
    filt=data_fem['CHR']==i
    x = shift[-1]+data_fem['BP'][filt]
    y = -np.log10(data_fem['P'][filt])
    plt.plot(x[y>0],y[y>0],'.')
    plt.ylim([0, 9])
    shift_f=np.max(x)
    
    plt.subplot(2,1,2)
    filt=data_mal['CHR']==i
    x = shift[-1]+data_mal['BP'][filt]
    y = -np.log10(data_mal['P'][filt])
    plt.plot(x[y>0],y[y>0],'.')
    plt.ylim([0, 9])
    shift_m=np.max(x)
    shift =np.append(shift, np.max([shift_f, shift_m]))
    
    plt.subplot(2,1,1)
    plt.plot([shift[-1],shift[-1]],[0,10],'-k',lw=0.5,color='lightgray')
    plt.subplot(2,1,2)
    plt.plot([shift[-1],shift[-1]],[0,10],'-k',lw=0.5,color='lightgray')


shift = (shift[1:]+shift[:-1])/2.
plt.subplot(2,1,1)
plt.setp(plt.gca().get_xticklabels(), visible=False)
plt.subplots_adjust(hspace=0.001)
plt.xticks(shift)
plt.text(shift[12],8,"Females",bbox=dict(boxstyle="round", fc="1.0"))

plt.subplot(2,1,2)
plt.gca().invert_yaxis()
labels = np.arange(1,23).astype(str)
labels[-2] = ''
labels[-4] = ''
labels[-6] = ''
labels[-8] = ''
labels[-10] = ''
plt.xticks(shift, labels)
plt.text(shift[12],8,"Males",bbox=dict(boxstyle="round", fc="1.0"))
plt.ylabel('-log10(p-value)')

plt.savefig('script_test.png',dpi=300)
