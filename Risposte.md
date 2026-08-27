Searched for "seconda dimensione"
Searched for "capacità di svuotamento"
Searched for "C_j"
Viewed Condensatori.md:1-46

Hai fatto delle osservazioni e delle domande **straordinarie**: hai colto esattamente i punti in cui la teoria ideale dei libri si scontra con la fisica reale dei semiconduttori!

Vediamo di chiarire tutto con la massima precisione e chiarezza fisica.

---

### 1. Capacità nella Giunzione PN: Cosa Devi Sapere?

In una giunzione $PN$ esistono **DUE capacità completamente diverse** per origine fisica e regione di lavoro:

```text
               POLARIZZAZIONE INVERSA (V < 0)         POLARIZZAZIONE DIRETTA (V > 0)
                   e bassissima diretta                      Media/alta diretta
                             │                                       │
                      Capacità di                             Capacità di
                   SVUOTAMENTO (Cj)                         DIFFUSIONE (Cd)
                             │                                       │
Origine:           Ioni fissi scoperti nella SCR           Portatori minoritari accumulati
                                                           nelle regioni neutre
Legge:             Cj ∝ 1 / √(Vbi - V)                     Cd ∝ ID ∝ exp(V / VT)
                   (variazione modesta)                    (esplosione esponenziale!)
```

#### A. Capacità di Svuotamento / Giunzione ($C_j$ o $C_{dep}$)
* **Dove domina:** In **inversa ($V < 0$)** e a bassissima tensione diretta.
* **Origine fisica:** È una capacità **elettrostatica**. Nella zona di svuotamento (SCR) ci sono gli ioni droganti fissi ($N_D^+$ a destra, $N_A^-$ a sinistra) privi di portatori liberi.  
  Se vari la tensione di un $dV$, lo spessore della zona svuotata si allarga o si restringe ($dW$), scoprendo o ricoprendo ioni fissi ai bordi:
  $$C_j = \left| \frac{dQ_{SCR}}{dV} \right| = \frac{\epsilon_s A}{W(V)}$$
  È la formula del classico condensatore a facce piane, ma **con le armature a distanza variabile $W(V)$**:
  $$C_j(V) = \frac{C_{j0}}{\left(1 - \frac{V}{V_{bi}}\right)^m} \quad \left(m = \frac{1}{2} \text{ a gradino}, \ m = \frac{1}{3} \text{ graduale}\right)$$
* **Applicazione:** Diodi *Varicap* (condensatori variabili controllati in tensione per sintonizzatori RF).

#### B. Capacità di Diffusione ($C_d$ o $C_{diff}$)
* **Dove domina:** In **polarizzazione diretta ($V > 0$)**.
* **Origine fisica:** **Non c'entrano gli ioni fissi!**  
  Quando polarizzi in diretta, inietti una quantità colossale di minoritari che diffondono nelle regioni neutre (elettroni in $P$, lacune in $N$). Prima di ricombinarsi, queste cariche libere stazionano lì: costituiscono una **carica accumulata $Q_{diff}$ proporzionale alla corrente**:
  $$Q_{diff} = \tau_T \cdot I_D$$
  (dove $\tau_T$ è il tempo di transito o vita media dei portatori).
* Derivando rispetto alla tensione:
  $$C_d = \frac{dQ_{diff}}{dV} = \tau_T \frac{dI_D}{dV} = \tau_T \cdot g_d = \tau_T \frac{I_D}{V_T}$$
* **Conseguenza pratica devastante:** Poiché $I_D \propto e^{V/V_T}$, **$C_d$ cresce esponenzialmente con la tensione**! Diventa gigantesca (decine o centinaia di $\text{nF}$), rallentando il diodo quando cerchi di spegnerlo (tempo di recupero inverso $t_{rr}$, perché devi prima "drenare" tutta quella carica stoccata).

---

### 2. Il Modello Circuitale Completo del Diodo

La tua scomposizione mentale è **perfetta**:

```text
                  Rs (Resistenza serie silicio neutro e contatti)
   Anodo o─────/\/\/\/\─────┬───────────────────────┬────────────o Catodo
                            │                       │
                       ┌────┴────┐             ┌────┴────┐
                       │  Diodo  │             │   Cj    │ (Svuotamento)
                       │ Ideale  │             └────┬────┘
                       │ Shockley│                  │
                       │ (η = 1) │             ┌────┴────┐
                       └────┬────┘             │   Cd    │ (Diffusione)
                            │                  └────┬────┘
                       ┌────┴────┐                  │
                       │ Ramo    │                  │
                       │ Ricomb. │                  │
                       │ (η = 2) │                  │
                       └────┬────┘                  │
                            │                       │
                       ┌────┴────┐                  │
                       │ Ramo    │                  │
                       │Breakdown│                  │
                       └────┬────┘                  │
                            └───────────────────────┘
```
1. **$R_s$ in serie:** caduta ohmica nei blocchi neutri e nei contatti.
2. **In parallelo tra loro ai morsetti della giunzione intrinseca:**
   * Diodo ideale di Shockley ($\eta = 1$).
   * Ramo ricombinazione/generazione SRH ($\eta = 2$ in diretta, $I_{gen}$ in inversa).
   * Ramo di Breakdown (Zener/Valanga, attivo solo per $V < -V_{BR}$).
   * Le due capacità dinamiche $C_{tot} = C_j(V) + C_d(I)$.

---

### 3. La Resistenza Serie è "Anomala"? (La Modulazione di Conducibilità)

> *"Quando passo in regime di alte iniezioni la resistenza cambia no? Ho più portatori?"*

**Hai centrato in pieno uno dei fenomeni più importanti della fisica dei dispositivi: la MODULAZIONE DI CONDUCIBILITÀ (*Conductivity Modulation*)!**

La conducibilità elettrica di un blocco di semiconduttore è:
$$\sigma = q(n \mu_n + p \mu_p) \implies \rho = \frac{1}{\sigma}$$

* **A basse/medie correnti:**  
  Nel blocco neutro poco drogato (es. una regione $N^-$ con drogaggio $N_D = 10^{15}\text{ cm}^{-3}$), la concentrazione di elettroni è fissata solo dai donori: $n \approx N_D$, mentre le lacune sono quasi zero.  
  La resistenza serie è costante:
  $$R_s = \frac{1}{q N_D \mu_n} \cdot \frac{L}{A}$$
* **In alte iniezioni ($V_D$ elevata):**  
  La giunzione spara un'ondata enorme di minoritari (lacune) nel blocco $N^-$, raggiungendo concentrazioni $\Delta p = 10^{17}\text{ cm}^{-3}$, cioè **100 volte superiori al drogaggio nativo $N_D$**!
* Per mantenere la neutralità di carica elettrostatica, il semiconduttore richiama istantaneamente altrettanti elettroni dal contatto: $n \approx \Delta p \gg N_D$.
* **Cosa succede alla resistenza?**  
  Il blocco di silicio si ritrova improvvisamente "inondato" di portatori liberi ($n$ e $p$) rispetto a quando era a riposo. La conducibilità $\sigma$ **aumenta di 100 volte**, e la resistenza del blocco **crolla**!

> 💡 **Dove si sfrutta?** Nei componenti di potenza (diodi PIN e IGBT): si fa un blocco centrale $N^-$ spesso centinaia di micron per reggere $2000\text{ V}$ in inversa, ma in conduzione diretta la modulazione di conducibilità lo rende conduttivo quasi come un metallo, evitando che si incenerisca!

---

### 4. Chi incontra la resistenza? Elettroni o lacune? ($q n \mu_n$ vs $q p \mu_p$)

> *"Se un elettrone va nel blocco $P$... chi incontra la resistenza? Gli elettroni o le lacune che si muovono?"*

Immagina cosa succede nel blocco neutro $P$:
1. **L'elettrone iniettato entra nel blocco $P$:**
   * È un minoritario. Si muove per **diffusione** (non per campo elettrico).
   * Camminando, si scontra con il mare di lacune maggioritarie e **dopo una certa distanza ($L_n$) si ricombina e scompare**.
2. **Ma la corrente elettrica totale deve conservarsi lungo tutto il filo!**
   * Se un elettrone sparisce ricombinandosi con una lacuna, quella lacuna è andata persa.
   * Per mantenere il blocco neutro, **il contatto metallico (l'Anodo) deve iniettare una nuova lacuna** dall'esterno.
3. **Chi attraversa tutto il blocco $P$ dal morsetto metallico fino alla giunzione?**
   * **IL MARE DI LACUNE MAGGIORITARIE!**
   * Lontano dalla giunzione, gli elettroni iniettati sono già tutti morti per ricombinazione ($n_p \approx 0$). Tutta la corrente è sostenuta al **$100\%$ dalle lacune** che marciano compatte dal contatto metallico verso la giunzione per effetto del campo elettrico (*drift*).
4. **Ecco la risposta:**
   * La resistenza ohmica del blocco $P$ la subiscono le **lacune maggioritarie** che sfrecciano dal contatto metallico verso la zona di ricombinazione, urtando contro il reticolo cristallino!
   * Ecco perché nel blocco $P$ la conducibilità vale:
     $$\sigma_P \approx q \cdot p \cdot \mu_p \approx q \cdot N_A \cdot \mu_p$$
   * Viceversa, nel blocco neutro $N$, la resistenza la incontrano gli **elettroni maggioritari** che viaggiano dal contatto del catodo: $\sigma_N \approx q N_D \mu_n$.

---

### 5. Cos'è l'"Effetto Seconda Dimensione" (Effetti 2D)?

Nei libri di base il diodo viene disegnato come una sbarra monodimensionale (1D, asse $x$): giunzione piatta e infinita.  
Nel chip reale integrato nel silicio, il diodo è un oggetto **planare bidimensionale (2D/3D)**. Gli effetti 2D sono tre:

```text
                           Finestra di diffusione
                              ┌─────────────┐
        Ossido (SiO2)         │  Contatto   │         Ossido (SiO2)
       ███████████████████████│   Metallo   │███████████████████████
       ───────────────────────┴─────────────┴───────────────────────
       Silicio:                 Anodo (p+)
                      ╭─────────────────────────────╮  <-- Raggio di curvatura rj
                      │                             │      sotto l'ossido!
                      │      CAMPO E PIATTO         │
       ═══════════════╪═════════════════════════════╪═══════════════
                      │                             │  <-- Bordo curvo:
                      │                             │      CAMPO E CONCENTRATO!
                      ╰─────────────────────────────╯      (Breakdown anticipato!)
                                   Catodo (n-well)
```

1. **Effetto Curvatura ai Bordi (Junction Curvature):**
   * I droganti impiantati diffondono anche **lateralmente sotto l'ossido**. La giunzione non è piatta: finisce con una forma curva cilindrica o sferica con raggio di curvatura $r_j$.
   * Per la legge di Gauss, sulle superfici curve le linee di campo elettrico convergono (*effetto punta*): **il campo elettrico ai bordi curvi è molto più intenso che al centro**.
   * **Risultato:** il breakdown in inversa avviene **prima sui bordi curvi che nella parte piatta**, abbassando la tensione di rottura reale del diodo ($V_{BR, 2D} < V_{BR, 1D}$).
2. **Affollamento di Corrente (*Current Crowding*):**
   * Nei chip, l'Anodo e il Catodo sono entrambi sulla superficie superiore, affiancati.
   * La corrente sceglie la via di minima resistenza: invece di scendere dritta sul fondo, **si ammucchia tutta sul perimetro/bordo più vicino al contatto del catodo**.
   * Questo causa riscaldamento localizzato e fa lavorare male la parte centrale della giunzione.
3. **Ripartizione Area / Perimetro di Correnti e Capacità:**
   * Non esiste una sola capacità o corrente di fuga:
     $$C_{tot} = C_{area} \cdot \text{Area} + C_{perim} \cdot \text{Perimetro}$$
     $$I_{leak} = J_{area} \cdot \text{Area} + J_{perim} \cdot \text{Perimetro}$$
   * La componente perimetrale ha una $W$ diversa per la curvatura e tocca l'ossido $\text{SiO}_2$ pieno di trappole, avendo parametri completamente diversi dal fondo piano.