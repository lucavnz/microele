# Dimensionamento dei Transistor e Ritardo di Pattern nei Circuiti CMOS

Nelle porte logiche combinatorie statiche [CMOS](../Famiglie%20Logiche/Inverter%20CMOS%20e%20Regioni%20di%20Funzionamento.md), la velocità di commutazione e il ritardo di propagazione dipendono sia dalla topologia della rete (Pull-Up e Pull-Down) sia dal **pattern specifico degli ingressi**. 

Per garantire prestazioni stabili e confrontabili con un invertitore di riferimento, i transistor di una porta complessa devono essere dimensionati (*Transistor Sizing*) in base al cammino di conduzione nel caso peggiore (*worst-case*).

---

### 1. Dipendenza del Ritardo dai Pattern di Ingresso (NAND2)

Prendiamo come modello di riferimento una porta **NAND a due ingressi (NAND2)**:
* **Pull-Up Network (PUN):** 2 pMOS in **parallelo** tra $V_{DD}$ e l'uscita (pilotati da $A$ e $B$).
* **Pull-Down Network (PDN):** 2 nMOS in **serie** tra l'uscita e massa (pilotati da $A$ e $B$).

```text
                VDD
           ┌─────┴─────┐
           │           │
         [Rp]        [Rp]       <-- 2 pMOS in PARALLELO
         A \         B \
           │           │
           └─────┬─────┘
                 o──────── OUT (CL)
                 │
                [Rn]   B        <-- 2 nMOS in SERIE
                 │
                 ├── Cint       (Capacità parassita del nodo intermedio)
                 │
                [Rn]   A
                 │
                GND
```

#### A) Transizione Low-to-High ($0 \to 1$ all'uscita, spegnimento ingressi)
La corrente di carica fluisce dall'alimentazione $V_{DD}$ verso il condensatore $C_L$ attraverso la PUN:
* **Entrambi gli ingressi vanno a 0 ($A=B=1 \to 0$):** Entrambi i pMOS conducono contemporaneamente. Le due resistenze $R_p$ sono in parallelo, per cui la resistenza equivalente è dimezzata:
  $$R_{eq} = R_p \parallel R_p = \frac{R_p}{2} \implies t_{pLH} \approx 0.69 \cdot \left(\frac{R_p}{2}\right) C_L$$
* **Un solo ingresso va a 0 (es. $A=0, B=1$):** Conduce un solo pMOS. La resistenza di carica è l'intera $R_p$:
  $$t_{pLH} \approx 0.69 \cdot R_p \cdot C_L \quad (\mathbf{\text{Ritardo raddoppiato!}})$$

#### B) Transizione High-to-Low ($1 \to 0$ all'uscita, accensione ingressi)
Per scaricare $C_L$ verso massa, devono accendersi **entrambi** gli nMOS in serie ($A=B=1$). La corrente attraversa due canali in cascata:
$$R_{eq} = R_n + R_n = 2R_n \implies t_{pHL} \approx 0.69 \cdot (2R_n) \cdot C_L$$

#### C) Validazione Sperimentale / Simulativa SPICE (Slide 25 di combin.pdf)
I risultati di simulazione per una tecnologia CMOS sub-micrometrica con $C_L = 100\text{ fF}$ confermano l'analisi analitica:

| Transizione | Pattern Ingressi | Ritardo $t_p$ [ps] | Spiegazione Fisica |
| :--- | :---: | :---: | :--- |
| **Basso $\to$ Alto** | $A=B=1 \to 0$ | **$45\text{ ps}$** | Entrambi i pMOS accesi in parallelo ($R_p/2$). |
| **Basso $\to$ Alto** | $A=1, B=1 \to 0$ | **$80\text{ ps}$** | Solo pMOS $B$ acceso ($R_p$). |
| **Basso $\to$ Alto** | $A=1 \to 0, B=1$ | **$81\text{ ps}$** | Solo pMOS $A$ acceso ($R_p$). |
| **Alto $\to$ Basso** | $A=B=0 \to 1$ | **$67\text{ ps}$** | Entrambi nMOS accendono, scarica nodo interno $C_{int}$ e $C_L$. |
| **Alto $\to$ Basso** | $A=1, B=0 \to 1$ | **$64\text{ ps}$** | $A$ era già a 1 ($C_{int}$ già scaricato a massa). |
| **Alto $\to$ Basso** | $A=0 \to 1, B=1$ | **$61\text{ ps}$** | $B$ era già a 1 ($C_{int}$ era carico a $V_{DD}-V_{Tn}$). |

> Il ritardo di scarica dipende anche da chi commuta per primo: la capacità del nodo intermedio $C_{int}$ tra i due nMOS deve essere scaricata a massa, alterando leggermente il tempo di discesa.

---

### 2. Criterio di Dimensionamento (Transistor Sizing)

L'obiettivo del dimensionamento è fare in modo che la porta logica complessa presenti, **nel caso peggiore (*worst-case*)**, la stessa identica resistenza equivalente (e quindi la stessa capacità di pilotaggio) di un **invertitore unitario simmetrico di riferimento** (vedi [Ritardo di Propagazione e Dimensionamento dell'Inverter CMOS](../Famiglie%20Logiche/Ritardo%20di%20Propagazione%20e%20Dimensionamento%20dell'Inverter%20CMOS.md)):
* L'nMOS unitario ha taglia $W_n = 1$ e resistenza di canale $R_n$.
* Poiché la mobilità delle lacune è circa metà di quella degli elettroni ($\mu_n \approx 2\mu_p$), a parità di dimensioni un pMOS presenta resistenza doppia:
  $$\mathbf{R_p = 2 R_n}$$
* Per bilanciare un invertitore, il pMOS viene fatto largo il doppio: $W_p = 2 \implies R_{pMOS} = \frac{R_p}{2} = \frac{2R_n}{2} = R_n$.

---

### 3. La Notazione e la Regola del Prodotto: `[Serie] x [Tipo]`

La taglia di ciascun transistor in una porta complessa è calcolata come il prodotto di **due fattori**:

$$\mathbf{\text{Taglia } W = \underbrace{N_{\text{serie}}}_{\text{Fattore Topologico}} \;\times\; \underbrace{\text{Fattore Tecnologico}}_{\text{1 per nMOS, 2 per pMOS}}}$$

1. **Fattore Topologico ($N_{\text{serie}}$):** Quanti transistor conducono **in serie** lungo quel percorso nel caso peggiore.
   * Se ci sono $N$ transistor in serie, ciascuno deve essere allargato di $N$ volte affinché la somma delle loro resistenze dia la resistenza base:
     $$\sum_{i=1}^N \frac{R}{N} = R$$
   * Se i transistor sono in parallelo, nel caso peggiore ne conduce uno solo $\implies N_{\text{serie}} = 1$.
2. **Fattore Tecnologico:**
   * Per un **nMOS:** vale **$1$** (ha mobilità piena).
   * Per un **pMOS:** vale **$2$** (perché $R_p = 2R_n$, serve il doppio della larghezza per eguagliare la conduttanza dell'nMOS).

---

### 4. Confronto Dettagliato: NAND2 vs NOR2

```text
           NAND2                                   NOR2
       (PUN parallelo,                         (PUN serie,
         PDN serie)                             PDN parallelo)
 
   pMOS A: 1x2    pMOS B: 1x2             pMOS B: 2x2
        \             /                        \
         └─────┬─────┘                          [Rp]
               │                                │
            OUT (CL)                      pMOS A: 2x2
               │                                \
   nMOS B: 2x1                                  [Rp]
         \                                      │
        [Rn]                                 OUT (CL)
         │                                      │
   nMOS A: 2x1                            ┌─────┴─────┐
         \                                │           │
        [Rn]                         nMOS A: 1x1  nMOS B: 1x1
         │                                │           │
        GND                              GND         GND
```

| Porta | Transistor | $N_{\text{serie}}$ | Fattore Tipo | Notazione | Taglia $W$ | Resistenza Worst-Case |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **NAND2** | **nMOS (A, B)** | $2$ (in serie) | $1$ (nMOS) | **`2x1`** | **$2$** | $\frac{R_n}{2} + \frac{R_n}{2} = \mathbf{R_n}$ |
| **NAND2** | **pMOS (A, B)** | $1$ (in parallelo) | $2$ (pMOS) | **`1x2`** | **$2$** | $\frac{R_p}{2} = \frac{2R_n}{2} = \mathbf{R_n}$ |
| **NOR2** | **pMOS (A, B)** | $2$ (in serie) | $2$ (pMOS) | **`2x2`** | **$4$** | $\frac{R_p}{4} + \frac{R_p}{4} = \frac{2R_n}{4} + \frac{2R_n}{4} = \mathbf{R_n}$ |
| **NOR2** | **nMOS (A, B)** | $1$ (in parallelo) | $1$ (nMOS) | **`1x1`** | **$1$** | $\frac{R_n}{1} = \mathbf{R_n}$ |

#### Perché i progettisti evitano le porte NOR a favore delle NAND?
* Nella **NAND**, la taglia massima dei transistor è pari a **$2$**.
* Nella **NOR**, i pMOS devono essere dimensionati a **`2x2 = 4`**: transistor enormi, che consumano una quantità spropositata di area sul silicio e introducono gigantesche [Capacità parassite nel MOSFET](../Dispositivi%20e%20Componenti/Capacit%C3%A0%20parassite%20nel%20MOSFET.md), rallentando pesantemente le commutazioni.

---

### 5. Esempio su Porta Complessa: $OUT = \overline{D + A \cdot (B + C)}$

Consideriamo la porta complessa mostrata a Slide 27 di `combin.pdf`:

```text
                     VDD
                      │
               ┌──────┴──────┐
               │             │
              [A]           [B]
               │             │
               │            [C]
               │             │
               └──────┬──────┘
                      │
                     [D] (pMOS in serie a monte)
                      │
                      o────────────────── OUT
                      │
               ┌──────┴──────┐
               │             │
              [D]           [A]
               │             │
               │       ┌─────┴─────┐
               │       │           │
               │      [B]         [C]
               │       │           │
               └───────┴─────┬─────┘
                             │
                            GND
```

1. **Pull-Down Network (nMOS):**
   * Il ramo $D$ ha un solo nMOS $\implies \mathbf{W_D = 1}$.
   * Il ramo alternativo attraversa $A$ in serie con ($B$ o $C$). Il cammino peggiore attraversa 2 transistor $\implies \mathbf{W_A = 2, \; W_B = 2, \; W_C = 2}$.
   * Verifica resistenza PDN:
     * Percorso $D$: $R_n / 1 = R_n$.
     * Percorso $A + B$: $R_n / 2 + R_n / 2 = R_n$.
2. **Pull-Up Network (pMOS):**
   * Il transistor $D$ è in serie con l'intero blocco superiore.
   * Ramo $D + A$: 2 pMOS in serie $\implies W_D = 4, \; W_A = 4$.
     $$R_{eq} = \frac{R_p}{4} + \frac{R_p}{4} = \frac{R_p}{2} = R_n$$
   * Ramo $D + B + C$: 3 pMOS in serie ($D$, $B$, $C$).
     Poiché $W_D = 4$, la sua resistenza è $R_p/4$. I transistor $B$ e $C$ devono fornire complessivamente l'altra metà $R_p/4$. Essendo due in serie, ciascuno deve valere $R_p/8 \implies \mathbf{W_B = 8, \; W_C = 8}$!
     $$R_{eq} = \frac{R_p}{4} + \frac{R_p}{8} + \frac{R_p}{8} = \frac{R_p}{2} = R_n$$

---

*Pagine correlate:*
- [Effetto di Fan-In e Fan-Out sul Ritardo (Elmore)](./Effetto%20di%20Fan-In%20e%20Fan-Out%20sul%20Ritardo%20(Elmore).md)
- [Tecniche di Ottimizzazione per Porte Complesse Veloci](./Tecniche%20di%20Ottimizzazione%20per%20Porte%20Complesse%20Veloci.md)
- [Ratioed Logic e DCVSL](./Ratioed%20Logic%20e%20DCVSL.md)
- [Pass-Transistor Logic e Level Restorer](./Pass-Transistor%20Logic%20e%20Level%20Restorer.md)
- [Ritardo di Propagazione e Dimensionamento dell'Inverter CMOS](../Famiglie%20Logiche/Ritardo%20di%20Propagazione%20e%20Dimensionamento%20dell'Inverter%20CMOS.md)
- [Inverter CMOS e Regioni di Funzionamento](../Famiglie%20Logiche/Inverter%20CMOS%20e%20Regioni%20di%20Funzionamento.md)
- [Capacità parassite nel MOSFET](../Dispositivi%20e%20Componenti/Capacit%C3%A0%20parassite%20nel%20MOSFET.md)
- [Layout e Tecniche di Progettazione dei MOS](../Dispositivi%20e%20Componenti/Layout%20e%20Tecniche%20di%20Progettazione%20dei%20MOS.md)
