# Effetto di Fan-In e Fan-Out sul Ritardo (Modello di Elmore)

Nelle porte logiche [CMOS](../Famiglie%20Logiche/Inverter%20CMOS%20e%20Regioni%20di%20Funzionamento.md), il ritardo di propagazione $t_p$ è fortemente penalizzato da due parametri architetturali fondamentali:
1. **Fan-In ($\text{FI}$):** Il numero di ingressi della singola porta.
2. **Fan-Out ($\text{FO}$):** Il numero di ingressi delle porte a valle collegate al nodo di uscita.

---

### 1. Il Modello RC Distribuito di Elmore per la Catena di Pull-Down (Slide 28)

Consideriamo una porta **NAND a 4 ingressi (NAND4)**. La rete di pull-up ha 4 pMOS in parallelo, mentre la rete di pull-down ha **4 nMOS in serie** collegati a massa:

```text
                         VDD
           ┌──────┬───────┼───────┬──────┐
           │      │       │       │      │
          [A]    [B]     [C]     [D]    (4 pMOS in parallelo)
           │      │       │       │      │
           └──────┴───────┬───────┴──────┘
                          o──────────────── OUT (Capacità di carico CL)
                          │
                         [A]  nMOS (Reqn)
                          │
                          ├── C3 (Capacità parassita nodo intermedio 3)
                          │
                         [B]  nMOS (Reqn)
                          │
                          ├── C2 (Capacità parassita nodo intermedio 2)
                          │
                         [C]  nMOS (Reqn)
                          │
                          ├── C1 (Capacità parassita nodo intermedio 1)
                          │
                         [D]  nMOS (Reqn)
                          │
                         GND
```

Ciascun nMOS presenta una resistenza di canale accesa $R_{eqn}$. Tra un transistor e l'altro risiede una sacca di diffusione drogata che crea un nodo capacitivo parassita verso il substrato ($C_1, C_2, C_3$).

#### A) Derivazione dei Pesi della Formula di Elmore
Secondo il **modello di ritardo di Elmore**, il tempo impiegato per scaricare una rete RC ad albero/linea è la somma dei contributi di ciascun condensatore moltiplicato per la **resistenza totale che la sua carica incontra per raggiungere la massa**:

* La carica su **$C_1$** (nodo sopra $D$) attraversa **solo il transistor $D$** $\implies R_{\text{vista}} = \mathbf{1 \cdot R_{eqn}}$.
* La carica su **$C_2$** attraversa **$D$ e $C$** $\implies R_{\text{vista}} = \mathbf{2 \cdot R_{eqn}}$.
* La carica su **$C_3$** attraversa **$D$, $C$ e $B$** $\implies R_{\text{vista}} = \mathbf{3 \cdot R_{eqn}}$.
* La carica su **$C_L$** (nodo di uscita) deve attraversare **tutti e 4 i transistor** ($D, C, B, A$) $\implies R_{\text{vista}} = \mathbf{4 \cdot R_{eqn}}$.

Sommando tutti i percorsi e moltiplicando per il fattore di commutazione $\ln(2) \approx 0.69$:
$$\mathbf{t_{pHL} = 0.69 \cdot R_{eqn} \cdot \left( C_1 + 2C_2 + 3C_3 + 4C_L \right)}$$

---

### 2. Perché il Ritardo di Scarica cresce in modo QUADRATICO ($N^2$)?

Se generalizziamo a una porta con $N$ ingressi in serie ($\text{FI} = N$):
* La resistenza vista dall'$i$-esimo condensatore è proporzionale a $i \cdot R_{eqn}$.
* La sommatoria delle capacità parassite interne vale:
  $$\tau_{int} = \sum_{i=1}^{N-1} i \cdot R_{eqn} \cdot C_{int} = R_{eqn} \cdot C_{int} \cdot \frac{N(N-1)}{2} \propto \mathbf{N^2}$$
* Anche se allarghiamo i transistor ($W \propto N$) per abbattere la resistenza in serie ($R_{eqn} \propto 1/N$), l'area dei transistor cresce di $N$ volte, e con essa aumentano proporzionalmente le [Capacità parassite nel MOSFET](../Dispositivi%20e%20Componenti/Capacit%C3%A0%20parassite%20nel%20MOSFET.md) interne ($C_{int} \propto N$).
* Di conseguenza, il prodotto $(R_{eqn}/N) \cdot (N C_{int}) \cdot \frac{N^2}{2}$ conserva la dipendenza **quadratica rispetto al Fan-In ($O(N^2)$)**.

---

### 3. Asimmetria: $t_{pHL}$ (Quadratico) vs $t_{pLH}$ (Lineare) (Slide 29)

Il grafico del ritardo in funzione del Fan-In mette in luce una forte disparità:

```text
  tp [ps]
   1250 │                                       / tpHL (QUADRATICO: N^2)
        │                                      /
   1000 │                                    /
        │                                  /  - - - tp medio
    750 │                                /
        │                             _ /
    500 │                         _ -
        │                     _ -
    250 │                _ - 
        │          _ - - ───────────────────────── tpLH (LINEARE: N)
      0 └───┬──────┬──────┬──────┬──────┬──────┬──────
            2      4      6      8     10     12     14   Fan-In
```

1. **$t_{pHL}$ (scarica, serie):** cresce come **$N^2$** a causa dell'effetto scala di Elmore.
2. **$t_{pLH}$ (carica, parallelo):** cresce in modo **strettamente lineare ($N$)**.
   * Nella PUN della NAND, tutti i pMOS sono in parallelo tra $V_{DD}$ e OUT.
   * Nel caso peggiore conduce un solo pMOS (resistenza costante $R_p$).
   * Aggiungere un ingresso significa solo saldare un altro drain a OUT, aggiungendo un incremento capacitivo costante $\Delta C_{drain}$ al carico:
     $$t_{pLH} = 0.69 \cdot R_p \cdot (C_{L,\text{ext}} + N \cdot C_{drain}) \propto \mathbf{N}$$

> **Regola d'oro del progettista VLSI:**  
> **"Gates with a fan-in greater than 4 should be avoided."**  
> Oltre i 4 ingressi, una singola porta monolitica diventa intollerabilmente lenta. È sempre preferibile scomporla in un albero logico gerarchico a 2 o 4 ingressi (vedi [Tecniche di Ottimizzazione per Porte Complesse Veloci](./Tecniche%20di%20Ottimizzazione%20per%20Porte%20Complesse%20Veloci.md)).

---

### 4. Perché $0.69 = \ln(2)$?

Nei circuiti digitali, il ritardo di propagazione $t_p$ si misura convenzionalmente quando la forma d'onda della tensione attraversa la soglia al **$50\%$ dell'escursione totale** ($V_{out} = 0.5 V_{DD}$).

Durante la scarica di un condensatore $C$ attraverso una resistenza equivalente $R$:
$$v(t) = V_{DD} \cdot e^{-\frac{t}{RC}}$$
Imponendo $v(t) = 0.5 V_{DD}$:
$$0.5 V_{DD} = V_{DD} \cdot e^{-\frac{t}{RC}} \implies e^{-\frac{t}{RC}} = 0.5$$
Applicando il logaritmo naturale ad ambo i membri:
$$-\frac{t}{RC} = \ln(0.5) = -\ln(2) \implies \mathbf{t = \ln(2) \cdot RC \approx 0.693 \cdot RC}$$

---

### 5. Comportamento a Grandi Segnali delle Capacità di Drain-Body ($C_{db}$)

Un dubbio tipico riguarda il motivo per cui le capacità di Drain-Body dei pMOS (collegate tra $V_{out}$ e $V_{DD}$) siano da considerarsi **in parallelo** al condensatore di carico $C_L$ (collegato tra $V_{out}$ e massa) anche in regime digitale di **grandi segnali**:

```text
                           VDD (Tensione costante nel tempo, dVDD/dt = 0!)
                            │
                           === Cdb
                            │
       Corrente pMOS        │
     ────────────────► o────┴────o──────── Vout(t)
                       │
                      === CL
                       │
                      GND (Tensione costante nel tempo!)
```

1. **Equazione di Corrente:**
   La corrente totale che deve erogare il transistor per far commutare il nodo è:
   $$i_{\text{tot}}(t) = i_{C_L}(t) + i_{C_{db}}(t) = C_L \frac{d(V_{out} - 0)}{dt} + C_{db} \frac{d(V_{out} - V_{DD})}{dt}$$
   Poiché l'alimentazione è ideale e costante nel tempo, $\frac{d(V_{DD})}{dt} = 0$. Dunque:
   $$\mathbf{i_{\text{tot}}(t) = (C_L + C_{db}) \cdot \frac{dV_{out}}{dt}}$$
2. **Bilancio di Carica $\Delta Q$:**
   Per far compiere a $V_{out}$ un'escursione completa $0 \to V_{DD}$:
   * $C_L$ passa da $0\text{ V}$ a $V_{DD} \implies \Delta Q_1 = C_L \cdot V_{DD}$.
   * $C_{db}$ passa da $V_{DD}$ a $0\text{ V}$ $\implies \Delta Q_2 = C_{db} \cdot V_{DD}$.
   * La carica totale erogata dal transistor è:
     $$\mathbf{\Delta Q_{\text{tot}} = (C_L + C_{db}) \cdot V_{DD}}$$

Qualsiasi capacità affacciata sul nodo di uscita e ancorata a una tensione fissa (continua) richiede corrente proporzionale a $\frac{dV_{out}}{dt}$ e si comporta **esattamente in parallelo a $C_L$**.

---

### 6. Dipendenza dal Fan-Out e la Formula Generale (Slide 30 – 31)

Ogni porta logica collegata all'uscita aggiunge al nodo la capacità dei propri gate: $C_{in} = C_{gn} + C_{gp}$.  
Se la nostra porta pilota $\text{FO}$ carichi identici, la capacità totale vale:
$$C_L = C_{\text{intrinseca}} + \text{FO} \cdot C_{in}$$

Il ritardo cresce in modo **strettamente lineare con il Fan-Out**:
$$t_p = 0.69 R_{eq} C_{\text{intrinseca}} + \left(0.69 R_{eq} C_{in}\right) \cdot \mathbf{\text{FO}}$$

#### La Formula Analitica Unificata:
Riassumendo tutti gli effetti in una singola espressione:

$$\mathbf{t_p = a_1 \cdot \text{FI} + a_2 \cdot \text{FI}^2 + a_3 \cdot \text{FO}}$$

| Coefficiente | Dipendenza | Meccanismo Fisico |
| :--- | :---: | :--- |
| **$a_2 \cdot \text{FI}^2$** | **Quadratica con Fan-In** | Reti in **serie** (nMOS nella NAND, pMOS nella NOR). Crescita contemporanea di resistenze e nodi capacitivi interni (effetto Elmore). |
| **$a_1 \cdot \text{FI}$** | **Lineare con Fan-In** | Reti in **parallelo**. Ogni ingresso in più aggiunge un drain in parallelo affacciato su OUT, incrementando $C_{db}$. |
| **$a_3 \cdot \text{FO}$** | **Lineare con Fan-Out** | Porte guidate a valle. Ogni porta in più aggiunge due capacità di gate ($C_g$ nMOS e pMOS) a $C_L$. |

---

*Pagine correlate:*
- [Dimensionamento Transistor e Ritardo di Pattern (Sizing)](./Dimensionamento%20Transistor%20e%20Ritardo%20di%20Pattern%20(Sizing).md)
- [Tecniche di Ottimizzazione per Porte Complesse Veloci](./Tecniche%20di%20Ottimizzazione%20per%20Porte%20Complesse%20Veloci.md)
- [Ratioed Logic e DCVSL](./Ratioed%20Logic%20e%20DCVSL.md)
- [Pass-Transistor Logic e Level Restorer](./Pass-Transistor%20Logic%20e%20Level%20Restorer.md)
- [Dimensionamento Progressivo e Tapered Buffer](../Famiglie%20Logiche/Dimensionamento%20Progressivo%20e%20Tapered%20Buffer.md)
- [Ritardo di Propagazione e Dimensionamento dell'Inverter CMOS](../Famiglie%20Logiche/Ritardo%20di%20Propagazione%20e%20Dimensionamento%20dell'Inverter%20CMOS.md)
- [Capacità parassite nel MOSFET](../Dispositivi%20e%20Componenti/Capacit%C3%A0%20parassite%20nel%20MOSFET.md)
