#ex3ques1
#emissions
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_df = pd.read_csv('traffic.csv', sep=';', encoding='latin-1')

#ensirekisterointipvm=register date.
vehData=vehData[vehData["ajoneuvoluokka"].isin(["M1","M1G"])]
co2Data=vehData.loc[:,["ensirekisterointipvm","Co2"]].dropna()
co2Data["ensirekisterointipvm"]=co2Data["ensirekisterointipvm"].apply(lambda x:x[:4])

Sum=co2Data.groupby("ensirekisterointipvm")
average=Sum.sum()/Sum.count()

xdata=list(average.index)
xdata_set_to_1=list(map(lambda x:int(x)-1989,xdata))
# The exercise ask us to set the year to (0,1,2..)
# but i think start with 1, that(1,2,3...) is better.

ydata=list(average["Co2"])

print()
print(" Co2 emission in 2005, 2010, 2015:")
print(average.loc[["2005","2010","2015"],["Co2"]])
print("======================================")


x=xdata_set_to_1+list(range(29,42))
x2=[i+1989 for i in x]#for ploting use

plt.figure(figsize=(10,10),dpi=98)
plt.subplots_adjust(wspace=0.5, hspace=0.5)

##################################
#linear regression
##################################

slope, intercept, _, _, _=stats.linregress(xdata_set_to_1, ydata)

plt.subplot(221)
plt.scatter(xdata,ydata)
plt.plot(x2,[slope*k+intercept for k in x])
plt.title("linear regression")

print("estimate(linear regression) Co2 emission in 2020, 2025, 2030:")
print([slope*k+intercept for k in (2020-1989, 2025-1989, 2030-1989)])
print("======================================")
##################################
#polynomial regression
##################################

p1=np.poly1d(np.polyfit(xdata_set_to_1,ydata,deg=3))
#p2=np.poly1d(np.polyfit(xdata_set_to_1,ydata,deg=7))
#p3=np.poly1d(np.polyfit(xdata_set_to_1,ydata,deg=11))

#plt.figure()
plt.subplot(222)
plt.scatter(xdata,ydata)
plt.plot(x2,[p1(i) for i in x])
plt.title("polynomial regression")

print("estimate(polynomial regression) Co2 emission in 2020, 2025, 2030:")
print([p1(i) for i in (2020-1989, 2025-1989, 2030-1989)])
print("======================================")

#==============================================================================
# #plt.figure()
# #plt.scatter(xdata_set_to_1,ydata)
# #plt.plot(xdata_set_to_1,[p2(i) for i in xdata_set_to_1], color="green")
# #plt.figure()
# #plt.scatter(xdata,ydata)
# #plt.plot(x2,[p3(i) for i in x], color="yellow")
# #
# #the plot for deg=7,11 is obviously overfitting. cannot be used in prediction
#==============================================================================

##################################
#exponential function fit 1
##################################

#there is no registration data in 1991, 1993, 1994

def func(x,a,b,c):
    return a * np.exp(-b *x) + c

curve, _=scipy.optimize.curve_fit(func,xdata_set_to_1,ydata,maxfev=2000)

plt.subplot(223)
plt.scatter(xdata,ydata)
y_curve=list(map(lambda x:func(x,curve[0],curve[1],curve[2]), x))
plt.plot(x2,y_curve)
plt.title("exponential function fit 1")

print("estimate(exponential function fit 1) Co2 emission in 2020, 2025, 2030:")
print([y_curve[k] for k in (2020-1993, 2025-1993, 2030-1993)])
print("======================================")

##################################
#exponential function fit 2
##################################

xdata2=xdata[15:]
xdata_set_to_1_2=list(map(lambda x:int(x)-1989-18,xdata2))

ydata2=list(average["Co2"])[15:]

def func(x,a,b,c):
    return a * np.exp(-b *x) + c

curve, _=scipy.optimize.curve_fit(func,xdata_set_to_1_2,ydata2,
                                  bounds=(0,[np.inf,np.inf,np.inf]),maxfev=2000)

#I add a bounds a,b,c > 0 that makes result much better.

plt.subplot(224)
plt.scatter(xdata2,ydata2)
y_curve=list(map(lambda x:func(x,curve[0],curve[1],curve[2]), range(1,24)))
plt.plot(x2[15:],y_curve)
plt.title("exponential function fit 2  (start year 2008 and with bounds)")

print("estimate(exponential function fit 2) Co2 emission in 2020, 2025, 2030:")
print(y_curve[12], y_curve[17], y_curve[22])

plt.savefig("emissions.png")

