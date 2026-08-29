In microelettronica (soprattutto in applicazioni a radiofrequenza RF, oscillatori VCO, amplificatori LNA e filtri integrati), l'**induttore integrato a spirale** è uno dei componenti più critici, ingombranti e difficili da realizzare in modo ideale.

---

### 1. Il Problema dell'Area e del Costo

Nei chip planari in silicio (CMOS/BiCMOS), gli induttori si realizzano sagomando i livelli metallici più alti (*Top Metal*) a forma di spirale (quadrata, ottagonale o circolare):

$$L_S \approx \mu_0 \frac{n^2 r_{medio}^2}{2 r_{medio} - a}$$

* **Area enorme = Costo altissimo:** Per ottenere induttanze utili ($1 \div 10\text{ nH}$) servono spirali con diametri di centinaia di micrometri (es. $200 \times 200\ \mu\text{m}^2$). In un circuito integrato, l'area di silicio corrisponde direttamente al costo economico del die; un solo induttore può occupare lo spazio di centinaia o migliaia di transistor!
* **Metalli spessi in alto:** Per ridurre la resistenza parassita serie ($R_S$) del metallo e allontanarsi il più possibile dal silicio, si usano gli strati metallici più spessi e superficiali (es. Metal 5, Metal 6 o metallizzazioni in Rame / Alluminio spesso).

---

### 2. I Tre Grandi Parassiti dell'Induttore (La "Sfiga" del Componente)

Mentre un componente ideale accumula solo energia nel campo magnetico, l'induttore reale su silicio soffre di tre gravi interazioni parassite con l'ambiente circostante:

#### A. Capacità Parassita verso il Substrato ($C_{ox}$) e Perdite nel Silicio ($R_1$)
* Ai capi dell'induttore c'è una tensione alternata $V(t) = L \frac{dI}{dt} \neq 0$.
* L'enorme superficie metallica della spirale a potenziale $V(t)$ si affaccia sul substrato di silicio sottostante ($P\text{-sub}$), che si trova a massa ($0\text{ V}$): **la spirale si comporta fisicamente come l'armatura di un condensatore parassita gigante ($C_{ox}$)** verso il substrato.
* Poiché il silicio è un semiconduttore drogato con resistività finita ($\rho \approx 1 \div 10\ \Omega\cdot\text{cm}$), a frequenze di GHz l'impedenza capacitiva crolla e le correnti di spostamento entrano nel silicio.
* Queste correnti scorrono nella resistenza del substrato ($R_1$), **dissipando energia per effetto Joule e crollando il rendimento del circuito**.

#### B. Accoppiamento Orizzontale Inter-Spira ($C_P$) e Frequenza di Autorisonanza ($f_{SRF}$)
* I tratti metallici adiacenti della spirale corrono affiancati lungo la direzione orizzontale a distanza ravvicinata.
* Tra una spira e la successiva c'è una caduta di potenziale, che dà origine a una **capacità parassita laterale distribuita ($C_P$)** in parallelo all'induttore.
* **Frequenza di Autorisonanza ($f_{SRF}$):**  
  $$f_{SRF} = \frac{1}{2\pi \sqrt{L_S C_P}}$$  
  Oltre questa frequenza limite, l'ammettenza capacitiva $j\omega C_P$ supera quella induttiva $\frac{1}{j\omega L_S}$: la corrente "scavalca" le spire attraverso $C_P$ e **l'induttore smette di funzionare da induttore, comportandosi a tutti gli effetti come un condensatore!**

#### C. Campo Magnetico Disperso e Correnti Parassite (*Eddy Currents*)
* L'induttore su silicio è una bobina aperta senza nucleo ferromagnetico chiuso (*air-core*). Le linee del campo magnetico $\vec{B}(t)$ non sono confinate: penetrano nel substrato e possono concatenarsi con i circuiti vicini (*crosstalk* induttivo).
* Il flusso magnetico variabile $\frac{d\Phi_B}{dt}$ induce f.e.m. nel silicio conduttivo sottostante, generando **correnti parassite vorticose (correnti di Foucault)**.
* Per la **Legge di Lenz**, queste correnti circolari generano un campo magnetico contrario a quello dell'induttore, riducendo l'induttanza effettiva ($L_{eff} \downarrow$) e aumentando le perdite.

---

### 3. La Schermatura: Piastra Continua vs Patterned Ground Shield (PGS)

Per eliminare il campo elettrico verso il silicio conduttivo, verrebbe spontaneo inserire una lamina metallica a massa ($GND$) tra l'induttore e il substrato:

```
    A. PIASTRA METALLICA CONTINUA (DISASTRO MAGNETICO):
    ┌─────────────────────────┐
    │   Induttore (Spirale)   │  ---> Produce B(t) variabile
    └─────────────────────────┘
    ───────────────────────────
    │ ↺  ↺  ↺  ↺  ↺  ↺  ↺  ↺  │  ---> Correnti circolari di Foucault nel metallo!
    ───────────────────────────       Per Legge di Lenz ammazzano il campo B e l'induttanza L!
          Substrato Silicio
```

* **Perché la piastra continua fallisce:** Pur facendo da gabbia di Faraday elettrostatica (bloccando $E$), la piastra metallica continua offre un circuito chiuso a bassissima resistenza per le correnti parassite magnetiche. L'induttanza crolla e le perdite sono enormi.

#### La Soluzione: Lo Schermo a Pettine (Patterned Ground Shield - PGS)
Si realizza una griglia metallica (es. su *Metal 1* o polisilicio siliciurato) **tagliata a strisce/fettine isolate (a dita di pettine)**, collegate a massa solo da una barra dorsale comune:

```
    B. SCHERMO A PETTINE / PGS (SOLUZIONE OTTIMALE):
    ┌─────────────────────────┐
    │   Induttore (Spirale)   │
    └─────────────────────────┘
    ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  ---> Dita metalliche a massa separate da tagli isolanti
    │ | │ | │ | │ | │ | │ | │ |       1) Campo E termina a massa sulle lamelle (E = 0 sotto)
    ═══════════════════════════       2) Circuiti chiusi per B INTERROTTI (niente eddy currents)
          Substrato Silicio
```

1. **Per il campo elettrico:** Le dita metalliche sono a $0\text{ V}$. Le linee di campo elettrico $E$ terminano sulle lamelle e la carica viene scaricata a massa attraverso il metallo anziché dissipare nel silicio. Sotto lo schermo, la d.d.p. verso il substrato è $\Delta V = 0 - 0 = 0\text{ V}$, quindi **il campo elettrico nel silicio si azzera**.
2. **Per il campo magnetico:** I tagli isolanti interrompono fisicamente i percorsi circolari. Le correnti vorticose non possono chiudersi in loop ($R_{loop} \to \infty$); il flusso $\vec{B}$ attraversa i tagli senza essere cancellato e $L_S$ resta intatta.

---

### 4. Circuito Equivalente a $\pi$ e Fattore di Merito $Q$

Il modello circuitale compatto dell'induttore integrato tiene conto di tutti questi effetti fisici:

```
          ┌─────── L_S ─────── R_S ───────┐
   IN ────┤                               ├──── OUT
          ├────────────── C_P ────────────┤
          │                               │
       ┌──┴──┐                         ┌──┴──┐
       │Cox/2│                         │Cox/2│  (Capacità dell'ossido verso lo schermo/substrato)
       └──┬──┘                         └──┬──┘
          ├──────────────┐                ├──────────────┐
       ┌──┴──┐        ┌──┴──┐          ┌──┴──┐        ┌──┴──┐
       │ C1  │        │ R1  │          │ C1  │        │ R1  │  (Resistenza e capacità del silicio)
       └──┬──┘        └──┬──┘          └──┬──┘        └──┬──┘
          └──────┬───────┘                └──────┬───────┘
                GND                             GND
```

Il **Fattore di Qualità ($Q$)** misura l'efficienza dell'induttore:

$$Q = 2\pi \frac{\text{Energia Magnetica Immagazzinata}}{\text{Energia Dissipata in Calore per Ciclo}} \approx \frac{\omega L_S}{R_{serie} + R_{substrato}}$$

* **Senza schermo:** Le perdite nel silicio ($R_1$) fanno crollare il fattore di merito a valori mediocri ($Q \approx 3 \div 6$).
* **Con schermo PGS:** La dissipazione nel silicio viene schermata ($R_1 \to \infty$ nel ramo di perdita verso terra), permettendo a $Q$ di raddoppiare o triplicare ($Q \approx 10 \div 15$).

---

### 5. Perché il Condensatore NON ha questi problemi con il Campo Magnetico?

Rispetto all'induttore, il condensatore integrato è un componente molto più "pulito" ed educato:

| Aspetto | Condensatore Integrato | Induttore Integrato |
| :--- | :--- | :--- |
| **Confinamento del Campo $E$** | **Ultra-confinato** tra le due armature adiacenti ($t_{ox} \approx 10\text{ nm}$). All'esterno il campo è quasi nullo. | **Disperso** nell'ossido e verso il substrato di silicio ($C_{ox}$ parassita). |
| **Comportamento con il Campo $B$** | La corrente entra da un'armatura ed esce dall'altra in verso opposto a distanza microscopica: **i due campi magnetici si cancellano all'istante all'esterno**. | **Non confinato:** bobina aperta che proietta $\vec{B}$ in tutto il silicio e nell'ambiente circostante. |
| **Area del Loop di Corrente** | Minuscola ($A \approx w \cdot t_{ox} \approx 0.1\ \mu\text{m}^2$) $\implies$ flusso magnetico concatenato quasi nullo. | Enorme ($A \approx 40.000\ \mu\text{m}^2$) $\implies$ flusso magnetico e *crosstalk* elevati. |
| **Schermatura Naturale** | Collegando l'armatura inferiore a $GND$, essa fa **automaticamente da gabbia di Faraday** proteggendo il substrato. | Richiede uno schermo dedicato a pettine (PGS) per non farsi distruggere dalle correnti di Foucault. |

---

*Pagine correlate:*
- [Condensatori](./Condensatori.md)
- [Difficoltà nel fare un componente ideale](../Scaling%20e%20Limiti%20Fisici/Difficolt%C3%A0%20nel%20fare%20un%20componente%20ideale.md)
- [Resistore](./Resistore.md)
- [Elettromigrazione e tossicità dei metalli](../Tecnologia%20e%20Fabbricazione/Elettromigrazione%20e%20tossicit%C3%A0%20dei%20metalli.md)
- [Integrati protetti da interferenze](../Scaling%20e%20Limiti%20Fisici/Integrati%20protetti%20da%20interferenze.md)
