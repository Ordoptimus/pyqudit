import numpy as np
import math

#Function for Conversion of qudits into ket format
def convKet(d,qt):
  qtk= [0]*d
  qtk[qt] = 1
  return qtk

#Function for Conversion of ket format into qudits
def convDec(d,qtk):
  for i in range(d):
    if qtk[i]==1:
      return i

#Converting states to State Matrix
def stateMat(d,qt1k,qt2k):
  state = []
  for i in range(d):
    state.extend(np.dot(qt1k[i],qt2k))
  return state

#Tensor product of I and (H or X or Z)
def tensorIGt(d,gate):
  if gate.upper() == 'H':
    gt = pauli_hd(d)
  elif gate.upper() == 'X':
    gt = pauli_xd(d)
  elif gate.upper() == 'Z':
    gt = pauli_zd(d)
  else:
    print('Give Valid Input')
    return 0
  igt = []
  for i in range(d):
    for j in range(d):
      temp = []
      for k in range(0,i*d):
        temp.append(0 * d)
      for k in range(1):
        temp.extend(gt[j])
      for k in range(0,d-i-1):
        temp.extend([0] * d)
      igt.append(temp)
  return np.array(igt)

#Controlled Not Gate
# qt1 is Control Bit while qt2 is Target bit
def cxdGen(d,qtk1,qtk2):
  qt1 = convDec(d,qtk1)
  qt2 = convDec(d,qtk2)
  res = convKet(d,(qt1+qt2)%d)
  return  res

#Controlled Not_Drag gate
def cxdDragGen(d,qtk1,qtk2):
  qt1 = convDec(d,qtk1)
  qt2 = convDec(d,qtk2)
  res = convKet(d,(qt2-qt1)%d)
  return  res

#GXOR gate
def gxorGen(d,qtk1,qtk2):
  qt1 = convDec(d,qtk1)
  qt2 = convDec(d,qtk2)
  res = convKet(d,(qt1-qt2)%d)
  return  res

#Swap gate implementation using CNOT,CNOTDrag and GXOR Gate for D Dimensions
def swap(d,qt1,qt2):
    #Implementation of CNOTDrag gate where control Bit is qt2 while target Bit is qt1
    qt1=cxdDragGen(d,qt2,qt1)
    #Implementation of CNOT gate where control Bit is qt1 while target Bit is qt2
    qt2=cxdGen(d,qt1,qt2)
    #Implementation of GXOR gate
    qt1=gxorGen(d,qt2,qt1)
    return qt1,qt2

#Generalized Hadamard for any dimensions but can't take superposed states
#since it first convert states into decimal and then use it in mathematical formula
def hdGen(d,qtk):
    j = convDec(d,qtk)
    theta = complex(0,(2*3.141592)/d)
    w=np.exp(theta)
    hc=(1/math.sqrt(d))
    i_ket = [0] * d
    hm = []
    hm = [0] * d
    for i in range(d):
      hm[i] = w ** (i*j)
    h1m = np.array(hm)
    return h1m*hc

#CNOT implementation With NEW Formula
def pauli_cxdFor(d):
  #start = time.time()
  cnot = []
  for i in range(d*d):
    f = int((i-(i%d)) / d)
    r = convKet(d*d,d*f+((d-f)+i)%d)
    cnot.append(r)
  #end = time.time()
  #print(f"Runtime of the program is {end - start}")
  return np.array(cnot)

def pauli_cxd(d):
  #start = time.time()
  size = d * d
  pau = list([0]*size for i in range(size))
  temp = 0
  for i in range(d):
    for j in range(d):
      c = temp + ((i+j) % d)
      pau[c][temp+j] = 1
    temp += d
  #end = time.time()
  #print(f"Runtime of the program is {end - start}")
  return np.array(pau)

def pauli_cxDragd(d):
  size = d * d
  pau = list([0]*size for i in range(size))
  temp = 0
  for i in range(d):
    for j in range(d):
      c = temp + ((j-i) % d)
      pau[c][temp+j] = 1
    temp += d
  return np.array(pau)

def pauli_gXord(d):
  size = d * d
  pau = list([0]*size for i in range(size))
  temp = 0
  for i in range(d):
    for j in range(d):
      c = temp + ((i-j) % d)
      pau[c][temp+j] = 1
    temp += d
  return np.array(pau)

def pauli_xd(d):
  pau = list([0]*d for i in range(d))
  for i in range(d):
    pau[(i+1) % d][i] = 1
  return np.array(pau)

def pauli_zd(d):
  theta = complex(0,(2*3.141592)/d)
  w=np.exp(theta)
  pau = list([0]*d for i in range(d))
  for i in range(d):
    c = w ** i
    pau[i][i] = c
  return np.array(pau)

def pauli_yd(d):
  con = complex(0,1)
  return con*(np.dot(pauli_xd(d),pauli_zd(d)))

def pauli_toffoli(d):
  size = d * d * d
  pau = list([0]*size for i in range(size))
  temp = 0
  for i in range(d):
    for j in range(d):
      for k in range(d):
        c = temp + ((k+(i*j)) % d)
        pau[c][temp+k] = 1
      temp += d
  return np.array(pau)

def hm(d):
  if d == 2:
    return np.array([[1,1],[1,-1]])
  else:
    h1m = hm(d/2)
    return np.concatenate((np.concatenate((h1m,h1m),axis=1),(np.concatenate((h1m,(-1*h1m)),axis=1))),axis=0)

def pauli_hd(d):
  return (1/math.sqrt(d))*hm(d)

def pauli_czd(d):
  hd = pauli_hd(d)
  nih = np.array(tensorIGt(d,'H'))
  cnot = pauli_cxd(d)
  res = np.dot(nih, cnot)
  pau_cz = np.dot(res,nih)
  return pau_cz

#Pauli matrix representation of Hadamard gate
#Only for 2^n dimesions but works with superposed states
def hdSup(d,qtk):
  return np.dot(pauli_hd(d),qtk)

def czdSup(d,states):
  return (np.dot(pauli_czd(d),states))

#Pauli Matrix representation for X and Z gate:
#works for all dimesions also works on superposed states
def xdSup(d,qtk):
  return np.dot(pauli_xd(d),qtk)

def zdSup(d,qtk):
  return (np.dot(pauli_zd(d),qtk))

def ydSup(d,qtk):
  return (np.dot(pauli_yd(d),qtk))

#Using formula of Cnot
def cxdSup(d,states):
  #start = time.time()
  res = np.dot(pauli_cxd(d),states)
  #end = time.time()
  #print(f"Runtime of the program is {end - start}")
  return res

#Using NEW formula of Cnot
def cxdSupFor(d,states):
  #start = time.time()
  state = np.array([0.0] * (d*d))
  for i in range(d*d):
    f = int((i-(i%d)) / d)
    r = convKet(d*d,d*f+((d-f)+i)%d)
    state[i] = sum(np.multiply(r,states))
  #end = time.time()
  #print(f"Runtime of the program is {end - start}")
  return list(state)

def cxDragdSup(d,qtk):
  return (np.dot(pauli_cxDragd(d),qtk))

def gXordSup(d,qtk):
  return (np.dot(pauli_gXord(d),qtk))

#Toffoli Gate
def toffoliSup(d,qtk1,qtk2,qtk3):
  t = stateMat(d,qtk2,qtk3)
  res = np.array(stateMat(d,qtk1,t))
  return np.dot(pauli_toffoli(d),res)
