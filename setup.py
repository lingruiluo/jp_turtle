from setuptools import setup

url = ""
version = "0.1.0"
readme = open('README.md').read()

setup(
    name="jp_turtle",
    packages=["jp_turtle"],
    version=version,
    description="Simple jupyter widget wrappers for turtle implementation",
    long_description=readme,
    include_package_data=True,
    author="Aaron Watters; Lingrui Luo",
    author_email="awatters@flatironinstitute.org; ll3356@columbia.edu",
    url=url,
    install_requires=[
        "jp_doodle", 
        "jp_proxy_widget",
        #"requests", 
        #"matplotlib", 
        #"numpy", 
        #"scipy", 
        "pillow", 
        #"psutil",
        "imageio",
        #"sklearn",
        "jupyter-ui-poll",
        "pytz",
        ],
    license="MIT"
)
