L'**Invertitore CMOS** è costituito da una coppia complementare formata da un transistore ad arricchimento a canale n ([NMOS](../Dispositivi%20e%20Componenti/MOS.md), $M_n$) collegato a massa e un transistore a canale p (PMOS, $M_p$) collegato all'alimentazione $V_{DD}$, con gate e drain cortocircuitati rispettivamente all'ingresso ($V_I$) e all'uscita ($V_O$).

Per analizzare la [Caratteristica Statica di Trasferimento (VTC)](./Caratteristica%20di%20Trasferimento%20e%20Rigenerazione.md) si traccia prima la **mappa bidimensionale delle regioni di funzionamento** nel piano $(V_I, V_O)$, ricavando poi la traiettoria percorsa dall'invertitore al variare della tensione d'ingresso.

---

### 1. La Mappa delle Regioni nel Piano $(V_I, V_O)$

Nel piano compreso tra $0$ e $V_{DD}$ su entrambi gli assi, le regioni di polarizzazione simultanea di $M_n$ ed $M_p$ sono delimitate da **quattro rette di confine fisico**:

```
      Vo ^
         │ [n-off, p-lin]   / [n-sat, p-lin]  / [n-sat, p-off]
     VDD ├─────────┐───────/─────────────────/────────┐
         │         │      /                 /  (sat)  │
         │         │     /  Vo = VI + VTp  /          │
         │ (lin)   │    /                 /           │
         │         │   /  ┌─────────────┐/            │
         │         │  /   │ n-sat,p-sat │             │
         │         │ /    │ (commutaz.) │/            │
         │         │/     └─────────────/             │
         │         /                   /              │
         │        /                   / (lin)         │
     VTp ├───────/                   /                │
         │      /  Vo = VI - VTn    /                 │
         │ (sat)                   /                  │
         │ [n-off, p-sat]         / [n-lin, p-sat]    │ [n-lin, p-off]
       0 └─────────┴─────────────┴────────────────────┴─────> VI
         0        VTn          VDD-VTp               VDD
```

#### Condizioni di Demarcazione per $M_n$ (NMOS a massa)
Dato che il source è a massa ($V_{Sn} = 0$), le tensioni terminali valgono $V_{GSn} = V_I$ e $V_{DSn} = V_O$:
* **Confine di Conduzione (Interdizione / Accensione):**
  $$V_{GSn} = V_{Tn} \implies \mathbf{V_I = V_{Tn}}$$
  * A sinistra ($V_I < V_{Tn}$): $M_n$ è **spento (off)**.
  * A destra ($V_I > V_{Tn}$): $M_n$ è **acceso**.
* **Confine di Strozzamento (Lineare / Saturazione):**
  $$V_{DSn} = V_{GSn} - V_{Tn} \implies \mathbf{V_O = V_I - V_{Tn}}$$
  * Al di sopra ($V_O > V_I - V_{Tn}$): $M_n$ è in **Saturazione (sat)**.
  * Al di sotto ($V_O < V_I - V_{Tn}$): $M_n$ è in **Regione Lineare/Triodo (lin)**.

#### Condizioni di Demarcazione per $M_p$ (PMOS a $V_{DD}$)
Dato che il source è collegato a $V_{DD}$ ($V_{Sp} = V_{DD}$), le tensioni valgono $V_{SGp} = V_{DD} - V_I$ e $V_{SDp} = V_{DD} - V_O$:
* **Confine di Conduzione (Interdizione / Accensione):**
  $$V_{SGp} = V_{Tp} \iff V_{DD} - V_I = V_{Tp} \implies \mathbf{V_I = V_{DD} - V_{Tp}}$$
  * A destra ($V_I > V_{DD} - V_{Tp}$): $M_p$ è **spento (off)**.
  * A sinistra ($V_I < V_{DD} - V_{Tp}$): $M_p$ è **acceso**.
* **Confine di Strozzamento (Lineare / Saturazione):**
  $$V_{SDp} = V_{SGp} - V_{Tp} \iff V_{DD} - V_O = V_{DD} - V_I - V_{Tp} \implies \mathbf{V_O = V_I + V_{Tp}}$$
  * Al di sopra ($V_O > V_I + V_{Tp}$, ovvero $V_{SDp} < V_{SGp} - V_{Tp}$): $M_p$ è in **Regione Lineare/Triodo (lin)**.
  * Al di sotto ($V_O < V_I + V_{Tp}$, ovvero $V_{SDp} > V_{SGp} - V_{Tp}$): $M_p$ è in **Saturazione (sat)**.

---

### 2. La Regola dell'Interruttore: Perché a Riposo è Lineare e NON Saturo?

Uno degli errori più frequenti nell'analisi qualitativa dei circuiti logici MOS è confondere la saturazione con la piena conduzione:

> [!IMPORTANT]
> **Nei transistori MOS, un interruttore chiuso opera in ZONA LINEARE, mai in saturazione.**
> * **Interruttore chiuso:** un transistore che conduce e collega saldamente l'uscita al proprio terminale di alimentazione ha una caduta di potenziale ai suoi capi quasi nulla ($V_{DS} \approx 0$ o $V_{SD} \approx 0$). Trovandosi all'origine della caratteristica $I_D - V_{DS}$, si comporta come una resistenza equivalente piccolissima ($R_{on}$): è in **ZONA LINEARE**.
> * **Saturazione:** richiede invece una caduta $V_{DS}$ (o $V_{SD}$) elevata, sufficiente a svuotare e strozzare il canale all'estremità di drain ($V_{DS} > V_{GS} - V_{T}$), comportandosi come un generatore di corrente controllato in tensione.

---

### 3. La Sequenza delle 5 Regioni lungo la VTC

Nel funzionamento statico dell'inverter a vuoto, i due transistori sono posti rigorosamente in serie:
$$I_{DSn} = I_{SDp}$$

Aumentando $V_I$ in modo continuo da $0$ a $V_{DD}$, la tensione di uscita $V_O$ scende dal livello logico alto ($V_{DD}$) al livello logico basso ($0$). La curva attraversa **5 regioni di funzionamento** in un ordine univoco:

```
(Vo = VDD)  In alto:    n-off, p-lin
               │
               ▼
            Discesa:    n-sat, p-lin
               │
               ▼
            Centro:     n-sat, p-sat   <-- Max Guadagno (|Av| >> 1)
               │
               ▼
            Fondo:      n-lin, p-sat
               │
               ▼
(Vo = 0V)   In basso:   n-lin, p-off
```

| Regione | Intervallo di Ingresso $V_I$ | Stato $M_n$ | Stato $M_p$ | Equazione Correnti e Tensione $V_O$ |
| :--- | :--- | :---: | :---: | :--- |
| **1. Tratto Alto** | $0 \le V_I \le V_{Tn}$ | **OFF** | **LIN** | $I_{DSn} = 0 \implies I_{SDp} = 0 \implies V_{SDp} = 0 \implies \mathbf{V_O = V_{DD}}$ |
| **2. Transizione Alta** | $V_{Tn} < V_I < V_{IS}$ | **SAT** | **LIN** | $I_{DSn,\text{sat}}(V_I) = I_{SDp,\text{lin}}(V_I, V_O) \implies V_O$ decresce |
| **3. Commutazione** | $V_I = V_{IS} \approx \frac{V_{DD}}{2}$ | **SAT** | **SAT** | Entrambi in pinch-off: tratto verticale a pendenza massima ($|A_v| \gg 1$) |
| **4. Transizione Bassa** | $V_{IS} < V_I < V_{DD} - V_{Tp}$ | **LIN** | **SAT** | $I_{DSn,\text{lin}}(V_I, V_O) = I_{SDp,\text{sat}}(V_I) \implies V_O$ scende verso $0$ |
| **5. Tratto Basso** | $V_{DD} - V_{Tp} \le V_I \le V_{DD}$ | **LIN** | **OFF** | $I_{SDp} = 0 \implies I_{DSn} = 0 \implies V_{DSn} = 0 \implies \mathbf{V_O = 0}$ |

👉 Approfondimento sulla soglia logica $V_{IS} \equiv V_M$ e il calcolo del guadagno di commutazione: [Soglia Logica e Margine di Rumore](./Soglia%20Logica%20e%20Margine%20di%20Rumore.md).

---

### 4. Perché le Regioni $[n\text{-off}, p\text{-sat}]$ e $[n\text{-sat}, p\text{-off}]$ Non Fanno Parte della VTC?

Nel diagramma a colori compaiono anche due regioni "anomale":
* In basso a sinistra: **$n\text{-off}, p\text{-sat}$** (giallo)
* In alto a destra: **$n\text{-sat}, p\text{-off}$** (giallo)

Queste zone **non appartengono mai alla caratteristica statica** per un vincolo di consistenza elettrica:
1. Se un transistore è in interdizione (off), la sua corrente di canale è rigorosamente nulla ($I = 0$).
2. Affinché l'altro transistore si trovi in saturazione con canale acceso, la sua corrente dovrebbe valere:
   $$I = \frac{k}{2}(V_{GS} - V_T)^2 > 0$$
3. Poiché i dispositivi sono in serie, la legge di Kirchhoff per le correnti renderebbe incompatibili $I = 0$ e $I > 0$.

Di conseguenza, il punto di lavoro a circuito aperto deve necessariamente attestarsi nella regione in cui il transistore acceso è in **zona lineare con caduta nulla** ($V_{DS}=0$ oppure $V_{SD}=0$), dove una corrente $I = 0$ è pienamente compatibile.

---

### 5. Guadagno e Temperatura: Perché all'Aumentare di $T$ il Guadagno Scende?

Nella regione di commutazione ($V_I = V_{IS} \equiv V_M$, regione 3), entrambi i transistori sono in saturazione. Il guadagno differenziale di piccolo segnale vale:
$$|A_v| = \frac{g_{mn} + g_{mp}}{g_{dsn} + g_{dsp}} = (g_{mn} + g_{mp}) \cdot (r_{on} \parallel r_{op})$$

All'aumentare della temperatura $T$:
1. **Crollo della mobilità ($\mu$):** A causa dell'aumento dello scattering termico fononico con il reticolo di silicio (*lattice scattering*), la mobilità decade rapidamente:
   $$\mu(T) \propto T^{-m} \quad (m \approx 1.5 \div 2.0)$$
2. **Crollo della transconduttanza ($g_m$):** Sebbene la tensione di soglia $|V_T|$ si riduca leggermente con la temperatura (circa $-1 \div -2\text{ mV/K}$), l'effetto della mobilità è nettamente predominante:
   $$g_m \approx \mu C_{ox} \frac{W}{L} (V_{GS} - V_T)$$
   Di conseguenza $g_m$ cala fortemente con $T$.
3. **Effetto sulla caratteristica:** La transizione da alto a basso nel tratto centrale diventa meno ripida (la curva si "sdraia" leggermente): **il guadagno in modulo $|A_v|$ dell'invertitore scende con la temperatura**.

---

*Pagine correlate:*
- [Ritardo di Propagazione e Dimensionamento dell'Inverter CMOS](./Ritardo%20di%20Propagazione%20e%20Dimensionamento%20dell%27Inverter%20CMOS.md)
- [Dimensionamento Progressivo e Tapered Buffer](./Dimensionamento%20Progressivo%20e%20Tapered%20Buffer.md)
- [Latchup nei circuiti CMOS](./Latchup%20nei%20circuiti%20CMOS.md)
- [Effetto Miller](../Dispositivi%20e%20Componenti/Effetto%20Miller.md)
- [Caratteristica di Trasferimento e Rigenerazione](./Caratteristica%20di%20Trasferimento%20e%20Rigenerazione.md)
- [Soglia Logica e Margine di Rumore](./Soglia%20Logica%20e%20Margine%20di%20Rumore.md)
- [Retroazione nell'Inverter e Ring Oscillator](./Retroazione%20nell%27Inverter%20e%20Ring%20Oscillator.md)
- [Potenza Dinamica e Dissipazione di Carica](./Potenza%20Dinamica%20e%20Dissipazione%20di%20Carica.md)
- [MOS](../Dispositivi%20e%20Componenti/MOS.md)
- [Crollo della Resistenza di Uscita (ro) e Guadagno Intrinseco](../Effetti%20di%20Canale%20Corto/Crollo%20di%20ro.md)
- [Coppia Differenziale e Cascode Telescopico](../Dispositivi%20e%20Componenti/Coppia%20Differenziale%20e%20Cascode%20Telescopico.md)
- [Resistenza termica](../Scaling%20e%20Limiti%20Fisici/Resistenza%20termica.md)
