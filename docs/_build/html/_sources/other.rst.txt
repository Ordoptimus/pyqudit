Other Functions
===============

These functions serve as utilities that help the user with activities
such as conversions and tensor products.
They are used within and in tandem with the gate and matrix functions.

.. contents:: Table of Contents
    :local:

Convert2Ket
-----------
| ``convKet(d,decimal_qudit)``

A function which enables qudit conversion from decimal form to ket form.

>>> convKet(4,1)
[0, 1, 0, 0]

Convert2Decimal
---------------
| ``convDec(d,ket_qudit)``

A function which enables qudit conversion from ket form to decimal form.

>>> pq.convDec(4,[0,1,0,0])
1

StateMatrix
-----------
| ``stateMat(d,qudit1,qudit2)``

A function which facilitates conversion of the states of two qudits in Ket form to a state matrix.

>>> stateMat(4,[0,1,0,0],[1,0,0,0])
[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

IdentityTensorProduct
---------------------
| ``tensorIGt(d,gate_symbol)``

A function to output the tensor product of an identity matrix with either of
Hadamard (H), X, or Z gates.

>>> tensorIGt(2,'H')
array([[ 0.70710678,  0.70710678,  0.        ,  0.        ],
       [ 0.70710678, -0.70710678,  0.        ,  0.        ],
       [ 0.        ,  0.        ,  0.70710678,  0.70710678],
       [ 0.        ,  0.        ,  0.70710678, -0.70710678]])
