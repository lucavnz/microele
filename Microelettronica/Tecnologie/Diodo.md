Il **diodo a giunzione $PN$** è la struttura fondamentale dell'elettronica a semiconduttore. 
Sul silicio integrato, il comportamento reale si discosta dal modello matematico ideale a causa di fenomeni di ricombinazione/generazione, effetti ad alte correnti e resistenze parassite distributive.

---

### 1. La Caratteristica Statica $I(V)$ Reale

L'equazione ideale di Shockley descrive la corrente come:
$$I = I_S \left( e^{\frac{V}{\eta V_T}} - 1 \right)$$
dove $V_T = \frac{k T}{q} \approx 26\text{ mV}$ è la tensione termica e $\eta$ è il **fattore di idealità** ($\eta = 1$ nel modello ideale).

![Caratteristica Statica Diodo Reale](../../Immagini/diodo_caratteristica_reale.png)

Nel dispositivo reale si distinguono **4 regioni di funzionamento**:

#### A. Polarizzazione Inversa e Corrente di Generazione ($-I_S - I_G$)
Quando il diodo è polarizzato inversamente ($V < 0$), la corrente non è rigorosamente costante a $-I_S$, ma cresce in modulo con la tensione inversa:
* **Corrente di saturazione inversa $-I_S$:** è dovuta ai portatori minoritari generati termicamente nelle regioni neutre che, diffondendo casualmente verso il bordo della zona di svuotamento (regione di carica spaziale - SCR), vengono **scaraventati dall'altra parte** dall'intenso campo elettrico interno.
* **Corrente di generazione nella SCR ($-I_G$):** dentro la regione di svuotamento, l'agitazione termica sfrutta i difetti reticolari e le impurità (centri trappola Shockley-Read-Hall, SRH) per strappare elettroni e creare coppie elettrone-lacuna. Più aumentiamo la tensione inversa, più la regione di svuotamento si allarga ($W \propto \sqrt{V_R}$), più volume attivo c'è per generare coppie $\implies I_G$ aumenta con la tensione inversa.
* **Breakdown / Rottura ($V_{Br}$):** superata una certa tensione inversa critica, il campo elettrico diventa così violento da innescare l'**effetto tunnel (Zener)** o la **moltiplicazione a valanga** (*impact ionization*), facendo esplodere la corrente negativa.

#### B. Bassa Tensione Diretta e Fenomeni di Ricombinazione ($\eta = 2$)
A basse tensioni dirette ($V < 0.4\text{ V}$), i portatori che provano ad attraversare la zona di carica spaziale incontrano le trappole SRH e si ricombinano prima di completare il passaggio.
* Questa corrente parassita di ricombinazione segue la legge $I_{\text{rec}} = I_{R0} \cdot e^{\frac{V}{2 V_T}}$, introducendo un **fattore di idealità $\eta = 2$**.
* **Il ruolo dei difetti ($N_t$):** il pre-fattore $I_{R0} = q A \frac{W n_i}{2 \tau_0}$ è **direttamente proporzionale alla densità di trappole $N_t$** nel silicio ($I_{R0} \propto N_t$). Più difetti e legami rotti ci sono (es. all'interfaccia superficiale tra silicio e ossido $\text{SiO}_2$), più $I_{R0}$ è grande e più a lungo la regione degradata con $\eta = 2$ domina la caratteristica.
* **Perché $\eta = 2$ è uno svantaggio?**
  * **Peggior rapporto $I_{\text{on}}/I_{\text{off}}$ nel digitale:** la pendenza di sottosoglia vale $S = \eta \cdot \ln(10) \cdot V_T \approx \eta \cdot 60\text{ mV/decade}$. Con $\eta = 2$ servono $120\text{ mV}$ per ogni decade di spegnimento anziché $60\text{ mV}$: il componente è "pigro", si spegne male e genera correnti di perdita (*leakage*) elevate a riposo.
    👉 Vedi: [Rapporto Ion Ioff e sottosoglia](../Introduzione/Effetti%20di%20canale%20corto/Rapporto%20Ion%20Ioff%20e%20sottosoglia.md)
  * **Perdita di precisione nell'analogico:** nei riferimenti di tensione a temperatura compensata (Bandgap) e generatori PTAT, la tensione generata $\Delta V = \eta V_T \ln(I_1 / I_2)$ richiede che $\eta$ sia rigorosamente $1.00$ costante per non sballare le misure.

#### C. Media Tensione Diretta e Diffusione Pura ($\eta = 1$)
Attorno a $0.4\text{ V} < V < 0.7\text{ V}$, la barriera di potenziale si abbassa a sufficienza da far prevalere in modo schiacciante la corrente di diffusione utile rispetto alla ricombinazione.
* La corrente segue la curva ideale di Shockley: $I \approx I_{S0} e^{\frac{V}{V_T}}$ con **$\eta = 1$**.

#### D. Alta Tensione Diretta (Alte Iniezioni e Resistenza Serie $R_s$)
Per tensioni $V > 0.8\text{ V}$ e correnti elevate ($I > 10\text{ mA}$), la curva devia dall'esponenziale a causa di due fattori:
1. **Alte iniezioni (*High-Level Injection*):** la concentrazione di portatori minoritari iniettati supera il drogaggio nativo del silicio ($n \approx p > N_A$). Per la legge di azione di massa $n \cdot p \approx n^2 = n_i^2 e^{V/V_T} \implies n \propto e^{V / (2 V_T)}$, la pendenza esponenziale della giunzione torna a dimezzarsi ($\eta \to 2$).
2. **Resistenza serie parassita $R_s$:** il silicio neutro e i contatti metallici introducono una caduta ohmica $R_s \cdot I$. Poiché la tensione applicata si ripartisce come $V = V_{\text{giunzione}} + R_s I$, ogni volt aggiuntivo cade interamente su $R_s \implies I \approx \frac{V - V_\gamma}{R_s}$. **La curva esponenziale si piega a destra e diventa una linea retta puramente resistiva.**
   👉 Vedi: [Difficoltà nel fare un componente ideale](./Difficolt%C3%A0%20nel%20fare%20un%20componente%20ideale.md)

---

### 2. Anatomia del Diodo Integrato: La Struttura $p^+ - n^- - n^+$

Nel flusso CMOS standard, il diodo viene ricavato all'interno di una $n\text{-well}$:

![Layout a U e Diodo da BJT](../../Immagini/diodo_layout_u_e_bjt.png)

1. **La Giunzione $p^+ - n^-$ asimmetrica:**
   La giunzione attiva vera e propria è formata tra la sacca fortemente drogata $p^+$ (Anodo) e la $n\text{-well}$ poco drogata $n^-$.
   Poiché $N_A (p^+) \gg N_D (n\text{-well})$, la regione di svuotamento si estende quasi al $100\%$ all'interno della $n\text{-well}$ ($W \propto \sqrt{1/N_D}$).
2. **Il ruolo della sacca $n^+$ (Contatto Ohmico):**
   Non serve a creare una seconda giunzione, ma a garantire un **contatto ohmico a bassa resistenza con il metallo del Catodo**:
   * Se appoggiassimo il metallo direttamente sul silicio poco drogato della $n\text{-well}$, si formerebbe una barriera Schottky rettificante (un **diodo Schottky parassita** che bloccherebbe la corrente!).
   * L'iper-drogaggio $n^+$ rende la barriera metallo-silicio così sottile da essere scavalcata per **effetto tunnel** quantistico, azzerando la resistenza di contatto.
3. **Differenza rispetto a un vero Diodo PIN ($P-I-N$):**
   In un diodo PIN lo strato centrale è **silicio intrinseco (non drogato)** molto spesso:
   * **Capacità parassita $C_j \to 0$:** avendo $W$ grande, azzera la capacità per **interruttori e attenuatori RF/microonde**.
   * **Fotodiodi PIN:** la zona $I$ fa da enorme volume di cattura per generare coppie ottiche con la luce.
   * **Altissima tensione:** sopporta migliaia di Volt senza rottura.
   Nel CMOS standard, la $n\text{-well}$ è invece semplicemente poco drogata ($n^-$), realizzando un diodo $p^+-n$ asimmetrico.

---

### 3. Perché NON Drogare Forte la $n\text{-well}$ (Evitare la Giunzione $p^+-n^+$)?

Verrebbe spontaneo pensare di drogare forte la $n\text{-well}$ ($n^+$) per abbattere la resistenza parassita, ma fare una giunzione $p^+-n^+$ distruggerebbe il componente:

1. **Breakdown a soli $2-3\text{ V}$ (Diodo Zener):**
   Con $N_A$ e $N_D$ entrambi elevati, la regione di svuotamento $W \approx \sqrt{1/N_A + 1/N_D}$ si riduce a pochi nanometri. A soli $2-3\text{ V}$ di tensione inversa il campo elettrico interno supera $10^6\text{ V/cm}$, innescando l'**effetto tunnel (rottura Zener)**: il diodo perde la capacità di bloccare tensioni inverse normali.
2. **Capacità Parassita $C_j$ Gigantesca ($C_j = \frac{\epsilon A}{W}$):**
   Essendo $W$ microscopica, la capacità parassita sale di $50-100$ volte, rallentando drasticamente il circuito con costanti di tempo $\tau = R C_j$ inaccettabili.
3. **Incompatibilità con i Transistori [MOS](./MOS.md) (PMOS):**
   La $n\text{-well}$ è la stessa sacca in cui vengono costruiti tutti i transistori **PMOS** del chip:
   * Con una $n\text{-well}$ drogata $n^+$, la tensione di soglia $|V_{thp}|$ salirebbe a $3-4\text{ V}$ (impossibile da accendere a tensioni logiche standard).
   * La mobilità delle lacune $\mu_p$ crollerebbe per l'eccessivo scattering ionico con i droganti.
   * Le giunzioni di Source e Drain dei PMOS andrebbero in breakdown a $2\text{ V}$.

---

### 4. Layout del Diodo Integrato: La Struttura a "U"

Per minimizzare la resistenza parassita della $n\text{-well}$ poco drogata senza alterarne il drogaggio, si ottimizza la geometria del layout:
* La resistenza parassita vale $R_s = \rho \frac{L}{S}$.
* **Sezione $S$ triplicata:** sagomando il Catodo a forma di "U" intorno all'Anodo, la corrente scorre su tre fronti in parallelo contemporaneamente.
* **Percorso $L$ ridotto al minimo:** Anodo e Catodo sono affacciati a distanza minima su tutto il perimetro.
* **Matrice di Vias:** contatti metallici multipli in parallelo azzerano la resistenza di contatto.
* **Risultato:** $R_s$ crolla, abbattendo il ritardo $R_s C_j$ per commutazioni ad altissima velocità.
  👉 Vedi: [Vias](./Vias.md) e [Siliciuro](./Siliciuro.md)

---

### 5. Diodo Realizzato da BJT (Transistore Connesso a Diodo)

Nei circuiti analogici di precisione si preferisce realizzare il diodo prendendo un transistore bipolare [BJT](./BJT.md) e **cortocircuitando la Base con il Collettore** ($V_{BC} = 0$).

#### Perché il BJT connesso a diodo garantisce $\eta \approx 1.00$ ideale?
1. **Filtro naturale della ricombinazione:**
   Le cariche che subiscono ricombinazione SRH nella zona di svuotamento vengono drenate sul morsetto di Base ($I_B$). La corrente principale che attraversa il dispositivo ed esce dal Collettore ($I_C$) è composta unicamente dalle cariche che hanno attraversato la base per pura diffusione:
   $$I_C = I_S \cdot e^{\frac{V_{BE}}{V_T}} \quad (\text{con } \eta = 1.00 \text{ esatto!})$$
   Poiché $I_C \gg I_B$ (grazie al guadagno $\beta > 100$), la corrente totale $I_{\text{tot}} \approx I_C$ mantiene $\eta = 1$ su oltre **6-8 decadi di corrente**.
2. **Giunzione sepolta nel bulk profondo:**
   Mentre in un diodo planare la giunzione tocca la superficie ricca di difetti sotto l'ossido $\text{SiO}_2$, in un [BJT](./BJT.md) verticale la giunzione attiva E-B si trova in profondità nel silicio monocristallino perfetto. La densità di trappole $N_t$ è quasi nulla $\implies I_{R0}$ è minuscolo e la ricombinazione è soppressa.

---

*Pagine correlate:*
- [BJT](./BJT.md)
- [MOS](./MOS.md)
- [Difficoltà nel fare un componente ideale](./Difficolt%C3%A0%20nel%20fare%20un%20componente%20ideale.md)
- [Siliciuro](./Siliciuro.md)
- [Vias](./Vias.md)
- [Resistore](./Resistore.md)
- [Rapporto Ion Ioff e sottosoglia](../Introduzione/Effetti%20di%20canale%20corto/Rapporto%20Ion%20Ioff%20e%20sottosoglia.md)
- [Analogico non si scende di dimensioni](../Introduzione/Analogico%20non%20si%20scende%20di%20dimensioni.md)
