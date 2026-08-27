In microelettronica, integrare una capacità $C$ richiede di bilanciare occupazione di area, complessità di processo e linearità. I condensatori integrati si realizzano principalmente sfruttando il polisilicio, i transistor MOS o i livelli di metallizzazione.

---

### 1. Condensatore MOS vs Poly-Poly (PIP) e il Costo delle Maschere

Per realizzare un condensatore planare classico abbiamo due strade principali:

* **Il Condensatore MOS (MOSCap):**
  Si sfrutta la capacità di gate di un transistor MOSFET (tra Gate e canale, con Source e Drain cortocircuitati).
  * *Vantaggio:* **Zero maschere aggiuntive** (usa i passaggi standard del transistor) e dielettrico sottilissimo ($t_{ox}$ piccolo $\implies C_{ox}$ elevata).
  * *Svantaggio:* Fortemente **non lineare** con la tensione (la capacità varia drasticamente se il canale non è formato).

* **Il Condensatore Poly-Poly ($\text{Poly1}$-$\text{Poly2}$ / PIP):**
  Due strati di polisilicio conduttivo separati da un sottile ossido dielettrico dedicato.
  * *Il problema del "costo":* richiede una **maschera extra** ($\text{Poly2}$). In camera bianca ogni maschera in più non è solo il costo materiale della lastra con i dettagli in cromo nero, ma comporta un intero ciclo industriale aggiuntivo: stesura fotoresist, allineamento fotolitografico, esposizione, sviluppo chimico, etching e lavaggio.
  * *La regola d'oro:* i processi sono rigidamente standardizzati; meno passaggi si fanno, minore è la probabilità di difetti e scarti di fabbricazione (*yield*).

---

### 2. Regola di Layout Poly-Poly: Piastre Sfalsate e Vias

Nei condensatori Poly-Poly la piastra superiore ($\text{Poly2}$) viene disegnata **leggermente più piccola** rispetto alla piastra inferiore ($\text{Poly1}$), lasciando un bordo che sporge:
* La sporgenza permette di realizzare i **vias verticali di contatto** per scendere sul piatto inferiore in un'area sicura.
* Si evita di posizionare i contatti "in mezzo al lago" (sopra l'area attiva), prevenendo stress meccanici e il rischio di perforare l'ossido sottile durante l'incisione, che manderebbe le due piastre in cortocircuito.

---

### 3. Geometrie per Aumentare l'Area: Trench, Metallo (MIM) e Strutture a Pettine

Per aumentare la capacità senza consumare troppa superficie orizzontale di wafer:

* **Scavare in profondità (Trench Capacitors):** si scavano trincee/pozzi verticali nel silicio, accumulando carica sulle pareti verticali nel volume del substrato (approccio tipico delle celle di memoria DRAM).
* **Condensatori Metallo-Metallo (MIM - *Metal-Insulator-Metal*):** realizzati tra due livelli di metallizzazione separati da un dielettrico isolante.
* **Strutture a Pettine / Interdigitate (MOM - *Metal-Oxide-Metal* / *Fringe Caps*):**
  Le armature vengono realizzate come "dita" metalliche affiancate e intrecciate sullo stesso livello (come le dita di una mano inserite tra quelle dell'altra) o su più livelli sovrapposti a griglia 3D. In questo modo si sfrutta la **capacità di frangia laterale** tra i bordi delle piste, massimizzando $C$ con zero maschere extra.
  👉 Vedi: [Difficoltà nel fare un componente ideale](./Difficolt%C3%A0%20nel%20fare%20un%20componente%20ideale.md) per l'effetto parassita analogo tra le piste vicine.

---

*Pagine correlate:*
- [Diodo](./Diodo.md)
- [MOS](./MOS.md)
- [Resistore](./Resistore.md)
- [Induttore](./Induttore.md)
- [Difficoltà nel fare un componente ideale](./Difficolt%C3%A0%20nel%20fare%20un%20componente%20ideale.md)
- [Wafer produzione](./Wafer%20produzione.md)