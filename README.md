# Entrelazamiento-EMQR

## 0. Identificadores

```math
\mathcal{E}_{\mathrm{EMQR}}
=
(S,\mathcal{C},\mathrm{Reg},\mathcal{P},\mathrm{Val},B^{\mathrm{Rel}})
```

```math
\mathrm{Ent}_{\mathrm{EMQR}}(I,J)
\iff
R^{\mathrm{EMQR}}_{IJ}\neq R_I\times R_J \pmod{A_{\mathrm{abs}}}
\;\wedge\;
\exists(c,\rho):\Pi_{c,\rho}(R^{\mathrm{EMQR}}_{IJ})\in O^{\mathrm{nsep}}_{c,\rho}
```

```math
\mathrm{Comm}_{\mathrm{EMQR}}(I,J)
\neq
\mathrm{Signal}_{T_\alpha}(I\to J)
```

```math
\mathrm{Comm}_{\mathrm{EMQR}}(I,J)
=
D_{\mathrm{Rel}}\left(\{b_{IJ}(t_n)\}_{n}\right)
\pmod{A_{\mathrm{abs}}}
```

---

## 1. Notación

| Símbolo | Tipo |
|---|---|
| `S` | fuente estructuralmente no agotable |
| `\mathcal{C}` | clase de cartas |
| `Reg` | clase de regímenes de lectura |
| `\mathcal{P}` | clase de planos activos |
| `Val` | clase de valores cerrados |
| `B^{Rel}` | espacio de bits relacionales |
| `A_abs(ρ)` | dominio de residuos absorbibles bajo régimen `ρ` |
| `Π_nabs` | proyección sobre residuo no absorbible |
| `ω` | residuo de carta, relación o actualización |
| `κ` | operador de cierre |
| `π` | proyección admisible |
| `λ` | pérdida inducida |
| `Θ_{αβ}` | transición entre cartas temporales |
| `Ω` | curvatura composicional, relacional o transtemporal |
| `Key(I)` | clave topológica de identidad |
| `D_Rel` | decodificador relacional |
| `F^{Rel}` | energía libre / curvatura relacional según contexto |
| `S_sig` | estadístico de señalización ordinaria |

---

## 2. Núcleo EMQR

### 2.1 Carta

```math
c_\rho:S\dashrightarrow P,
\qquad
c\in\mathcal{C},
\quad
\rho\in Reg,
\quad
P\in\mathcal{P}
```

```math
\pi_{c,\rho}:P\to O_{c,\rho}
```

```math
\lambda(c,\rho;S)=\omega_{c,\rho}\in\Omega_{c,\rho}
```

```math
\kappa_{c,\rho}(P)=1
\iff
\omega_{c,\rho}(P)\in A_{\mathrm{abs}}(\rho)
```

```math
v_{c,\rho}=\pi_{c,\rho}(P),
\qquad
\kappa_{c,\rho}(P)=1
```

```math
\mathrm{Leg}(o_{c,\rho})
\iff
\omega_{c,\rho}\in A_{\mathrm{abs}}(\rho)
```

### 2.2 Axiomas

```math
\forall c\in\mathcal{C}_{fin},\forall\rho\in Reg:
c_\rho(S)\not\equiv S
```

```math
x\in Comp
\Rightarrow
\exists(c,\rho,P):x\in c_\rho(S)\subseteq P
```

```math
\forall(c,\rho):\lambda(c,\rho;S)\ge 0
```

```math
T_{c,\rho}\not\equiv S
```

```math
\forall c,\rho,P,v:
c_\rho(S)\not\equiv S,\quad
P\not\equiv S,\quad
v\not\equiv S
```

---

## 3. Plano activo

```math
P=(X_P,\le_P,\partial P,\tau_P,M_P,\rho_P,\pi_P,\lambda_P,\kappa_P,\Omega_P)
```

```math
ST(P)=(X_P,T_P,\partial P,\le_P,\tau_P)
```

```math
T_P=\langle \le_P,\tau_P\rangle
```

```math
S_{\mathrm{EMQR}}(P)
=
E_P\times_{B_P}M_P\times_{B_P}Q_P\times_{B_P}R_P
```

```math
s_P=(e,m,q,r),
\qquad
e\in E_P,\;m\in M_P,\;q\in Q_P,\;r\in R_P
```

```math
\Gamma_P(e,m,q,r)\in\Omega_P
```

```math
s_P\;\mathrm{cerrado}
\iff
\Gamma_P(e,m,q,r)\in A_{\mathrm{abs}}(\rho_P)
```

```math
Val\Rightarrow P\Rightarrow ST(P)\Rightarrow S_{\mathrm{EMQR}}(P)\Rightarrow V^{n/\infty}_{\mathrm{EMQR}}
```

```math
\dim_{\mathrm{act}}(V)=n,
\qquad
\mathrm{Dim}_\delta(V)=\infty
```

---

## 4. Cardinalidades del plano

```math
E_P=\{e:e\;\mathrm{comparece\ como\ algo\ en}\;P\}
```

```math
M_P=(D_P,Rel_P,Inv_P,\circ_P,\sim_P,I_P)
```

```math
Q_P=(A_P,\Theta_P,\mu_P,\Pi_P,K_P,O_P,N_P)
```

```math
R_P=(\rho_P,\partial P,o_P,\tau_P,\ell_P,T_P)
```

```math
E_{\mathrm{ord}}\subsetneq E_P,
\qquad
M_{\mathrm{form}}\subsetneq M_P,
\qquad
Q_{\mathrm{fis}}\subsetneq Q_P,
\qquad
R_{\mathrm{fis}}\subsetneq R_P
```

```math
\Gamma_{\mathrm{mix}}(e,m,q,r)
=
\|\alpha_{EM}(e,m)-m\|
+
\|\alpha_{MQ}(m,q)-q\|
+
\|\alpha_{QR}(q,r)-r\|
+
\|\alpha_{RE}(r,e)-e\|
```

```math
\Gamma_P
=
\Gamma_E+\Gamma_M+\Gamma_Q+\Gamma_R+\Gamma_{\mathrm{mix}}
```

```math
\Gamma_P(e,m,q,r)=0
\Rightarrow
s_P\;\mathrm{compatible}
```

```math
\Gamma_P(e,m,q,r)\in A_{\mathrm{abs}}(\rho_P)
\Rightarrow
s_P\;\mathrm{admisible}
```

---

## 5. Totalidad y conmutatividad homotópica

```math
X=(F_X,S_X,\circ_X,\simeq_X,I_X,A_X,\partial X)
```

```math
\forall a,b\in F_X:
R_X(a,b)\in A_X
\Rightarrow
a\circ_X b\simeq_X b\circ_X a
```

```math
R_X(a,b)=\Delta_X(a\circ_X b,b\circ_X a)
```

```math
R_X(a,b)=0
\Rightarrow
a\circ_X b=b\circ_X a
```

```math
R_X(a,b)\in A_X
\Rightarrow
a\circ_X b\simeq_X b\circ_X a
```

```math
R_X(a,b)\notin A_X
\Rightarrow
a\circ_X b\not\simeq_X b\circ_X a
```

```math
\tau_X(a,b)=\inf_{\gamma\in\Gamma_X(a,b)}C_X(\gamma)
```

```math
\tau_X(a,b)=0
\iff
a\circ_X b=b\circ_X a
```

```math
0<\tau_X(a,b)<\tau_X^{crit}
\iff
a\circ_X b\simeq_X b\circ_X a
```

```math
\tau_X(a,b)\ge\tau_X^{crit}
\iff
(a,b)\in O_X
```

---

## 6. Polaridad 6D

```math
C_6(X,Y)
=
(L_{XY},P_{XY},Pr_{XY},Or_{XY},Int_{XY},Cl_{XY})
```

```math
X\neq Y,
\qquad
XCY\in S_{XY}
```

```math
R_C(X,Y)=\Delta_C(XCY,YCX)
```

```math
R_T(a,b)\in A_T
\Rightarrow
a\circ_T b\simeq_T b\circ_T a
```

```math
q:C_6(0,N)\to\mathbb{N}
```

```math
c:C_6(X,Y)\to\mathrm{TipoRel}(X/Y)
```

---

## 7. Identidad relacional

```math
I=\sum_{a\in A}I^a e_a\in H_\infty
```

```math
\langle I,J\rangle_{\mathrm{EMQR},\rho}
=
\sum_{a,b}I^aG^\rho_{ab}J^b
+
\langle\omega_I,\omega_J\rangle_{W,\rho}
+
\langle\mu_I,\mu_J\rangle_M
```

```math
I\perp_\rho J
\iff
\langle I,J\rangle_{\mathrm{EMQR},\rho}
=
0\pmod{A_{\mathrm{abs}}(\rho)}
```

```math
M_{\mathrm{real,eff}}(I)
=
\mathcal{I}\left(j_s^\infty\gamma_I,j_s^\infty b_I\right)
```

```math
j_s^\infty b_I
=
(b_I,\nabla_{\mathrm{Rel}}b_I,\nabla_{\mathrm{Rel}}^2b_I,\ldots)_s
```

```math
\nabla_{\mathrm{Rel}}b_{xy}
=
b_{xy}^{-1}\otimes_\rho db_{xy}+\Omega_{xy}
```

```math
M^{\mathrm{eff}}_{c,\rho,\mathrm{Rel}}(v)
=
M^{\mathrm{eff}}_{c,\rho}(v)
+
\alpha_{\mathrm{Rel}}\|\nabla_{\mathrm{Rel}}b_X\|^2
+
\beta_{\mathrm{Rel}}\|F^{\mathrm{Rel}}\|^2_{\mathrm{nabs}}
```

```math
Key(I)
=
(\tau(I),Bar_{\mathrm{Rel}}(I),Hol_{\mathrm{Rel}}(I),M_{\mathrm{real,eff}}(I))_{A_{\mathrm{abs}}}
```

```math
d_K(I,J)=dist_{\mathrm{Rel}}(Key(I),Key(J))
```

```math
d_K(I,J)\le\epsilon_K\pmod{A_{\mathrm{abs}}}
```

---

## 8. Entrelazamiento cuántico como carta regional

```math
Q_{c,\rho}:S\dashrightarrow H_{c,\rho}
```

```math
\rho_{AB}\in D(H_A\otimes H_B),
\qquad
\rho_A=\mathrm{tr}_B\rho_{AB},
\qquad
\rho_B=\mathrm{tr}_A\rho_{AB}
```

```math
\rho_{AB}\notin
\mathrm{Conv}\{\rho_A^{(k)}\otimes\rho_B^{(k)}\}_k
```

```math
\rho_{AB}
=
Q_{c,\rho}(R^{\mathrm{EMQR}}_{IJ})
+
\omega_Q
```

```math
\omega_Q\in A_{\mathrm{abs}}(\rho_Q)
```

```math
R^{\mathrm{EMQR}}_{IJ}\neq R_I\times R_J\pmod{A_{\mathrm{abs}}}
```

```math
\exists(c,\rho):
\Pi_{c,\rho}(R^{\mathrm{EMQR}}_{IJ})\in O^{\mathrm{nsep}}_{c,\rho}
```

```math
O^{\mathrm{nsep}}_{c,\rho}
=
\{\rho_{AB}:\rho_{AB}\;\mathrm{no\ separable}\}
```

---

## 9. Bit relacional

```math
b_{c,\rho}(x,y)
=
(\epsilon_{xy},\sigma_{xy},\omega_{xy},\kappa_{xy},\mu_{xy},\iota_{xy})
\in B^{\mathrm{Rel}}_\rho
```

```math
B^{\mathrm{Rel}}_\rho
=
\{0,1\}
\times
\{-1,0,1\}
\times
A_\rho
\times
[0,1]
\times
M
\times
[0,1]
```

```math
\pi_0:B^{\mathrm{Rel}}_\rho\to\{0,1\},
\qquad
\pi_0(b_{c,\rho}(x,y))=\epsilon_{xy}
```

```math
\mathrm{supp}(b_{c,\rho})
=
\{(x,y):\epsilon_{xy}=1,\kappa_{xy}>0,\omega_{xy}\in A_{\mathrm{abs}}(\rho)\}
```

```math
b_{xy}\otimes_\rho b_{yz}
=
(
\epsilon_{xy}\epsilon_{yz},
\sigma_{xy}\sigma_{yz},
\omega_{xy}\oplus\tau_{xy}^\ast\omega_{yz},
\min(\kappa_{xy},\kappa_{yz}),
\mu_{xy}\star\mu_{yz},
\iota_{xy}\iota_{yz}
)
```

```math
F^{\mathrm{Rel}}(x,y,z)
=
b_{xy}\otimes_\rho b_{yz}\ominus b_{xz}
```

```math
F^{\mathrm{Rel}}(x,y,z)\in A_{\mathrm{abs}}(\rho)
\Rightarrow
\mathrm{Transitividad}_{\mathrm{leg}}(x,y,z)
```

```math
(\partial_{\mathrm{Rel}}b)_{x_0\ldots x_k}
=
\sum_{r=0}^{k}(-1)^r b_{x_0\ldots\widehat{x_r}\ldots x_k}
```

```math
\partial_{\mathrm{Rel}}^2 b
=
F^{\mathrm{Rel}}\wedge b
```

```math
F^{\mathrm{Rel}}\in A_{\mathrm{abs}}
\Rightarrow
\partial_{\mathrm{Rel}}^2=0\pmod{A_{\mathrm{abs}}}
```

---

## 10. Homología, espectro e información relacional

```math
B_\rho=(b_{ij})_{i,j=1}^{n}
```

```math
W_{ij}
=
\epsilon_{ij}\kappa_{ij}\exp(-\|\omega_{ij}\|_{W,\rho})
```

```math
\Delta_{\mathrm{rel}}
=
D_W-W,
\qquad
(D_W)_{ii}=\sum_j W_{ij}
```

```math
H^{\mathrm{Rel}}_k(B_\rho)
=
\frac{\ker(\partial_{\mathrm{Rel}}:C^{\mathrm{Rel}}_k\to C^{\mathrm{Rel}}_{k-1})}
{\mathrm{Im}(\partial_{\mathrm{Rel}}:C^{\mathrm{Rel}}_{k+1}\to C^{\mathrm{Rel}}_k)+A^k_{\mathrm{abs}}}
```

```math
\beta^{\mathrm{Rel}}_k
=
\dim H^{\mathrm{Rel}}_k(B_\rho)
```

```math
S_{\mathrm{Rel}}(B_\rho)
=
-\mathrm{Tr}(\widetilde{W}\log\widetilde{W})
+
\|\Pi_{\mathrm{nabs}}F^{\mathrm{Rel}}\|^2
+
\sum_{i,j}dist^2(\omega_{ij},A_{\mathrm{abs}}(\rho))
```

```math
I_{\mathrm{Rel}}(A;B)
=
S_{\mathrm{Rel}}(A)+S_{\mathrm{Rel}}(B)-S_{\mathrm{Rel}}(A\cup B)
+
\|F^{\mathrm{Rel}}_{A,B}\|^2_{\mathrm{nabs}}
```

```math
D_{\mathrm{Rel}}
=
\partial_{\mathrm{Rel}}+\partial_{\mathrm{Rel}}^\ast+A_b
```

```math
A_b\psi(x)=\sum_y W_{xy}\sigma_{xy}\psi(y)
```

```math
\Delta_{\mathrm{rel}}
=
D_{\mathrm{Rel}}^2
=
\partial\partial^\ast+\partial^\ast\partial+
[\partial+\partial^\ast,A_b]+A_b^2
```

```math
\zeta_{\mathrm{Rel}}(s)
=
\mathrm{Tr}'((\Delta_{\mathrm{rel}}+\Pi_{\mathrm{nabs}})^{-s})
```

```math
\log T_{\mathrm{Rel}}
=
\frac12
\sum_k(-1)^k k\,\zeta'_{\mathrm{Rel},k}(0)
```

```math
\mathrm{Ind}_b
=
\dim\ker D_{\mathrm{Rel}}^+
-
\dim\ker D_{\mathrm{Rel}}^-
+
\mathrm{Tr}(e^{-t\Delta_{\mathrm{rel}}}\Pi_{\mathrm{nabs}})
```

---

## 11. Cubo de diferencia

```math
D_{XY}=\{d_1,\ldots,d_n\}
```

```math
Q^{(n)}_{XY}
=
\prod_{k=1}^{n}[0,d_k]
```

```math
\partial_k^\epsilon Q^{(n)}_{XY}
=
\{(a_1,\ldots,a_n):a_k=\epsilon d_k,\;0\le a_j\le d_j\}
```

```math
\Phi_k=\frac{\partial}{\partial d_k}+A^{\mathrm{Rel}}_k
```

```math
\langle\Phi_i,\Phi_j\rangle_{Q,\rho}
=
\delta_{ij}m_i+\Pi_{\mathrm{nabs}}\Omega_{ij}
```

```math
\partial_Q\sigma
=
\sum_{r=1}^{k}(-1)^{r-1}(\partial_r^1\sigma-\partial_r^0\sigma)
+
\Pi_{\mathrm{nabs}}(\Omega_\sigma\cap\sigma)
```

```math
\partial_Q^2\sigma
=
\Pi_{\mathrm{nabs}}
((d_{\mathrm{Rel}}\Omega_\sigma+
A^{\mathrm{Rel}}\wedge\Omega_\sigma-
\Omega_\sigma\wedge A^{\mathrm{Rel}})\cap\sigma)
```

```math
d_{\mathrm{Rel}}\Omega+[A^{\mathrm{Rel}},\Omega]\in A_{\mathrm{abs}}
```

```math
H^k_{Q,\mathrm{Rel}}(X,Y)
=
\frac{\ker(\partial_Q:C^Q_k\to C^Q_{k-1})}
{\mathrm{Im}(\partial_Q:C^Q_{k+1}\to C^Q_k)+A^k_{\mathrm{abs}}}
```

```math
o^{(k)}_{XY}
=
[\Pi_{\mathrm{nabs}}\Omega^{(k)}_{XY}]
\in
H^k_{Q,\mathrm{Rel}}(X,Y)
```

```math
\partial_Q h_{\mathrm{Th}}+h_{\mathrm{Th}}\partial_Q
=
o^{(k)}_{XY}+a,
\qquad
a\in A_{\mathrm{abs}}
```

---

## 12. Canal temporal ordinario

```math
\alpha=(c_\alpha,\rho_\alpha,P_\alpha)
```

```math
t_\alpha:P_\alpha\to T_\alpha
```

```math
AT(S)=
\{\alpha:c_{\alpha,\rho_\alpha}(S)\dashrightarrow P_\alpha,\;t_\alpha:P_\alpha\to T_\alpha\}
```

```math
\Gamma^\alpha_{IJ}:[t_0,t_1]\to ST(P_\alpha)
```

```math
v_\alpha=
\frac{d_\alpha(I,J)}{t_1-t_0}
```

---

## 13. Canal de fuente

```math
K^S_{IJ}
=
(Key(I),Key(J),A_{\mathrm{abs}},\omega_{IJ},b_{IJ},D_{\mathrm{Rel}})
```

```math
K^S_{IJ}\;\mathrm{existe}
\iff
d_K(I,J)\le\epsilon_K
\;\wedge\;
\exists t:\omega_{IJ}(t)\in A_{\mathrm{abs}}(\rho)
```

```math
v_S(K^S_{IJ})\;\mathrm{no\ definida}
```

```math
v^{\alpha}_{\mathrm{proj}}
=
\frac{d_\alpha(I,J)}{\Delta t_\alpha}
```

---

## 14. Canal transtemporal

```math
K^{\mathrm{trT}}_{IJ}
=
\{K^S_{IJ};\Pi_\alpha K^S_{IJ}\to T_\alpha\}_{\alpha\in AT(S)}
```

```math
\Theta_{\alpha\beta}(b^\alpha_{IJ}(t_\alpha))
=
b^\beta_{IJ}(t_\beta)
\pmod{A_{\mathrm{abs}}}
```

```math
\Omega^{\mathrm{trT}}_{\alpha\beta\gamma}
=
\Theta_{\gamma\alpha}\Theta_{\beta\gamma}\Theta_{\alpha\beta}
-
\mathrm{id}
```

```math
\Omega^{\mathrm{trT}}_{\alpha\beta\gamma}\in A_{\mathrm{abs}}
\Rightarrow
\mathrm{Cierre}_{\mathrm{trT}}(\alpha,\beta,\gamma)
```

```math
\mathrm{Comm}^{\mathrm{trT}}_{IJ}
=
D_{\mathrm{Rel}}
(
\{\Theta_{\alpha\beta}b^\alpha_{IJ}(t_\alpha)\}_{\alpha,\beta}
)
\pmod{A_{\mathrm{abs}}}
```

---

## 15. Termodinámica del cierre

```math
F^{\mathrm{Rel}}_{IJ}
=
E^{\mathrm{Rel}}_{IJ}
-
T_{ST}S^{\mathrm{Rel}}_{IJ}
+
\Lambda^\omega_{IJ}
```

```math
\Lambda^\omega_{IJ}
=
\lambda_\omega dist^2(\omega_{IJ},A_{\mathrm{abs}})
+
\lambda_F\|\Pi_{\mathrm{nabs}}F^{\mathrm{Rel}}_{IJ}\|^2
```

```math
\Delta F^{\mathrm{Rel}}_{IJ}\le 0
\;\wedge\;
\omega_{IJ}\in A_{\mathrm{abs}}(\rho)
\Rightarrow
\mathrm{Cierre}_{\mathrm{Th}}(I,J)
```

```math
\Sigma^{\mathrm{Rel}}_{IJ}
=
\frac{dS^{\mathrm{Rel}}_{IJ}}{dt}
-
\frac{\dot Q_{IJ}}{T_{ST}}
+
\zeta_\omega dist^2(\omega_{IJ},A_{\mathrm{abs}})
+
\zeta_F\|\Pi_{\mathrm{nabs}}F^{\mathrm{Rel}}_{IJ}\|^2
```

```math
\Sigma^{\mathrm{Rel}}_{IJ}=0
\Rightarrow
\mathrm{Proceso}_{\mathrm{rev}}(I,J)
```

```math
f_{\mathrm{Th}}(I)
=
\frac{1}{2\pi}
\left|
\frac{\partial F^{\mathrm{Rel}}}{\partial M_{\mathrm{real,eff}}(I)}
\right|_{\rho,S,\tau(I)}
```

```math
f^{\mathrm{Th}}_{ij}
=
gcd_{\mathrm{Rel}}(f_{\mathrm{Th}}(I_i),f_{\mathrm{Th}}(I_j))
+
\delta f^\tau_{ij}
+
\delta f^\omega_{ij}
```

```math
\omega_{ij}(t)
=
\omega^0_{ij}
+
A_{ij}\cos(2\pi f^{\mathrm{Th}}_{ij}t+\phi_{ij})
+
\eta_{ij}(t)
```

```math
b_{ij}(t)
=
\Theta(\epsilon_\rho-\|\Pi_{\mathrm{nabs}}\omega_{ij}(t)\|_{W,\rho})
```

```math
O_{ij}(t)=1-b_{ij}(t)
```

---

## 16. Principio variacional

```math
\gamma:[t_0,t_1]\to P_{\mathrm{Rel}},
\qquad
\gamma(t)=(I_i(t),I_j(t),\rho(t),\omega_{ij}(t),B_{ij}(t))
```

```math
\mathcal{A}_{ij}[\gamma]
=
\int_{t_0}^{t_1}
\left[
\frac12\|\nabla^{\mathrm{Rel}}_t\omega_{ij}\|^2_{W,\rho}
+
F^{\mathrm{Rel}}_{ij}
+
\alpha\|\Pi_{\mathrm{nabs}}F^{\mathrm{Rel}}_{ij}\|^2
+
\beta(\Sigma^{\mathrm{Rel}}_{ij})^2
\right]dt
```

```math
G_{ij}(\gamma)
=
dist_{\mathrm{Rel}}(Key(I_i(t)),Key(I_j(t)))
\in A_{\mathrm{abs}}
\quad
\forall t
```

```math
\nabla^{\mathrm{Rel},\ast}_t\nabla^{\mathrm{Rel}}_t\omega_{ij}
=
\nabla_\omega F^{\mathrm{Rel}}_{ij}
+
\alpha\nabla_\omega\|\Pi_{\mathrm{nabs}}F^{\mathrm{Rel}}_{ij}\|^2
+
\beta\nabla_\omega(\Sigma^{\mathrm{Rel}}_{ij})^2
+
\lambda_K\nabla_\omega dist^2_{\mathrm{Rel}}(Key_i,Key_j)
```

```math
\mathcal{M}_{rev}
=
\{
\gamma:
\Sigma^{\mathrm{Rel}}_{ij}=0,\;
\Pi_{\mathrm{nabs}}F^{\mathrm{Rel}}_{ij}=0,\;
\nabla^{\mathrm{Rel}}_t Key(I_i)-\nabla^{\mathrm{Rel}}_t Key(I_j)\in A_{\mathrm{abs}}
\}
```

```math
\langle\xi,J_{\gamma^\ast}\xi\rangle
\ge
c\|\xi\|^2
\Rightarrow
\mathrm{Estabilidad}_{\mathrm{ventanas}}(\gamma^\ast)
```

---

## 17. Tres niveles

```math
L_1(I,J)
=
\mathbf{1}[d_K(I,J)\le\epsilon_K]
```

```math
L_2(I,J;\rho)
=
\{b_{IJ}(t_n)\}_{n=1}^{N}
```

```math
L_3(I,J;\rho,D_{\mathrm{Rel}})
=
D_{\mathrm{Rel}}(\{b_{IJ}(t_n)\}_{n=1}^{N})
```

```math
\mathrm{Leg}(L_3)
\iff
L_1=1
\;\wedge\;
Stab(L_2)\ge s_{\min}
\;\wedge\;
\omega_D\in A_{\mathrm{abs}}
```

---

## 18. Modelo mínimo

```math
\chi_{12}=\Theta(\epsilon_K-d_{12})
```

```math
\omega_{12}(t)=\omega_0+A\cos(2\pi ft+\phi)
```

```math
A_{\mathrm{abs}}=[-\epsilon,\epsilon]
```

```math
b_{12}(t)
=
\Theta(\epsilon-|\omega_0+A\cos(2\pi ft+\phi)|)\chi_{12}
```

```math
D_{\mathrm{close}}(T)
=
\frac{1}{T}\int_0^T b_{12}(t)\,dt
```

Sea

```math
h=\frac{\epsilon-\omega_0}{A},
\qquad
\ell=\frac{-\epsilon-\omega_0}{A}
```

```math
D_{\mathrm{close}}^{cycle}
=
\frac{\arccos(\ell)-\arccos(h)}{\pi}
\quad
(-1\le\ell\le h\le 1)
```

```math
I_{\mathrm{cycle}}^{\mathrm{Rel}}
=
H(B)
-
H(B|K_1,K_2,\rho)
-
\|\Pi_{\mathrm{nabs}}F^{\mathrm{Rel}}\|^2
```

```math
D_{\mathrm{close}}>0
\iff
\chi_{12}=1
\;\wedge\;
\exists t:\omega_{12}(t)\in A_{\mathrm{abs}}
```

---

## 19. No señalización ordinaria

```math
p(a,b|x,y)
```

```math
\sum_b p(a,b|x,y)
=
\sum_b p(a,b|x,y')
\qquad
\forall a,x,y,y'
```

```math
\sum_a p(a,b|x,y)
=
\sum_a p(a,b|x',y)
\qquad
\forall b,y,x,x'
```

```math
S_{\mathrm{sig}}
=
\max
\left\{
\sup_{a,x,y,y'}
\left|
\sum_b p(a,b|x,y)-\sum_b p(a,b|x,y')
\right|,
\;
\sup_{b,y,x,x'}
\left|
\sum_a p(a,b|x,y)-\sum_a p(a,b|x',y)
\right|
\right\}
```

```math
S_{\mathrm{sig}}\le\epsilon_{\mathrm{ns}}
```

Modelos:

```math
M_0=\mathrm{corr}_{stat}
```

```math
M_{\mathrm{top}}=\mathrm{canal}_{fuente}+\mathrm{cierre}_{trT}
```

```math
M_{\mathrm{sig}}=\mathrm{signal}_{T_\alpha}
```

```math
\log\frac{\mathcal{L}(D|M_{\mathrm{top}})}{\mathcal{L}(D|M_0)}>\tau_0
```

```math
\log\frac{\mathcal{L}(D|M_{\mathrm{top}})}{\mathcal{L}(D|M_{\mathrm{sig}})}>\tau_1
```

```math
\Delta_{\mathrm{perm}}
=
\left|
\Gamma_{\mathrm{top}}(D)
-
\mathbb{E}_{\pi}\Gamma_{\mathrm{top}}(\pi D)
\right|
```

```math
Cert_{\mathrm{EMQR}}=1
\iff
\left[
\log\frac{\mathcal{L}(D|M_{\mathrm{top}})}{\mathcal{L}(D|M_0)}>\tau_0
\right]
\wedge
\left[
\log\frac{\mathcal{L}(D|M_{\mathrm{top}})}{\mathcal{L}(D|M_{\mathrm{sig}})}>\tau_1
\right]
\wedge
(S_{\mathrm{sig}}\le\epsilon_{\mathrm{ns}})
\wedge
(\Delta_{\mathrm{perm}}\ge\delta_{\min})
\wedge
(\omega_{\mathrm{fit}}\in A_{\mathrm{abs}})
```

---

## 20. Certificador

Entrada:

```math
D,\quad \mathcal{A}_T,\quad \epsilon_K,\quad \epsilon_{\mathrm{ns}},
\quad \tau_0,\tau_1,\quad \delta_{\min},\quad A_{\mathrm{abs}}
```

Salida:

```math
Cert_{\mathrm{EMQR}}\in\{0,1\}
```

Procedimiento:

```text
1. Estimar Key(I), Key(J).
2. Calcular d_K(I,J).
3. Rechazar si d_K(I,J) > epsilon_K.
4. Reconstruir omega_IJ(t) bajo carta de lectura.
5. Calcular b_IJ(t) = 1[omega_IJ(t) in A_abs].
6. Calcular D_close.
7. Calcular I_cycle^Rel.
8. Estimar p(a,b|x,y).
9. Calcular S_sig.
10. Ajustar M_0, M_top, M_sig.
11. Calcular log L(D|M_top)/L(D|M_0).
12. Calcular log L(D|M_top)/L(D|M_sig).
13. Permutar temporalmente D -> pi D.
14. Calcular Delta_perm.
15. Aceptar si se cumplen simultáneamente:
    d_K <= epsilon_K
    D_close > 0
    S_sig <= epsilon_ns
    L_top/L_0 > tau_0
    L_top/L_sig > tau_1
    Delta_perm >= delta_min
    omega_fit in A_abs
```

---

## 21. CTNet

```math
z_t=(a_t,r_t,m_t,\rho_t,\omega_t,B_t)
```

```math
B_t=(b_{ij,t})_{i,j}
```

```math
z_{t+1}
=
\Pi_{\mathrm{adm}}
\left(
U_\theta(z_t,u_t)
\oplus
R_\omega(z_t)
\oplus
\nabla_{\mathrm{Rel}}B_t
\right)
```

```math
B_{t+1}
=
\Pi^{B^{rel}}_{\rho_{t+1}}
\left(
U_B(B_t,z_t,u_t)
\oplus
d_M\omega_t
\oplus
F^{rel}_t
\right)
```

```math
\mathrm{Leg}(y_t)
\iff
m(y_t)\ge m_{\min}
\wedge
\omega_t\in A_{\mathrm{abs}}(\rho_t)
\wedge
F^{rel}_t\in A_{\mathrm{abs}}(\rho_t)
```

```math
\mathcal{L}_{CTNet}
=
\mathcal{L}_{task}
+
\alpha\|\Pi_{\mathrm{nabs}}\omega_t\|^2
+
\beta\|\Pi_{\mathrm{nabs}}F^{rel}_t\|^2
+
\gamma S_{\mathrm{sig}}
```

Invariantes de implementación:

```math
Inv_1:\quad
\omega_t\in A_{\mathrm{abs}}(\rho_t)\Rightarrow \mathrm{salida\ admisible}
```

```math
Inv_2:\quad
F^{rel}_t\in A_{\mathrm{abs}}(\rho_t)\Rightarrow \partial_{\mathrm{Rel}}^2=0\pmod{A_{\mathrm{abs}}}
```

```math
Inv_3:\quad
S_{\mathrm{sig}}\le\epsilon_{\mathrm{ns}}
```

```math
Inv_4:\quad
d_K(I,J)\le\epsilon_K
```

---

## 22. Inferencia estadística y falsabilidad

```math
H_0:
D\sim M_0
```

```math
H_1:
D\sim M_{\mathrm{top}}
```

```math
H_2:
D\sim M_{\mathrm{sig}}
```

```math
BF_{top/0}
=
\frac{p(D|M_{\mathrm{top}})}{p(D|M_0)}
```

```math
BF_{top/sig}
=
\frac{p(D|M_{\mathrm{top}})}{p(D|M_{\mathrm{sig}})}
```

```math
\log BF_{top/0}>\tau_0,
\qquad
\log BF_{top/sig}>\tau_1
```

```math
\mathrm{Falsacion}_1:
S_{\mathrm{sig}}>\epsilon_{\mathrm{ns}}
```

```math
\mathrm{Falsacion}_2:
d_K(I,J)>\epsilon_K
```

```math
\mathrm{Falsacion}_3:
D_{\mathrm{close}}=0
```

```math
\mathrm{Falsacion}_4:
\Delta_{\mathrm{perm}}<\delta_{\min}
```

```math
\mathrm{Falsacion}_5:
\omega_{\mathrm{fit}}\notin A_{\mathrm{abs}}
```

---

## 23. Predicciones formales

```math
P_1:
\exists\{t_n\}:
\omega_{IJ}(t_n)\in A_{\mathrm{abs}},
\qquad
\omega_{IJ}(t\notin\{t_n\})\notin A_{\mathrm{abs}}
```

```math
P_2:
\Theta_{\alpha\beta}(b^\alpha_{IJ})
=
b^\beta_{IJ}
\pmod{A_{\mathrm{abs}}}
```

```math
P_3:
d_K(I,J)>\epsilon_K
\Rightarrow
D_{\mathrm{close}}=0
```

```math
P_4:
D_{\mathrm{close}}>0
\not\Rightarrow
S_{\mathrm{sig}}>\epsilon_{\mathrm{ns}}
```

```math
P_5:
f^{\mathrm{Th}}_{IJ}
=
gcd_{\mathrm{Rel}}(f_{\mathrm{Th}}(I),f_{\mathrm{Th}}(J))
+
\delta f^\tau_{IJ}
+
\delta f^\omega_{IJ}
```

---

## 24. Límites degenerados

### 24.1 Señal clásica

```math
K^S_{IJ}\to\Gamma^\alpha_{IJ}
```

```math
A_{\mathrm{abs}}\to\{0\},
\qquad
\omega\to 0,
\qquad
v_S\to v_\alpha
```

### 24.2 Carta cuántica

```math
K^{trT}_{IJ}\to Q_{c,\rho}(R^{EMQR}_{IJ})
```

```math
b_{IJ}\to\rho_{AB}
```

```math
R^{EMQR}_{IJ}\neq R_I\times R_J
\mapsto
\rho_{AB}\notin\mathrm{Conv}\{\rho_A^{(k)}\otimes\rho_B^{(k)}\}_k
```

### 24.3 Estadística pura

```math
d_K(I,J)>\epsilon_K
```

```math
D_{\mathrm{close}}=0
```

```math
D\sim M_0
```

### 24.4 Pseudocanal

```math
D_{\mathrm{close}}>0
\wedge
S_{\mathrm{sig}}>\epsilon_{\mathrm{ns}}
\Rightarrow
M_{\mathrm{sig}}
```

```math
D_{\mathrm{close}}>0
\wedge
\Delta_{\mathrm{perm}}<\delta_{\min}
\Rightarrow
M_0
```

---

## 25. Teoremas

```math
T_1:
K^S_{IJ}\;\mathrm{no\ tiene\ velocidad\ fundamental}
```

Demostración formal:

```math
v=\frac{d}{\Delta t}
\quad\mathrm{requiere}\quad
\Gamma:[t_0,t_1]\to ST(P_\alpha)
```

```math
K^S_{IJ}
=
(Key(I),Key(J),A_{\mathrm{abs}},\omega_{IJ},b_{IJ},D_{\mathrm{Rel}})
```

```math
K^S_{IJ}\;\mathrm{no\ contiene}\;\Gamma
\Rightarrow
v_S(K^S_{IJ})\;\mathrm{indefinida}
```

```math
T_2:
\rho_{AB}\;\mathrm{no\ separable}
=
\Pi_Q(R^{EMQR}_{IJ})
\quad
\mathrm{si}
\quad
\omega_Q\in A_{\mathrm{abs}}
```

```math
T_3:
\mathrm{Comm}^{trT}_{IJ}
\not\Rightarrow
S_{\mathrm{sig}}>\epsilon_{\mathrm{ns}}
```

```math
T_4:
D_{\mathrm{close}}>0
\iff
d_K(I,J)\le\epsilon_K
\wedge
\exists t:\omega_{IJ}(t)\in A_{\mathrm{abs}}
```

```math
T_5:
F^{rel}\in A_{\mathrm{abs}}
\Rightarrow
\partial_{\mathrm{Rel}}^2=0\pmod{A_{\mathrm{abs}}}
```

```math
T_6:
d_{\mathrm{Rel}}\Omega+[A^{Rel},\Omega]\in A_{\mathrm{abs}}
\Rightarrow
\partial_Q^2=0\pmod{A_{\mathrm{abs}}}
```

---

## 26. Ecuación maestra

```math
S
\xdashrightarrow{c_\rho}
P
\Rightarrow
ST(P)
\Rightarrow
S_{\mathrm{EMQR}}(P)
\Rightarrow
Val
```

```math
I,J\in H_\infty
```

```math
Key(I),Key(J)
\Rightarrow
d_K(I,J)
```

```math
d_K(I,J)\le\epsilon_K
\Rightarrow
K^S_{IJ}
```

```math
K^S_{IJ}
=
(Key(I),Key(J),A_{\mathrm{abs}},\omega_{IJ},b_{IJ},D_{\mathrm{Rel}})
```

```math
K^{trT}_{IJ}
=
\{K^S_{IJ};\Pi_\alpha K^S_{IJ}\to T_\alpha\}_{\alpha\in AT(S)}
```

```math
\Theta_{\alpha\beta}(b^\alpha_{IJ}(t_\alpha))
=
b^\beta_{IJ}(t_\beta)
\pmod{A_{\mathrm{abs}}}
```

```math
\Omega^{trT}_{\alpha\beta\gamma}
\in
A_{\mathrm{abs}}
```

```math
\mathrm{Comm}^{trT}_{IJ}
=
D_{\mathrm{Rel}}
(
\{\Theta_{\alpha\beta}b^\alpha_{IJ}(t_\alpha)\}
)
\pmod{A_{\mathrm{abs}}}
```

---

## 27. API matemática mínima

### 27.1 Entrada

```text
I, J
rho
c
P
A_abs
epsilon_K
epsilon_ns
tau_0
tau_1
delta_min
D
```

### 27.2 Salida

```text
Key(I), Key(J)
d_K(I,J)
omega_IJ(t)
b_IJ(t)
D_close
I_cycle^Rel
S_sig
Delta_perm
Cert_EMQR
```

### 27.3 Funciones

```text
key(I) -> Key(I)
dist_key(Key(I), Key(J)) -> d_K
residual(I,J,rho,c,D) -> omega_IJ(t)
closure_bit(omega,A_abs) -> b(t)
closure_density(b,T) -> D_close
cycle_information(b,Key(I),Key(J),rho,FRel) -> I_cycle^Rel
signalling_score(p(a,b|x,y)) -> S_sig
fit_models(D) -> L_0,L_top,L_sig
temporal_permutation(D) -> Delta_perm
certify(...) -> {0,1}
```

---

## 28. Estructura de implementación

```text
src/emqr/core.py
    Source
    Chart
    Regime
    ActivePlane
    Residual
    AbsorbableDomain

src/emqr/identity.py
    Identity
    EffectiveMass
    TopologicalKey
    KeyMetric

src/emqr/relbit.py
    RelationalBit
    RelationalBitField
    RelationalCurvature
    RelationalBoundary

src/emqr/channel.py
    SourceChannel
    TemporalChart
    TranstemporalChannel
    AtlasCoherence

src/emqr/thermo.py
    RelationalFreeEnergy
    EntropyProduction
    ClosureFrequency
    OscillatoryResidual

src/emqr/certifier.py
    SignallingScore
    LikelihoodComparison
    PermutationStability
    EMQRCertifier

src/emqr/ctnet.py
    CTNetState
    CTNetUpdate
    AdmissibilityProjector
    CTNetLoss

tests/
    test_axioms.py
    test_relbit.py
    test_source_channel.py
    test_no_signalling.py
    test_minimal_model.py
    test_certifier.py
```

---

## 29. Archivos del bloque

```text
entrelazamiento_emqr_transtemporal.pdf
    canal de fuente
    comunicación transtemporal
    cierre relacional
    certificador contra falsa señalización
    modelo mínimo
    CTNet

main-19.pdf
    canal topológico atemporal
    ortogonalidad termodinámica
    cubo de diferencia
    capacidad relacional
    certificador total

main_actualizado.pdf
    monografía EMQR-CTNet
    primitivas
    bit relacional
    CTNet
    auditoría multicarta
    teoremas de cierre

conmutatividad_interaccion_irreducible.pdf
    totalidad
    conmutatividad homotópica
    residuo absorbible
    frontera de ruptura

emqr_plano_estado_variedad_revtex.pdf
    plano activo
    espacio-tiempo local
    producto cardinal EMQR
    variedad n/infinito

algebra_polaridad_6d_integracion_total_revtex.pdf
    polaridad 6D
    diferencia X/Y
    inscripción relacional
    hipercubo funcional
```

---

## 30. Criterio de aceptación de una ejecución

```math
Accept(D)=1
```

si y sólo si:

```math
d_K(I,J)\le\epsilon_K
```

```math
D_{\mathrm{close}}>0
```

```math
S_{\mathrm{sig}}\le\epsilon_{\mathrm{ns}}
```

```math
\log\frac{\mathcal{L}(D|M_{\mathrm{top}})}{\mathcal{L}(D|M_0)}>\tau_0
```

```math
\log\frac{\mathcal{L}(D|M_{\mathrm{top}})}{\mathcal{L}(D|M_{\mathrm{sig}})}>\tau_1
```

```math
\Delta_{\mathrm{perm}}\ge\delta_{\min}
```

```math
\omega_{\mathrm{fit}}\in A_{\mathrm{abs}}
```

```math
\Omega^{trT}_{\alpha\beta\gamma}\in A_{\mathrm{abs}}
```

```math
F^{rel}\in A_{\mathrm{abs}}
```

---

## 31. Firma compacta

```math
\boxed{
\mathrm{Ent}_{\mathrm{EMQR}}
=
\left[
R^{EMQR}_{IJ}\neq R_I\times R_J
\pmod{A_{\mathrm{abs}}}
\right]
\wedge
\left[
\exists(c,\rho):\Pi_{c,\rho}(R^{EMQR}_{IJ})\in O^{nsep}_{c,\rho}
\right]
}
```

```math
\boxed{
K^S_{IJ}
=
(Key(I),Key(J),A_{\mathrm{abs}},\omega_{IJ},b_{IJ},D_{\mathrm{Rel}})
}
```

```math
\boxed{
K^{trT}_{IJ}
=
\{K^S_{IJ};\Pi_\alpha K^S_{IJ}\to T_\alpha\}_{\alpha\in AT(S)}
}
```

```math
\boxed{
\mathrm{Comm}^{trT}_{IJ}
=
D_{\mathrm{Rel}}
(
\{\Theta_{\alpha\beta}b^\alpha_{IJ}(t_\alpha)\}
)
\pmod{A_{\mathrm{abs}}}
}
```

```math
\boxed{
Cert_{\mathrm{EMQR}}
=
1
\iff
d_K\le\epsilon_K
\wedge
D_{\mathrm{close}}>0
\wedge
S_{\mathrm{sig}}\le\epsilon_{\mathrm{ns}}
\wedge
BF_{top/0}>\tau_0
\wedge
BF_{top/sig}>\tau_1
\wedge
\Delta_{\mathrm{perm}}\ge\delta_{\min}
\wedge
\omega_{\mathrm{fit}}\in A_{\mathrm{abs}}
}
```