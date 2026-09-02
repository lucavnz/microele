In microelettronica, integrare una capacità $C$ richiede di bilanciare occupazione di area, complessità di processo e linearità. I condensatori integrati si realizzano principalmente sfruttando il polisilicio, i transistor MOS o i livelli di metallizzazione.

---

### 1. Condensatore MOS vs Poly-Poly (PIP) e il Costo delle Maschere

Per realizzare un condensatore planare classico abbiamo due strade principali:

* **Il Condensatore MOS (MOSCap):**
  Si sfrutta la capacità di gate di un transistor MOSFET (tra Gate e canale, con Source e Drain cortocircuitati).
  * *Vantaggio:* **Zero maschere aggiuntive** (usa i passaggi standard del transistor) e dielettrico sottilissimo ($t_{ox}$ piccolo $\implies C_{ox}$ elevata).
  * *Svantaggio:* Fortemente **non lineare** con la tensione (la capacità varia drasticamente se il canale non è formato).
  👉 Approfondimento sulla fisica e i regimi del MOS: [La soglia da cosa dipende](./La%20soglia%20da%20cosa%20dipende.md)

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
  👉 Vedi: [Difficoltà nel fare un componente ideale](../Scaling%20e%20Limiti%20Fisici/Difficolt%C3%A0%20nel%20fare%20un%20componente%20ideale.md) per l'effetto parassita analogo tra le piste vicine.

---

### 4. Non-Linearità con la Tensione e Coefficiente $V_L$ (VCC)

La capacità di un condensatore reale varia con la tensione $V$ applicata tra le armature secondo lo sviluppo in serie:

$$C(V) = C_0 \left\{ 1 + V_L \cdot V + V_Q \cdot V^2 + \dots \right\}$$

* **$C_0$:** capacità nominale a tensione nulla ($V = 0\text{ V}$).
* **$V_L$ ($VCC$ - *Voltage Coefficient of Capacitance*):** variazione lineare espressa in $\text{ppm/V}$ ($10^{-6}/\text{V}$).

#### Perché la capacità varia con la tensione? (Fisica dei Semiconduttori vs Metalli)

```
          A) POLARIZZAZIONE DI SVUOTAMENTO (Depletion)
                     Tensione Positiva (+)
               ┌───────────────────────────────┐
               │    Armatura Superiore (+)     │
               ├───────────────────────────────┤
               │       Ossido (t_ox)           │
               ├───────────────────────────────┤
  xd(V) ──►    │ ░░ Regione di Svuotamento ░░  │ ◄── Portatori respinti!
  (Isolante)   ├───────────────────────────────┤
               │   Silicio tipo p (Substrato)  │
               └───────────────────────────────┘
                     C_tot = C_ox // C_dep  (C crolla!)

          B) POLARIZZAZIONE DI ACCUMULAZIONE
                     Tensione Negativa (-)
               ┌───────────────────────────────┐
               │    Armatura Superiore (-)     │
               ├───────────────────────────────┤
               │       Ossido (t_ox)           │
               ├───────────────────────────────┤
               │ +++++++++++++++++++++++++++++ │ ◄── Portatori attirati all'interfaccia!
               │   Silicio tipo p (Substrato)  │
               └───────────────────────────────┘
                     C_tot ≈ C_ox  (C massima)
```

1. **Nei Metalli (MIM):** la densità di elettroni liberi è enorme ($n \approx 10^{23}\,\text{cm}^{-3}$). Le cariche si accumulano sulla superficie geometrica; non esiste svuotamento, la distanza $d = t_{ox}$ è rigidamente fissa e **$V_L \approx 10\text{ ppm/V}$ (linearità quasi perfetta)**.
2. **Nei Semiconduttori (MOSCap e Poly-Cap / PIP):**
   * **Svuotamento (*Depletion*):** Se il campo elettrico respinge i portatori liberi dall'interfaccia con l'ossido, si crea una **regione di carica spaziale svuotata** di spessore $x_d(V) \propto \sqrt{V}$. Questa regione priva di cariche agisce come un secondo dielettrico in serie:
     $$\frac{1}{C_{\text{tot}}(V)} = \frac{1}{C_{ox}} + \frac{1}{C_{\text{dep}}(V)} \implies C_{\text{tot}}(V) < C_{ox}$$
   * **Accumulazione:** Invertendo la polarità, i portatori maggioritari vengono richiamati a ridosso dell'ossido, $x_d \to 0$ e la capacità torna al valore massimo $C_{ox}$.
   * **Poly-Depletion nel PIP:** Nel condensatore Poly-Poly entrambe le armature sono in polisilicio drogato ($n^+$). Applicando una tensione, mentre la piastra negativa va in accumulazione, la piastra positiva subisce un lieve **svuotamento superficiale (*poly depletion*)** di spessore nanometrico, generando una debole dipendenza $V_L \approx 20\text{ ppm/V}$.

---

### 5. Tabella Comparativa delle Tecnologie di Condensatori

| Caratteristica | MOSCap ($C_{ox}$) | PIP (Poly-Poly) | MIM (Metal-Insulator-Metal) |
| :--- | :--- | :--- | :--- |
| **Materiali Armature** | Poly / Silicio attivo | Polisilicio 1 / Polisilicio 2 | Metallo 1 / Metallo 2 (o $\text{TiN}$) |
| **Costo Industriale** | **Zero maschere extra** | **1 maschera extra** ($\text{Poly2}$) | **Maschere extra** per strato MIM |
| **Linearità ($V_L$)** | **Pessima** ($500\text{ ppm/V}$); crolla se non polarizzato | **Buona** ($20\text{ ppm/V}$), lieve *poly depletion* | **Eccellente** ($10\text{ ppm/V}$), insensibile a $V$ |
| **Densità ($C_0$)** | Alta ($\approx 1.5\,\text{fF}/\mu\text{m}^2$) | Buona ($\approx 1.0\,\text{fF}/\mu\text{m}^2$) | Minore ($\approx 0.3\,\text{fF}/\mu\text{m}^2$, più area) |
| **Tensione Massima** | Limitata dalla rottura $t_{ox}$ | Buona | **Elevata** ($V < 15\text{ V}$) |
| **Resistenza Serie $R_s$** | Alta (diffusione di silicio) | Media ($\approx 50\,\Omega/\square$) | **Bassissima** ($\text{m}\Omega/\square$) |
| **Campi di Applicazione** | Disaccoppiamento di alimentazione | Filtri analogici a capacità commutate (SC) | **Circuiti analogici e RF di alta precisione** |

---

### 6. Effetti Parassiti, Rottura Dielettrica e Regole di Layout

1. **Rottura del Dielettrico (*Breakdown*):** L'ossido sottile supporta un campo limite operativo di circa **$7\,\text{MV/cm}$**. Campi superiori causano perforazione irreversibile del dielettrico (*punch-through*).
2. **Capacità di Bordo (*Fringing*):**
   $$C_{\text{tot}} = c_{\text{area}} \cdot \text{Area} + c_{\text{perimetro}} \cdot \text{Perimetro}$$
   Nei rapporti precisi, tutti i condensatori devono mantenere lo **stesso rapporto Area/Perimetro ($A/P$)**.
3. **Schermatura dal Substrato (Top Plate vs Bottom Plate):** L'armatura inferiore ha una forte capacità parassita verso il substrato di silicio; l'armatura superiore è schermata. Nel circuito, l'armatura superiore va **sempre connessa al nodo a più alta impedenza** (es. l'ingresso invertente dell'amplificatore).

👉 Per le tecniche di matching (matrice di celle unitarie, angoli a $135^\circ$, anelli di guardia e baricentro comune), vedi: [Matching e Variabilita nei Componenti Integrati](./Matching%20e%20Variabilita%20nei%20Componenti%20Integrati.md).

---

*Pagine correlate:*
- [Matching e Variabilita nei Componenti Integrati](./Matching%20e%20Variabilita%20nei%20Componenti%20Integrati.md)
- [Potenza Dinamica e Dissipazione di Carica](../Famiglie%20Logiche/Potenza%20Dinamica%20e%20Dissipazione%20di%20Carica.md)
- [Diodo](./Diodo.md)
- [Transitori del diodo e capacità](./Transitori%20del%20diodo%20e%20capacita.md)
- [MOS](./MOS.md)
- [La soglia da cosa dipende](./La%20soglia%20da%20cosa%20dipende.md)
- [Resistore](./Resistore.md)
- [Induttore](./Induttore.md)
- [Narrow resistenze](./Narrow%20resistenze.md)
- [Difficoltà nel fare un componente ideale](../Scaling%20e%20Limiti%20Fisici/Difficolt%C3%A0%20nel%20fare%20un%20componente%20ideale.md)
- [Wafer produzione](../Tecnologia%20e%20Fabbricazione/Wafer%20produzione.md)