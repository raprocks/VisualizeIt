from setuptools import setup

with open('./README.md') as fd:
    long_des = fd.read()

setup(
    name="VisualizeIt",
    version="0.1",
    description="Terminal based Algorithm Visualizer made in Python3 with Typer and Colorama",
    author="Rohit Patil",
    packages=['VisualizeIt', 'VisualizeIt_implementations'],
    author_email="rahulhimesh09@gmail.com",
    license="GPLv3+",
    url="https://github.com/raprocks/VisualizeIt",
    install_requires=["colorama", "typer"],
    long_description=long_des,
    long_description_content_type="text/markdown",
    package_dir={'VisualizeIt': "VisualizeIt",
                 'VisualizeIt_implementations': "VisualizeIt/VisualizeIt_implementations"},
    package_data={
        "VisualizeIt": ["VisualizeIt_implementations/*"]
    },
    entry_points={
        "console_scripts": ["visualize=VisualizeIt.main:app"
                            ]
    }
)
