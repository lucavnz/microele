La tecnologia **SOI** (*Silicon On Insulator*) rappresenta l'evoluzione fondamentale del classico MOSFET su silicio massivo (*bulk*). 

Il principio chiave consiste nell'introdurre uno strato continuo di ossido isolante sepolto (**BOX** - *Buried Oxide*, $\text{SiO}_2$) tra il sottile film superiore di silicio attivo (in cui si realizzano canale, Source e Drain) e il substrato massivo inferiore di supporto.

---

### 1. Perché la tecnologia SOI? (I Vantaggi Fisici Rispetto al Bulk)

1. **Azzeramento delle Perdite in Continua verso il Substrato ($I_{DC} = 0$):**
   * Nel bulk tradizionale, sotto il canale c'è silicio continuo con giunzioni p-n estese sul fondo e sui lati dei pozzetti di Drain/Source, soggette a correnti di perdita inversa e passaggio di cariche in profondità (*punchthrough*).
   * Nel SOI, l'ossido sepolto è un isolante perfetto ($R > 10^{16}\,\Omega$): **nessuna corrente parassita in DC può penetrare nel substrato**.
2. **Crollo delle Correnti di Generazione Termica:**
   * La corrente di generazione termica (SRH) è proporzionale al volume di silicio svuotato ($I_{\text{gen}} = q \cdot G_{\text{th}} \cdot \text{Volume}$).
   * Nel bulk il volume include tutti i pozzetti profondi micrometri nel substrato; in SOI il volume è confinato al solo sottilissimo film attivo ($W \cdot L \cdot t_{\text{Si}}$), abbattendo $I_{\text{gen}}$ di ordini di grandezza.
   * *Dove scorre la generazione in FD-SOI?* A transistor spento ($V_D = V_{DD}$, $V_S = 0\,\text{V}$), gli elettroni generati vanno al Drain e le lacune al Source: la corrente scorre **esclusivamente tra Drain e Source** come frazione trascurabile di $I_{\text{OFF}}$, mentre verso il substrato è rigorosamente **$0\,\text{A}$**.
3. **Crollo delle Capacità Parassite di Giunzione ($C_{db}, C_{sb}$):**
   * Il dielettrico del BOX è biossido di silicio ($\epsilon_{SiO2} \approx 3.9$), che ha una costante dielettrica **3 volte inferiore rispetto al silicio** ($\epsilon_{Si} \approx 11.7$).
   * Le capacità parassite verso il fondo crollano del $70-80\%$, aumentando drasticamente la velocità di commutazione dei circuiti e abbattendo l'accoppiamento di rumore in AC.
4. **Immunità Totale al [Latch-Up](./Isolamento.md):**
   * Non esistendo un substrato continuo condiviso tra NMOS e PMOS, la catena di transistori parassiti a tiristore ($p^+-n-p-n^+$) è fisicamente interrotta. Il rischio di Latch-Up è **azzerato al $100\%$**.
5. **Isolamento Dielettrico Completo tra Transistor Adiacenti:**
   * Le trincee di isolamento superficiale [STI](./Isolamento.md) vengono scavate nel film di silicio fino a **toccare direttamente il BOX**. Ogni transistor è un'isola dielettrica sigillata su tutti i lati.

---

### 2. PD-SOI (*Partially Depleted SOI*)

Nel **PD-SOI**, il film di silicio attivo è relativamente spesso ($t_{Si} \approx 50 - 100\,\text{nm}$).

![PD-SOI Struttura a Due Transistor e Linee di Campo](../../Immagini/pd_soi_two_transistors.png)

#### A. La Nascita del Floating Body
Poiché lo spessore del silicio $t_{Si}$ è maggiore della massima profondità di svuotamento naturale del Gate ($t_{Si} > W_{d,max}$):
* La tensione di Gate svuota solo i primi $30-40\,\text{nm}$ superiori del film.
* Sotto la zona svuotata rimane una sacca di **silicio neutro $p$ non svuotato** a contatto con il BOX.
* Questa sacca è priva di qualsiasi contatto ohmico verso massa ed è completamente isolata da ossido: prende il nome di **Corpo Flottante (*Floating Body*)**.

#### B. L'Effetto Kink e l'History Effect
1. Quando il transistor conduce ad alta $V_{DS}$, gli elettroni ad alta energia generano per **ionizzazione da impatto** coppie elettrone-lacuna ($e^- - h^+$) in prossimità del Drain (a cui si aggiunge la generazione termica).
2. Gli elettroni vengono assorbiti dal Drain positivo, mentre **le lacune ($h^+$) non potendo scendere nel substrato (bloccate dal BOX) si accumulano nel corpo flottante**.
3. L'accumulo di carica positiva alza il potenziale del corpo ($V_{\text{body}} \uparrow$).
4. Per effetto body, **la tensione di soglia crolla improvvisamente ($V_{th} \downarrow$)**, provocando un'impennata anomala della corrente di Drain: questo scalino nella curva $I_D - V_{DS}$ prende il nome di **Effetto Kink** (*Kink Effect*).
5. Nei circuiti digitali, il ritardo di commutazione di una porta logica dipende dallo stato di carica lasciato dalla transizione precedente (**History Effect**), rendendo il timing non deterministico.

#### C. Chiusura delle Linee di Campo del Drain nel PD-SOI
Il Drain ($n^+$) attraversa l'intero spessore del silicio e tocca il BOX sul fondo:
* **Verso l'alto (Gate):** le linee formano la capacità Miller $C_{gd}$. Il metallo del Gate, mantenuto a potenziale imposto dal generatore/driver esterno, fornisce cariche immagine senza variare la propria tensione.
* **Di lato (Floating Body):** le linee accoppiano capacitivamente il Drain al corpo flottante ($C_{db}$), modulando $V_{\text{body}}$.
* **Dal fondo (BOX $\to$ Substrato):** le linee attraversano l'ossido sepolto chiudendosi sul piano conduttivo del substrato inferiore.

---

### 3. UTBB FD-SOI (*Ultra-Thin Body and Buried Oxide Fully Depleted SOI*)

Nel **Fully Depleted SOI**, il film di silicio viene assottigliato a soli **$t_{Si} \approx 5 - 7\,\text{nm}$** (circa $15-20$ strati atomici di silicio), poggiato su un ossido sepolto ultrasottile (**UTBOX**, $t_{BOX} \approx 15 - 25\,\text{nm}$).

![UTBB FD-SOI Struttura a Due Transistor e Schermatura](../../Immagini/fd_soi_two_transistors.png)

#### A. Canale 100% Svuotato e Senza Drogaggio
Poiché $t_{Si} \ll W_{d,max}$, il campo elettrico del Gate attraversa l'intero spessore del silicio fino al BOX:
* **Zero Floating Body:** non esiste silicio neutro, eliminando al $100\%$ l'effetto Kink e l'History Effect (le lacune fluiscono liberamente verso il Source).
* **Canale Intrinseco (Non Drogato, $N_A \approx 0$):** non dovendo inserire atomi di drogante per controllare la soglia, si azzera lo scattering ionico (**mobilità dei portatori $\mu$ elevatissima**) e si elimina la dispersione statistica di soglia dovuta alle fluttuazioni casuali dei droganti (mismatch di Pelgrom / RDF).

#### B. Efficienza Elettrostatica Ideale ($S \to 60\,\text{mV/dec}$)
Nel partitore capacitivo tra Gate e superficie del canale:
$$\frac{\partial \psi_s}{\partial V_{GS}} = \frac{1}{1 + \frac{C_{\text{sotto}}}{C_{ox}}} \approx \frac{1}{1 + \frac{C_{BOX}}{C_{ox}}} \approx 1.0$$
* Poiché il BOX è un isolante a bassa capacità ($C_{BOX} \ll C_{ox}$), quasi il **$100\%$ della variazione di tensione di Gate si trasferisce direttamente sul potenziale di canale**.
* Il fattore di sottosoglia $n \to 1.05 \approx 1.0$, permettendo al **Subthreshold Swing di raggiungere il limite termodinamico ideale**:
  $$S \approx 62 - 65\,\text{mV/dec}$$
* Il transistor commuta tra ON e OFF con massima pendenza, garantendo correnti di perdita da spento ($I_{OFF}$) microscopiche.

#### C. Soppressione Totale del DIBL ([DIBL](../Introduzione/Effetti%20di%20canale%20corto/DIBL.md)) e Modello Elettrostatico 2D
Nei nodi nanometrici su bulk, le linee di campo del Drain penetrano in profondità nel silicio e abbassano la barriera di potenziale del Source da sotto (DIBL).
Nell'FD-SOI il DIBL è soppresso geometricamente per **Doppia Schermatura Elettrostatica**:

1. **Chiusura delle Linee di Campo (Legge di Gauss):**
   * Le cariche positive nel Drain ($+Q_D$) richiamano cariche negative. 
   * Il Gate sopra ($V_G = 0\,\text{V}$) e il Back-Gate sotto ($V_{BG} = 0\,\text{V}$) sono piastre conduttrici collegate a potenziale fisso: su di esse **si accumulano cariche negative reali indotte** ($-Q_{\text{gate}}$ e $-Q_{\text{backgate}}$) fornite dai generatori esterni.
   * Le linee di campo del Drain vengono intercettate e "mangiate" immediatamente sopra e sotto.

2. **Il Partitore Capacitivo e la Capacità Laterale ($C_{\text{lat}}$):**
   Il potenziale in un punto $X$ del canale è determinato dal partitore capacitivo a 4 vie:
   $$\phi_X = \frac{C_{ox} \cdot V_G + C_{BOX} \cdot V_{BG} + C_{\text{lat,S}} \cdot V_S + C_{\text{lat,D}} \cdot V_D}{C_{ox} + C_{BOX} + C_{\text{lat,S}} + C_{\text{lat,D}}}$$
   dove la **Capacità Laterale** è l'accoppiamento orizzontale attraverso la sezione del canale:
   $$C_{\text{lat}} = \epsilon_{Si} \frac{W \cdot t_{Si}}{L}$$
   * Poiché $t_{Si} \approx 6\,\text{nm}$, l'area laterale $W \times t_{Si}$ è minuscola $\implies C_{\text{lat,D}}$ è trascurabile rispetto a $C_{ox} = \frac{\epsilon_{ox}}{t_{ox}}$ (con $t_{ox} \approx 1\,\text{nm}$).
   * Risultato: $(C_{ox} + C_{BOX}) \gg C_{\text{lat,D}}$, quindi Gate e Back-Gate inchiodano il potenziale del canale, impedendo al Drain di alzare la tensione verso il Source.

3. **Decadimento Esponenziale del Campo ($\lambda$):**
   L'influenza del Drain decade lungo il canale secondo:
   $$\Delta V(x) \propto \exp\left(-\frac{x}{\lambda}\right) \quad \text{con} \quad \lambda \approx \sqrt{\frac{\epsilon_{Si}}{\epsilon_{ox}} t_{ox} t_{Si}} \approx 3 - 5\,\text{nm}$$
   * Con $\lambda$ così piccolo, il disturbo di potenziale del Drain si estingue completamente dopo pochissimi nanometri: il Source non risente minimamente della tensione $V_{DS}$ ($\mathbf{\Delta V_{th} = 0}$, **Zero DIBL**).

#### D. Controllo Dinamico di Soglia via Back-Gate (*Body Biasing*)
Sotto il BOX sottile si realizzano well indipendenti ($N\text{-Well}$ o $P\text{-Well}$) che fungono da **secondo Gate inferiore (*Back-Gate*)**:
* Applicando una tensione $V_{\text{backgate}}$, si può spostare la soglia nominale $V_{th}$ di $\pm 300\,\text{mV}$ in tempo reale.
* **Modalità Turbo (Forward Body Bias):** abbassa $V_{th}$ per massimizzare la velocità quando il chip esegue calcoli pesanti.
* **Modalità Risparmio (Reverse Body Bias):** alza $V_{th}$ per azzerare i consumi in standby.
* Il tutto senza alcun pericolo di Latch-Up grazie all'isolamento galvanico totale garantito dal BOX.

---

### 4. Tabella Comparativa Finale

| Parametro Fisico | Bulk MOSFET | PD-SOI | UTBB FD-SOI |
| :--- | :--- | :--- | :--- |
| **Spessore Silicio ($t_{Si}$)** | $\infty$ (Wafer Massivo) | $50 - 100\,\text{nm}$ | **$5 - 7\,\text{nm}$ (Ultra-sottile)** |
| **Drogaggio nel Canale** | Molto forte ($N_A > 10^{18}\,\text{cm}^{-3}$) | Forte | **Nullo (Silicio Intrinseco)** |
| **Floating Body ed Effetto Kink** | Assente | **Presente (Instabilità)** | **Assente al $100\%$** |
| **Correnti di Perdita verso Substrato** | Presenti (Giunzioni $pn$) | **Zero (Isolato da BOX)** | **Zero (Isolato da BOX)** |
| **Subthreshold Swing ($S$)** | $80 - 95\,\text{mV/dec}$ | $80 - 90\,\text{mV/dec}$ | **$\approx 62 - 65\,\text{mV/dec}$ (Quasi ideale)** |
| **Controllo del [DIBL](../Introduzione/Effetti%20di%20canale%20corto/DIBL.md)** | Scarso (Linee passano sotto) | Moderato | **Eccellente (Schermato a $6\text{ nm}$)** |
| **Rischio di [Latch-Up](./Isolamento.md)** | Alto (Richiede tap frequenti) | **Zero ($100\%$ Immune)** | **Zero ($100\%$ Immune)** |
| **Regolazione Dinamica $V_{th}$** | Limitata (Rischio Latch-Up) | Impossibile | **Ampia e Sicura (Back-Gate)** |

---

*Pagine correlate:*
- [Isolamento](./Isolamento.md)
- [MOS](./MOS.md)
- [DIBL](../Introduzione/Effetti%20di%20canale%20corto/DIBL.md)
- [Rapporto Ion/Ioff e Sottosoglia](../Introduzione/Effetti%20di%20canale%20corto/Rapporto%20Ion%20Ioff%20e%20sottosoglia.md)
- [La soglia da cosa dipende](../Introduzione/La%20soglia%20da%20cosa%20dipende.md)
