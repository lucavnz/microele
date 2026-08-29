# Conduzione di Sottosoglia e Rapporto $I_{ON}/I_{OFF}$

### 1. Il MOSFET non è un interruttore ideale ON/OFF
Nei modelli digitali semplificati si assume spesso che per $V_{GS} < V_{th}$ la corrente sia esattamente zero. Nella realtà fisica la transizione è continua.

Quando $V_{GS} < V_{th}$ (regime di **debole inversione** o **sottosoglia**, vedi la fisica dei regimi in [La soglia da cosa dipende](../Dispositivi%20e%20Componenti/La%20soglia%20da%20cosa%20dipende.md)), non c'è ancora un canale continuo di elettroni, ma i portatori si muovono per **diffusione** (come nei transistori bipolari BJT). 
La corrente segue una legge **esponenziale**:

$$I_{D,sub} = I_0 \cdot \exp\left( \frac{V_{GS} - V_{th}}{n V_T} \right) \cdot \left(1 - \exp\left(-\frac{V_{DS}}{V_T}\right)\right)$$

Dove:
* $V_T = \frac{k_B T}{q} \approx 26\,\text{mV}$ a temperatura ambiente.
* $n = 1 + \frac{C_{dep}}{C_{ox}} \approx 1.2 - 1.5$ è il fattore di sottosoglia (partitore capacitivo tra ossido e silicio svuotato).

---

### 2. La corrente di perdita a riposo ($I_{OFF}$)

Cosa succede quando spegniamo il transistor ponendo $V_{GS} = 0\text{ V}$?
La corrente residua di perdita (*leakage*) vale:

$$I_{OFF} \propto \exp\left( - \frac{V_{th}}{n V_T} \right)$$

Poiché $V_{th}$ compare all'esponente:
* **Nei canali lunghi ($V_{th} \approx 0.7\text{ V}$):** $I_{OFF}$ è nell'ordine dei **pico-ampere** ($10^{-12}\text{ A}$), trascurabile.
* **Nei canali nanometrici con forte DIBL ($V_{th} \approx 0.2 - 0.3\text{ V}$):** la barriera si riduce di $400\,\text{mV}$. A causa della funzione esponenziale, la corrente di perdita cresce di **$4 - 5$ ordini di grandezza**, arrivando a micro-ampere ($10^{-6}\text{ A}$)!

---

### 3. Crollo del Rapporto $I_{ON}/I_{OFF}$

Il rapporto $I_{ON}/I_{OFF}$ definisce la qualità del MOSFET come interruttore:
* **Canale lungo:** $\frac{I_{ON}}{I_{OFF}} \approx 10^8 - 10^9$ (interruttore praticamente ideale).
* **Canale corto:** $\frac{I_{ON}}{I_{OFF}} \approx 10^3 - 10^4$ (interruttore che "gocciola" corrente).

---

### 4. Il *Subthreshold Swing* ($S$)
Il parametro $S$ quantifica quanti millivolt di Gate servono per ridurre la corrente di perdita di un fattore 10 (un decennio):

$$S = \ln(10) \cdot n V_T \approx 60 - 90\,\text{mV/decade}$$

* Il limite termodinamico ideale a $300\text{ K}$ è $S_{ideal} = \ln(10) \cdot 26\,\text{mV} \approx 60\,\text{mV/dec}$.
* Nei nodi nanometrici con effetti di canale corto e DIBL, il Gate perde efficienza elettrostatica ($n$ peggiora) e $S$ sale verso $90 - 100\,\text{mV/dec}$ (la curva di spegnimento diventa più "moscia").

---

### Perché distrugge le prestazioni in Analogico?

Nei circuiti analogici a capacità commutate (**Switched-Capacitor**) e nei blocchi **Sample & Hold** (usati all'ingresso di tutti gli ADC):
1. Il transistor MOS viene usato come interruttore per caricare un [condensatore](../Dispositivi%20e%20Componenti/Condensatori.md) con la tensione del segnale analogico $V_{in}$.
2. Quando l'interruttore si apre ($V_{GS} = 0\text{ V}$), il condensatore dovrebbe mantenere la carica costante durante la conversione.
3. A causa dell'alta corrente $I_{OFF}$, la carica sul condensatore **si scarica rapidamente** (*droop rate*):
   $$\frac{dV_{out}}{dt} = \frac{I_{OFF}}{C_{hold}}$$
4. La tensione memorizzata decade prima che la conversione sia completata, introducendo errori gravi di linearità e risoluzione nell'ADC.

---
*Pagine correlate:*
- [La soglia da cosa dipende](../Dispositivi%20e%20Componenti/La%20soglia%20da%20cosa%20dipende.md)
- [SOI](../Dispositivi%20e%20Componenti/SOI.md)
- [Condensatori](../Dispositivi%20e%20Componenti/Condensatori.md)
- [DIBL](./DIBL.md)
- [Analogico non si scende di dimensioni](../Scaling%20e%20Limiti%20Fisici/Analogico%20non%20si%20scende%20di%20dimensioni.md)
- [Vth roll off](./Vth%20roll%20off.md)
