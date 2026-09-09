# Ritardo di Propagazione e Dimensionamento dell'Inverter CMOS

Il calcolo delle prestazioni dinamiche dell'invertitore [CMOS](./Inverter%20CMOS%20e%20Regioni%20di%20Funzionamento.md) si basa sulla determinazione del tempo necessario per caricare e scaricare le capacità parassite durante le transizioni logiche.

Per evitare simulazioni differenziali non lineari complesse, l'analisi manuale riconduce l'intera rete parassita a un'**unica capacità di carico equivalente concentrata $C_L$ a massa sull'uscita**.

---

### 1. Il Modello a Capacità Concentrata $C_L$ e la Prova del Nove (Slide 44 – 45)

Nel circuito reale (due inverter in cascata) sono presenti molteplici contributi capacitivi sparsi:
1. **Capacità di overlap gate-drain:** $C_{GD12} = W_1 C_{On} + W_2 C_{Op}$, che per [Effetto Miller](../Dispositivi%20e%20Componenti/Effetto%20Miller.md) a grandi segnali viene vista all'uscita moltiplicata per 2:
   $$\Delta C_{L,\text{Miller}} \approx 2 (W_1 + W_2) C_{GDO} = \mathbf{6.2\text{ fF}}$$
2. **Capacità di giunzione di Drain ($pn$ polarizzati inversamente):** linearizzate tramite il fattore integrale medio $K_{eq}$:
   $$C_{DBeq1} + C_{DBeq2} = 5.0\text{ fF} + 6.2\text{ fF} = \mathbf{11.2\text{ fF}}$$
3. **Capacità di interconnessione metallica dal layout:** $C_W = \mathbf{1.6\text{ fF}}$.
4. **Capacità di gate dello stadio a valle (fan-out):**
   $$C_{G3} + C_{G4} \approx C_{ox} (W_3 L_3 + W_4 L_4) = \mathbf{15.1\text{ fF}}$$

Sommando tutti i contributi (Slide 44 di [cmos.pdf](../../cmos.pdf)):
$$\mathbf{C_L \approx 34.2\text{ fF}}$$

```text
       VDD                         VDD
        │                           │
     ┌──┴──┐                     ┌──┴──┐
     │ M2  │                     │ M2  │
VI ──┤     ├── VO        VI ─────┤     ├── VO
     │ M1  │                     │ M1  │   │
     └──┬──┘                     └──┬──┘  === CL ≈ 34fF
        │ Rete parassiti            │      │
       GND  sparsi                 GND    GND
   (Circuito Reale)            (Modello Semplificato)
```

#### La Validazione Sperimentale / Simulativa (Slide 45)
Confrontando su SPICE la risposta del circuito completo non lineare (curva azzurra) con quella del modello semplificato con solo $C_L = 34\text{ fF}$ (curva rossa):
* Circuito reale completo (modello non lineare con tutti i parassiti): $t_p = \mathbf{290\text{ ps}}$
* Modello analitico semplificato con $C_L = 34\text{ fF}$: $t_p = \mathbf{276\text{ ps}}$
* **Errore relativo:**
  $$\text{Errore} = \frac{290 - 276}{290} \approx \mathbf{4.8\%}$$
Un errore inferiore al $5\%$ convalida pienamente l'uso di una singola capacità concentrata $C_L$ per il dimensionamento manuale.

---

### 2. Il Calcolo Analitico a Mano di $t_{pHL}$ (Slide 46 – 47)

Durante una transizione High-to-Low all'uscita ($V_I$ salta da $0$ a $V_{DD}$), il PMOS $M_2$ è spento e l'NMOS $M_1$ scarica la capacità $C_L$:
$$t_{pHL} = C_L \int_{V_{DD}/2}^{V_{DD}} \frac{dV_O}{I_{D1}(V_O)}$$

La scarica attraversa **due regimi di funzionamento distinti** per il transistor $M_1$:

```text
VO:  VDD (5V) ──────────────> VDD - VTn (4.26V) ──────────────> VDD/2 (2.5V)
           │                   │                               │
           └──── SATURAZIONE ──┴────────── REGIONE LINEARE ────┘
                   (ts = 71.5ps)             (179.9ps)
```

#### Fase 1: Transistor in Saturazione ($V_O > V_{DD} - V_{Tn}$, Slide 46)
Finché $V_{DS1} > V_{GS1} - V_{Tn}$, il canale è strozzato: la corrente è **costante e massima**:
$$I_{D1} = \frac{k_n}{2} (V_{DD} - V_{Tn})^2 = \text{costante}$$
La tensione scende con una retta a pendenza costante (scarica a corrente impressa).  
Il tempo trascorso in saturazione vale:
$$t_s = \frac{2 V_{Tn} C_L}{k_n (V_{DD} - V_{Tn})^2} = \mathbf{71.5\text{ ps}}$$

#### Fase 2: Transistor in Regione Lineare ($V_O < V_{DD} - V_{Tn}$, Slide 47)
Quando la strozzatura svanisce, la corrente segue la caratteristica parabolica:
$$I_{D1} = k_n \left[ (V_{DD} - V_{Tn}) V_O - \frac{V_O^2}{2} \right] = -C_L \frac{dV_O}{dt}$$
Separando le variabili e integrando tra $(V_{DD} - V_{Tn})$ e $V_{DD}/2$:
$$t_{pHL} - t_s = \frac{C_L}{k_n (V_{DD} - V_{Tn})} \ln\left( \frac{3 V_{DD} - 4 V_{Tn}}{V_{DD}} \right) = \mathbf{179.9\text{ ps}}$$

#### Tempo di Propagazione Totale:
$$t_{pHL} = t_s + (t_{pHL} - t_s) = 71.5\text{ ps} + 179.9\text{ ps} = \mathbf{251.4\text{ ps}}$$

---

### 3. Dove sta più tempo il transistor? Fino a Regime

Se analizziamo l'intera commutazione fino a regime stazionario ($V_O \to 0\text{ V}$):
* **In Saturazione:** ci sta solo per $\Delta V = V_{Tn} \approx 0.74\text{ V}$ (da $5\text{ V}$ a $4.26\text{ V}$), impiegando appena **$71.5\text{ ps}$**.
* **In Lineare:** deve percorrere tutta la restante discesa da $4.26\text{ V}$ fino a $0\text{ V}$.  
  Man mano che $V_O \to 0$, la corrente $I_{D1} \approx k_n (V_{DD} - V_{Tn}) V_O$ **tende a zero**: la scarica rallenta diventando una **coda esponenziale asintotica** ($e^{-t/R_{on}C_L}$).
* Per raggiungere il regime quasi-zero ($t \approx 1.2 \div 1.5\text{ ns}$ a Slide 45), il transistor passa oltre **$1200 \div 1400\text{ ps}$ in regione lineare**.

> **Conclusione:** il transistor passa oltre il **$95\%$ del transitorio totale in regione lineare**.

---

### 4. Semplificazioni Rapide di Progetto (Slide 48 – 50)

Per stimare il ritardo senza risolvere integrali logaritmici:
1. **Metodo della Corrente Media $I_{av}$ (Slide 48):**
   Media aritmetica tra la corrente a inizio scarica e quella al $50\%$: $I_{av} = 325\,\mu\text{A}$.
   $$t_{pHL} \approx \frac{C_L (V_{DD}/2)}{I_{av}} = \mathbf{263\text{ ps}}$$
2. **Metodo a Corrente di Saturazione Costante (Slide 49):**
   Assumendo $I \approx I_{sat} = \frac{k_n}{2}(V_{DD} - V_{Tn})^2$ su tutto l'intervallo:
   $$t_{pHL} \approx \frac{C_L V_{DD}}{2 I_{sat}} = \frac{C_L V_{DD}}{k_n (V_{DD} - V_{Tn})^2} = \mathbf{241\text{ ps}}$$
3. **Formula Compatta di Prima Approssimazione (Slide 50):**
   Trascurando $V_{Tn} \ll V_{DD}$:
   $$\mathbf{t_{pHL} \approx \frac{C_L}{k_n V_{DD}}} \qquad \mathbf{t_{pLH} \approx \frac{C_L}{k_p V_{DD}}}$$
   $$t_p = \frac{t_{pHL} + t_{pLH}}{2} \approx \frac{C_L}{2 V_{DD}} \left( \frac{1}{k_n} + \frac{1}{k_p} \right)$$

---

### 5. Il Dilemma del Dimensionamento Ottimo di $W_p$ (Slide 51)

Poiché la mobilità degli elettroni è circa 3 volte superiore a quella delle lacune ($\mu_n / \mu_p \approx 3$):

#### A) Dimensionamento per Margini di Rumore Ottimi ($NM$)
Per avere la caratteristica statica perfettamente simmetrica centrata su $V_M = V_{DD}/2$ (vedi [Soglia Logica e Margine di Rumore](./Soglia%20Logica%20e%20Margine%20di%20Rumore.md)), si impone $k_p = k_n$:
$$W_p = \frac{\mu_n}{\mu_p} W_n \approx \mathbf{3 \, W_n}$$

#### B) Dimensionamento per Massima Velocità (Minimo $t_p$)
Se facciamo $W_p = 3 W_n$, il PMOS diventa enorme, triplicando le proprie capacità parassite di drain e di gate, appesantendo drasticamente $C_L$!  
Definendo $\alpha = \frac{W_p}{W_n}$:
$$C_L \approx (1 + \alpha)(C_{D1} + C_{G3}) + C_W$$
$$t_p \approx \frac{C_L}{2 V_{DD} k_n} \left( 1 + \frac{\mu_n}{\mu_p \alpha} \right)$$
Uguagliando a zero la derivata $\frac{\partial t_p}{\partial \alpha} = 0$:
$$\mathbf{\alpha_{opt} = \sqrt{\frac{\mu_n}{\mu_p}} \approx \sqrt{3} \approx 1.73 \implies W_p \approx 1.73 \, W_n}$$

| Obiettivo Primario | Criterio | Rapporto Ottimo $W_p / W_n$ |
| :--- | :--- | :--- |
| **Margini di Rumore ($NM$)** | Simmetria statica ($k_p = k_n$) | $W_p \approx 3 \, W_n$ |
| **Velocità Massima (Minimo $t_p$)** | Minimo del prodotto $R_{on} \cdot C_L$ | $\mathbf{W_p \approx 1.73 \, W_n}$ |

---

### 6. Dipendenza da $V_{DD}$ e dal Fronte d'Ingresso $t_r$ (Slide 52 – 53)

1. **Influenza della Tensione di Alimentazione (Slide 52):**  
   Al diminuire di $V_{DD}$, il ritardo $t_p \propto \frac{1}{V_{DD}}$ cresce. Quando $V_{DD}$ si avvicina alla tensione di soglia ($V_{DD} \to V_T$), la corrente $I_D$ crolla a zero e il ritardo **esplode asintoticamente all'infinito**.
2. **Influenza del Tempo di Salita dell'Ingresso (Slide 53):**  
   Se l'ingresso non è un gradino ideale ma una rampa con tempo di salita finito $t_r$, il ritardo aumenta:
   $$\delta t_{pHL} \approx 0.14 \, \delta t_r \quad \iff \quad t_{pHL} \approx \sqrt{t_{pHL(ideal)}^2 + \frac{t_r^2}{4}}$$
   Finché l'ingresso sale, il PMOS conduce ancora parzialmente opponendosi alla scarica, e l'NMOS non è ancora pienamente acceso.

---

### 7. Potenza Dissipata Totale e PDP (Slide 54 – 56)

La potenza totale assorbita dall'inverter comprende tre termini distinti:
$$P_{tot} = \mathbf{P_d} + \mathbf{P_{dp}} + \mathbf{P_s}$$

1. **Potenza Dinamica di Commutazione ($P_d$, Slide 56):**
   $$P_d = C_L \cdot V_{DD}^2 \cdot f$$
   È la potenza necessaria per caricare e scaricare $C_L$ a frequenza $f$. **Rappresenta oltre l'85-90% del consumo totale.**
   👉 Approfondimento termodinamico sul dilemma del 50%: [Potenza Dinamica e Dissipazione di Carica](./Potenza%20Dinamica%20e%20Dissipazione%20di%20Carica.md).
2. **Potenza di Cortocircuito ($P_{dp}$, Slide 54):**
   Durante la transizione, quando $V_{Tn} < V_I < V_{DD} - |V_{Tp}|$, entrambi i transistori conducono simultaneamente. Si crea un percorso diretto di corrente da $V_{DD}$ a massa con picco $I_{peak}$:
   $$P_{dp} \approx \frac{t_r + t_f}{2} I_{peak} V_{DD} f$$
3. **Potenza Statica di Perdita ($P_s$, Slide 55):**
   Dovuta alle correnti di sottosoglia e di perdita delle giunzioni $pn$ polarizzate inversamente ($I_{leak} < 1\text{ nA}$):
   $$P_s = V_{DD} \cdot I_{leak}$$

#### Il Prodotto Ritardo-Consumo (PDP)
$$PDP = P_d \cdot t_p \approx \mathbf{C_L \cdot V_{DD}^2}$$
Nel CMOS analizzato ($C_L = 34.2\text{ fF}, V_{DD} = 5\text{ V}$): $\mathbf{PDP = 0.86\text{ pJ}}$.

#### Ripartizione nei Chip Integrati Complessi (Slide 56):
* **$1/3$ nei PIN di I/O:** a causa delle enormi capacità parassite esterne ($10 \div 50\text{ pF}$ per pin).
* **$1/3$ nella rete di Clock:** perché l'albero di clock commuta continuamente al $100\%$ dell'attività.
* **$1/3$ nella logica di calcolo:** le porte logiche interne, soggette a un fattore di attività medio $\alpha \approx 10\% \div 20\%$.

---

### 8. Il Problema dei Grandi Carichi e il Dimensionamento Progressivo (Slide 59 – 63)

Quando l'inverter deve pilotare capacità di carico rilevanti ($C_L \gg C_{in}$, come nel caso di piedini di I/O, bus o linee di clock), il ritardo scala linearmente con la capacità ($t_p \approx x \cdot t_{p0}$). 
Allargare semplicemente l'inverter finale non risolve il problema poiché sposta il carico sulla logica interna a monte.
La soluzione consiste nell'inserire una cascata di inverter a fattore di scala costante $u = \sqrt[N]{x}$.

👉 Trattazione completa, dimostrazione analitica ed esempio numerico: [Dimensionamento Progressivo e Tapered Buffer](./Dimensionamento%20Progressivo%20e%20Tapered%20Buffer.md).  
👉 Estensione alle porte logiche complesse (NAND, NOR), sizing equivalente e ritardo di pattern: [Dimensionamento Transistor e Ritardo di Pattern (Sizing)](../Circuiti%20Combinatori%20CMOS/Dimensionamento%20Transistor%20e%20Ritardo%20di%20Pattern%20(Sizing).md).  
👉 Effetto del Fan-In quadratico e modello RC distribuito: [Effetto di Fan-In e Fan-Out sul Ritardo (Elmore)](../Circuiti%20Combinatori%20CMOS/Effetto%20di%20Fan-In%20e%20Fan-Out%20sul%20Ritardo%20(Elmore).md).  
👉 Per i vincoli di affidabilità nel layout e il rischio di cortocircuito parassita $V_{DD}-\text{GND}$ (Slide 57 – 58): [Latchup nei circuiti CMOS](./Latchup%20nei%20circuiti%20CMOS.md).

---

*Pagine correlate:*
- [Dimensionamento Transistor e Ritardo di Pattern (Sizing)](../Circuiti%20Combinatori%20CMOS/Dimensionamento%20Transistor%20e%20Ritardo%20di%20Pattern%20(Sizing).md)
- [Effetto di Fan-In e Fan-Out sul Ritardo (Elmore)](../Circuiti%20Combinatori%20CMOS/Effetto%20di%20Fan-In%20e%20Fan-Out%20sul%20Ritardo%20(Elmore).md)
- [Tecniche di Ottimizzazione per Porte Complesse Veloci](../Circuiti%20Combinatori%20CMOS/Tecniche%20di%20Ottimizzazione%20per%20Porte%20Complesse%20Veloci.md)
- [Dimensionamento Progressivo e Tapered Buffer](./Dimensionamento%20Progressivo%20e%20Tapered%20Buffer.md)
- [Latchup nei circuiti CMOS](./Latchup%20nei%20circuiti%20CMOS.md)
- [Inverter CMOS e Regioni di Funzionamento](./Inverter%20CMOS%20e%20Regioni%20di%20Funzionamento.md)
- [Soglia Logica e Margine di Rumore](./Soglia%20Logica%20e%20Margine%20di%20Rumore.md)
- [Potenza Dinamica e Dissipazione di Carica](./Potenza%20Dinamica%20e%20Dissipazione%20di%20Carica.md)
- [RTL e Prodotto Ritardo-Consumo (PDP)](./RTL%20e%20Prodotto%20Ritardo-Consumo%20%28PDP%29.md)
- [Retroazione nell'Inverter e Ring Oscillator](./Retroazione%20nell%27Inverter%20e%20Ring%20Oscillator.md)
- [Effetto Miller](../Dispositivi%20e%20Componenti/Effetto%20Miller.md)
- [Capacità parassite nel MOSFET](../Dispositivi%20e%20Componenti/Capacit%C3%A0%20parassite%20nel%20MOSFET.md)
- [MOS](../Dispositivi%20e%20Componenti/MOS.md)
- [Layout e Tecniche di Progettazione dei MOS](../Dispositivi%20e%20Componenti/Layout%20e%20Tecniche%20di%20Progettazione%20dei%20MOS.md)
