PyQudit
=======

.. |PyPIVersion| image:: https://img.shields.io/pypi/v/pyqudit?logo=pypi&logoColor=yellow
                  :target: https://pypi.org/project/pyqudit
.. |Docs| image:: https://readthedocs.org/projects/pyqudit/badge/?version=latest
            :target: https://pyqudit.readthedocs.io/en/latest/?badge=latest
.. |GitLanguage| image:: https://img.shields.io/github/languages/top/Ordoptimus/pyqudit?color=yellow&logo=python
.. |PyPIFormat| image:: https://img.shields.io/pypi/format/pyqudit?color=purple
.. |PyPIImplementation| image:: https://img.shields.io/pypi/implementation/pyqudit?color=%23333
.. |GitIssues| image:: https://img.shields.io/github/issues/Ordoptimus/pyqudit?color=blue&logo=github
                :target: https://github.com/Ordoptimus/pyqudit/issues
.. |License| image:: https://img.shields.io/github/license/Ordoptimus/pyqudit?color=skyblue
.. _official documentation: https://pyqudit.readthedocs.io

|PyPIVersion| |Docs| |GitLanguage| |PyPIFormat| |PyPIImplementation| |GitIssues| |License|

PyQudit is a Python package for using generalised and universal versions of quantum gates, in N-dimensions. Enables building simple quantum circuit simulations on qudit logic using higher dimensional gates.

Getting Started
===============

Concept
-------
Mainstream QuantumComputing uses qubits which operate in a two dimensional
Hilber space. Qudits are their higher dimensional equivalents with better
informaiton density and potential for higher efficiency.
PyQudit includes the qudit versions of fundamental quantum gates,
useable over any dimension\ :sup:`*` as specified by the user.
It can be used to understand the behaviour of qudit gates as also to build
higher dimensional circuits for experimentation.

:sup:`*refer gate functions`

Install
-------
The latest stable version of PyQudit is available on PyPI and can be installed with pip.
It is recommeded to install in your quantum computing python environment, alongside existing packages.

.. code-block:: bash

    pip install pyqudit

Build Locally
-------------
Alternatively, you can build the package wheel from source and then install it via pip.

.. code-block:: console

    pip3 install --upgrade pip
    pip3 install --upgrade setuptools
    git clone https://github.com/Ordoptimus/pyqudit.git
    cd pyqudit
    python3 setup.py bdist_wheel

Replace [version] with the latest version as seen in the wheel file in /bdist_wheel

.. code-block:: console

    pip3 install dist/pyqudit-[version]-py3-none-any.whl

Use
---
.. code-block:: python

    import pyqudit.qudit as pq

Use ``dir(pq)`` to show all package methods.

Sample
------

>>> import pyqudit.qudit as pq
>>> d = int(input('Enter Dimensions: '))
Enter Dimensions: 3
>>> print("\n---CX's Pauli Matrix---")
>>> print(pq.CXd_pauli(d))
---CX's Pauli Matrix---
[[1 0 0 0 0 0 0 0 0]
 [0 1 0 0 0 0 0 0 0]
 [0 0 1 0 0 0 0 0 0]
 [0 0 0 0 0 1 0 0 0]
 [0 0 0 1 0 0 0 0 0]
 [0 0 0 0 1 0 0 0 0]
 [0 0 0 0 0 0 0 1 0]
 [0 0 0 0 0 0 0 0 1]
 [0 0 0 0 0 0 1 0 0]]

Documentation
=============
Refer the `official documentation`_ for detailed examples and syntax.
