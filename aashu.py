class A(): 
    # 1.1 property
    name = 'Aashish'
    surname = 'Mali'
    # 1.2 constructor
    # 1.3 method

class B(A): 
    # 1.1 property
    # 1.2 constructor
    # 1.3 method
    pass
class C(B): 
    # 1.1 property
    # 1.2 constructor
    # 1.3 method
    pass
class D(C): 
    # 1.1 property
    # 1.2 constructor
    # 1.3 method
    pass

class E(D): 
    # 1.1 property
    # 1.2 constructor
    # 1.3 method
    pass
class F(E): 
    # 1.1 property
    # 1.2 constructor
    # 1.3 method
    pass
class G(F): 
    # 1.1 property
    # 1.2 constructor
    # 1.3 method
    pass
class H(G): 
    # 1.1 property
    # 1.2 constructor
    # 1.3 method
    pass
class I(H): 
    # 1.1 property
    # 1.2 constructor
    # 1.3 method
    pass
class J(I): 
    # 1.1 property
    # 1.2 constructor
    # 1.3 method
    pass
class K(J): 
    # 1.1 property
    # 1.2 constructor
    # 1.3 method
    pass
class L(K): 
    # 1.1 property
    # 1.2 constructor
    # 1.3 method
    pass
class M(L): 
    # 1.1 property
    # 1.2 constructor
    # 1.3 method
    pass
class N(M): 
    # 1.1 property
    # 1.2 constructor
    # 1.3 method
    pass
class O(N): 
    # 1.1 property
    # 1.2 constructor
    # 1.3 method
    pass
class P(O): 
    # 1.1 property
    # 1.2 constructor
    # 1.3 method
    pass
class Q(P): 
    # 1.1 property
    # 1.2 constructor
    # 1.3 method
    pass
class R(Q): 
    # 1.1 property
    # 1.2 constructor
    # 1.3 method
    pass
class S(R): 
    # 1.1 property
    # 1.2 constructor
    # 1.3 method
    pass
class T(S): 
    # 1.1 property
    # 1.2 constructor
    # 1.3 method
    pass
class U(T): 
    # 1.1 property
    # 1.2 constructor
    # 1.3 method
    pass
class V(U): 
    # 1.1 property
    # 1.2 constructor
    # 1.3 method
    pass
class W(V): 
    # 1.1 property
    # 1.2 constructor
    # 1.3 method
    pass
class X(W): 
    # 1.1 property
    # 1.2 constructor
    # 1.3 method
    pass
class Y(X): 
    # 1.1 property
    # 1.2 constructor
    # 1.3 method
    pass

class Z(Y): 
    # 1.1 property
    # 1.2 constructor
    # 1.3 method
    def getMyName(self): 
        # self is the internal object
        print(f'My Name Is {self.name}')
        print(f'My Surname Is {self.surname}')

# Create class object
# classobject = classname()
co = Z()
# classobject.method
co.getMyName()
