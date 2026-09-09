In microelettronica e nella progettazione analogica di precisione, la **variabilità tecnologica** è uno dei vincoli fisici più severi. I componenti integrati fabbricati su silicio non possono mai garantire un valore assoluto esatto; tuttavia, sfruttando la simmetria geometrica e l'accoppiamento locale, è possibile ottenere **rapporti tra componenti con precisione elevatissima** attraverso le tecniche di **matching**.

---

### 1. Il Principio del Matching: Valore Assoluto vs Rapporti

A causa delle tolleranze industriali di fonderia (fluttuazioni di temperatura nei forni chimici, spessore dell'ossido, dosi di impiantazione ionica e sovraincisione litografica):
* **Il Valore Assoluto varia del $\pm 20\% \div \pm 30\%$:**
  Un resistore nominale da $10\text{ k}\Omega$ o un condensatore da $1\text{ pF}$ possono variare significativamente tra wafer diversi o lotti di produzione differenti (*process spread*).
* **Il Rapporto Relativo ha precisione fino allo $0.01\%$:**
  Due componenti identici posizionati a pochi micrometri di distanza sullo stesso pezzetto di silicio (*die*) subiscono le **stesse identiche fluttuazioni ambientali e di processo**:
  $$\frac{R_1}{R_2} = \frac{\cancel{R_\square} \cdot (L_1 / W_1)}{\cancel{R_\square} \cdot (L_2 / W_2)} = \frac{L_1 / W_1}{L_2 / W_2}$$
  $$\frac{C_1}{C_2} = \frac{\cancel{\frac{\varepsilon_{ox}}{t_{ox}}} \cdot A_1}{\cancel{\frac{\varepsilon_{ox}}{t_{ox}}} \cdot A_2} = \frac{A_1}{A_2}$$

> 💡 **Regola d'oro del design analogico:** I circuiti integrati di precisione (amplificatori, partitori, filtri, riferimenti di tensione Bandgap, convertitori ADC/DAC a reti R-2R o a pesi capacitivi) non devono **mai dipendere dal valore assoluto**, ma solo da **rapporti tra componenti ($R_1/R_2$ o $C_1/C_2$)**.

---

### 2. Il Concetto di Dispositivo Unitario (*Unit Element*)

Per realizzare un rapporto razionale qualsiasi tra due componenti (es. $\frac{R_1}{R_2} = \frac{m}{n}$ oppure $\frac{C_1}{C_2} = \frac{m}{n}$), **non si disegnano componenti con geometrie arbitrarie diverse**.
Se disegnassimo $R_1$ lungo $10\,\mu\text{m}$ e $R_2$ lungo $20\,\mu\text{m}$, essi avrebbero impatti percentuali diversi da parte delle teste, dei contatti e degli errori di bordo.

Si definisce invece una **cella base unitaria identica ($R_u$ o $C_u$)**:
* $R_1$ viene realizzato mettendo in serie o in parallelo $m$ celle unitarie identiche ($R_1 = m \cdot R_u$).
* $R_2$ viene realizzato con $n$ celle unitarie identiche ($R_2 = n \cdot R_u$).
* In questo modo, ogni singola cella subisce le medesime alterazioni parassite e il rapporto rimane ideale.

---

### 3. Regole di Layout per il Matching dei Resistori

Per garantire un matching moderato ($\pm 0.1\%$) o preciso ($\pm 0.01\%$) nei resistori integrati, il layout deve seguire regole rigorose:

```
    [Contatto]                             [Contatto]
     ┌───────┐                             ┌───────┐
     │ ░░░░░ │◄── Incertezza               │ ░░░░░ │
     └──┐ ┌──┘    flusso 2D                └──┐ ┌──┘
        │ │                                   │ │
        │ ├─── Corrente uniforme (1D) ────────┤ │
        │ │                                   │ │
        │ │◄──────────── L ──────────────────►│ │
        │ │                                   │ │
     ┌──┘ └──┐                             ┌──┘ └──┐
     │ ░░░░░ │                             │ ░░░░░ │
     └───────┘                             └───────┘
         ▲                                     ▲
     Testa 1                                Testa 2
```

#### A) Rapporto di forma allungato ($L/W > 5$)
La resistenza reale include la resistenza delle teste e dei contatti metallici:
$$R_{\text{tot}} = R_\square \frac{L}{W} + 2 R_{\text{testa}} + 2 R_{\text{contatto}}$$
* Se $L/W$ è piccolo, le teste e i contatti (affetti da grandissima incertezza e addensamento di corrente bidimensionale) costituiscono una percentuale elevata del totale ($30\% - 50\%$), rendendo $R$ incontrollabile.
* Se **$L/W > 5$**, il corpo centrale a flusso di corrente 1D uniforme costituisce oltre il $90\%-95\%$ del valore totale, rendendo trascurabile l'errore delle teste.

#### B) Stessa Orientazione e Stesso Verso di Corrente
Tutti i resistori da accoppiare devono essere rigorosamente **paralleli e orientati nella stessa direzione** (es. tutti orizzontali) e percorsi dalla corrente nello **stesso verso**:
1. **Piezoresistività e Stress Meccanico:** Il silicio è anisotropo. La colla del package e le dilatazioni termiche esercitano trazioni/compressioni direzionali che alterano la mobilità dei portatori ($\mu$) in modo asimmetrico tra asse $X$ e asse $Y$. Se due resistori sono ortogonali, subiscono variazioni di resistenza opposte, distruggendo il matching.
2. **Anisotropia di Fabbricazione:** L'impiantazione ionica avviene con un angolo inclinato di $7^\circ$ (*tilt angle*) che crea un'ombra asimmetrica; l'attacco chimico (*etching*) differisce tra $X$ e $Y$.
3. **Effetto Termoelettrico Seebeck:** Nei contatti metallo-silicio i gradienti termici generano tensioni $V = S \cdot \Delta T$. Con lo stesso verso di corrente, queste cadute termoelettriche parassite si elidono nelle maglie circuitali.

#### C) Stesso Vicinato e Strutture Dummy
I resistori risentono dell'ambiente chimico, ottico ed elettrostatico circostante:
* **Effetto di bordo di etching:** Le strisce esterne vengono scavate dall'acido più velocemente di quelle interne. Si aggiungono strisce fittizie non collegate (**Dummy**) alle estremità della matrice per garantire che tutte le strisce attive "vedano" lo stesso identico vicinato.
* **Effetto di campo (*Field Effect*):** Linee metalliche o pozzetti (*well*) adiacenti possono modulare elettrostaticamente la densità dei portatori nel resistore.
* **Schermatura da segnali rumorosi:** Se una pista metallica rumorosa deve attraversare la matrice, si interpone uno schermo metallico inferiore connesso a potenziale pulito (substrato/massa).

#### D) Stesso Profilo di Temperatura
Gli *hot spot* (transistor che scaldano molto) generano isoterme concentriche sul die. I resistori devono essere disposti **radialmente o simmetricamente rispetto alle isoterme**, in modo che entrambi subiscano lo stesso identico gradiente di temperatura lungo il loro asse.

#### E) Baricentro Comune (*Common Centroid*)
Per annullare i gradienti lineari bidimensionali di drogaggio, ossido e temperatura lungo il chip, i resistori si dividono in frazioni uguali disposte a matrice incrociata con **baricentro geometrico coincidente** (es. configurazione a croce $R_{1a}, R_{2a}, R_{2b}, R_{1b}$).

---

### 4. Regole di Layout per il Matching dei Condensatori

Nei condensatori integrati ([Condensatori](./Condensatori.md)), oltre alla variabilità d'area, entrano in gioco le capacità di dispersione laterale:

```
                Armatura Superiore (Top Plate)
                    ┌─────────────────┐
                    │                 │
       Fringing ──►((                 ))◄── Fringing (Effetto Bordo)
                   ┌┴─────────────────┴┐
                   │    Dielettrico    │
                   └┬─────────────────┬┘
       Fringing ──►((                 ))◄── Fringing verso substrato
             ┌──────┴─────────────────┴──────┐
             │ Armatura Inferiore (Bot Plate)│
             └───────────────────────────────┘
```

#### A) Stesso Rapporto Area/Perimetro ($A/P$) e Aumento della Capacità Reale
Nel modello teorico a facce piane e parallele ($C_{\text{ideale}} = c_{\text{area}} \cdot \text{Area}$), si assume che tutte le linee di campo elettrico siano verticali e confinate tra le armature. Nella realtà:
* Le cariche sui bordi e sulle pareti laterali generano **linee di campo elettrico incurvate verso l'esterno e verso il substrato (*fringing*)**.
* Ogni linea di campo in più corrisponde a ulteriore carica $Q$ immagazzinata a parità di tensione $\implies$ **la capacità reale è SEMPRE MAGGIORE di quella ideale**:
  $$C_{\text{tot}} = c_{\text{area}} \cdot \text{Area} + c_{\text{perimetro}} \cdot \text{Perimetro} > C_{\text{ideale}}$$
* Raccogliendo l'area:
  $$C = c_{\text{area}} \cdot \text{Area} \left( 1 + \frac{c_{\text{perimetro}}}{c_{\text{area}}} \cdot \frac{\text{Perimetro}}{\text{Area}} \right)$$

Per calcolare il rapporto preciso $\frac{C_1}{C_2}$ tra due condensatori:
$$\frac{C_1}{C_2} = \frac{c_{\text{area}} \cdot \text{Area}_1 \left( 1 + \frac{c_{\text{perimetro}}}{c_{\text{area}}} \cdot \frac{\text{Perimetro}_1}{\text{Area}_1} \right)}{c_{\text{area}} \cdot \text{Area}_2 \left( 1 + \frac{c_{\text{perimetro}}}{c_{\text{area}}} \cdot \frac{\text{Perimetro}_2}{\text{Area}_2} \right)}$$

> 💡 **Condizione di cancellazione perfetta:** Se $\frac{\text{Perimetro}_1}{\text{Area}_1} = \frac{\text{Perimetro}_2}{\text{Area}_2}$, il termine parassita tra parentesi **si cancella esattamente**, garantendo $\frac{C_1}{C_2} = \frac{\text{Area}_1}{\text{Area}_2}$ senza errori di bordo. Questo è il motivo per cui si usano solo **celle unitarie quadrate identiche** (stessa Area e stesso Perimetro per costruzione).

#### B) Forma Quadrata e Dimensioni Generose
Per la legge di Pelgrom, la deviazione standard del mismatch diminuisce con l'aumentare dell'area:
$$\sigma\left(\frac{\Delta C}{C}\right) \propto \frac{1}{\sqrt{\text{Area}}}$$
* Cella $25\,\mu\text{m} \times 25\,\mu\text{m} \implies \text{mismatch} \approx 2.0\%$
* Cella $125\,\mu\text{m} \times 125\,\mu\text{m} \implies \text{mismatch} \approx 0.4\%$

#### C) Angoli a $135^\circ$ (*Chamfered Corners*)
Gli spigoli vivi a $90^\circ$ tendono ad arrotondarsi in modo incontrollabile durante la fotolitografia e concentrano linee di campo elettrico elevate. Smussare gli angoli a $135^\circ$ rende l'attacco chimico estremamente uniforme e riproducibile.

#### D) Connessione Asimmetrica Top Plate vs Bottom Plate
* L'armatura inferiore (*bottom plate*) ha una notevole capacità parassita verso il substrato di silicio sottostante.
* L'armatura superiore (*top plate*) è schermata da quella inferiore ed è virtualmente isolata dal substrato.
* **Regola circuitale:** La piastra superiore va sempre connessa al nodo più sensibile ad **alta impedenza** (es. l'ingresso invertente dell'operazionale), mentre la piastra inferiore va verso il segnale a **bassa impedenza** o verso massa.

#### E) Cella Unitaria Pre-Simmetrizzata a 8 Segmenti (Indipendenza dai Collegamenti)
Quando si collegano le celle unitarie in una matrice per formare rapporti (es. $C_1/C_2 = 7/2$):
* **Il problema dei fili di instradamento:** Ogni traccia metallica aggiunta per collegare una cella a quelle vicine introduce capacità parassite. Una cella collegata in una sola direzione avrebbe meno capacità parassita di una collegata in due o tre direzioni, sbilanciando il matching.
* **La soluzione degli 8 segmenti sporgenti:** Ogni singola cella unitaria viene disegnata a CAD già provvista di serie di:
  * **4 bracci sporgenti per la Top Plate** (Nord, Sud, Est, Ovest).
  * **4 bracci sporgenti per la Bottom Plate** (Nord, Sud, Est, Ovest).
* **Risultato:**
  1. Tutte le celle nascono con la **stessa identica geometria e capacità parassita totale**.
  2. Per collegare due celle adiacenti è sufficiente toccare i due bracci già affacciati.
  3. I bracci non utilizzati restano come appendici simmetriche (*dummy stubs*), rendendo la **capacità della cella rigorosamente indipendente dal numero di connessioni attive**.

---

### 5. Regole di Layout per il Matching dei Transistor MOS

Nei transistor MOS per circuiti analogici di precisione (coppie differenziali, specchi di corrente), la variabilità statistica locale tra due dispositivi identici adiacenti è governata dalla **Legge di Pelgrom**:

$$\sigma(\Delta V_T) = \frac{C_{VT}}{\sqrt{W_{\text{eff}} \cdot L_{\text{eff}}}} \qquad \frac{\sigma(\Delta k)}{k} = \frac{C_k}{\sqrt{W_{\text{eff}} \cdot L_{\text{eff}}}}$$

> 📌 **Effetto dello scaling dell'ossido ($t_{ox}$):** Se lo spessore dell'ossido di gate $t_{ox}$ cala, $C_{ox}$ aumenta e la dispersione della soglia $\sigma(V_T)$ cala; tuttavia la dispersione relativa del fattore di guadagno $\sigma(k)/k$ **non diminuisce**, poiché governata principalmente dalla variabilità locale della mobilità $\mu$.

```
                              REGOLE CHIAVE DI MATCHING PER I MOS
  ┌─────────────────────────┬─────────────────────────────────────────────────────────────┐
  │ Regola                  │ Motivazione Fisica / Layout                                 │
  ├─────────────────────────┼─────────────────────────────────────────────────────────────┤
  │ Distanza minima         │ Riduce l'impatto dei gradienti spaziali continui            │
  │ Dimensioni non minime   │ Aumenta l'area W · L riducendo il mismatch di Pelgrom       │
  │ Stessa orientazione (!) │ Elimina l'anisotropia da stress del package e fotolitografia│
  │ Stesso vicinato / Dummy │ Scherma i bordi da over-etching e riflessioni ottiche       │
  │ No contatti su active   │ I contatti di Gate si fanno solo su FOX per non rovinare tox│
  └─────────────────────────┴─────────────────────────────────────────────────────────────┘
```

#### A) Confronto nMOS vs pMOS per il Matching (Perché vince il pMOS?)
* **A parità di dimensioni pure ($W \times L$ identici):** I coefficienti tecnologici di Pelgrom $C_{VT}$ sono comparabili.
* **A parità di prestazioni circuitali ($I_D$ o $g_m$):** Poiché $\mu_p \approx \frac{1}{3}\mu_n$, il pMOS richiede una larghezza $W_p \approx 3 W_n$. La sua area fisica è 3 volte superiore $\implies \sigma(\Delta V_T) \propto 1/\sqrt{3 \cdot \text{Area}} \approx \mathbf{0.58 \cdot \sigma(\Delta V_{T,n})}$. Il pMOS offre circa il **$42\%$ in meno di mismatch** ed ha un **rumore $1/f$ nettamente inferiore**.

#### B) Perché la Stessa Orientazione vale anche per il Polisilicio fuori dal Substrato?
Anche se il polisilicio è depositato sopra l'ossido e non nel silicio monocristallino del wafer:
1. **Piezoresistività del Poly:** La resina e il frame metallico del package si contraggono a freddo molto più del silicio, **incurvando l'intero chip**. Questo stress meccanico si trasmette attraverso l'ossido al polisilicio: poiché $\pi_l \neq \pi_t$ e lo stress $\sigma_x \neq \sigma_y$, due strisce ortogonali deviano in direzioni opposte ($R_X \uparrow, R_Y \downarrow$).
2. **Asimmetria di Incisione (Etching Bias):** L'incisione plasma RIE e la fotolitografia (vedi [Litografia Ottica e Immersione](../Tecnologia%20e%20Fabbricazione/Litografia%20Ottica%20e%20Immersione.md)) incidono larghezze diverse lungo $X$ e $Y$ ($W_X \neq W_Y$).
3. **Tilt Angle dell'Impiantazione ($7^\circ$):** Genera ombreggiature asimmetriche nel drogaggio.

#### C) Bilanciamento delle Sacche di Drain nelle Coppie Differenziali (1D vs 2D)
* **Nel layout 1D asimmetrico ($A-A-B-B$):** Il ramo differenziale $A$ ha 1 sacca di Drain condivisa ($C_C \approx 1 \cdot C_{\text{drain}}$), mentre il ramo $B$ ha 2 sacche ($C_D \approx 2 \cdot C_{\text{drain}}$). Questo raddoppio di capacità parassita distrugge la simmetria dinamica e il **CMRR ad alta frequenza** (vedi [Coppia Differenziale e Cascode Telescopico](./Coppia%20Differenziale%20e%20Cascode%20Telescopico.md)).
* **Nel layout 2D Common Centroid:** La seconda riga inverte l'ordine dei finger, garantendo **$5 + 5$ sacche di Drain perfettamente pareggiate** su entrambi i rami.

👉 Approfondimento completo con schemi e calcoli: [Layout e Tecniche di Progettazione dei MOS](./Layout%20e%20Tecniche%20di%20Progettazione%20dei%20MOS.md)

---

*Pagine correlate:*
- [Litografia Ottica e Immersione](../Tecnologia%20e%20Fabbricazione/Litografia%20Ottica%20e%20Immersione.md)
- [Coppia Differenziale e Cascode Telescopico](./Coppia%20Differenziale%20e%20Cascode%20Telescopico.md)
- [Layout e Tecniche di Progettazione dei MOS](./Layout%20e%20Tecniche%20di%20Progettazione%20dei%20MOS.md)
- [MOS](./MOS.md)
- [Capacità parassite nel MOSFET](./Capacit%C3%A0%20parassite%20nel%20MOSFET.md)
- [La soglia da cosa dipende](./La%20soglia%20da%20cosa%20dipende.md)
- [Resistore](./Resistore.md)
- [Condensatori](./Condensatori.md)
- [Narrow resistenze](./Narrow%20resistenze.md)
- [Analogico non si scende di dimensioni](../Scaling%20e%20Limiti%20Fisici/Analogico%20non%20si%20scende%20di%20dimensioni.md)
- [Difficoltà nel fare un componente ideale](../Scaling%20e%20Limiti%20Fisici/Difficolt%C3%A0%20nel%20fare%20un%20componente%20ideale.md)
- [Siliciuro](../Tecnologia%20e%20Fabbricazione/Siliciuro.md)
- [Wafer produzione](../Tecnologia%20e%20Fabbricazione/Wafer%20produzione.md)
- [Confronto Tecnologie CMOS e BiCMOS](../Tecnologia%20e%20Fabbricazione/Confronto%20Tecnologie%20CMOS%20e%20BiCMOS.md)
