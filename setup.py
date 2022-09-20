from setuptools import setup
import versioneer

requirements = [
    "beautifulsoup4",
]

setup(
    name="tableau-xray",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="A high-level parser for Tableau's .twb and .twbx file formats.",
    license="MIT",
    author="Elias Jaffe",
    author_email="elijaffe173@gmail.com",
    url="https://github.com/Ejjaffe/tableau-xray",
    packages=["tableau_xray"],
    entry_points={"console_scripts": ["tableau_xray=tableau_xray.cli:cli"]},
    install_requires=requirements,
    keywords=[
        "tableau-xray",
        "tableau",
        "introspection",
        "inspection",
        "tableauxray",
    ],
    classifiers=[
        # "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
