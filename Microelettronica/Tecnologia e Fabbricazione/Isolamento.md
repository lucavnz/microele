Nei circuiti integrati è fondamentale **isolare elettricamente e dielettricamente i singoli dispositivi** (MOS, BJT, diodi e resistori) realizzati sul medesimo substrato di silicio. Senza un adeguato isolamento, si creerebbero canali parassiti conduttivi, correnti di perdita incontrollate, accoppiamento di rumore (*cross-talk*) o cortocircuiti distruttivi tra blocchi adiacenti.

---

### 1. Isolamento Dielettrico Superficiale: Dal LOCOS alla STI

L'isolamento superficiale serve a separare le aree attive dei transistor affiancati, impedendo che le piste di gate o di metallo superiori accendano canali parassiti nel silicio sottostante.
#### A. Il Limite Storico del LOCOS (*LOCal Oxidation of Silicon*)
* **Principio:** si protegge l'area attiva con nitruro di silicio ($\text{Si}_3\text{N}_4$) e si fa crescere termicamente uno spesso ossido di campo (*Field Oxide* / $\text{FOX}$) a $1000^\circ\text{C}$.
* **Il Becco d'Uccello (*Bird's Beak*):** l'ossidazione termica è **isotropa** e consuma il silicio del substrato espandendosi in volume del $+220\%$. L'ossigeno si infila lateralmente sotto la maschera sollevandola e creando una svasatura laterale a cuneo che **mangia e strozza la larghezza utile $W$ del transistor** ($W_{eff} = W_{drawn} - 2\Delta W_{beak}$).
👉 Per i dettagli fisici del LOCOS, vedi: [MOS](../Dispositivi%20e%20Componenti/MOS.md).

#### B. La Soluzione Moderna: STI (*Shallow Trench Isolation*)
Nei nodi sub-micrometrici e nanometrici lo spreco di area del LOCOS è insostenibile. Si impiega quindi la **STI**:
1. **Scavo Anisotropo al Plasma (RIE):** tramite attacco ionico reattivo (*Reactive Ion Etching*) si scava una trincea verticale netta nel silicio ($0.3 - 0.5\,\mu\text{m}$ di profondità) con pareti a $90^\circ$.
2. **Liner Termico Sottilissimo:** una brevissima ossidazione termica di pochi nanometri "cicatrizza" e passiva i difetti reticolari provocati dal bombardamento del plasma sulle pareti della trincea.
3. **Riempimento per Deposizione ([CVD](./CVD.md) / HDP-CVD):** la trincea **NON viene riempita per ossidazione termica del silicio** (che ricreerebbe espansioni laterali), ma tramite **deposizione chimica da fase vapore** di biossido di silicio ($\text{SiO}_2$).
4. **Spianatura ([CMP](../Dispositivi%20e%20Componenti/MOS.md)):** una lucidatura chimico-meccanica rimuove l'ossido in eccesso lasciando la superficie planare.
* **Vantaggi:** pareti verticali, **zero Bird's Beak**, profilo perfettamente piano e massima densità di impaccamento.

---

### 2. Isolamento a Giunzione e Sacche: Well-Isolation e Triple-Well

Oltre all'isolamento dielettrico superficiale (STI), i transistor devono essere isolati nel corpo del semiconduttore tramite **giunzioni p-n polarizzate inversamente**.
#### A. Perché non si mette ogni singolo transistor nella propria sacca isolata?
In un chip digitale con miliardi di porte logiche, gli NMOS condividono il comune substrato $p$ e i PMOS condividono ampie $n\text{-well}$. Non si crea una sacca isolata per ogni singolo dispositivo per 3 motivi critici:
1. **Spreco Colossale di Area (*Area Penalty*):** le regole di layout (*Design Rules*) impongono distanze di sicurezza considerevoli (*well-to-well spacing*) per evitare che le diffusioni laterali vadano in corto. Inoltre ogni sacca richiede anelli di guardia e contatti dedicati (*taps*). Isolare ciascun transistor moltiplicherebbe l'area del silicio per $3-5\times$.
2. **Capacità Parassite di Giunzione ($C_{well-sub}$):** ogni sacca forma una giunzione p-n estesa con il substrato. Se il potenziale della sacca oscilla, la carica e scarica di questa enorme capacità degrada drasticamente la velocità del circuito e consuma potenza dinamica ($P = C f V^2$).
3. **Costi e Maschere Extra:** realizzare sacche profonde (*Deep N-Well*) richiede maschere fotolitografiche aggiuntive e costosi impianti ionici ad altissima energia.

#### B. Quando si usano le Sacche Isolate (Triple-Well)?
* **Circuiti a Segnale Misto (Analogico/Digitale/RF):** per schermare transistor analogici ad altissima sensibilità (es. LNA, ADC) dal rumore ad alta frequenza generato dai blocchi digitali sul substrato.
* **Eliminazione dell'Effetto Body ($V_{SB} = 0$):** in configurazioni a transistori impilati (*cascode*, *source-follower* o interruttori di trasmissione), collegando localmente il Source al proprio Bulk dedicato ($V_{SB}=0$) si mantiene la tensione di soglia $V_{th}$ costante e indipendente dal livello di segnale.
* 👉 Per il confronto dettagliato di compattezza di layout, matching e costi tra Bulk, Triple-Well, SOI e BiCMOS: [Confronto Tecnologie CMOS e BiCMOS](./Confronto%20Tecnologie%20CMOS%20e%20BiCMOS.md).

---

### 3. Dinamica di Carica/Scarica e Iniezione di Corrente (Substrate Noise)

Anche se le sacche sono polarizzate a tensioni continue DC ($V_{DD}$ per le $n\text{-well}$ e $\text{GND}$ per il substrato $p$), **correnti impulsive dinamiche si iniettano continuamente nel silicio**.

#### A. Commutazione dei Drenaggi e Sorgenti ($C_{db}, C_{sb}$)
Ogni volta che una porta logica commuta tra $0$ e $V_{DD}$, la capacità di giunzione inversa tra la diffusione di Drain ($p^+$) e la $n\text{-well}$ si carica e scarica:
$$i_{\text{spunto}}(t) = C_{db} \cdot \frac{d(V_{\text{drain}} - V_{\text{well}})}{dt}$$

#### B. Il Bivio della Corrente: Il Partitore tra Contatto di Alimentazione e Substrato
Nel punto in cui entra la corrente di spunto, il flusso trova **due percorsi in parallelo**:
1. **Ramo verso il contatto di $V_{DD}$:** percorso resistivo nel silicio della well attraverso la resistenza $R_{\text{well\_tap}}$.
2. **Ramo verso il Substrato:** percorso capacitivo attraverso la giunzione sacca-substrato $C_{\text{well-sub}}$ e la resistenza di substrato $R_{sub}$.

```
                                  NODO DRAIN (Commuta 0 ↔ V_DD)
                                             │
                                             ▼
                                            ┬  C_db (Capacità di giunzione)
                                            ┴
                                             │
                           (Spunto)  i_spunto(t)
                                             │
                       ┌─────────────────────┴─────────────────────┐
                       │                                           │
             (Percorso 1: Verso V_DD)                    (Percorso 2: Verso Substrato)
                       │                                           │
                       ▼ i_VDD                                     ▼ i_sub
                 ┌───────────┐                               ┌───────────┐
                 │ R_well_tap│                               │C_well-sub │ (Capacità Well-Sub)
                 └─────┬─────┘                               └─────┬─────┘
                       │                                           │
                       ▼                                           ▼
                 Pista metallica                             ┌───────────┐
                    di V_DD                                  │   R_sub   │ (Resistenza Silicio)
                                                             └─────┬─────┘
                                                                   │
                                                                   ▼
                                                             Massa Substrato (GND)
```

La frazione di corrente che penetra nel substrato dipende dal partitore di ammettenze:
$$i_{\text{sub}} = i_{\text{spunto}} \cdot \frac{R_{\text{well\_tap}}}{R_{\text{well\_tap}} + \left( R_{sub} + \frac{1}{j\omega C_{\text{well-sub}}} \right)}$$

* **Se il contatto di $V_{DD}$ (*well tap*) è vicinissimo:** $R_{\text{well\_tap}} \to 0$, l'impedenza capacitiva a frequenze normali è nettamente superiore ($\frac{1}{\omega C_{\text{well-sub}}} \gg R_{\text{well\_tap}}$) $\implies$ **la quasi totalità della corrente viene drenata all'istante dal contatto di $V_{DD}$**, proteggendo il substrato.
* **Se il contatto di $V_{DD}$ è lontano o i fronti sono ultra-rapidi:** $R_{\text{well\_tap}}$ è alta, l'impedenza del condensatore crolla ad alta frequenza $\implies$ una consistente frazione di corrente penetra nel substrato, creando oscillazioni di potenziale $\Delta V_{sub} = R_{sub} \cdot i_{\text{sub}}$.

#### C. Accoppiamento AC da Alimentazione "Ballerina" (*Supply Bounce*)
A causa delle commutazioni simultanee e dell'induttanza parassita dei package ($L \frac{di}{dt}$), le linee di alimentazione presentano oscillazioni $\Delta V_{DD}(t)$. Questa tensione AC scavalca la barriera capacitiva $C_{\text{well-sub}}$ iniettando correnti di spostamento direttamente nel substrato (*Substrate Noise Coupling*).

---

### 4. Il Rischio Fatale: Il Meccanismo del Latch-Up

L'effetto più distruttivo dell'interazione tra sacche, substrato e cadute di potenziale resistivo è il [Latchup nei circuiti CMOS](../Famiglie%20Logiche/Latchup%20nei%20circuiti%20CMOS.md).

#### A. La Struttura Parassita a Tiristore (SCR)
In qualsiasi processo CMOS su bulk, le diffusioni $p^+$ del PMOS, la $n\text{-well}$, il substrato $p$ e le diffusioni $n^+$ dell'NMOS creano una sequenza a 4 strati **$p^+ - n - p - n^+$**:
* **Transistor BJT PNP parassita:** Emettitore = Source PMOS ($p^+$), Base = $n\text{-well}$ ($n$), Collettore = Substrato ($p$).
* **Transistor BJT NPN parassita:** Emettitore = Source NMOS ($n^+$), Base = Substrato ($p$), Collettore = $n\text{-well}$ ($n$).

I due BJT sono collegati a feedback incrociato, costituendo un **Tiristore (SCR - *Silicon Controlled Rectifier*)**:

```
                       V_DD
                        │
                        ▼ (Emettitore PNP: Source PMOS)
                   ┌─────────┐
                   │ BJT PNP │◄──────────┐
                   └────┬────┘           │
      Collettore PNP    │                │ Base PNP (n-well)
      alimenta la Base  │     ┌──────────┴┐
      del BJT NPN       └───► │  BJT NPN  │
                              └─────┬─────┘
                                    │ (Emettitore NPN: Source NMOS)
                                    ▼
                                   GND
```

#### B. La Dinamica di Innesco
1. Il silicio presenta resistenze distribuite non nulle **$R_{sub}$** e **$R_{well}$**.
2. Uno spunto di corrente impulsivo (da rumore di commutazione, glitch di I/O o accoppiamento capacitivo) attraversa il substrato.
3. Attraversando $R_{sub}$, la corrente genera una caduta ohmica locale:
   $$\Delta V_{sub} = R_{sub} \cdot I_{\text{spunto}}$$
4. Non appena $\Delta V_{sub} \ge 0.6 - 0.7\text{ V}$, la giunzione Base-Emettitore del BJT NPN parassita si polarizza direttamente e si **accende**.
5. L'NPN acceso drena corrente dalla base del PNP, accendendo anche quest'ultimo.
6. Se il prodotto dei guadagni di corrente soddisfa la condizione di innesco rigenerativo:
   $$\beta_{NPN} \cdot \beta_{PNP} \ge 1$$
7. **Cortocircuito permanente a bassa impedenza tra $V_{DD}$ e $\text{GND}$:** il dispositivo entra in uno stato a valanga che non si spegne più da solo. Scorrono correnti elevatissime che fondono e carbonizzano localmente il silicio per sovrariscaldamento termico (**guasto distruttivo**).

---

### 5. Strategie Industriali di Prevenzione del Latch-Up

Per garantire che $\beta_{NPN} \cdot \beta_{PNP} < 1$ e che le cadute ohmiche non superino mai la soglia di accensione ($0.7\text{ V}$), l'industria impiega regole rigorose:

1. **Regola di Layout sui Tap (*Tap Cells* e Max Tap Distance):** le fonderie impongono una distanza massima (es. $< 15-20\,\mu\text{m}$) tra qualsiasi transistor e il più vicino contatto metallico di alimentazione o massa. Questo mantiene $R_{well}$ e $R_{sub}$ talmente basse che nessun picco di corrente può sviluppare $0.7\text{ V}$.
2. **Anelli di Guardia (*Guard Rings*):** recinti continui di silicio fortemente drogato ($p^+$ su substrato e $n^+$ su well) polarizzati a metallo, che raccolgono e drenano i portatori minoritari prima che raggiungano le giunzioni parassite.
3. **Trincee STI Profonde:** le trincee dielettriche STI scavate tra i transistor interrompono fisicamente i percorsi orizzontali dei portatori, abbattendo drasticamente i guadagni $\beta$ dei BJT parassiti.
4. **Wafer Epitassiali (*Epi-Wafers*):** si fa crescere un sottile strato attivo di silicio sopra un substrato massivo ad altissimo drogaggio ($p^{++}$), che agisce da piano di massa a resistenza trascurabile.
5. **Tecnologia SOI (*Silicon On Insulator*):** i transistor poggiano su uno strato sepolto di ossido continuo (**BOX** - *Buried Oxide*). L'isolamento dielettrico totale **elimina alla radice le giunzioni p-n parassite verso il substrato, rendendo il circuito fisicamente immune al Latch-Up al $100\%$**.

---

*Pagine correlate:*
- [Latchup nei circuiti CMOS](../Famiglie%20Logiche/Latchup%20nei%20circuiti%20CMOS.md)
- [SOI](../Dispositivi%20e%20Componenti/SOI.md)
- [MOS](../Dispositivi%20e%20Componenti/MOS.md)
- [CVD](./CVD.md)
- [PVD](./PVD.md)
- [Siliciuro](./Siliciuro.md)
- [Vias](./Vias.md)
- [Diodo](../Dispositivi%20e%20Componenti/Diodo.md)
- [BJT](../Dispositivi%20e%20Componenti/BJT.md)
- [Elettromigrazione e tossicità dei metalli](./Elettromigrazione%20e%20tossicit%C3%A0%20dei%20metalli.md)
- [Difficoltà nel fare un componente ideale](../Scaling%20e%20Limiti%20Fisici/Difficolt%C3%A0%20nel%20fare%20un%20componente%20ideale.md)
- [Integrati protetti da interferenze](../Scaling%20e%20Limiti%20Fisici/Integrati%20protetti%20da%20interferenze.md)
- [Confronto Tecnologie CMOS e BiCMOS](./Confronto%20Tecnologie%20CMOS%20e%20BiCMOS.md)
