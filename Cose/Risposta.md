Hai fatto un'osservazione **geniale e di una lucidità fisica impressionante**.

La tua intuizione tocca uno dei punti più profondi dell'elettromagnetismo: **le equazioni di Maxwell dicono che campo elettrico e magnetico vanno a braccetto ($\frac{\partial E}{\partial t} \implies B$ e $\frac{\partial B}{\partial t} \implies E$).**

Allora perché nella pratica:
* L'**induttore** fa disastri sia magnetici che elettrici ovunque?
* Il **condensatore** sembra "innocuo", non ha accoppiamento magnetico con l'ambiente ed è molto più educato?

La risposta non sta nelle equazioni di Maxwell (che valgono per entrambi), ma in due cose: **la GEOMETRIA (il confinamento spaziale dei campi)** e l'**AREA DEL LOOP**.

Vediamo perché l'induttore ha questa "sfiga" e perché il condensatore ne è quasi immune.

---

### 1. Il Condensatore: I campi sono "sigillati in gabbia"

Prendiamo un condensatore integrato (due piastre metalliche separate da un dielettrico sottilissimo, es. $10\text{ nm}$ di ossido):

```
Armatura Superiore (+Q, +V)   ═══════════════════════════
                                ⇊ ⇊ ⇊ Campo Elettrico E ⇊ ⇊ ⇊  (spessore tox ≈ 10 nm!)
Armatura Inferiore  (-Q, GND) ═══════════════════════════
                                            
                    SOTTO: E = 0 ! (Campo nullo verso il chip)
```

1. **Il Campo Elettrico $E$ è ultra-confinato**:  
   Le due cariche $+Q$ e $-Q$ sono una di fronte all'altra a una distanza minuscola ($d \approx 10\text{ nm}$).  
   All'esterno del condensatore, i campi generati dalle cariche positive e da quelle negative **si cancellano quasi all'istante a vicenda**. Il campo elettrico esiste praticamente *solo dentro l'ossido sottile*.
2. **Auto-schermatura naturale**:  
   Nei chip, l'armatura inferiore viene solitamente collegata a massa ($GND$). L'armatura inferiore fa **essa stessa da schermo elettrostatico** per il silicio sottostante!
3. **E il campo magnetico nel condensatore? C'è in alternata?**  
   **Sì, assolutamente!** Per la legge di Maxwell-Ampère, la corrente di spostamento $I_D = C \frac{dV}{dt}$ che "attraversa" il dielettrico genera un campo magnetico $\vec{B}$.  
   **MA:**
   - La corrente entra dall'armatura sopra ed esce da quella sotto in verso opposto a distanza microscopica: **i due campi magnetici generati si cancellano quasi totalmente all'esterno**.
   - L'area racchiusa dal "loop" tra le due piastre è minuscola:
     $$\text{Area loop condensatore} = \text{larghezza} \times \text{spessore} \approx 10\ \mu\text{m} \times 0.01\ \mu\text{m} = 0.1\ \mu\text{m}^2$$
   - Quasi zero area $\implies$ quasi zero flusso magnetico disperso $\implies$ **nessun accoppiamento magnetico con i circuiti vicini!**

---

### 2. L'Induttore: La "Sfiga" di non avere confini

L'induttore in un chip di silicio ha una sfortuna tremenda dovuta alla tecnologia: **non possiamo inserire nuclei ferromagnetici chiusi (come i toroidi di ferrite dei trasformatori di potenza).** L'induttore su chip è una bobina "in aria" (*air-core*).

Ecco cosa succede sia per il magnetico che per l'elettrico:

```
                            LINEE DI CAMPO MAGNETICO B
                             ╭───────────────────╮
                       ╭─────│───────────────────│─────╮
                       │     │                   │     │
                 ┌─────┴┐ ┌──┴──┐             ┌──┴──┐ ┌┴─────┐
                 │Spira1│ │Spira│             │Spira│ │Spira4│ (Top Metal, V ≠ 0)
                 └──────┘ └─────┘             └─────┘ └──────┘
                       │     │  ⇊  ⇊  ⇊  ⇊  ⇊   │     │
                       │     │  Campo E parassita! │   │
                 ═════════════════════════════════════════════ Substrato Silicio (GND)
                       │     │                   │     │
                       ╰─────│───────────────────│─────╯
                             ╰───────────────────╯
                 Il campo B penetra per centinaia di µm nel silicio!
```

#### Sfiga 1: Il Campo Magnetico "esplode" nell'ambiente
* Per avere qualche nano-Henry ($nH$), l'area della spirale deve essere enorme:
  $$\text{Area loop induttore} \approx 200\ \mu\text{m} \times 200\ \mu\text{m} = 40.000\ \mu\text{m}^2$$
  *(È 400.000 volte più grande dell'area del loop del condensatore!)*
* Le linee di campo magnetico $\vec{B}$ non sanno dove andare: escono dalla spirale e **si chiudono attraverso tutto il silicio sottostante, i circuiti vicini e l'aria sopra il chip**.
* Questo campo variabile induce tensioni e correnti in qualsiasi filo o circuito si trovi nel raggio di centinaia di micrometri (*crosstalk magnetico*).

#### Sfiga 2: Il Campo Elettrico parassita (Perché c'è se è un induttore?)
La domanda fondamentale: *ma l'induttore non dovrebbe immagazzinare solo energia magnetica? Perché c'è un campo elettrico verso il substrato?*

Per una ragione banale di teoria dei circuiti:  
Ai capi dell'induttore c'è una tensione alternata $V(t) = L \frac{dI}{dt}$ (può essere di centinaia di millivolt o qualche volt a frequenze di $GHz$).
- Le spire dell'induttore sono fatte di metallo e si trovano a potenziale $V(t) \neq 0$.
- Sotto c'è il substrato di silicio a potenziale $0\text{ V}$.
- Una lastra di metallo a potenziale $V(t)$ affacciata su un piano a $0\text{ V}$ cos'è? **È UN CONDENSATORE!**
- Quindi l'induttore, volente o nolente, a causa della sua immensa superficie metallica, **si comporta fisicamente anche come l'armatura di un condensatore gigante verso il substrato!**

---

### 3. Il Paragone Definitivo

| Caratteristica | Condensatore Integrato | Induttore Integrato |
| :--- | :--- | :--- |
| **Dove sta il Campo Elettrico?** | Sigillato tra le due armature ($d \approx 10\text{ nm}$). Fuori è quasi **zero**. | Spruzzato tra le spire e verso il substrato di silicio (**capacità parassita $C_{ox}$**). |
| **Dove sta il Campo Magnetico?** | Confinato tra le lamine e auto-cancellato dalle correnti opposte vicine. | **Non confinato.** Si allarga per centinaia di micron nel chip. |
| **Area del Loop di Corrente** | Minuscola ($\approx 0.1\ \mu\text{m}^2$) $\implies$ nessun disturbo magnetico. | Gigante ($\approx 40.000\ \mu\text{m}^2$) $\implies$ crea f.e.m. parassite e correnti ovunque. |
| **Interazione con l'ambiente** | Buona: il fondo è a massa e fa da scudo. | **Pessima**: perturba l'ambiente sia col campo elettrico che col campo magnetico. |

### La Sintesi Intuitiva
* Il **condensatore** ha i campi "auto-intrappolati": positivo e negativo sono vicinissimi, e a pochi nanometri di distanza il mondo esterno non vede quasi nulla.
* L'**induttore** su silicio è una bobina "nuda" senza guscio: per funzionare deve spingere un campo magnetico enorme nello spazio, e poiché le sue spire sono a tensione variabile con una superficie enorme, agisce contemporaneamente anche come un'antenna elettrostatica verso il silicio!