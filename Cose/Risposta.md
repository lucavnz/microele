La tua intuizione è **eccellente**: se c'è una capacità parassita tra due punti, ogni volta che un nodo commuta bruscamente ($\frac{dV}{dt}$ elevato), attraverso il condensatore scorre una corrente di spostamento:
$$i = C \cdot \frac{dV}{dt}$$
Quindi sì: se una piastra "balla", la capacità tende a trascinare anche l'altra (accoppiamento capacitivo / partitore capacitivo).

Allora **perché diciamo che il SOI riduce la capacità e isola molto meglio dal rumore?**
Ci sono 3 motivi fisici e geometrici ben precisi.

---

### 1. L'area non è "vasta": il Drain è un'isoletta microscopica
È vero che l'ossido sepolto (BOX) copre l'intero wafer, ma un condensatore esiste solo dove ci sono **due armature conduttive affacciate**.
* L'armatura inferiore è il substrato sotto.
* L'armatura superiore **non è tutto il silicio**, ma **soltanto la microscopica area del singolo drain** di quel transistor (perché ogni transistor è isolato lateralmente da trincee di ossido dielettrico, la STI).
* Parliamo di dimensioni nanometriche/micrometriche (es. $0.3\,\mu\text{m} \times 0.1\,\mu\text{m} = 0.03\,\mu\text{m}^2$). L'area $A$ è minuscola.

---

### 2. Perché la capacità in SOI è molto più piccola rispetto al Bulk?
Ricordando la formula del condensatore a facce piane:
$$C = \frac{\varepsilon \cdot A}{d}$$

Nel **Bulk CMOS**, la capacità di drain non è fatta da un ossido, ma dalla **giunzione $p$-$n$ polarizzata inversamente**:

```
BULK CMOS:
                Gate
        Source ┌───┐  Drain (n+)
       ─────── │   │ ─────────
      (n+)     └───┘ │░░░░░░░│
                     │  Wdep │ ◄── Giunzione pn (depletion layer)
     ────────────────┴───────┴──────
               Substrato (p)
```

1. **La costante dielettrica $\varepsilon$:**
   * Nel silicio puro (Bulk): $\varepsilon_{Si} \approx 11.7 \cdot \varepsilon_0$
   * Nel biossido di silicio (SOI): $\varepsilon_{SiO_2} \approx 3.9 \cdot \varepsilon_0$
   Solo per il materiale, a parità di spessore la capacità nel SOI è già **3 volte più piccola**!
2. **Lo spessore $d$:**
   * Nel Bulk moderno i drogaggi sono altissimi, quindi lo spessore della zona di carica spaziale (svuotamento, $W_{dep}$) è ridottissimo (spesso solo $20 \div 40\text{ nm}$).
   * Nel SOI classico il BOX è spesso tipicamente $100 \div 400\text{ nm}$ (molto più spesso di $W_{dep}$). Nei nodi avanzati (FD-SOI) dove il BOX è sottile ($10 \div 25\text{ nm}$), sotto il BOX il silicio si svuota creando una capacità di svuotamento *in serie*, e due condensatori in serie danno una capacità totale **ancora più piccola**.
3. **Le pareti laterali (il perimetro):**
   Nel Bulk il drain è una "vaschetta tridimensionale" scavata nel silicio opposto: hai la capacità di fondo **PIÙ la capacità su tutte e 4 le pareti laterali**, dove il drogaggio è molto alto (e le pareti contano spesso per il 50-60% della capacità totale!).  
   Nel SOI le pareti laterali toccano l'ossido spesso (STI): **le capacità di perimetro sono azzerate**.

Risultato netto: **la capacità parassita complessiva di drain nel SOI è dal 50% all'80% più bassa che nel Bulk.**

---

### 3. "Se balla un'armatura balla anche l'altra": perché il SOI isola meglio dal rumore?

Nel **Bulk**, il substrato è un semiconduttore **conduttivo** (ha una sua resistività finita, $\rho \approx 1 \div 10\ \Omega\cdot\text{cm}$).
Quando milioni di porte logiche digitali commutano:
1. **Conduzione resistiva:** Iniettano cariche e portatori di corrente direttamente dentro la massa del substrato. La corrente scorre come in un reticolo di resistenze ($V = R_{sub} \cdot I$) facendo "rimbalzare" il potenziale del substrato sotto un vicino circuito analogico (*Substrate Bounce*).
2. **Effetto Body diretto:** Poiché i transistor Bulk poggiano direttamente su questo silicio conduttivo, se il potenziale del substrato sotto di loro si sposta di $50\text{ mV}$, la tensione $V_{SB}$ cambia e la soglia $V_{th}$ del transistor si sposta per **effetto body**, introducendo rumore enorme nel segnale.

Nel **SOI**:
1. **Barriera dielettrica perfetta:** L'ossido sepolto è un isolante eccezionale (resistività oltre $10^{14}\ \Omega\cdot\text{cm}$). **Nessuna corrente DC o pacchetto di portatori di carica può attraversare fisicamente l'ossido.**
2. **Minore corrente reattiva:** Essendo la capacità $C$ molto più piccola (come visto al punto 2), a parità di "ballo" ($\frac{dV}{dt}$), la corrente di disturbo iniettata $i = C \frac{dV}{dt}$ è drasticamente inferiore.
3. **Nessun contatto galvanico con il canale:** Il canale del transistor non tocca il substrato, eliminando l'effetto body indotto dal rumore del substrato comune.
4. Nelle applicazioni a radiofrequenza (RF-SOI), sotto il BOX si impiega persino un substrato in silicio ad altissima resistività (*High-Resistivity Substrate*, $>1000\ \Omega\cdot\text{cm}$), che dissipa e sopprime quasi del tutto anche i residui campi elettromagnetici ad alta frequenza.