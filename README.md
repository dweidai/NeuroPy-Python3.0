# NeuroPy-Python3.0
I updated NeuroPy to Python version 3.*. NeuroPy library written in python to connect, interact and get data from neurosky's MindWave headset.  This library is based on https://pypi.org/project/NeuroPy/
NeuroPy library written in python to connect, interact and get data from neurosky's MindWave EEG headset.

This library is based on the minwave mindset communication protocol published by Neurosky and is tested with Neurosky Mindwave EEG headset.

##Installation##

Download the source distribution (zip file) from dist directory or from PyPi
unzip and navigate to the folder containing setup.py and other files
run the following command: python setup.py install


##Usage##

After initialising , if required the callbacks must be set then using the start method the library will start fetching data from mindwave i.e. object1.start() similarly stop method can be called to stop fetching the data i.e. object1.stop()

###The data from the device can be obtained using either of the following methods or bot of them together:###

Obtaining value: variable1=object1.attention #to get value of attention

#other variables: attention,meditation,rawValue,delta,theta,lowAlpha,highAlpha,lowBeta,highBeta,lowGamma,midGamma, poorSignal and blinkStrength

Setting callback:a call back can be associated with all the above variables so that a function is called when the variable is updated. Syntax: setCallBack("variable",callback_function) 
for eg. to set a callback for attention data the syntax will be setCallBack("attention",callback_function)

#other variables: attention,meditation,rawValue,delta,theta,lowAlpha,highAlpha,lowBeta,highBeta,lowGamma,midGamma, poorSignal and blinkStrength
