### La formula classica di $V_{th}$ (Teoria 1D a canale lungo)

In teoria, nella formula classica monodimensionale a canale lungo, la tensione di soglia **non dipende né da $W$ né da $L$**:

$$V_{th0} = V_{FB} + 2\phi_F + \frac{\sqrt{2 q \varepsilon_{si} N_A (2\phi_F)}}{C_{ox}}$$

Dove:
* $V_{FB}$ (*Flat-Band Voltage*): potenziale dovuto alla differenza di lavoro d'estrazione metallo-semiconduttore e alle cariche fisse nell'ossido $Q_{ox}$.
* $2\phi_F = 2 V_T \ln\left(\frac{N_A}{n_i}\right)$: potenziale di Fermi necessario per raggiungere la forte inversione.
* $\frac{\sqrt{2 q \varepsilon_{si} N_A (2\phi_F)}}{C_{ox}} = \frac{Q_{dep}}{C_{ox}}$: termine associato alla carica della zona di svuotamento che il Gate deve sostenere nel silicio prima di creare il canale.

---

### Cosa succede quando scendiamo di dimensioni?

Quando rimpiccioliamo le dimensioni del MOS intervengono **due fenomeni distinti**:

#### 1. La variabilità statistica di processo (Legge di Pelgrom & RDF)
Anche se due transistor sono disegnati con la stessa geometria nominale, a causa del numero finito di atomi di drogante nel canale (*Random Dopant Fluctuation - RDF*), la tensione di soglia presenta una dispersione statistica $\sigma$:

$$\sigma(\Delta V_{th}) = \frac{A_{Vth}}{\sqrt{W \cdot L}}$$

Più l'area $W \cdot L$ è piccola, più le asimmetrie tra transistor vicini diventano enormi.

---

#### 2. L'abbassamento deterministico della soglia nominale ($V_{th}$ Roll-Off)
Quando scendiamo con la lunghezza $L$, le sacche di svuotamento delle giunzioni PN di Source e Drain si estendono lateralmente nel canale.
Queste sacche svuotano già parte del canale: il Gate deve fare **meno sforzo** per invertire la superficie, quindi la tensione di soglia nominale **scende al calare di $L$**.

👉 Approfondimento: [$V_{th}$ Roll-Off](./Effetti%20di%20canale%20corto/Vth%20roll%20off.md)

---

#### 3. L'effetto del potenziale di Drain (DIBL)
Nei canali corti, la tensione applicata al Drain abbassa ulteriormente la barriera di potenziale:
$$V_{th}(V_{DS}) = V_{th0} - \eta V_{DS}$$

👉 Approfondimento: [DIBL](./Effetti%20di%20canale%20corto/DIBL.md)

---
*Pagine correlate:*
- [MOS](../Tecnologie/MOS.md)
- [Analogico non si scende di dimensioni](./Analogico%20non%20si%20scende%20di%20dimensioni.md)
- [Vth roll off](./Effetti%20di%20canale%20corto/Vth%20roll%20off.md)
- [DIBL](./Effetti%20di%20canale%20corto/DIBL.md)
