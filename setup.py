from setuptools import setup, Extension
from glob import glob
import numpy as np

setup(
    ext_modules=[
        Extension(
            name="MPImfp",
            sources=glob("src/*.c"),
            include_dirs=[np.get_include()]
        ),
    ]
)
