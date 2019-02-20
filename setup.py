from setuptools import setup
from setuptools import find_packages


setup(name='tf-keras-rl',
      version='0.0.1',
      description='Deep Reinforcement Learning for Tensorflow-Keras',
      author='Matthias Plappert',
      author_email='matthiasplappert@me.com',
      url='https://github.com/keras-rl/keras-rl',
      license='MIT',
      #install_requires=['tensorflow>=2.0.0-dev20190219'],
      extras_require={
          'gym': ['gym'],
      },
      packages=find_packages())
