# Ratioed Logic e DCVSL (Differential Cascode Voltage Switch Logic)

Nella logica CMOS complementare convenzionale, implementare una funzione booleana con $N$ ingressi richiede rigorosamente **$2N$ transistor** ($N$ nella rete di pull-down e $N$ nella rete di pull-up).  
Questa simmetria presenta svantaggi pesanti quando il numero di ingressi cresce:
* I pMOS hanno mobilità ridotta ($\mu_p \approx \frac{1}{2} \div \frac{1}{3} \mu_n$) e richiedono larghezze $W_p$ triple, occupando la maggior parte dell'area di silicio.
* Nelle porte NOR ad alto Fan-In, mettere molti pMOS in serie degrada pesantemente la velocità a causa della resistenza e delle capacità parassite interne (vedi [Dimensionamento Transistor e Ritardo di Pattern (Sizing)](./Dimensionamento%20Transistor%20e%20Ritardo%20di%20Pattern%20(Sizing).md)).

La **Ratioed Logic** (*Logica a Rapporto*) nasce per rompere questo vincolo: **elimina completamente la rete complessa di pull-up (PUN), sostituendola con un unico dispositivo di carico collegato a $V_{DD}$**.

```
    CMOS STATICO (2N transistor)                    RATIOED LOGIC (N + 1 transistor)
    
               VDD                                                VDD
                │                                                  │
       ┌─────────────────┐                                ┌─────────────────┐
       │     PUN         │                                │ UNICO CARICO    │ (Resistivo,
       │ (N pMOS complessi)                               │ (Load Device)   │  Depletion o
       └────────┬────────┘                                └────────┬────────┘  Pseudo-NMOS)
                o──────── OUT                                      o──────── OUT
       ┌────────┴────────┐                                ┌────────┴────────┐
       │     PDN         │                                │     PDN         │
       │ (N nMOS veloci) │                                │ (N nMOS veloci) │
       └────────┬────────┘                                └────────┬────────┘
               GND                                                GND
```

---

### 1. I 3 Tipi di Carico nella Ratioed Logic

Il dispositivo di carico collegato tra l'uscita e $V_{DD}$ può essere implementato in tre modi:

```
  (A) CARICO RESISTIVO           (B) DEPLETION-LOAD NMOS          (C) PSEUDO-NMOS
  
           VDD                            VDD                            VDD
            │                              │                              │
           [RL] Resistore                 │\  nMOS a svuotamento         │\  pMOS (Gate a massa!)
            │                             │ \ (VT < 0V, sempre ON)       │ \ (VGS = -VDD, sempre ON)
            o──────── OUT                  o──────── OUT                  o──────── OUT
            │                              │                              │
       ┌────┴────┐                    ┌────┴────┐                    ┌────┴────┐
       │   PDN   │                    │   PDN   │                    │   PDN   │
       └────┬────┘                    └────┬────┘                    └────┬────┘
           GND                            GND                            GND
```

1. **Carico Resistivo Passivo ($R_L$):**
   * Usato storicamente nelle logiche RTL (vedi [RTL e Prodotto Ritardo-Consumo (PDP)](../Famiglie%20Logiche/RTL%20e%20Prodotto%20Ritardo-Consumo%20(PDP).md)).
   * **Criticità:** Per limitare la corrente statica serve una resistenza elevata ($R_L \ge 50 \div 100\text{ k}\Omega$). In tecnologia integrata, un resistore da $100\text{ k}\Omega$ in polisilicio o diffusione occupa un'area centinaia di volte più grande di un transistor MOS (vedi [Resistore](../Dispositivi%20e%20Componenti/Resistore.md)), rendendolo inaccettabile nei moderni VLSI.
2. **Depletion-Load nMOS:**
   * Utilizza un transistor nMOS a svuotamento (*depletion*, con drogaggio di canale tale da avere $V_{Tn} < 0\text{ V}$). Collegando Gate e Source insieme ($V_{GS} = 0\text{ V}$), il transistor è permanentemente acceso ed eroga corrente quasi costante.
   * **Criticità:** Richiede un passaggio fotolitografico e un'impiantazione ionica aggiuntiva per modificare la soglia di un solo tipo di transistor, aumentando i costi di fabbricazione.
3. **Pseudo-NMOS (Lo Standard Moderno):**
   * Utilizza un **singolo transistor pMOS standard con il Gate collegato permanentemente a massa** ($V_G = 0\text{ V} \implies V_{GS,p} = -V_{DD}$).
   * Il pMOS è sempre in conduzione, pronto a tirare l'uscita verso $V_{DD}$ non appena la rete di nMOS si spegne.
   * Non richiede maschere speciali ed è pienamente compatibile con qualsiasi processo CMOS standard.

---

### 2. Dimensionamento e Calcolo Analitico di $V_{OL}$ nello Pseudo-NMOS

A differenza del CMOS complementare (in cui a regime o la PUN o la PDN è spenta al 100%, garantendo $V_{OL} = 0\text{ V}$ esatto), nello Pseudo-NMOS **quando l'ingresso è alto ($V_{\text{in}} = V_{DD}$), sia l'nMOS che il pMOS sono simultaneamente accesi**.

Si crea una contesa (*ratio*) tra la corrente di pull-down e la corrente di pull-up: il livello basso $V_{OL}$ è dato dal partitore non lineare tra i due canali:

```
                            EQUILIBRIO DI CORRENTI A LIVELLO BASSO
                            
                                      VDD = 2.5V
                                       │
                                   ┌───┴───┐
                                   │  pMOS │  VGS,p = -VDD  (Sempre acceso!)
                                   └───┬───┘  Regione: SATURAZIONE (VSD = VDD - VOL)
                                       │
                                       ├──────► VOL (Deve essere vicino a 0V!)
                                       │
                                   ┌───┴───┐
                       Vin = VDD ──┤  nMOS │  VGS,n = VDD  (Acceso dall'ingresso)
                                   └───┬───┘  Regione: TRIODO / LINEARE (VDS = VOL)
                                       │
                                      GND
```

#### Dimostrazione Analitica:
All'equilibrio stazionario sul nodo di uscita, la corrente dell'nMOS deve eguagliare la corrente del pMOS:
$$I_{Dn} = I_{Dp}$$

1. **Regione operativa del pMOS:**
   La tensione Source-Gate vale $V_{SG,p} = V_{DD}$.  
   La tensione Source-Drain vale $V_{SD,p} = V_{DD} - V_{OL}$.  
   Poiché $V_{OL}$ è piccolo ($V_{OL} \ll V_{DD}$), si ha $V_{SD,p} > V_{SG,p} - |V_{Tp}|$, quindi **il pMOS opera in saturazione**:
   $$I_{Dp} = \frac{k_p}{2} \left( V_{DD} - |V_{Tp}| \right)^2 \qquad \text{con } k_p = \mu_p C_{ox} \left(\frac{W}{L}\right)_p$$

2. **Regione operativa dell'nMOS:**
   La tensione Gate-Source vale $V_{GS,n} = V_{DD}$.  
   La tensione Drain-Source è $V_{DS,n} = V_{OL}$.  
   Poiché $V_{DS,n} = V_{OL} \ll V_{DD} - V_{Tn}$, **l'nMOS opera in regione lineare (triodo)**:
   $$I_{Dn} = k_n \left[ (V_{DD} - V_{Tn}) V_{OL} - \frac{V_{OL}^2}{2} \right] \qquad \text{con } k_n = \mu_n C_{ox} \left(\frac{W}{L}\right)_n$$

Trascurando il termine quadratico $\frac{V_{OL}^2}{2}$ poiché $V_{OL}$ è piccolo:
$$k_n (V_{DD} - V_{Tn}) V_{OL} \approx \frac{k_p}{2} (V_{DD} - |V_{Tp}|)^2$$

Esplicitando la tensione di uscita a livello basso **$V_{OL}$**:
$$\mathbf{V_{OL} \approx \frac{k_p}{2 k_n} \cdot \frac{(V_{DD} - |V_{Tp}|)^2}{V_{DD} - V_{Tn}} = \frac{1}{2 \cdot r} \cdot \frac{(V_{DD} - |V_{Tp}|)^2}{V_{DD} - V_{Tn}}}$$
dove $r = \frac{k_n}{k_p} = \frac{\mu_n W_n}{\mu_p W_p}$ è il **rapporto di forza (*ratio*) tra nMOS e pMOS**.

#### Il Vincolo di Progetto:
* Se $r$ è troppo piccolo (pMOS troppo forte o nMOS troppo debole), $V_{OL}$ sale verso $0.5 \div 1.0\text{ V}$.
* Uno zero logico a $1\text{ V}$ distrugge il margine di rumore $NM_L$ (vedi [Soglia Logica e Margine di Rumore](../Famiglie%20Logiche/Soglia%20Logica%20e%20Margine%20di%20Rumore.md)) e rischia di accendere i transistor degli stadi logici successivi!
* **Regola di Progetto:** Per garantire $V_{OL} \le 0.1 \cdot V_{DD}$, occorre imporre:
  $$\mathbf{r = \frac{k_n}{k_p} \ge 3 \div 4}$$
  Poiché $\mu_n \approx 2 \div 3 \mu_p$, significa che **la larghezza dell'nMOS deve essere almeno paragonabile o superiore a quella del pMOS** ($W_n \ge W_p$).

---

### 3. Il Grande Trade-Off: Velocità vs Dissipazione di Potenza Statica

Il punto debole insito nella natura della logica Pseudo-NMOS è la **dissipazione di potenza statica continua**:

$$P_{\text{statica}} = V_{DD} \cdot I_{Dp,\text{sat}} \approx V_{DD} \cdot \frac{k_p}{2} (V_{DD} - |V_{Tp}|)^2$$

* Finché l'uscita rimane a livello basso ($V_{out} = V_{OL}$), scorre una corrente ininterrotta da $V_{DD}$ verso terra attraverso i due transistor accesi.
* **Il dilemma del progettista:**
  * Se si sceglie un pMOS **largo** ($W_p$ grande $\implies k_p$ alto), la carica del condensatore di carico $C_L$ durante la commutazione $0 \to 1$ è rapidissima $\implies \mathbf{t_{pLH} \text{ brevissimo}}$ (porta veloce). Ma la potenza statica a livello basso esplode e $V_{OL}$ sale pericolosamente.
  * Se si sceglie un pMOS **stretto** ($W_p$ minimo), si riduce la potenza statica e si abbassa $V_{OL}$, ma il tempo di salita diventa lumaca $\implies \mathbf{t_{pLH} \text{ altissimo}}$.

```
                     IL COMPROMESSO PSEUDO-NMOS
                     
         pMOS FORTE (Wp grande)           pMOS DEBOLE (Wp piccolo)
         ──────────────────────           ────────────────────────
         [+] Salita veloce (tpLH basso)   [+] Potenza statica ridotta
         [-] VOL degradato (alto)         [+] VOL eccellente (basso)
         [-] Dissipazione statica enorme  [-] Salita lentissima (tpLH alto)
```

#### Soluzione per Standby: Adaptive Load (Carico Abilitato)
Nelle applicazioni low-power, il gate del pMOS non viene collegato direttamente a massa fissa, ma a un segnale di controllo $\overline{\text{Enable}}$ (o al clock):
* Durante il normale calcolo attivo: $\overline{\text{Enable}} = 0\text{ V}$ (porta abilitata).
* Durante le pause di calcolo o in modalità sleep: $\overline{\text{Enable}} = V_{DD}$ (pMOS spento al 100%, potenza statica azzerata istantaneamente).

---

### 4. DCVSL: Differential Cascode Voltage Switch Logic

Come conservare i vantaggi di compattezza della Ratioed Logic (nessuna PUN complessa) **eliminando al contempo il $100\%$ della potenza statica**?  
La soluzione architetturale definitiva è la **DCVSL** (*Differential Cascode Voltage Switch Logic*).

```
                            SCHEMA CIRCUITALE DCVSL
                            
                                     VDD
                                  ┌───┴───┐
                                  │       │
                                 [Mp1]   [Mp2]  Coppia di pMOS a Latch
                                  │   X   │     (Incrociati bistabili)
                                  ├───o───┤
                   OUT (Q) o──────┤       ├──────o /OUT (/Q)
                           │      │       │
                       ┌───┴───┐  │   ┌───┴───┐
                       │       │  │   │       │
                       │  PDN  │  │   │ /PDN  │  Due reti di nMOS
                       │       │  └───┤       │  mutuamente esclusive!
                       └───┬───┘      └───┬───┘  (Funzione Vera e Negata)
                           │              │
                          GND            GND
```

#### Architettura Circu رمale:
1. **Rete di Pull-Down Doppia Differenziale:**
   * Contiene due reti a soli transistor nMOS: la **PDN diretta** che calcola la funzione $F$, e la **$\overline{\text{PDN}}$ complementare** che calcola la funzione negata $\overline{F}$.
   * Poiché gli ingressi sono forniti in forma differenziale ($A, \overline{A}, B, \overline{B}$), le due reti sono **mutuamente esclusive**: quando una conduce, l'altra è rigorosamente aperta e non conduce mai!
2. **Carico a Latch Rigenerativo Incrociato (Cross-Coupled pMOS):**
   * Non ci sono resistori né gate a massa. Il gate di $M_{p1}$ è pilotato dall'uscita opposta $\overline{Q}$, mentre il gate di $M_{p2}$ è pilotato dall'uscita $Q$.

---

### 5. Funzionamento Dinamico e Risposta ai Transitori della DCVSL

Analizziamo il transitorio quando l'uscita $Q$ deve andare a $0\text{ V}$ e $\overline{Q}$ deve andare a $V_{DD}$:

1. **Stato Iniziale ($Q = V_{DD}, \; \overline{Q} = 0\text{ V}$):**
   * $M_{p1}$ è ACCESO (perché pilotato da $\overline{Q} = 0$).
   * $M_{p2}$ è SPENTO (perché pilotato da $Q = V_{DD}$).
   * Nessuna corrente scorre: una PDN è aperta, l'altro ramo ha il pMOS spento. **Potenza statica = ZERO!**

2. **Commutazione e Contesa Dinamica (*Cross-Over Contention*):**
   * Gli ingressi commutano: la PDN di sinistra si accende per tirare giù il nodo $Q$.
   * All'inizio della commutazione, $M_{p1}$ è ancora acceso: per qualche frazione di frazione di nanosecondo ($100 \div 200\text{ ps}$), **l'nMOS di sinistra deve combattere contro $M_{p1}$** per riuscire ad abbassare la tensione di $Q$.
   * Non appena il potenziale di $Q$ scende al di sotto di $V_{DD} - |V_{Tp}|$, il transistor $M_{p2}$ sul ramo destro comincia ad accendersi.

3. **Innesco Rigenerativo (*Positive Feedback*):**
   * $M_{p2}$ inietta corrente sul nodo di destra, facendo schizzare $\overline{Q}$ rapidamente verso $V_{DD}$.
   * La salita di $\overline{Q}$ verso $V_{DD}$ chiude progressivamente $M_{p1}$ sul ramo sinistro, eliminando la resistenza all'nMOS.
   * Il meccanismo a retroazione positiva commuta istantaneamente lo stato.

4. **Stato Finale a Regime:**
   * $Q = 0\text{ V}$ esatto, $\overline{Q} = V_{DD}$ esatto (*full rail-to-rail swing*).
   * $M_{p1}$ è completamente spento, la $\overline{\text{PDN}}$ di destra è completamente spenta.
   * **Corrente statica a regime: rigorosamente ZERO!**

---

### Confronto Riassuntivo tra Famiglie Logiche

| Parametro | CMOS Complementare | Pseudo-NMOS | DCVSL |
| :--- | :--- | :--- | :--- |
| **Transistor per $N$ ingressi** | $2N$ | **$N + 1$ (Minimo assoluto)** | $2N + 2$ (Tutti nMOS veloci tranne 2) |
| **Capacità di Ingresso ($C_{\text{in}}$)** | Elevata ($C_n + C_p$) | **Bassa (solo $C_n$)** | Bassa su ciascuna linea |
| **Escursione di Uscita ($V_{OL}$)** | $0\text{ V}$ (Ideale Rail-to-Rail) | Degradato ($V_{OL} > 0\text{ V}$, logica a rapporto) | **$0\text{ V}$ (Ideale Rail-to-Rail)** |
| **Potenza Statica ($P_{\text{stat}}$)** | **Zero (solo leakage)** | **Elevata (quando $V_{\text{out}} = V_{OL}$)** | **Zero (a regime stazionario)** |
| **Uscite generate** | Singola ($F$) | Singola ($F$) | **Differenziale nativa ($F$ e $\overline{F}$)** |
| **Velocità su funzioni complesse** | Limitata da PUN serie | Veloce in discesa, lenta in salita | Molto veloce (PDN ad albero nMOS) |

---

*Pagine correlate:*
- [Dimensionamento Transistor e Ritardo di Pattern (Sizing)](./Dimensionamento%20Transistor%20e%20Ritardo%20di%20Pattern%20(Sizing).md)
- [Effetto di Fan-In e Fan-Out sul Ritardo (Elmore)](./Effetto%20di%20Fan-In%20e%20Fan-Out%20sul%20Ritardo%20(Elmore).md)
- [Tecniche di Ottimizzazione per Porte Complesse Veloci](./Tecniche%20di%20Ottimizzazione%20per%20Porte%20Complesse%20Veloci.md)
- [Pass-Transistor Logic e Level Restorer](./Pass-Transistor%20Logic%20e%20Level%20Restorer.md)
- [Soglia Logica e Margine di Rumore](../Famiglie%20Logiche/Soglia%20Logica%20e%20Margine%20di%20Rumore.md)
- [Potenza Dinamica e Dissipazione di Carica](../Famiglie%20Logiche/Potenza%20Dinamica%20e%20Dissipazione%20di%20Carica.md)
- [RTL e Prodotto Ritardo-Consumo (PDP)](../Famiglie%20Logiche/RTL%20e%20Prodotto%20Ritardo-Consumo%20(PDP).md)
