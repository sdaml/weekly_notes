Installation of Tools
===

We're gonna all use Linux or OSX, if you're on Windows I recommend a VM running Ubuntu ([VMWare player](https://my.vmware.com/en/web/vmware/free#desktop_end_user_computing/vmware_workstation_player/12_0) is pretty awesome)

(Also just a note, a lot of the stuff we're using supports GPU acceleration but can be pretty setup. We're really not doing anything where GPU is mandatory, just know that the way ML gets sped up a lot of the time)

### Git

[Install from here](https://git-scm.com/)

### Python 2.7
I highly recommend installing [Anaconda Python](https://www.continuum.io/downloads) if you're on Mac just because it provides a lot of stuff for you. If you're on Ubuntu Python is installed but is usually 2.6.X, `sudo apt-get install python-dev` will upgrade you to 2.7

Also make sure you install pip, if you installed Anaconda its already there, if you're on Ubuntu, `sudo apt-get install python-pip`

### General Python Packages

(If you installed Anaconda all of these have already been installed)

We are using the following:
- Numpy: Library for linear algebra and other math stuff
- matplotlib: a graphing library
- pandas: a library for data structures and visualization
- iPython: a better python shell
- iPython Notebook:Awesome for prototyping stuff
- nose: a unittest runner
- SciPy: for scientific computing (mostly just installing because some of our packages require it)

On Ubuntu:
```sudo apt-get install python-numpy python-matplotlib ipython ipython-notebook scipy python-pandas python-nose```

### [SciKit Learn](http://scikit-learn.org/stable/)

One of the largest and most commonly used ML libraries. Not as optimized as TensorFlow, but has less of a learning curve than TensorFlow. I figure we can start with SciKit Learn and move to TensorFlow when we have a bit more experience.

Ubuntu/Mac: ```pip install -U scikit-learn```

### [TensorFlow](https://www.tensorflow.org/)
Tensorflow is the machine learning library Google uses for a lot of their products. It's super powerful but is designed mostly for deep learning and more advanced ML concepts. You totally can do basics in it, its just not as easy as scikit-learn for the basics.

Ubuntu:

```sudo pip install --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.5.0-cp27-none-linux_x86_64.whl```

Mac:

```
sudo pip install --upgrade six https://storage.googleapis.com/tensorflow/mac/tensorflow-0.5.0-py2-none-any.whl```

### [Kera](http://keras.io)
A library for neural networks. You can do neural networks in Tensorflow as well but Keras abstracts a bit more from you and provides a bunch of common layer strategies, and other stuff that makes neural networks easier. Keras actually runs on top of TensorFlow.

Ubuntu/Mac: `sudo pip install keras`
