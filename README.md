# PyQudit

![PyPI](https://img.shields.io/pypi/v/pyqudit?logo=pypi&logoColor=yellow) ![GitHub top language](https://img.shields.io/github/languages/top/Ordoptimus/pyqudit?color=yellow&logo=python) ![PyPI - Format](https://img.shields.io/pypi/format/pyqudit) ![PyPI - Implementation](https://img.shields.io/pypi/implementation/pyqudit?color=%23333) ![GitHub issues](https://img.shields.io/github/issues/Ordoptimus/pyqudit?color=blue&logo=github) ![GitHub](https://img.shields.io/github/license/Ordoptimus/pyqudit)

<p style="text-align:justify">A Python package for using generalised and universal versions of quantum gates, in N-dimensions. Enables building simple quantum circuit simulations on qudit logic using higher dimensional gates.</p>

### Concept
<p style="text-align:justify">Mainstream Quantum Computing uses qubits which operate in a two dimensional Hilber space. Qudits are their higher dimensional equivalents with better informaiton density and potential for hgher efficiency. PyQudit includes the qudit versions of fundamental quantum gates, useable over any dimension<sup>*</sup> as specified by the user. It can be used to understand the behaviour of qudit gates as also to build higher dimensional circuits for experimentation.</p>
<p style="text-align:right"><sup>*check documentation for exceptions</sup></p>

### Install
```
pip install pyqudit
```

### Build Locally
```
pip3 install --upgrade pip
pip3 install --upgrade setuptools
git clone https://github.com/Ordoptimus/pyqudit.git
cd pyqudit
python3 setup.py bdist_wheel
```
Replace [version] with the latest version as seen in the wheel file in /bdist_wheel
```
pip3 install dist/pyqudit-[version]-py3-none-any.whl
```

### Use
```
import pyqudit.qudit as pq
```

##### Show all package functions
```dir(pq)```

### Demo
Detailed examples available in the Documentation!

### Documentation
[link coming soon]
