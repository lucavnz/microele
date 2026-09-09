# Conduzione di Sottosoglia e Rapporto $I_{ON}/I_{OFF}$

### 1. Il MOSFET non è un interruttore ideale ON/OFF
Nei modelli digitali a soglia netta si assume che per $V_{GS} < V_{th}$ la corrente sia rigorosamente zero. Nella realtà fisica la transizione è continua.

Quando $V_{GS} < V_{th}$ (regime di **debole inversione** o **sottosoglia**, vedi [Overdrive e Regioni di Inversione](../Dispositivi%20e%20Componenti/Overdrive%20e%20Regioni%20di%20Inversione.md) e [La soglia da cosa dipende](../Dispositivi%20e%20Componenti/La%20soglia%20da%20cosa%20dipende.md)), non c'è ancora un canale continuo di elettroni in forte inversione, ma i portatori superano la barriera di potenziale muovendosi per **diffusione** (esattamente come avviene nella base di un transistore bipolare [BJT](../Dispositivi%20e%20Componenti/BJT.md)). 

La corrente segue una legge **esponenziale**:

$$I_{D,sub} = I_{D0} \cdot \exp\left( \frac{V_{GS} - V_{th}}{n V_T} \right) \cdot \left(1 - \exp\left(-\frac{V_{DS}}{V_T}\right)\right)$$

Dove:
* $V_T = \frac{k_B T}{q} \approx 25.86\,\text{mV} \approx 26\,\text{mV}$ a temperatura ambiente ($300\text{ K}$).
* $n = 1 + \frac{C_{dep}}{C_{ox}} \approx 1.2 - 1.5$ è il fattore di sottosoglia (*body factor* o fattore di non idealità, generato dal partitore capacitivo tra l'ossido di gate $C_{ox}$ e la capacità di svuotamento $C_{dep}$).
* $I_{D0} \approx 0.1\,\mu\text{A} \cdot \frac{W}{L}$ è la corrente alla soglia nominale ($V_{GS} = V_{th}$), punto di raccordo con la forte inversione.

#### Perché all'esponente c'è $(V_{GS} - V_{th})$ e non solo $V_{GS}$ come nel BJT?
* **Nel BJT ($I_C \propto \exp(V_{BE}/V_T)$):** il terminale di base è a contatto ohmico diretto con il silicio; ogni variazione di $V_{BE}$ modula direttamente la barriera della giunzione $p\text{-}n$.
* **Nel MOSFET:** il Gate non tocca il silicio, ma è separato dal dielettrico dell'ossido ($C_{ox}$). La forte inversione inizia quando il potenziale superficiale raggiunge $\psi_s = 2\Phi_F$, condizione che definisce $V_{GS} = V_{th}$. Sotto soglia, la barriera di potenziale che i portatori devono superare per fluire dal Source al canale è direttamente proporzionale a **quanto ci troviamo al di sotto della soglia**, cioè a $(V_{th} - V_{GS})$. Per questo la corrente si normalizza a $I_{D0}$ proprio in corrispondenza del riferimento $V_{GS} = V_{th}$ (dove l'esponenziale vale $e^0 = 1$).

---

### 2. La corrente di perdita a riposo ($I_{OFF}$) e la traslazione a sinistra della curva

Cosa succede quando spegniamo il transistor ponendo nominalmente $V_{GS} = 0\text{ V}$?
Valutando la formula per $V_{GS} = 0\text{ V}$ (con $V_{DS} \gg V_T$ tale che $1 - e^{-V_{DS}/V_T} \approx 1$), la corrente di perdita a riposo (*leakage*) vale:

$$I_{OFF} = I_{D0} \cdot \exp\left( - \frac{V_{th}}{n V_T} \right)$$

Poiché $V_{th}$ compare all'esponente:
* **Nei canali lunghi ($V_{th} \approx 0.7\text{ V}$):** la distanza dalla soglia è enorme rispetto a $n V_T$. $I_{OFF}$ è nell'ordine dei **pico-ampere** ($10^{-12}\text{ A}$), del tutto trascurabile.
* **Nei canali corti submicrometrici (Short Channel Effects):**
  1. Il [Vth Roll-Off](./Vth%20roll%20off.md) (dovuto al *charge sharing* delle giunzioni) abbassa $V_{th}$ per motivi geometrici.
  2. Il [DIBL](./DIBL.md) (*Drain-Induced Barrier Lowering*) abbassa ulteriormente la barriera elettrostatica all'ingresso del canale poiché il Drain si trova a $V_{DD}$, tirando giù la soglia: $V_{th}(V_{DS}) = V_{th0} - \eta V_{DS}$.

**Il nocciolo intuitivo:** L'abbassamento di $V_{th}$ si traduce in una **traslazione rigida verso sinistra dell'intera curva $\log_{10}(I_D) - V_{GS}$**. 
Ponendo $V_{GS} = 0\text{ V}$, ci troviamo molto più vicini alla soglia rispetto a prima. Essendo la transizione esponenziale, anche una riduzione di soli $120-180\,\text{mV}$ su $V_{th}$ non fa aumentare $I_{OFF}$ del $20\%$, ma **la fa schizzare di 2 o 3 ordini di grandezza** (da picoampere a microampere)!

---

### 3. Il Dilemma del Rapporto $I_{ON}/I_{OFF}$ e la Dissipazione Statica

Il rapporto $I_{ON}/I_{OFF}$ misura l'efficacia del MOSFET come interruttore digitale:
* **Canale lungo:** $\frac{I_{ON}}{I_{OFF}} \approx 10^7 - 10^8$ (interruttore ideale, separazione netta tra ON e OFF).
* **Canale corto degradato:** $\frac{I_{ON}}{I_{OFF}} \approx 10^3 - 10^4$ (interruttore che "gocciola" corrente).

#### Perché non possiamo semplicemente rialzare $V_{th}$ per azzerare $I_{OFF}$?
Nello scaling tecnologico, per contenere la potenza dinamica ($P_{dyn} \propto V_{DD}^2 f$), la tensione di alimentazione è stata ridotta da $5\,\text{V}$ a meno di $1\,\text{V}$ (fino a $0.7 - 0.8\,\text{V}$).
* La corrente di conduzione $I_{ON}$ dipende dalla tensione di overdrive: $I_{ON} \propto (V_{DD} - V_{th})^\alpha$.
* Se aumentassimo il drogaggio per riportare $V_{th}$ a $0.6\,\text{V}$, l'overdrive $(V_{DD} - V_{th})$ crollerebbe a soli $0.1 - 0.2\,\text{V}$. La corrente $I_{ON}$ diventerebbe microscopica e il ritardo di propagazione delle porte logiche ($t_p \propto \frac{C_L V_{DD}}{I_{ON}}$) esploderebbe, rendendo il processore lentissimo.
* I progettisti sono quindi costretti a un trade-off brutale: abbassare $V_{th}$ per garantire velocità, pagando però un prezzo salatissimo in termini di $I_{OFF}$.

#### L'impatto a livello di chip (Potenza Statica)
Un singolo transistor con $I_{OFF} = 10\,\text{nA}$ sembra innocuo, ma un microprocessore moderno integra **$10 - 100$ miliardi di transistor**.
$$P_{static} = V_{DD} \cdot \sum I_{OFF} \approx 1\,\text{V} \times (10^{10} \times 10^{-8}\,\text{A}) = \mathbf{100\,\text{W}}$$
Senza contromisure avanzate, un chip dissiperebbe decine o centinaia di Watt solo stando fermo a riposo (*thermal runaway* e batteria scaricata in pochi minuti).

---

### 4. Il *Subthreshold Swing* ($S$): Origine Matematica dei $60\,\text{mV/decade}$

Il parametro $S$ (*Subthreshold Swing*) indica quanti millivolt di tensione di Gate occorre applicare per far variare la corrente di Drain di un fattore 10 (una decade). È definito come l'inverso della pendenza della caratteristica su scala semi-logaritmica:

$$S = \left( \frac{\partial \log_{10} I_D}{\partial V_{GS}} \right)^{-1} = \frac{\partial V_{GS}}{\partial \log_{10} I_D}$$

#### Dimostrazione analitica:
Dalla legge esponenziale di sottosoglia:
$$I_D = I_{D0} \exp\left( \frac{V_{GS} - V_{th}}{n V_T} \right)$$

Applicando il logaritmo naturale:
$$\ln(I_D) = \ln(I_{D0}) + \frac{V_{GS} - V_{th}}{n V_T}$$

Convertendo in logaritmo in base 10 sapendo che $\log_{10}(x) = \frac{\ln(x)}{\ln(10)}$:
$$\log_{10}(I_D) = \frac{1}{\ln(10)} \left[ \ln(I_{D0}) + \frac{V_{GS} - V_{th}}{n V_T} \right]$$

Derivando rispetto a $V_{GS}$ (notando che $(V_{GS} - V_{th})$ ha derivata unitaria e $V_{th}$ è costante):
$$\frac{\partial \log_{10}(I_D)}{\partial V_{GS}} = \frac{1}{\ln(10) \cdot n \cdot V_T}$$

Invertendo il rapporto per ottenere $S$:
$$S = \ln(10) \cdot n \cdot V_T = \ln(10) \cdot n \cdot \frac{k_B T}{q}$$

#### Valori numerici a temperatura ambiente ($T = 300\,\text{K}$):
* $\ln(10) \approx 2.3026$
* $V_T = \frac{k_B T}{q} \approx 25.86\,\text{mV}$
* Moltiplicando: $\ln(10) \times V_T = 2.3026 \times 25.86\,\text{mV} \approx \mathbf{59.5\,\text{mV}} \approx \mathbf{60\,\text{mV}}$

La formula compatta universale è:
$$\mathbf{S = n \times 60\,\text{mV/decade}}$$

* **Limite ideale termodinamico ($n = 1$):** Si avrebbe se non ci fosse accoppiamento capacitivo col substrato ($C_{dep} \to 0$ o $C_{ox} \to \infty$). Nel transistore bipolare ([BJT](../Dispositivi%20e%20Componenti/BJT.md)), la tensione di base modula direttamente la barriera senza dielettrico di mezzo ($n = 1$), raggiungendo esattamente **$60\,\text{mV/dec}$** a $300\,\text{K}$. Nel MOSFET, a causa della distribuzione termica di Boltzmann dei portatori (*Boltzmann Tyranny*), è impossibile scendere al di sotto di questa soglia.
* **MOSFET bulk reale:** $n \approx 1.2 - 1.5 \implies S \approx 75 - 95\,\text{mV/dec}$.
* **Canale corto degradato (DIBL):** Il Gate perde autorità elettrostatica sul canale a favore del Drain; $S$ sale oltre i **$100\,\text{mV/dec}$** (la pendenza si appiattisce, richiedendo ancora più tensione per spegnere il canale).
* **Soluzione moderna ([SOI](../Dispositivi%20e%20Componenti/SOI.md) e [FinFET](../Dispositivi%20e%20Componenti/FinFET.md)):** Eliminando il bulk neutro e avvolgendo il canale, $C_{dep} \approx 0$ e $n \to 1.05$, riportando lo swing a ridosso del limite ideale ($62 - 65\,\text{mV/dec}$).

#### Il termine $-V_{th}$ all'esponente cambia la pendenza?
Un dubbio comune è se la presenza di $-V_{th}$ al numeratore dell'esponenziale possa degradare la pendenza sottosoglia.
La risposta matematica e fisica è **no**:
$$\frac{\partial \log_{10}(I_D)}{\partial V_{GS}} = \frac{\partial}{\partial V_{GS}} \left[ \log_{10}(I_{D0}) + \frac{V_{GS} - V_{th}}{\ln(10) \cdot n V_T} \right] = \frac{1}{\ln(10) \cdot n V_T}$$
Essendo $V_{th}$ indipendente da $V_{GS}$, la sua derivata è **zero**. 
* La pendenza $S$ dipende **esclusivamente dal fattore di partitore $n$ e dalla temperatura $T$**.
* **$V_{th}$ agisce come un puro offset orizzontale**: sposta rigidamente la retta verso destra o sinistra.

Tuttavia, $V_{th}$ determina il numero di **decadi di spegnimento** a $V_{GS} = 0\,\text{V}$:
$$\text{Decadi di OFF} = \frac{V_{th}}{S}$$
Più la pendenza è ripida (es. $S \approx 60\,\text{mV/dec}$ nei FinFET), più possiamo scegliere un **$V_{th}$ basso** ($0.25 - 0.3\,\text{V}$) garantendo al contempo un'ottima corrente $I_{OFF}$ e un elevato overdrive in conduzione a basse tensioni!

---

### 5. Il Ruolo del Fattore $k$ e di $C_{ox}$: Perché Spingerli al Massimo?

Il fattore di conduzione del MOSFET:
$$k = k' \frac{W}{L} = \mu C_{ox} \frac{W}{L} = \mu \frac{\epsilon_{ox}}{t_{ox}} \frac{W}{L}$$
gioca un ruolo simmetrico ma complementare tra la regione di **ON** e la regione di **OFF**:

1. **Nello stato di ON (Forte Inversione):**
   * **Velocità di commutazione:** Il ritardo di propagazione di una porta digitale scala come $\tau \approx \frac{C_L V_{DD}}{I_{ON}}$. A parità di overdrive, un $k$ elevato fornisce una corrente $I_{ON}$ molto superiore, caricando e scaricando i nodi capacitivi a frequenze di clock elevate.
   * **Abbattimento della Potenza Dinamica ($P_{dyn} \propto V_{DD}^2$):** Con un $k$ grande, è possibile **ridurre drasticamente la tensione di alimentazione $V_{DD}$** (da $3.3\,\text{V}$ fino a $0.7\,\text{V}$) pur preservando una corrente $I_{ON}$ sufficiente per commutare velocemente. Poiché la potenza dinamica scala con $V_{DD}^2$, questo abbatte i consumi del processore.
   * **Risparmio d'area:** Consente di usare larghezze $W$ minori, riducendo l'impronta sul silicio.
2. **Nello stato di OFF (Sottosoglia):**
   * Spingere la capacità $C_{ox}$ tramite dielettrici [High-k e Metal Gate (HKMG)](../Dispositivi%20e%20Componenti/High-k%20e%20Metal%20Gate%20(HKMG).md) rende $C_{ox} \gg C_{dep}$, forzando il partitore di non idealità $n = 1 + \frac{C_{dep}}{C_{ox}} \to 1$.
   * Questo garantisce la massima efficienza elettrostatica, azzerando le perdite parassite.

---

### 6. Perché distrugge le prestazioni in Analogico?

Nei circuiti analogici a capacità commutate (**Switched-Capacitor**) e nei blocchi **Sample & Hold** (usati all'ingresso di tutti gli ADC):
1. Il transistor MOS viene usato come interruttore per caricare un [condensatore](../Dispositivi%20e%20Componenti/Condensatori.md) con la tensione del segnale analogico $V_{in}$.
2. Quando l'interruttore si apre ($V_{GS} = 0\text{ V}$), il condensatore dovrebbe mantenere la carica costante durante la conversione.
3. A causa dell'alta corrente $I_{OFF}$, la carica sul condensatore **si scarica rapidamente** (*droop rate*):
   $$\frac{dV_{out}}{dt} = \frac{I_{OFF}}{C_{hold}}$$
4. La tensione memorizzata decade prima che la conversione sia completata, introducendo errori gravi di linearità e risoluzione nell'ADC.

---
*Pagine correlate:*
- [FinFET](../Dispositivi%20e%20Componenti/FinFET.md)
- [High-k e Metal Gate (HKMG)](../Dispositivi%20e%20Componenti/High-k%20e%20Metal%20Gate%20(HKMG).md)
- [Strained Silicon (Silicio Deformato)](../Dispositivi%20e%20Componenti/Strained%20Silicon%20(Silicio%20Deformato).md)
- [Overdrive e Regioni di Inversione](../Dispositivi%20e%20Componenti/Overdrive%20e%20Regioni%20di%20Inversione.md)
- [La soglia da cosa dipende](../Dispositivi%20e%20Componenti/La%20soglia%20da%20cosa%20dipende.md)
- [SOI](../Dispositivi%20e%20Componenti/SOI.md)
- [Condensatori](../Dispositivi%20e%20Componenti/Condensatori.md)
- [DIBL](./DIBL.md)
- [Analogico non si scende di dimensioni](../Scaling%20e%20Limiti%20Fisici/Analogico%20non%20si%20scende%20di%20dimensioni.md)
- [Vth roll off](./Vth%20roll%20off.md)

