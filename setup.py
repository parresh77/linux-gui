"""setup.py: setuptools control."""
import re
import os
from setuptools import setup

from protonvpn_linux_gui.constants import VERSION

try:
    with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
        long_descr = '\n' + f.read()
except FileNotFoundError:
    long_descr = """
    The Unofficial Linux GUI for ProtonVPN.

    For further information and a usage guide, please view the project page:

    https://github.com/calexandru2018/protonvpn-linux-gui
    """



setup(
    name="protonvpn-linux-gui-calexandru2018",
    packages=[
        "protonvpn_linux_gui",
        "protonvpn_linux_gui.resources",
        "protonvpn_linux_gui.resources.img.flags",
        "protonvpn_linux_gui.resources.img.flags.small",
        "protonvpn_linux_gui.resources.img.flags.large",
        "protonvpn_linux_gui.resources.img.logo",
        "protonvpn_linux_gui.resources.img.utils",
        ],
    entry_points={
            "console_scripts": [
                "protonvpn-gui = protonvpn_linux_gui.protonvpn_gui:init",
                "protonvpn-tray = protonvpn_linux_gui.indicator:ProtonVPNIndicator",
            ]
        },
    include_package_data=True,
    version=VERSION,
    description="Unofficial Linux GUI client for ProtonVPN",
    long_description=long_descr,
    long_description_content_type="text/markdown",
    author="calexandru2018",
    author_email="acrandom@pm.me",
    license="GPLv3",
    url="https://github.com/calexandru2018/protonvpn-linux-gui",
    install_requires=[
        "protonvpn-cli>=2.2.2",
        "requests>=2.23.0",
        "configparser>=4.0.2"
    ],
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Environment :: X11 Applications :: GTK",
        "Intended Audience :: End Users/Desktop",
        "Operating System :: POSIX :: Linux",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
