La tecnologia **SOI** (*Silicon On Insulator*) rappresenta l'evoluzione fondamentale del classico MOSFET su silicio massivo (*bulk*). 

Il principio chiave consiste nell'introdurre uno strato continuo di ossido isolante sepolto (**BOX** - *Buried Oxide*, $\text{SiO}_2$) tra il sottile film superiore di silicio attivo (in cui si realizzano canale, Source e Drain) e il substrato massivo inferiore di supporto.

---

### 1. Perché la tecnologia SOI? (I Vantaggi Fisici Rispetto al Bulk)

1. **Azzeramento delle Perdite in Continua verso il Substrato ($I_{DC} = 0$):**
   * Nel bulk tradizionale, sotto il canale c'è silicio continuo con giunzioni p-n soggette a correnti di perdita inversa e passaggio di cariche in profondità (*punchthrough*).
   * Nel SOI, l'ossido sepolto è un isolante perfetto ($R > 10^{16}\,\Omega$): **nessuna corrente parassita in DC può penetrare nel substrato**.
2. **Crollo delle Capacità Parassite di Giunzione ($C_{db}, C_{sb}$):**
   * Il dielettrico del BOX è biossido di silicio ($\epsilon_{SiO2} \approx 3.9$), che ha una costante dielettrica **3 volte inferiore rispetto al silicio** ($\epsilon_{Si} \approx 11.7$).
   * Le capacità parassite verso il fondo crollano del $70-80\%$, aumentando drasticamente la velocità di commutazione dei circuiti e abbattendo l'accoppiamento di rumore in AC.
3. **Immunità Totale al [Latch-Up](./Isolamento.md):**
   * Non esistendo un substrato continuo condiviso tra NMOS e PMOS, la catena di transistori parassiti a tiristore ($p^+-n-p-n^+$) è fisicamente interrotta. Il rischio di Latch-Up è **azzerato al $100\%$**.
4. **Isolamento Dielettrico Completo tra Transistor Adiacenti:**
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
1. Quando il transistor conduce ad alta $V_{DS}$, gli elettroni ad alta energia generano per **ionizzazione da impatto** coppie elettrone-lacuna ($e^- - h^+$) in prossimità del Drain.
2. Gli elettroni vengono assorbiti dal Drain positivo, mentre **le lacune ($h^+$) si accumulano nel corpo flottante**.
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
* **Zero Floating Body:** non esiste silicio neutro, eliminando al $100\%$ l'effetto Kink e l'History Effect.
* **Canale Intrinseco (Non Drogato, $N_A \approx 0$):** non dovendo inserire atomi di drogante per controllare la soglia, si azzera lo scattering ionico (**mobilità dei portatori $\mu$ elevatissima**) e si elimina la dispersione statistica di soglia dovuta alle fluttuazioni casuali dei droganti (mismatch di Pelgrom / RDF).

#### B. Efficienza Elettrostatica Ideale ($S \to 60\,\text{mV/dec}$)
Nel partitore capacitivo tra Gate e superficie del canale:
$$\frac{\partial \psi_s}{\partial V_{GS}} = \frac{1}{1 + \frac{C_{\text{sotto}}}{C_{ox}}} \approx \frac{1}{1 + \frac{C_{BOX}}{C_{ox}}} \approx 1.0$$
* Poiché il BOX è un isolante a bassa capacità ($C_{BOX} \ll C_{ox}$), quasi il **$100\%$ della variazione di tensione di Gate si trasferisce direttamente sul potenziale di canale**.
* Il fattore di sottosoglia $n \to 1.05 \approx 1.0$, permettendo al **Subthreshold Swing di raggiungere il limite termodinamico ideale**:
  $$S \approx 62 - 65\,\text{mV/dec}$$
* Il transistor commuta tra ON e OFF con massima pendenza, garantendo correnti di perdita da spento ($I_{OFF}$) microscopiche.

#### C. Soppressione Totale del DIBL ([DIBL](../Introduzione/Effetti%20di%20canale%20corto/DIBL.md))
Nei nodi nanometrici su bulk, le linee di campo del Drain penetrano in profondità nel silicio e abbassano la barriera di potenziale del Source da sotto (DIBL).
Nell'FD-SOI il DIBL è soppresso geometricamente per **Doppia Schermatura Elettrostatica**:
1. **Nessuna via di fuga nel silicio:** sotto il canale spesso $6\text{ nm}$ c'è solo ossido isolante; non esiste silicio profondo in cui le linee di campo possano curvare verso il Source.
2. **Cattura da parte del Top Gate:** il Gate metallico dista appena $t_{ox} \approx 1\text{ nm}$ dal canale (è $20$ volte più vicino del Source, che dista $L \approx 20\text{ nm}$). Il Gate assorbe e neutralizza le linee di campo agendo da **Gabbia di Faraday**.
3. **Cattura da parte del Back-Gate:** le linee inferiori attraversano il BOX e si chiudono sul piano conduttivo inferiore.
4. **Risultato:** nessuna linea di campo raggiunge il Source in orizzontale. La barriera di potenziale del Source resta intatta e indipendente da $V_{DS}$ ($\mathbf{\Delta V_{th} = 0}$, **Zero DIBL**).

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
