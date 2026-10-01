In sintesi estrema: un **Self-Cascode** serve a ottenere l'**alta resistenza di uscita (e quindi l'alto guadagno)** tipica di un cascode, ma con la **bassissima caduta di tensione minima** di un singolo transistore e **senza bisogno di circuiti di polarizzazione dedicati**.

È la soluzione d'elezione nei circuiti analogici moderni a **bassissima tensione di alimentazione** (*Ultra-Low Voltage*, es. $V_{DD} \le 1\text{ V}$ o $0.6\text{ V}$).

---

### 1. Il problema di partenza: il dilemma del Cascode a bassa tensione

Nei processi tecnologici avanzati (canali corti), il singolo transistore MOS soffre di una forte modulazione di canale (effetto Early), per cui la sua resistenza d'uscita $r_o$ è bassa e il guadagno intrinseco $A_0 = g_m r_o$ crolla.

Tradizionalmente, per aumentare l'impedenza si usa il **Cascode classico** (due MOS in saturazione impilati):
* **Il vantaggio:** moltiplica la resistenza d'uscita per il fattore intrinseco: $R_{out} \approx g_{m2} r_{o2} r_{o1}$ (molto alta).
* **Il difetto fatale a bassa $V_{DD}$:** per tenere entrambi i MOS in saturazione, richiede una caduta minima di tensione pari a **due overdrive**:
  $$V_{DS,\min} = 2 \Delta V = V_{ov1} + V_{ov2} \approx 300 \div 400\text{ mV}$$
  Se l'alimentazione $V_{DD}$ è ad esempio di soli $0.8\text{ V} \div 1\text{ V}$, "sprecare" $400\text{ mV}$ solo per i transistori di fondo (e altrettanti per il carico attivo in alto) **distrugge completamente la dinamica del segnale d'uscita** (*voltage headroom/swing*).
* **Complessità circuitale:** richiede di generare una tensione di polarizzazione ausiliaria fissa ($V_{bias}$) per il gate del secondo MOS.

---

### 2. Come risolve il problema il Self-Cascode?

Il Self-Cascode è formato da due transistori ($M_S$ verso il source e $M_D$ verso il drain) con i **gate cortocircuitati insieme** ($V_{GD} = V_{GS} = V_G$).

Grazie a questo semplice collegamento:
1. **$M_S$ si trova in zona LINEARE (triodo):**
   * Essendo in zona ohmica, la caduta di tensione ai suoi capi ($V_{DS,S}$) è piccolissima (poche decine di millivolt, $\ll \Delta V$).
2. **$M_D$ si trova in SATURAZIONE:**
   * Poiché la sua sorgente è a un potenziale leggermente più alto, il suo $V_{GS}$ è minore di quello di $M_S$: per far passare la stessa corrente entra spontaneamente in saturazione.

---

### 3. I 4 grandi benefici pratici

| Proprietà | Singolo MOS | Cascode Classico | **Self-Cascode** |
| :--- | :---: | :---: | :---: |
| **Caduta minima richiesta ($V_{DS,\min}$)** | $\approx \Delta V$ (bassa) | $\approx 2\Delta V$ (alta, ruba dinamica) | **$\approx \Delta V$ (bassa come il singolo MOS!)** |
| **Resistenza d'uscita ($R_{out}$)** | $r_o$ (bassa) | $\approx g_m r_o^2$ (molto alta) | **Quasi come cascode ($2 \div 4 \times$ il singolo MOS)** |
| **Tensioni di polarizzazione extra** | Nessuna | Richiede $V_{bias}$ per il secondo gate | **Nessuna (i gate sono uniti)** |
| **Comportamento esterno** | 3/4 terminali | Circuito a 2 stadi distinti | **Equivalente a un "super-transistor" a 3/4 terminali** |

---

### 4. Dove e perché si usa nei circuiti reali?

1. **Specchi di corrente a basso consumo (Low-Voltage Current Mirrors):**
   Permette di avere correnti di riferimento precise ad altissima impedenza di uscita senza dover sprecare tensione di polarizzazione per tenere in saturazione lo specchio.
2. **Carichi attivi ad alto guadagno negli amplificatori (OTA / Op-Amp):**
   Permette di ottenere guadagni di anello aperto $A_v$ elevati in un singolo stadio anche quando $V_{DD} < 1\text{ V}$, preservando la massima escursione picco-picco del segnale d'uscita (rail-to-rail quasi completo).
3. **Superare il limite di compromesso $g_m$ vs $r_o$:**
   In un singolo MOS, se aumenti la lunghezza di canale $L$ per aumentare $r_o$, la transconduttanza $g_m$ crolla ($g_m \propto W/L$). Con il Self-Cascode dividi la lunghezza in $L_S$ ed $L_D$: $M_S$ fa da degeneratore ad alta resistenza, mentre $M_D$ mantiene un'alta $g_m$, massimizzando il prodotto $A_0 = g_m \cdot R_{out}$.