# Prontuario Stadi Elementari a MOSFET e Specchi Cascode

Perfetto, andiamo con ordine: prima capiamo **come si specchia la corrente in basso** nel tuo circuito (chi comanda e perché), e subito dopo trovi il **prontuario completo di tutti gli stadi elementari** da imparare a memoria per l'orale!

---

# PARTE 1: Chi comanda nello specchio in basso (M5, M6, M7, M8)?

Nel tuo circuito il carico inferiore è uno **specchio di corrente cascode NMOS**.
I transistor sono così disposti:
* Ramo sinistro (di riferimento): **M5** (sopra) e **M7** (sotto), entrambi con drain cortocircuitato al gate (connessi a diodo).
* Ramo destro (uscita): **M6** (sopra) e **M8** (sotto).

```
   (da M3)
      │
      ▼  i_in
   ┌──┴──┐
   │ M5  │ (diodo cascode) ─── Gate M6 (cascode)
   └──┬──┘                       │
      │                          ▼
   ┌──┴──┐                     ┌───┐
   │ M7  │ (diodo master)  ─── │M8 │ (slave di corrente)
   └──┬──┘                     └───┘
     GND                        GND
```

### 1. Come circola la corrente?
La corrente $i_{d3}$ scende dal drain di M3 ed entra nel ramo sinistro:
1. Attraversa prima **M5**.
2. Poi attraversa **M7** e va a massa.
Essendo in serie, **in M5 e M7 scorre esattamente la stessa corrente**.

### 2. Chi è che comanda la specchiatura?
Il vero **master dello specchio di corrente è M7** (in coppia con **M8**):
* **M7** ha il source a massa fissa ($0\,\text{V}$) e il drain cortocircuitato al suo gate. La corrente che vi scorre impone una ben precisa tensione $V_{GS7}$.
* Il gate di M7 è collegato direttamente al gate di M8.
* Anche **M8** ha il source a massa fissa ($0\,\text{V}$). Quindi si ritrova $V_{GS8} = V_{GS7}$.
* Poiché hanno stessa $V_{GS}$ e stesse dimensioni ($W/L$), **M8 è forzato a replicare (specchiare) esattamente la stessa corrente di M7** con rapporto $1:1$!

### 3. E allora M5 a cosa serve?
**M5 serve solo a polarizzare il cascode M6:**
* Se mettessimo solo M7 e M8, la resistenza vista dall'uscita verso il basso sarebbe solo $r_{o8}$.
* Per aumentare la resistenza di uscita serve un cascode (M6 sopra M8).
* Ma il gate di M6 deve trovarsi a un potenziale tale da tenere M8 in saturazione ($V_{D8} \ge V_{OV8}$).
* Cortocircuitando il drain di M5 al suo gate e collegandolo al gate di M6, M5 genera automaticamente la tensione di gate ideale per polarizzare M6.
* Quindi **M5 imposta la tensione di cascode**, mentre **M7 fissa la corrente specchiata da M8**.

---

# PARTE 2: Il Bignami degli Stadi Elementari a MOSFET
*(Assumiamo effetto body trascurabile $\eta = 0$ e canale lungo, ideale per l'esame).*

---

### 1. Transistor a Diodo (Gate cortocircuitato a Drain)
Non è un amplificatore, ma un **bipolo equivalente a due terminali** (Gate+Drain assieme vs Source).

| Parametro | Valore |
| :--- | :--- |
| **Resistenza equivalente $r_{eq}$** | $r_{eq} = \frac{1}{g_m} \parallel r_o \approx \mathbf{\frac{1}{g_m}}$ |
| **A cosa serve?** | Serve per creare **bassa impedenza**: come carico attivo (es. amplificatori a carico a diodo) o come ramo di riferimento negli specchi di corrente per convertire una corrente in tensione $V_{GS}$. |

---

### 2. Common Source (Source Comune - CS)
È il classico amplificatore di tensione ad alto guadagno.

| Caratteristica | Dettaglio |
| :--- | :--- |
| **Ingresso** | **Gate** |
| **Uscita** | **Drain** |
| **Terminale comune** | **Source** (a massa AC) |
| **Resistenza d'ingresso $R_{in}$** | $\mathbf{\infty}$ (a basse frequenze il gate è isolato dall'ossido) |
| **Resistenza d'uscita $R_{out}$** | $\mathbf{r_o}$ (in parallelo all'eventuale carico $R_D$) |
| **Guadagno di tensione $A_v$** | $\mathbf{-g_m (r_o \parallel R_D) \approx -g_m R_D}$ *(Invertente! Il segno meno è fondamentale)* |
| **Guadagno di corrente $A_i$** | $\mathbf{\infty}$ (assorbe corrente nulla in ingresso) |
| **Ruolo tipico** | **Amplificatore di tensione** e convertitore tensione-corrente ($i_{out} = g_m v_{in}$). |

> **Variante con Degenerazione di Source ($R_S$ sul source):**
> * $R_{in} = \infty$
> * $R_{out} \approx r_o (1 + g_m R_S) \approx \mathbf{g_m r_o R_S}$ *(aumenta tantissimo l'impedenza di uscita!)*
> * $A_v \approx -\frac{g_m R_D}{1 + g_m R_S} \approx \mathbf{-\frac{R_D}{R_S}}$ *(guadagno ridotto ma molto più lineare e stabile).*

---

### 3. Common Drain (Drain Comune - CD o Source Follower)
È l'inseguitore di tensione.

| Caratteristica | Dettaglio |
| :--- | :--- |
| **Ingresso** | **Gate** |
| **Uscita** | **Source** |
| **Terminale comune** | **Drain** (collegato ad alimentazione $V_{DD}$, quindi massa AC) |
| **Resistenza d'ingresso $R_{in}$** | $\mathbf{\infty}$ |
| **Resistenza d'uscita $R_{out}$** | $\mathbf{\frac{1}{g_m} \parallel r_o \parallel R_S \approx \frac{1}{g_m}}$ *(BASSISSIMA!)* |
| **Guadagno di tensione $A_v$** | $\mathbf{\frac{g_m R_S}{1 + g_m R_S} \approx +1}$ *(Non invertente, appena inferiore a 1)* |
| **Guadagno di corrente $A_i$** | $\mathbf{\infty}$ |
| **Ruolo tipico** | **Buffer di tensione** (adattatore di impedenza: alta impedenza in ingresso, bassa in uscita per pilotare carichi pesanti senza perdere segnale). |

---

### 4. Common Gate (Gate Comune - CG)
È l'inseguitore di corrente (current buffer). È proprio quello che fa il tuo cascode M3/M4!

| Caratteristica | Dettaglio |
| :--- | :--- |
| **Ingresso** | **Source** |
| **Uscita** | **Drain** |
| **Terminale comune** | **Gate** (polarizzato a tensione fissa $V_B$, quindi massa AC) |
| **Resistenza d'ingresso $R_{in}$** | $\mathbf{\frac{r_o + R_D}{1 + g_m r_o} \approx \frac{1}{g_m}}$ *(BASSISSIMA!)* |
| **Resistenza d'uscita $R_{out}$** | $\mathbf{r_o + (1 + g_m r_o) R_S \approx g_m r_o R_S}$ *(ALTISSIMA, amplifica la $R_S$ del generatore)* |
| **Guadagno di tensione $A_v$** | $\mathbf{+g_m (r_o \parallel R_D) \approx +g_m R_D}$ *(Non invertente)* |
| **Guadagno di corrente $A_i$** | $\mathbf{\approx 1}$ *(La corrente che entra dal source esce quasi identica dal drain!)* |
| **Ruolo tipico** | **Buffer di corrente** (assorbe corrente su un nodo a bassa impedenza $1/g_m$ e la trasferisce inalterata su un nodo ad altissima impedenza). Elimina l'effetto Miller. |

---

### 5. Stadio Cascode (CS + CG)
Mette insieme un Source Comune in basso (M1/M2) e un Gate Comune in alto (M3/M4):

* **Ingresso:** Gate del CS inferiore.
* **Uscita:** Drain del CG superiore.
* **Resistenza d'ingresso:** $R_{in} = \mathbf{\infty}$.
* **Resistenza d'uscita:** $R_{out} \approx \mathbf{g_{m,casc} \cdot r_{o,casc} \cdot r_{o,cs}}$ *(moltiplica la resistenza di un fattore $g_m r_o \sim 50\div 100$)*.
* **Transconduttanza complessiva:** $G_m \approx \mathbf{g_{m,cs}}$.
* **Guadagno di tensione:** $A_v = -G_m R_{out} \approx \mathbf{-g_{m,cs} (g_{m,casc} r_{o,casc} r_{o,cs})}$.
* **Ruolo tipico:** Permette di ottenere **guadagni enormi ($60\div 80\,\text{dB}$) in un singolo stadio**, isolando l'ingresso dall'uscita (zero effetto Miller).

---

### Tabella riassuntiva "salva-esame":

| Stadio                   | Ingresso  |   Uscita   |    $R_{in}$     |       $R_{out}$       |         $A_v$          |        $A_i$         | Funzione principale                                     |
| :----------------------- | :-------: | :--------: | :-------------: | :-------------------: | :--------------------: | :------------------: | :------------------------------------------------------ |
| **Diodo**                |    D+G    |     S      | $\approx 1/g_m$ |    $\approx 1/g_m$    |           —            |          —           | Carico attivo / Riferimento                             |
| **CS (Source Comune)**   |   Gate    |   Drain    |    $\infty$     |         $r_o$         |       $-g_m R_L$       |       $\infty$       | Amplificatore di tensione                               |
| **CD (Source Follower)** |   Gate    |   Source   |    $\infty$     |    $\approx 1/g_m$    |      $\approx +1$      |       $\infty$       | **Buffer di tensione** (alta $R_{in}$, bassa $R_{out}$) |
| **CG (Gate Comune)**     |  Source   |   Drain    | $\approx 1/g_m$ | $\approx g_m r_o R_S$ |       $+g_m R_L$       | $\approx \mathbf{1}$ | **Buffer di corrente / Cascode**                        |
| **Cascode (CS + CG)**    | Gate (CS) | Drain (CG) |    $\infty$     |  $\approx g_m r_o^2$  | $\approx -(g_m r_o)^2$ |       $\infty$       | Altissimo guadagno $A_v$, no Miller                     |
**Bravissimo! Hai avuto un'intuizione PAZZESCA ed è assolutamente corretta!** 👏

La risposta è: **SÌ, concettualmente SONO LA STESSA IDENTICA COSA!**

Perché? Perché in entrambi i casi stai guardando **dentro lo stesso identico terminale: il SOURCE del MOSFET, con il GATE a massa AC!**

* Nel **Drain Comune** (Source Follower): l'uscita è prelevata dal **Source**.
* Nel **Gate Comune**: l'ingresso è applicato sul **Source**.

In entrambi i casi, il transistor visto dal source ha un'impedenza intrinseca pari a:
$$R_{source} \approx \mathbf{\frac{1}{g_m}}$$

---

### La "Formula Madre" che unisce tutto

Se calcoli l'impedenza guardando dentro il source di un MOSFET (con il gate a massa AC e una qualsiasi resistenza $R_D$ collegata al drain), la formula generale esatta è **una sola per entrambi**:

$$R_{source} = \frac{r_o + R_D}{1 + g_m r_o}$$

Guarda cosa succede nei due stadi applicando questa stessa formula:

#### 1. Nel Drain Comune (CD)
Il Drain è collegato direttamente all'alimentazione $V_{DD}$ (che per il piccolo segnale è una **massa AC**). Quindi non c'è resistenza sul drain: **$R_D = 0$**.

Sostituendo $R_D = 0$ nella formula:
$$R_{source} = \frac{r_o + 0}{1 + g_m r_o} = \frac{r_o}{1 + g_m r_o} = \frac{1}{g_m + \frac{1}{r_o}} = \mathbf{\frac{1}{g_m} \parallel r_o \approx \frac{1}{g_m}}$$

*(L'unica cosa in più è che se sul source c'è collegato un carico esterno o una polarizzazione $R_S$, la $R_{out}$ totale sarà $R_{source} \parallel R_S \approx \frac{1}{g_m}$).*

#### 2. Nel Gate Comune (CG)
Il Drain è collegato a un carico di drain $R_D$. 
Spezziando la frazione della formula:
$$R_{in,CG} = \frac{r_o}{1 + g_m r_o} + \frac{R_D}{1 + g_m r_o} \approx \mathbf{\frac{1}{g_m} + \frac{R_D}{g_m r_o}}$$

Vedi? C'è sempre quel termine fondamentale **$\frac{1}{g_m}$**! 
C'è solo un pezzettino in più ($\frac{R_D}{g_m r_o}$) dovuto al fatto che sul drain c'è $R_D$. Ma poiché al denominatore c'è $g_m r_o \gg 1$ (fattore $50 \div 100$), quel pezzetto è molto piccolo, e quindi anche qui:
$$R_{in,CG} \approx \mathbf{\frac{1}{g_m}}$$

---

### In sintesi, la regola d'oro per l'orale:

> **"Ogni volta che guardo dentro il SOURCE di un transistor con il Gate a massa AC, vedo sempre un'impedenza bassissima, pari all'incirca a $\mathbf{1/g_m}$."**
> * Se sono in un **Drain Comune**, sto guardando l'uscita $\to R_{out} \approx 1/g_m$.
> * Se sono in un **Gate Comune**, sto guardando l'ingresso $\to R_{in} \approx 1/g_m$.

Questo tipo di collegamento logico è esattamente quello che fa capire a una commissione d'esame che **hai capito la fisica del circuito** e non hai solo imparato a memoria una tabella di formule!