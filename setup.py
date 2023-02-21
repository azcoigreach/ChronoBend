from setuptools import setup

# apt-get install fonts-dejavu python3-numpy python3-pil

setup(
    name="cb",
    version="0.1",
    author="AZcoigreach",
    author_email="azcoigreach@gmail.com",
    packages=["cb", "cb.commands"],
    include_package_data=True,
    install_requires=[
        "click",
        "coloredlogs",
        "adafruit-circuitpython-rgb-display",
        "adafruit-circuitpython-debouncer",
        "numpy",
        "psutil",
        "ifaddr",
        "speedtest-cli",
        "asyncclick",
        "anyio",
        ],
    entry_points="""
        [console_scripts]
        cb=cb.cli:cli
    """,
)
