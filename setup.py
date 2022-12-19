"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['lunar_lander.py']
DATA_FILES = []
OPTIONS = {'resources': ['/Users/matthew/Desktop/LunarLander/sounds', '/Users/matthew/Desktop/LunarLander/images'], 'iconfile':'/Users/matthew/Desktop/LunarLander/images/favicon.icns'}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2exe': OPTIONS},
    setup_requires=['py2exe'],
)
