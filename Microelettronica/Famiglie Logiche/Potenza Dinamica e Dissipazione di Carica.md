La **potenza dinamica $P_d$** rappresenta l'energia consumata da una porta logica esclusivamente durante le commutazioni di stato ($0 \to 1$ e $1 \to 0$). A clock fermo ($f = 0$), la potenza dinamica è nulla.

---

### 1. Il Calcolo dell'Energia Erogata dall'Alimentatore

Durante una transizione da Basso ad Alto ($0 \to 1$), il transistor di pull-up collega l'uscita a $V_{DD}$ per caricare la [capacità parassita di carico](../Dispositivi%20e%20Componenti/Capacit%C3%A0%20parassite%20nel%20MOSFET.md) $C$.

L'alimentatore lavora a **potenziale fisso $V_{DD}$** ed eroga una carica totale $Q = C \cdot (V_{OH} - V_{OL})$:

$$E_{\text{alim}} = \int_0^\infty V_{DD} \cdot i(t) \, dt = V_{DD} \int_0^Q dq = V_{DD} \cdot Q = C \cdot V_{DD} \cdot (V_{OH} - V_{OL})$$

Nel caso ideale (es. CMOS) con $V_{OL} \approx 0\text{ V}$ e $V_{OH} \approx V_{DD}$:
$$E_{\text{alim}} = C \cdot V_{DD}^2$$

---

### 2. L'Energia Immagazzinata nel Condensatore ($E_C$)

Mentre il [condensatore](../Dispositivi%20e%20Componenti/Condensatori.md) si carica, la sua tensione ai capi $v_C(t)$ non è costante: parte da $0\text{ V}$ e sale gradualmente fino a $V_{DD}$. L'energia effettivamente immagazzinata nel suo campo elettrostatico a fine carica vale:

$$E_C = \int_0^\infty v_C(t) \cdot i(t) \, dt = C \int_0^{V_{DD}} v_C \, dv_C = \mathbf{\frac{1}{2} C V_{DD}^2}$$

> **Il dilemma del 50%:**  
> L'alimentatore eroga $C V_{DD}^2$, ma nel condensatore ne entra solo la metà ($\frac{1}{2} C V_{DD}^2$).  
> Il restante **$50\%$ dell'energia viene inevitabilmente dissipato in calore per effetto Joule** durante la fase di carica.

---

### 3. Perché la Resistenza si Cancella nei Conti?

Dimostrazione del perché la perdita del $50\%$ non dipende dal valore della resistenza di canale $R$ del transistor di pull-up:

1. La corrente di carica vale $i(t) = \frac{V_{DD}}{R} e^{-t/RC}$.
2. L'energia dissipata sulla resistenza vale:
   $$E_R = \int_0^\infty R \cdot [i(t)]^2 \, dt = R \int_0^\infty \left( \frac{V_{DD}}{R} e^{-\frac{t}{RC}} \right)^2 dt = \frac{V_{DD}^2}{R} \int_0^\infty e^{-\frac{2t}{RC}} dt$$
3. Risolvendo l'integrale definito:
   $$\int_0^\infty e^{-\frac{2t}{RC}} dt = \frac{RC}{2} \implies E_R = \frac{V_{DD}^2}{\cancel{R}} \cdot \frac{\cancel{R} C}{2} = \mathbf{\frac{1}{2} C V_{DD}^2}$$

* Se il transistor è **molto conduttivo ($R$ piccola)**: la corrente di picco è enorme, ma il tempo di carica è brevissimo $\implies$ energia dissipata $= \frac{1}{2} C V_{DD}^2$.
* Se il transistor è **poco conduttivo ($R$ grande)**: la corrente è debole, ma il tempo di carica è lungo $\implies$ energia dissipata $= \frac{1}{2} C V_{DD}^2$.

---

### 4. Bilancio su Ciclo Completo e Formula di $P_d$

* **Transizione $0 \to 1$ (Carica):** l'alimentatore spende $C V_{DD}^2$; metà va in calore sul pull-up, metà resta immagazzinata in $C$.
* **Transizione $1 \to 0$ (Scarica):** l'alimentatore non eroga nulla; la metà immagazzinata ($\frac{1}{2} C V_{DD}^2$) viene interamente dissipata in calore sul transistor di pull-down che scarica a massa.
* **Per ogni ciclo completo ($0 \to 1 \to 0$):** l'energia prelevata è $E_{\text{ciclo}} = C V_{DD}^2$ e viene **dissipata al 100% in calore**.

Moltiplicando per la frequenza di commutazione $f = \frac{\alpha}{T}$ (con $\alpha$ fattore di attività e $T$ periodo di clock):

$$P_d = C \cdot V_{DD}^2 \cdot f$$

---

*Pagine correlate:*
- [Famiglia Logica e Costo per Bit](./Famiglia%20Logica%20e%20Costo%20per%20Bit.md)
- [Caratteristica di Trasferimento e Rigenerazione](./Caratteristica%20di%20Trasferimento%20e%20Rigenerazione.md)
- [Soglia Logica e Margine di Rumore](./Soglia%20Logica%20e%20Margine%20di%20Rumore.md)
- [Capacità parassite nel MOSFET](../Dispositivi%20e%20Componenti/Capacit%C3%A0%20parassite%20nel%20MOSFET.md)
- [Condensatori](../Dispositivi%20e%20Componenti/Condensatori.md)
- [Analogico non si scende di dimensioni](../Scaling%20e%20Limiti%20Fisici/Analogico%20non%20si%20scende%20di%20dimensioni.md)
- [Difficoltà nel fare un componente ideale](../Scaling%20e%20Limiti%20Fisici/Difficolt%C3%A0%20nel%20fare%20un%20componente%20ideale.md)
