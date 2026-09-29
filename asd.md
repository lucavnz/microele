# Guida al Recycling Folded Cascode (RFC) e Scelta di K=3

Ecco la guida **definitiva e passo-passo** per dominare il **Recycling Folded Cascode (RFC)** all'esame, sia a livello concettuale sia nel calcolo a piccolo segnale, con lo schema circuitale e la spiegazione del perché **$K = 3$**.

---

### 1. Il problema di partenza: lo "spreco" nel Folded Cascode Classico

Nel Folded Cascode classico hai:
1. Una coppia differenziale PMOS in alto, alimentata dalla corrente di coda $2I_B$ ($I_B$ per ramo).
2. Ai due nodi di ripiegamento (**nodi di folding $F_L$ e $F_R$**) ci sono due transistor NMOS verso massa polarizzati con una tensione DC fissa sul gate ($V_{bias}$).
3. Ciascuno di questi due transistor verso massa deve assorbire sia la corrente dell'ingresso ($I_B$) sia quella del cascode ($I_{casc}$):
   $$I_{sink} = I_B + I_{casc}$$

#### Il "peccato originale":
Quei due transistor verso massa bruciano **più della metà di tutta la corrente del circuito**, ma per il segnale AC hanno il Gate a massa virtuale ($v_{gs} = 0 \implies i_{ac} = 0$). **Sono rami "morti" che non contribuiscono né al guadagno né alla transconduttanza!**

L'idea dell'RFC è:  
> *«Invece di lasciare quei transistor fissi in DC, possiamo **riciclarli** per farli amplificare il segnale d'ingresso senza consumare un solo microampere in più?»*

---

### 2. Lo Schema Circuitale dell'RFC: Come viene modificato

Per fare il "riciclo" si fanno due modifiche geniali:

```text
                      +VDD
                        │
                      [ 2IB ]  (Generatore di coda)
                        │
         ┌──────────────┴──────────────┐
         │                             │
    ┌────┴────┐                   ┌────┴────┐
    │ M1a M1b │                   │ M2b M2a │   Coppia d'ingresso sdoppiata in 4:
    │(W/2)(W/2)│                  │(W/2)(W/2)│   ciascuno porta IB/2
    └─┬─────┬─┘                   └─┬─────┬─┘
Vin+ ─┤     │                      │     ├─ Vin-
      │     │  (Incrocio AC)       │     │
      │     └────────────┐   ┌─────┘     │
      │                  ▼   ▼           │
Nodo  │                                  │  Nodo
 FL   ●──────────────────────────────────●   FR
      │                                  │
      ├───► Ai Cascode NMOS              ├───► Ai Cascode NMOS
      │     e all'uscita VOUT            │     e all'uscita VOUT
      │                                  │
    ┌─┴─────┐   ┌───────┐      ┌───────┐   ┌─────┴─┐
    │  M3b  │   │  M3a  │      │  M4a  │   │  M4b  │   Specchi di corrente (1 : K)
    │  (K)  │   │  (1)  │      │  (1)  │   │  (K)  │   I rami K scaricano a GND!
    └───┬───┘   └───┬───┘      └───┬───┘   └───┬───┘
        │   Gate    │ (diodo)      │ (diodo)   │   Gate
        └─── condividono ──┘      └─── condividono ──┘
        │           │              │           │
       GND         GND            GND         GND
```

1. **Sdoppiamento della coppia PMOS:**  
   Ogni ramo d'ingresso viene diviso in due transistor di taglia dimezzata ($W/2$):
   * A sinistra: $M_{1a}$ e $M_{1b}$ (entrambi pilotati da $V_{in}^+$).
   * A destra: $M_{2a}$ e $M_{2b}$ (entrambi pilotati da $V_{in}^-$).  
   Ciascun transistor conduce metà corrente: $I_D' = \frac{I_B}{2}$.  
   La loro transconduttanza intrinseca è dimezzata: $g_m' = \frac{1}{2} g_{m0}$.

2. **Sostituzione dei transistor DC con Specchi di Corrente ($1 : K$):**
   * I transistor $M_{1a}$ e $M_{2a}$ scendono **dritti** sui nodi di folding ($F_L$ e $F_R$). Questo è il **Percorso Diretto**.
   * I transistor $M_{1b}$ e $M_{2b}$ vengono **incrociati**:
     * $M_{1b}$ (pilotato da $V_{in}^+$) scarica nel diodo $M_{4a}$ (taglia $1$, a destra).
     * $M_{2b}$ (pilotato da $V_{in}^-$) scarica nel diodo $M_{3a}$ (taglia $1$, a sinistra).
   * I transistor di uscita dello specchio ($M_{3b}$ e $M_{4b}$) hanno taglia **$K$** e sono collegati direttamente tra i nodi di folding e **massa (GND)**.

---

### 3. Analisi a Piccolo Segnale Passo per Passo

Applichiamo una tensione differenziale pura all'ingresso:
$$v_{in}^+ = +\frac{v_{in}}{2}, \qquad v_{in}^- = -\frac{v_{in}}{2}$$

Seguiamo cosa succede **al nodo di folding destro $F_R$** (che pilota l'uscita $V_{OUT}$):

#### Passo 1: Il contributo del percorso diretto ($M_{2a}$)
Il transistor $M_{2a}$ è un PMOS pilotato da $v_{in}^- = -v_{in}/2$.  
La corrente di segnale che inietta nel nodo $F_R$ è:
$$i_{dir} = - g_{m2a} \cdot v_{in}^- = - \left(\frac{1}{2} g_{m0}\right) \left(-\frac{v_{in}}{2}\right) = +\frac{1}{4} g_{m0} \cdot v_{in}$$

#### Passo 2: Il contributo del percorso riciclato ($M_{1b} \to M_{4a} \to M_{4b}$)
1. Sul ramo sinistro, il PMOS $M_{1b}$ è pilotato da $v_{in}^+ = +v_{in}/2$.  
   La sua corrente di drain vale:
   $$i_{1b} = - g_{m1b} \cdot v_{in}^+ = - \left(\frac{1}{2} g_{m0}\right) \left(+\frac{v_{in}}{2}\right) = -\frac{1}{4} g_{m0} \cdot v_{in}$$
   *(Il segno meno significa che conduce meno corrente rispetto alla DC).*
2. Questa corrente entra nel diodo $M_{4a}$ a destra.
3. Lo specchio di corrente moltiplica questa corrente per il fattore dimensionale **$K$** sul transistor $M_{4b}$:
   $$i_{4b} = K \cdot i_{1b} = - K \left(\frac{1}{4} g_{m0} \cdot v_{in}\right)$$

#### Passo 3: Legge di Kirchhoff al Nodo di Folding $F_R$
Al nodo di folding $F_R$:
* Dall'alto arriva la corrente dell'ingresso $i_{dir}$.
* Verso il basso, il transistor $M_{4b}$ aspira la corrente $i_{4b}$ verso massa.
* La rimanente corrente $i_{casc}$ è costretta a salire/scendere attraverso il transistor Cascode $M_6$ verso il nodo di uscita:

$$i_{casc} = i_{dir} - i_{4b} = \left(+\frac{1}{4} g_{m0} v_{in}\right) - \left(- K \frac{1}{4} g_{m0} v_{in}\right)$$

I due contributi si sommano in fase:
$$i_{casc} = \left(\frac{1 + K}{4}\right) g_{m0} \cdot v_{in}$$

Tenendo conto del contributo speculare sull'altro ramo differenziale (oppure considerando l'ingresso differenziale completo $v_{id}$), la **transconduttanza equivalente totale $G_m$ dell'amplificatore** è:

$$\mathbf{G_{m,RFC} = \left(\frac{1 + K}{2}\right) g_{m0}}$$

---

### 4. Perché si sceglie proprio $K = 3$?

Guarda cosa succede alla formula quando sostituisci **$K = 3$**:

$$G_{m,RFC} = \left(\frac{1 + 3}{2}\right) g_{m0} = \mathbf{2 \cdot g_{m0}}$$

A **parità identica di corrente assorbita dall'alimentatore**:
1. **Transconduttanza raddoppiata ($2 \times G_m$)**
2. **Guadagno di tensione raddoppiato ($+6\,\text{dB}$):**
   $$A_v = G_m \cdot R_{out} \implies A_{v,RFC} \approx 2 \cdot A_{v,classico}$$
3. **Banda a guadagno unitario raddoppiata ($2 \times GBW$):**
   $$GBW = \frac{G_m}{2\pi C_L} = \mathbf{2 \cdot GBW_{classico}}$$
4. **Slew Rate migliorato:** a grande segnale lo specchio $K$ scarica la capacità di carico $C_L$ con una corrente moltiplicata per $K$.

---

### 5. La domanda da lode: *"Perché allora non mettiamo $K = 10$ o $K = 50$?"*

Se aumentare $K$ aumenta il guadagno, perché fermarsi a 3? **Per colpa del Margine di Fase!**

1. **Il nodo a diodo ha una capacità parassita:**  
   Il gate del transistor a specchio $M_{4b}$ ha una larghezza $K$ volte quella del diodo.  
   La capacità parassita vista sul gate è la somma delle due:
   $$C_{nodo} \approx C_{gs,diodo} + C_{gs,K} = (1 + K) C_{gs1}$$

2. **Nasce un polo non dominante nello specchio:**  
   La resistenza vista sul diodo è $1/g_{m,diodo}$. Quindi la frequenza del polo introdotto dallo specchio vale:
   $$\omega_{p,\text{specchio}} \approx \frac{g_{m,diodo}}{C_{nodo}} = \mathbf{\frac{g_{m,diodo}}{(1 + K) C_{gs1}}}$$

3. **Il crollo della stabilità:**
   * Se scegli un $K$ troppo grande (es. $K = 8$ o $10$), il denominatore $(1+K)$ diventa enorme.
   * Il polo $\omega_{p,\text{specchio}}$ **crolla a frequenze basse** e si avvicina alla frequenza di cross-over ($GBW$).
   * Un polo vicino a $GBW$ introduce un ritardo di fase di quasi $-90^\circ$, facendo **crollare il Margine di Fase ($PM$)** sotto i $45^\circ \div 60^\circ$: l'amplificatore inizia a sovraoscillare (*ringing*) o peggio diventa un oscillatore instabile!

Inoltre, se $K$ è troppo grande, il transistor di taglia $K$ richiede una tensione di overdrive diversa e ruba swing di tensione.

> 💡 **La sintesi perfetta da dire all'esame:**  
> *"Si sceglie $K = 3$ (o tipicamente tra $2$ e $4$) perché rappresenta il punto di compromesso (*sweet spot*) ottimale: raddoppia la transconduttanza ($G_m = 2g_m$) e il guadagno a costo zero in potenza, mantenendo contemporaneamente il polo dello specchio a frequenza sufficientemente alta da garantire un margine di fase stabile ($PM \ge 60^\circ$)."*