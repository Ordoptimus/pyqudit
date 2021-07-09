Gate Functions
==============

All the gate functions available in PyQudit are documented here.

.. contents:: Table of Contents
    :local:

CX gate
-------
The functions for CX (CNOT) gate implementations.
The CX gate is a fundamental gate of both qubit and qudit logics
and essential for most kinds of qudit manipulations.

cxdGen
******
| ``cxdGen(d,qtk1,qtk2)``

Generalised CX (CNOT) Gate. Example:

>>> cxdGen(4,[0,1,0,0],[1,0,0,0])
[0,1,0,0]

Operates in Ket form. If working with decimal values, use ``convKet(d,qt)`` to convert each qudit value to Ket.

cxdSup
******
| ``cxdSup(d,states)``

Standard formulaic implementation of generalised CX, applicable for superposed states.

cxdSupFor
*********
| ``cxdSupFor(d,states)``

Custom, more efficient formulaic implementation of CX with same capabilities as ``cxdSup``.

CX Drag Gate
------------
The functions for CX Drag gate implementations.
The CX Drag gate is more commpnly seen in qudit logic
and required to make compound gates and emulate some aspects of qubit logic gates.

cxdDragGen
**********
| ``cxdDragGen(d,qtk1,qtk2)``

Generalised CX Drag Gate not applicable for superposed states.

cxDragdSup
**********
| ``cxDragdSup(d,qtk)``

Generalised CX Drag Gate applicable for superposed states.

GXOR Gate
---------
The various formulae for GXOR.
