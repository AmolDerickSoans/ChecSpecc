import setuptools

with open('requirements.txt') as f:
    requirements = f.readlines()

setuptools.setup(
    name='ChecSpecc',
    version='1.0',
    author='AmolDerickSoans',
    description='Python Hardware Configuration Check Utility',
    url='https://github.com/AmolDerickSoans/ChecSpecc',
    license ='MIT',
    packages=setuptools.find_packages(),
    classifiers =(
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ),
    entry_points ={
            'console_scripts': [
                'checspecc = ChecSpecc.main:checkspec'
            ]
        },
    python_requires='>=3',
    install_requires = requirements,
    zip_safe = False
    )