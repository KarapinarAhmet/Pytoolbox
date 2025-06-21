from setuptools import setup, find_packages

setup(
    name="pytoolbox",
    version="0.1",
    description="Kullanışlı CLI araçlar koleksiyonu",
    author="Ahmet Karapınar",
    packages=find_packages(),
    install_requires=[
        "requests",
        "colorama",
        "dnspython",
        "click"
    ],
    entry_points={
        'console_scripts': [
            'ptb=pytoolbox.ptb:main',  # ptb.py dosyasındaki main fonksiyonunu çalıştırır
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
