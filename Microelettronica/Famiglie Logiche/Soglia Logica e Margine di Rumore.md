La **Soglia Logica $V_M$** (o punto di commutazione) è il punto sulla [caratteristica di trasferimento](./Caratteristica%20di%20Trasferimento%20e%20Rigenerazione.md) in cui la tensione di uscita eguaglia esattamente la tensione di ingresso:

$$V_O = V_I = V_M$$

Graficamente corrisponde all'intersezione tra la curva di trasferimento $V_O = f(V_I)$ e la retta bisettrice $V_O = V_I$.

---

### 1. Il Bivio Decisionale e la Regione di Transizione

Il punto $V_M$ è il **punto di equilibrio instabile** (lo "spartiacque"):
* **Se $V_I > V_M$ (a destra della soglia):** l'uscita viene spinta verso il livello logico basso ($V_O \to V_{OL}$).
* **Se $V_I < V_M$ (a sinistra della soglia):** l'uscita viene spinta verso il livello logico alto ($V_O \to V_{OH}$).

#### Stato dei Transistor nella Regione di Transizione
Nella regione compresa nell'intervallo proibito tra i punti ad alto guadagno ($V_{ILM} < V_I < V_{IHM}$):
* I transistor **non sono spenti**: sono entrambi attivi e in **forte conduzione**.
  * Nei [MOS](../Dispositivi%20e%20Componenti/MOS.md) sia il PMOS che l'NMOS si trovano contemporaneamente in **saturazione MOS** (canale strozzato, forte transconduttanza).
  * Nei [BJT](../Dispositivi%20e%20Componenti/BJT.md) il transistore lavora in **zona attiva diretta** ($\Delta I_C = \beta_0 \Delta I_B$).
* In questa finestra scorre il **picco massimo di corrente istantanea** dall'alimentazione alla massa, con la massima potenza istantanea dissipata.

---

### 2. Il "Burrone" della Curva ed Esplosione del Rumore (Esempio RTL)

Nelle zone esterne piatte il guadagno differenziale è quasi nullo ($|A_v| < 1$, che funge da ammortizzatore). Ma nel ristretto intervallo della transizione il guadagno in modulo **esplode**.

Prendendo l'inverter RTL reale ($V_{CC} = 3\text{ V}$, $R_B = 450\ \Omega$, $R_C = 640\ \Omega$):
* $V_{ILM} = 553\text{ mV}$ (punto a pendenza $|A_v| = 1$)
* $V_{IHM} = 734\text{ mV}$ (punto a pendenza $|A_v| = 1$)
* Nel millimetro di spazio tra $0.553\text{ V}$ e $0.734\text{ V}$, il guadagno differenziale di picco vale:
  $$A_v = -\frac{\beta_0 R_C}{r_{be} + R_B} \approx \mathbf{-40}$$

```
V_O ^
    │ ──── (V_OH ≈ 3V)  [|Av| < 1 : rumore abbattuto]
    │      \
    │       \  <-- "BURRONE" (0.553V - 0.734V): |Av| ≈ 40
    │        \     Un piccolo disturbo viene amplificato x 40!
    │         \
    │          └──────── (V_OL ≈ 0.1V) [|Av| < 1 : rumore abbattuto]
    └─────────────────────────────> V_I
            V_ILM  V_IHM
           (553mV)(734mV)
```

> **Il pericolo dell'ambiguità:** se il segnale cade nella regione proibita a cavallo di $V_M$, basta un **minimo disturbo di rumore $\Delta V$** per decidere il destino del dato:
> * Se il segnale era a destra di $V_M$ e un disturbo lo spinge a sinistra di $V_M$, il guadagno elevato ($\times 40$) amplifica l'errore e fa saturare l'uscita allo stato logico opposto, causando un **bit flip irreversibile** (dato corrotto).

---

### 3. Asimmetria della Curva e Margine di Immunità ai Disturbi ($NM$)

Il **Margine di Rumore ($NM$)** quantifica la massima ampiezza di rumore tollerabile all'ingresso prima che una porta interpreti erroneamente il dato:
$$NM_H = V_{OHm} - V_{IHm}$$
$$NM_L = V_{ILM} - V_{OLM}$$
$$NM = \min\{NM_L, NM_H\}$$

* **Caso Ideale Simmetrico:** la caratteristica è centrata a metà dinamica ($V_M = V_{DD}/2$), garantendo il massimo margine possibile:
  $$NM = NM_L = NM_H = \frac{V_{DD}}{2}$$
* **Caratteristica Asimmetrica (come in RTL):** 
  * Poiché il BJT commuta quando la tensione di base supera la soglia di conduzione della giunzione ($V_M \approx V_{BE,on} \approx 0.7\text{ V}$), la curva è fortemente spostata a sinistra rispetto a $V_{CC}/2 = 1.5\text{ V}$.
  * Con $V_{ILM} = 553\text{ mV}$ e $V_{OLM} = 169\text{ mV}$, il margine sul livello basso crolla:
    $$NM_L = 553\text{ mV} - 169\text{ mV} = \mathbf{384\text{ mV}}$$
  * Al contrario, $NM_H = 2.97\text{ V} - 0.734\text{ V} = \mathbf{2.24\text{ V}}$.
  * Poiché $NM = \min\{NM_L, NM_H\}$, **l'asimmetria abbatte il margine di rumore complessivo** a soli $384\text{ mV}$.

---

*Pagine correlate:*
- [HTL (High-Threshold Logic)](./HTL%20%28High-Threshold%20Logic%29.md)
- [TTL (Transistor-Transistor Logic)](./TTL%20%28Transistor-Transistor%20Logic%29.md)
- [DTL (Diode-Transistor Logic)](./DTL%20%28Diode-Transistor%20Logic%29.md)
- [ECL (Emitter-Coupled Logic)](./ECL%20%28Emitter-Coupled%20Logic%29.md)
- [RTL e Prodotto Ritardo-Consumo (PDP)](./RTL%20e%20Prodotto%20Ritardo-Consumo%20%28PDP%29.md)
- [Famiglia Logica e Costo per Bit](./Famiglia%20Logica%20e%20Costo%20per%20Bit.md)
- [Potenza Dinamica e Dissipazione di Carica](./Potenza%20Dinamica%20e%20Dissipazione%20di%20Carica.md)
- [Caratteristica di Trasferimento e Rigenerazione](./Caratteristica%20di%20Trasferimento%20e%20Rigenerazione.md)
- [BJT](../Dispositivi%20e%20Componenti/BJT.md)
- [MOS](../Dispositivi%20e%20Componenti/MOS.md)
- [Analogico non si scende di dimensioni](../Scaling%20e%20Limiti%20Fisici/Analogico%20non%20si%20scende%20di%20dimensioni.md)
- [Difficoltà nel fare un componente ideale](../Scaling%20e%20Limiti%20Fisici/Difficolt%C3%A0%20nel%20fare%20un%20componente%20ideale.md)
