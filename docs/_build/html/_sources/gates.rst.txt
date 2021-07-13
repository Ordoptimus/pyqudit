Gate Functions
==============

All the gate functions available in PyQudit are documented here with examples.
Since all gates are generalised implementations, the user needs to provide
the dimension through the parameter ``d``. Unless specified otherwise,
all qudit parameters are in the Ket form. If number of qudits is not specified,
the gates are single-qudit ones.

.. contents:: Table of Contents
    :local:

CX gate
-------
The functions for the two-qudit CX (CNOT) gate implementations.
The CX gate is a fundamental gate of both qubit and qudit logics
and essential for most kinds of qudit manipulations.

CXd_dis
*******
| ``CXd_dis(d,qudit1,qudit2)``

Generalised CX (CNOT) Gate.

>>> CXd_dis(4,[0,1,0,0],[1,0,0,0])
[0,1,0,0]

Operates in Ket form. If working with decimal values,
use ``convKet(d,qt)`` to convert each qudit value to Ket.

CXd
***
| ``CXd(d,state)``

Standard formulaic implementation of generalised CX,
applicable for superposed states. Works using the state matrix form,
which can be obtained using the ``stateMat(d,qudit1,qudit2)`` function.

>>> statematrix = stateMat(4,[0,1,0,0],[1,0,0,0])
>>> CXd(4,statematrix)
array([0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

CXd_cstm
********
| ``CXd_cstm(d,statematrix)``

Custom, more efficient formulaic implementation of CX with same capabilities as ``CXd``.
Recommended for logic involving lower dimensions. Also involves state matrix form.

>>> statematrix = stateMat(4,[0,1,0,0],[1,0,0,0])
>>> CXd_cstm(4,statematrix)
[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

CX-Drag Gate
------------
The functions for the two-qudit CX-Drag gate.
The CX-Drag gate is an inverse of the CX gate and is required in qudit logic
to make compound gates and emulate some aspects of qubit gates.

CXDrag_dis
**********
| ``CXDrag_dis(d,qudit1,qudit2)``

Generalised CX Drag Gate not applicable for superposed states. Formulaic implementation.

>>> CXDrag_dis(4,[0,0,1,0],[1,0,0,0])
[0, 0, 0, 1]

CXDrag
******
| ``CXDrag(d,statematrix)``

Generalised CX Drag Gate applicable for superposed states.
Uses a state matrix of the two qudits, instead of their Ket forms.
Handles superposition well.

>>> statematrix = stateMat(4,[0,1,0,0],[1,0,0,0])
>>> CXDrag(4,statematrix)
array([0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0])

GXOR Gate
---------
The various functions for the two-qudit GXOR gate, which is used to achieve logic for other gates,
such as SWAP or the Hermetian CX.

GXOR_dis
********
| ``GXOR_dis(d,qudit,qudit2)``

Generalised GXOR gate not applicablefor superposed states. Formulaic implementation.

>>> GXOR_dis(4,[0,1,0,0],[1,0,0,0])
[0,1,0,0]

GXOR
****
| ``GXOR(d,statematrix)``

Generalised implementation of the GXOR gate, applicable for superposed states.
Uses the state matrix form of two qudits.

>>> statematrix = stateMat(4,[0,1,0,0],[1,0,0,0])
>>> GXOR(4,statematrix)
array([0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

SWAP Gate
---------
The functions of the two-qudit SWAP gate, used to swap the states of two qudits,
akin to its qubit equivalent. It is a compound gate,
with CX, CXDrag, and GXOR as its constituents.

SWAPd
*****
| ``SWAPd(d,qudit1,qudit2)``

Generalised swap gate implementation not applicable for superposition.

>>> SWAPd(4,[0,1,0,0],[1,0,0,0])
([1, 0, 0, 0], [0, 1, 0, 0])

Hadamard Gate
-------------
The functions of the Hadamard gate, one of the fundamental and crucial gates of quantum logic
used to carry out superposition.

Hd_dis
******
| ``Hd_dis(d,qudit)``

Generalised implementation for all dimensions. Can't handle superposed states.

>>> Hd_dis(4,[0,1,0,0])
array([ 5.00000000e-01+0.00000000e+00j,  1.63397448e-07+5.00000000e-01j,
       -5.00000000e-01+3.26794897e-07j, -4.90192345e-07-5.00000000e-01j])

Hd
**
| ``Hd(d,qudit)``

Generalised implementation for 2\ :sup:`n` dimensions. Handles superposed states.

>>> Hd(4,[0,1,0,0])
array([ 0.5, -0.5,  0.5, -0.5])

CZ Gate
-------
The functions for the two-qudit CZ gate. This is a compound gate,
with the Hadamard gate and CX gate as its constituents.
CZ inherits Hadamard's superposition conditions.

CZd
***
| ``CZd(d,statematrix)``

Generalised implementation for 2\ :sup:`n` dimensions. Handles superposed states.

>>> statematrix = stateMat(4,[0,1,0,0],[1,0,0,0])
>>> CZd(4,statematrix)
array([0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])

X Gate
------
The functions for the X gate. This gate works similar to the NOT gate in classical logic,
except on multiple dimensions.

Xd
**
| ``Xd(d,qudit)``

Generalised implementation of the X gate, applicable for all dimensions.
Supports superposed states.

>>> Xd(4,[0,1,0,0])
array([0, 0, 1, 0])

Y Gate
------
The functions for Y gate. It is a phase-change gate like its qubit equivalent,
but for multiple dimensions.

Yd
**
| ``Yd(d,qudit)``

Generalised implementation of the Y gate, applicable for all dimensions.
Supports superposed states.

>>> Yd(4,[0,1,0,0])
array([ 0.+0.00000000e+00j,  0.+0.00000000e+00j, -1.+3.26794897e-07j,
        0.+0.00000000e+00j])

Z Gate
------
The functions for Z gate. It is also a phase-change gate like its qubit equivalent,
but for multiple dimensions.

Zd
**
| ``Zd(d,qudit)``

Generalised implementation of the Z gate, applicable for all dimensions.
Supports superposed states.

>>> Zd(4,[0,1,0,0])
array([0.00000000e+00+0.j, 3.26794897e-07+1.j, 0.00000000e+00+0.j,
       0.00000000e+00+0.j])

Toffoli Gate
------------
The functions for the three-qudit Toffoli or CCNOT gate.
This is another fundamental gate useful in delaing with multiple qudits.

Toffolid
********
| ``Toffolid(d,qudit1,qudit2,qudit3)``

Generalised implementation of the Toffoli gate, applicable for all dimensions.
Supports superposed states.

>>> Toffolid(4,[0,1,0,0],[1,0,0,0],[0,0,0,0])
array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
