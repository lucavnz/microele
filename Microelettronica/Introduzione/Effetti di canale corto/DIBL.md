# DIBL (*Drain-Induced Barrier Lowering*)

### Cos'è il DIBL?
In un transistor ideale a canale lungo, è solo la tensione di Gate $V_{GS}$ che controlla la barriera di potenziale per accendere o spegnere il canale.

Quando la lunghezza $L$ diventa cortissima (sub-micrometrica o nanometrica), il Drain si trova fisicamente **troppo vicino al Source**:
* Le linee di campo elettrico generate dall'alta tensione di Drain $V_{DS}$ riescono a penetrare in profondità nel canale.
* Questo campo elettrico **abbassa la barriera di potenziale** della giunzione Source-canale **al posto del Gate**, facendo passare elettroni anche quando il Gate vorrebbe tenere il canale spento o meno conduttivo.

---

### La formula del DIBL
La tensione di soglia non è più un valore fisso, ma diventa funzione lineare decrescente di $V_{DS}$:

$$V_{th}(V_{DS}) = V_{th0} - \eta \cdot V_{DS}$$

Dove:
* $V_{th0}$ è la tensione di soglia a $V_{DS} \approx 0\text{ V}$.
* $\eta$ è il coefficiente di DIBL (espresso in $\text{mV/V}$ o adimensionale), che cresce man mano che $L$ diminuisce.

---

### Perché distrugge le prestazioni in Analogico?

1. **Forte Distorsione Non Lineare:**
   In un amplificatore analogico, la tensione di Drain $V_{DS}$ rappresenta il segnale di uscita $v_{out}$ che oscilla nel tempo.
   Se $V_{DS}$ oscilla, allora **anche la soglia $V_{th}$ oscilla in tempo reale**!
   Questo modula continuamente l'overdrive $(V_{gs} - V_{th}(t))$, introducendo distorsione armonica che deforma la sinusoide.

2. **Crollo ulteriore della resistenza di uscita $r_o$:**
   La corrente $I_D$ aumenta all'aumentare di $V_{DS}$ sia per la modulazione di lunghezza di canale (CLM), sia perché $V_{th}$ scende per via del DIBL. La pendenza della curva $I_D - V_{DS}$ in saturazione diventa ripida $\implies r_o$ crolla $\implies$ il guadagno intrinseco $A_0 = g_m r_o$ si azzera.

3. **Esplosione del Leakage Sottosoglia:**
   A $V_{GS} = 0\text{ V}$, se c'è una $V_{DS}$ alta, la soglia si abbassa e la corrente di perdita $I_{OFF}$ esplode esponenzialmente.

### Come si mitiga o si risolve il DIBL?

1. **Nel Silicio Bulk:** Si aumenta fortemente il drogaggio del canale sotto il Gate ($N_A \uparrow$). Questo crea una barriera di potenziale più robusta, ma penalizza la mobilità dei portatori $\mu$ (per collisioni ioniche) e peggiora la dispersione statistica di soglia (*Random Dopant Fluctuation* - RDF).
2. **Nelle Architetture Avanzate ([UTBB FD-SOI](../../Tecnologie/SOI.md)):** Si riduce lo spessore del film di silicio a soli $t_{Si} \approx 5-7\,\text{nm}$. Questo abbatte l'area laterale del canale e rende minuscola la capacità laterale di accoppiamento:
   $$C_{\text{lat}} = \epsilon_{Si} \frac{W \cdot t_{Si}}{L}$$
   Il Gate metallico sovrastante vince nettamente il partitore capacitivo ($C_{ox} \gg C_{\text{lat}}$), azzerando l'influenza del Drain sul Source (**Zero DIBL**).

---

*Pagine correlate:*
- [SOI](../../Tecnologie/SOI.md)
- [Analogico non si scende di dimensioni](../Analogico%20non%20si%20scende%20di%20dimensioni.md)
- [Crollo di ro](./Crollo%20di%20ro.md)
- [Rapporto Ion/Ioff e Sottosoglia](./Rapporto%20Ion%20Ioff%20e%20sottosoglia.md)
