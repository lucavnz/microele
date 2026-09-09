# Tecniche di Ottimizzazione per Porte Complesse Veloci

Nelle porte logiche CMOS statiche complesse con elevato numero di ingressi, la velocità è fortemente limitata da due fattori fisici (vedi [Effetto di Fan-In e Fan-Out sul Ritardo (Elmore)](./Effetto%20di%20Fan-In%20e%20Fan-Out%20sul%20Ritardo%20(Elmore).md)):
1. Il ritardo di propagazione scala in modo **quadratico con il Fan-In ($FI^2$)** a causa delle catene di transistor in serie e delle loro capacità parassite distribuite (modello RC di Elmore).
2. Il ritardo scala in modo **lineare con il Fan-Out ($FO$)** a causa del carico capacitivo esterno $C_L$.

Per superare la "barriera del Fan-In" ($FI \le 4$) e massimizzare le prestazioni nei percorsi critici dei microprocessori, vengono adottate **5 tecniche circuitali fondamentali**:

```
                       5 TECNICHE PER PORTE COMPLESSE VELOCI
                                       │
     ┌──────────────────┬──────────────┼──────────────┬──────────────────┐
     ▼                  ▼              ▼              ▼                  ▼
1. Progressive     2. Input       3. Alberi      4. Buffer          5. Reduced
      Sizing          Ordering       Logici         Insertion          Swing
  (M1 > M2 > M3)    (Critico su    (De Morgan     (Disaccoppia     (Sense Amplifier
                     nodo OUT)      FI <= 4)       FI da FO)        SRAM/Bitline)
```

---

### 1. Progressive Sizing (Dimensionamento Progressivo dei Transistor in Serie)

In una pila di transistor in serie (es. il Pull-Down di una NAND a 4 ingressi), **i transistor non svolgono lo stesso lavoro di scarica**:
* Quando l'uscita commuta da alto a basso ($1 \to 0$), la corrente che scarica il nodo di uscita $C_L$ deve attraversare l'intera catena.
* Tuttavia, il transistor **$M_1$ (collegato a massa)** deve scaricare verso terra **non solo $C_L$, ma anche tutte le capacità parassite intermedie** dei nodi interni ($C_1, C_2, \dots, C_{N-1}$).
* Al contrario, il transistor **$M_N$ (collegato all'uscita)** vede scorrere esclusivamente la carica immagazzinata su $C_L$.

```
           OUT o───────────────────────── CL (Carico esterno)
               │
              [MN]  (W più piccolo: Req maggiore, ma minimizza Cdb su OUT!)
               │
               ├── CN-1
               │
              [M2]  (W intermedio)
               │
               ├── C1
               │
              [M1]  (W più grande: resistenza Req minima verso GND!)
               │
             ──┴── GND
```

#### Strategia di Dimensionamento:
Anziché dimensionare tutti i transistor con la stessa larghezza ($W_1 = W_2 = \dots = W_N = N \cdot W_{\text{inv}}$):
* Si rende **$M_1$ più largo** ($W_1 > W_2 > \dots > W_N$) per abbattere la resistenza che vede scorrere la carica totale di tutti i nodi.
* Si rende **$M_N$ più stretto**, riducendo drasticamente la capacità parassita di giunzione $C_{db,N}$ affacciata direttamente sul nodo di uscita.
* **Fattore di scaling tipico:** Il rapporto tra transistor adiacenti è compreso tra $1.2$ e $1.5$ ($M_{i} \approx 1.2 \div 1.5 \cdot M_{i+1}$).

> [!WARNING]
> **Attenzione al limite di autosmorzamento (*Self-Loading*):** Allargare eccessivamente $M_1$ e i transistor inferiori aumenta a dismisura le loro capacità di diffusione ($C_1, C_2$). Oltre un certo limite, l'aumento di capacità parassita interna supera il beneficio della riduzione di resistenza, peggiorando il ritardo complessivo (stesso principio analizzato nel [Dimensionamento Progressivo e Tapered Buffer](../Famiglie%20Logiche/Dimensionamento%20Progressivo%20e%20Tapered%20Buffer.md)).

---

### 2. Transistor Ordering (Ordinamento degli Ingressi sul Cammino Critico)

In molti circuiti digitali (es. sommatori con carry-lookahead o ALU), i segnali di ingresso di una porta non arrivano tutti contemporaneamente:
* Alcuni ingressi sono **stabili da molto tempo** (*Early Inputs*).
* Uno specifico ingresso arriva **per ultimo** ed è quello che determina il momento esatto della commutazione (*Late / Critical Input*).

```
                      CONFRONTO ORDINAMENTO INGRESSI
                      
   (A) ORDINAMENTO ERRATO                      (B) ORDINAMENTO OTTIMALE
   
          OUT o──────── CL                            OUT o──────── CL
              │                                           │
             [M2] Gate: IN_lento (Arriva prima)          [M2] Gate: CRITICO (Arriva ultimo!)
              │                                           │
              ├── C1 (Carico a VDD!)                      ├── C1 (GIA' SCARICO A 0V!)
              │                                           │
             [M1] Gate: CRITICO (Arriva ultimo!)         [M1] Gate: IN_lento (GIA' ACCESO!)
              │                                           │
            ──┴── GND                                   ──┴── GND
```

#### Meccanismo Fisico del Risparmio di Ritardo:
* **Configurazione Errata (A):**
  L'ingresso veloce accende $M_2$, mentre il critico $M_1$ è ancora spento. Il nodo intermedio $C_1$ si carica a un potenziale prossimo a $V_{DD} - V_{Tn}$. Quando finalmente il segnale critico accende $M_1$, la catena deve scaricare **sia $C_1$ che $C_L$**, accumulando il massimo ritardo possibile:
  $$t_{pHL} = 0.69 \cdot \left[ R_1 C_1 + (R_1 + R_2) C_L \right]$$

* **Configurazione Ottimale (B):**
  L'ingresso non critico è collegato a $M_1$ (vicino a massa) ed è **già acceso da tempo**: di conseguenza, la capacità intermedia $C_1$ è **già stata pre-scaricata a $0\text{ V}$** prima ancora che arrivi il segnale critico!  
  Quando il segnale critico arriva su $M_2$, l'unica capacità che deve essere scaricata è $C_L$:
  $$t_{pHL, \text{effettivo}} \approx 0.69 \cdot (R_1 + R_2) C_L$$
  Il termine $R_1 C_1$ è stato azzerato durante il tempo morto di attesa, ottenendo una commutazione molto più rapida.

> [!TIP]
> **Regola d'oro di Layout:** Il segnale critico (più tardivo) va **sempre posizionato sul transistor più vicino al nodo di uscita**.

---

### 3. Decomposizione dell'Albero Logico (Alternative Logic Architectures)

La formula di Elmore impone che una porta con Fan-In $N$ abbia un ritardo intrinseco proporzionale a $N^2$.  
Pertanto, una singola porta con $FI = 8$ o $FI = 16$ è proibitiva in termini di velocità.

La soluzione consiste nel **decomporre la funzione booleana complessa in un albero di porte più semplici con $FI \le 4$**, sfruttando i Teoremi di De Morgan:

```
                  DECOMPOSIZIONE DI UNA NAND8
                  
  ARCHITETTURA DIRETTA (LENTA):
  A, B, C, D, E, F, G, H ──► [    NAND 8    ] ──► OUT  (Catena di 8 nMOS in serie, ritardo ~ 8^2 = 64)
  
  ARCHITETTURA AD ALBERO (VELOCE):
  A, B, C, D ──────────────► [ NAND 4 ] ──┐
                                          ├──► [ NOR 2 ] ──► OUT
  E, F, G, H ──────────────► [ NAND 4 ] ──┘
```

#### Dimostrazione Logica (De Morgan):
$$\overline{A \cdot B \cdot C \cdot D \cdot E \cdot F \cdot G \cdot H} = \overline{(A B C D) \cdot (E F G H)} = \overline{X \cdot Y}$$
Poiché non si dispone di porte AND native veloci in CMOS invertente, si applica l'involuzione:
$$\overline{X \cdot Y} = \overline{X} + \overline{Y} \quad \text{oppure} \quad \overline{\overline{\overline{X} + \overline{Y}}}$$
Riorganizzando con porte native invertenti:
$$OUT = \text{NOR2}\left( \overline{\text{NAND4}(A,B,C,D)}, \; \overline{\text{NAND4}(E,F,G,H)} \right)$$
* Il numero massimo di transistor in serie scende da $8$ a **$4$ nel primo stadio e $2$ nel secondo stadio**.
* Il ritardo passa da una dipendenza $O(N^2)$ a una dipendenza logaritmica $O(\log N)$, riducendo il tempo di calcolo di oltre il $60\%$.

---

### 4. Buffer Insertion (Isolare il Fan-In dal Fan-Out)

Nelle porte complesse ad alto Fan-In, la resistenza di uscita equivalente della catena di pull-down è intrinsecamente elevata ($R_{\text{pull-down}} = N \cdot R_{\text{inv}}$).  
Se tale porta deve pilotare direttamente una linea lunga o un elevato carico capacitivo esterno ($FO$ alto $\implies C_L$ grande), il ritardo esplode:
$$t_p \propto R_{\text{complessa}} \cdot C_L$$

```
                           INSERIMENTO DI UN BUFFER
                           
   (A) SENZA BUFFER (LENTO):
   Ingressi ──► [ Porta Complessa ] o────────────────────────────── CL (Enorme)
                (Rout = 4 * Rinv)   │
                                    └── Ritardo = (4 * Rinv) * CL  (Proibitivo!)

   (B) CON BUFFER ISOLANTE (VELOCE):
   Ingressi ──► [ Porta Complessa ] ──o── [ Inverter / Buffer ] ─── CL (Enorme)
                (Rout elevata)        │    (Rout bassissima)
                                     Cin,buf
                                    (Molto piccola!)
```

#### Principio di Funzionamento:
1. La porta logica complessa pilota unicamente la minuscola capacità di ingresso del buffer ($C_{\text{in,buf}} \ll C_L$).
2. Il buffer (avente $FI = 1$ e transistor molto larghi con bassa resistenza $R_{\text{buf}}$) si fa carico di erogare la forte corrente necessaria per caricare e scaricare $C_L$.
3. Sebbene sia stato aggiunto uno stadio logico aggiuntivo, **la somma dei due ritardi parziali è nettamente inferiore al ritardo del singolo stadio non bufferizzato**:
   $$t_{p, \text{totale}} = (R_{\text{complessa}} \cdot C_{\text{in,buf}}) + (R_{\text{buf}} \cdot C_L) \ll R_{\text{complessa}} \cdot C_L$$

---

### 5. Riduzione dell'Escursione Logica con Sense Amplifiers (Reduced Voltage Swing)

Quando il carico capacitivo è enorme (ad esempio le linee di **Bitline** nelle memorie SRAM/DRAM o i bus dati condivisi tra core su un microprocessore), la capacità $C_{\text{bus}}$ può raggiungere svariati picofarad ($pF$).

Ricaricare questa linea per l'intera escursione di alimentazione ($0 \to V_{DD} = 2.5\text{ V}$) richiede un tempo e un'energia enormi:
$$\Delta t = \frac{C_{\text{bus}} \cdot \Delta V}{I_D} \qquad E_{\text{dinamica}} = C_{\text{bus}} \cdot V_{DD}^2$$

```
                   ARCHITETTURA A RIDOTTA ESCURSIONE (SENSE AMP)
                   
   Cella di Memoria         Bitline (Capacità elevata Cbus)
      o Cella Logica ─────► ─────────────────────────────────┐
                            (ΔV ridotto: appena 100-200 mV!)  │
                                                              ▼
                                                   ┌─────────────────────┐
                                                   │   SENSE AMPLIFIER   │ ──► Uscita Full-Swing
                                                   │    (Differenziale)  │     (0V - 2.5V)
                                                   └─────────────────────┘
```

#### Meccanismo Fisico:
* La porta logica o la cella di memoria fa scendere il potenziale della linea di soli **$\Delta V \approx 100 \div 200\text{ mV}$** anziché scaricarla completamente fino a $0\text{ V}$.
* Un amplificatore differenziale ad altissimo guadagno (**Sense Amplifier**, realizzato con una coppia differenziale o con un latch bistabile rigenerativo) rileva questa minuscola differenza di potenziale e la converte istantaneamente in un'uscita digitale a piena escursione (*rail-to-rail*, $0 \div V_{DD}$).
* **Guadagno di velocità:** Il tempo di commutazione della linea viene ridotto di un fattore pari a:
  $$\frac{\Delta V}{V_{DD}} \approx \frac{0.15\text{ V}}{2.5\text{ V}} \approx \frac{1}{16} \implies \mathbf{\text{Velocizzazione di oltre } 15 \times!}$$
* Oltre a garantire frequenze di clock elevatissime, questa tecnica abbatte drasticamente la potenza dinamica consumata sulle linee capacitive globali.

---

### Tabella Comparativa delle Tecniche di Ottimizzazione

| Tecnica | Problema Risolto | Quando si Applica | Costo Hardware / Trade-off |
| :--- | :--- | :--- | :--- |
| **Progressive Sizing** | Sovraccarico dei transistor inferiori nella serie | Catene di serie lunghe ($N \ge 3$) | Aumento area e rischio di self-loading capacitivo |
| **Input Ordering** | Transitori lenti sui cammini critici noti | Presenza di segnali con tempi di arrivo disuguali | Nessun costo di area (solo riordino delle connessioni di gate) |
| **Decomposizione ad Albero** | Dipendenza quadratica dal Fan-In ($FI^2$) | Funzioni logiche con $FI > 4$ | Aumento del numero totale di transistor e porte |
| **Buffer Insertion** | Disaccoppiamento tra alto $FI$ e alto $FO$ | Porte complesse che pilotano carichi pesanti ($C_L \gg$) | Inserimento di 1 o 2 inverter aggiuntivi (lieve latenza fissa) |
| **Reduced Swing + Sense Amp** | Ritardi enormi su bus globali e bitline capacitive | Linee lunghe di interconnessione e memorie SRAM/DRAM | Richiede circuiteria analogica differenziale e segnali di sincronismo (strobe) |

---

*Pagine correlate:*
- [Effetto di Fan-In e Fan-Out sul Ritardo (Elmore)](./Effetto%20di%20Fan-In%20e%20Fan-Out%20sul%20Ritardo%20(Elmore).md)
- [Dimensionamento Transistor e Ritardo di Pattern (Sizing)](./Dimensionamento%20Transistor%20e%20Ritardo%20di%20Pattern%20(Sizing).md)
- [Dimensionamento Progressivo e Tapered Buffer](../Famiglie%20Logiche/Dimensionamento%20Progressivo%20e%20Tapered%20Buffer.md)
- [Ritardo di Propagazione e Dimensionamento dell'Inverter CMOS](../Famiglie%20Logiche/Ritardo%20di%20Propagazione%20e%20Dimensionamento%20dell'Inverter%20CMOS.md)
- [Coppia Differenziale e Cascode Telescopico](../Dispositivi%20e%20Componenti/Coppia%20Differenziale%20e%20Cascode%20Telescopico.md)
