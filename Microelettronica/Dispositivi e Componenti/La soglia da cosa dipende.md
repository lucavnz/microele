# La Tensione di Soglia $V_{th}$ e la Fisica del MOS

La **tensione di soglia ($V_{th}$)** è la tensione minima che dobbiamo applicare al Gate per "accendere" il transistor MOS, cioè per creare un canale superficiale conduttivo di elettroni liberi.

---

### 1. I 4 Regimi del Condensatore MOS (Substrato tipo $p$)

A seconda della tensione $V_{GS}$ applicata al Gate rispetto al substrato ($p$-bulk, drogato con accettori $N_A$), la struttura MOS attraversa 4 zone fisiche distinte:

```
  V < V_FB          V = V_FB          V_FB < V < V_th          V > V_th
-------------|-------------------|-----------------------|------------------> V_GS
Accumulazione     Banda Piatta           Svuotamento           Forte Inversione
                                     (Debole inversione)        (Canale Acceso)
```

1. **Accumulazione ($V_{GS} < V_{FB}$):** Tensione negativa sul gate. Le lacune (portatori maggioritari) vengono attratte all'interfaccia silicio-ossido ($p(0) > N_A$).
2. **Banda Piatta / Flat-Band ($V_{GS} = V_{FB}$):** Il campo elettrico interno nel silicio è nullo. Le bande energetiche sono perfettamente orizzontali e la densità di cariche è uniforme ($p = N_A$).
3. **Svuotamento e Debole Inversione ($V_{FB} < V_{GS} < V_{th}$):** Tensione positiva modesta. Le lacune vengono respinte in profondità, lasciando scoperti gli ioni accettori negativi fissi (zona di svuotamento $W_d$). I pochi elettroni all'interfaccia si muovono solo per diffusione.
   👉 Approfondimento: [Conduzione di Sottosoglia e Rapporto Ion/Ioff](../Effetti%20di%20Canale%20Corto/Rapporto%20Ion%20Ioff%20e%20sottosoglia.md)
4. **Forte Inversione ($V_{GS} > V_{th}$):** La concentrazione di elettroni alla superficie supera il drogaggio originario ($n(0) \ge N_A$). Si forma uno strato sottilissimo e denso di elettroni liberi (carica mobile $Q_i$): **il canale conduce corrente**.
   👉 Approfondimento su Overdrive, Saturazione ed Efficienza: [Overdrive e Regioni di Inversione](./Overdrive%20e%20Regioni%20di%20Inversione.md)

---

### 2. Carica Fissa ($Q_d$) vs Carica Mobile ($Q_i$)

Nel silicio sotto l'ossido, la carica spaziale totale per unità di superficie è la somma di due contributi:
$$Q_{SC} = Q_d + Q_i$$

* **Carica Fissa di Svuotamento ($Q_d$):** Sono gli ioni accettori $N_A^-$ rimasti senza lacune nel reticolo cristallino. Essendo atomi fissi, **non conducono corrente**. Cresce con la radice del potenziale di superficie $\Phi_S$ ($Q_d = -\sqrt{2 q \varepsilon_{si} N_A \Phi_S}$) fino a bloccarsi al valore massimo $Q_{d,MAX}$ appena si raggiunge la soglia ($\Phi_S = 2\Phi_F$).
* **Carica Mobile di Inversione ($Q_i$):** Sono gli elettroni liberi del canale. Sotto-soglia è praticamente trascurabile ($Q_i \approx 0$); sopra la soglia domina la carica totale ($Q_i \approx -C_{ox}(V_{GS} - V_{th})$) permettendo il passaggio della corrente $I_D$.

---

### 3. La Formula Classica di $V_{th0}$ (Teoria 1D a canale lungo)

Poiché l'ossido ($C_{ox}$) e lo strato di svuotamento nel silicio ($C_d$) si comportano come **due dielettrici / condensatori in serie**, la tensione esterna applicata si partiziona tra silicio ed ossido:

$$V_{th0} = \underbrace{V_{FB}}_{\text{Disallineamento}} + \underbrace{2\Phi_F}_{\text{Caduta nel Silicio}} + \underbrace{\gamma \sqrt{2\Phi_F}}_{\text{Caduta sull'Ossido}}$$

Scritta per esteso con i parametri fisici elementari:
$$V_{th0} = \left(\Phi_{ms} - \frac{Q_{ox}}{C_{ox}}\right) + 2\Phi_F + \frac{\sqrt{2 q \varepsilon_{si} N_A (2\Phi_F)}}{C_{ox}}$$

I tre termini hanno un significato fisico preciso:

#### A) Il termine di Banda Piatta ($V_{FB}$)
Annulla il campo elettrico spontaneo generato a riposo:
* $\Phi_{ms} = \Phi_m - \Phi_s = \frac{E_{Fs} - E_{Fm}}{q}$: differenza di potenziale di contatto tra Gate e Silicio dovuta al disallineamento spontaneo dei rispettivi livelli di Fermi.
* $-\frac{Q_{ox}}{C_{ox}}$: tensione per compensare le cariche positive intrappolate nell'ossido $SiO_2$.

#### B) Il salto di potenziale nel Silicio ($2\Phi_F$ - Lo "Specchio" di drogaggio)
$\Phi_F = \Phi_T \ln\left(\frac{N_A}{n_i}\right)$ è la distanza tra livello intrinseco $E_i$ e livello di Fermi $E_F$ nel bulk ($p$-type).
* A $\Phi_S = \Phi_F$: la superficie diventa intrinseca neutra ($n = p = n_i$).
* A $\Phi_S = 2\Phi_F$: la superficie si ribalta a tipo $n$ con $n(0) = N_A$. È la soglia fisica in cui nasce la forte inversione.

#### C) Il pedaggio perso sull'Ossido ($\gamma \sqrt{2\Phi_F} = \Delta V_{ox}$)
Per portare il silicio a $2\Phi_F$, il campo elettrico ha dovuto scoprire la carica fissa $Q_{d,MAX}$. Per sostenere questa carica attraverso il condensatore dell'ossido, dobbiamo applicare all'esterno una caduta extra:
$$\Delta V_{ox} = \frac{|Q_{d,MAX}|}{C_{ox}} = \frac{\sqrt{2 q \varepsilon_{si} N_A (2\Phi_F)}}{C_{ox}} = \gamma \sqrt{2\Phi_F}$$
*(dove $\gamma = \frac{\sqrt{2 q \varepsilon_{si} N_A}}{C_{ox}}$ è il coefficiente di effetto Body in $\text{V}^{1/2}$)*.

---

### 4. L'Effetto Body e la Formula Completa con $V_{SB}$

Se tra Source e Bulk applichiamo una tensione $V_{SB} > 0$, la giunzione substrato-canale viene polarizzata inversamente:
* La caduta totale richiesta nel silicio per l'inversione sale da $2\Phi_F$ a **$2\Phi_F + V_{SB}$**.
* La zona di svuotamento si allarga e la carica da sostenere aumenta.

La formula completa diretta della soglia diventa:
$$V_{th}(V_{SB}) = V_{FB} + 2\Phi_F + \gamma \sqrt{2\Phi_F + V_{SB}}$$

Ovvero, espressa rispetto alla soglia naturale $V_{th0}$:
$$V_{th}(V_{SB}) = V_{th0} + \gamma \left( \sqrt{2\Phi_F + V_{SB}} - \sqrt{2\Phi_F} \right)$$
All'aumentare di $V_{SB}$, la tensione di soglia $V_{th}$ **aumenta**.

> [!WARNING]
> **Il vincolo fisico della giunzione nel Bulk vs [SOI](./SOI.md):**
> Nel Bulk convenzionale, tra Source ($n^+$) e Substrato ($p$) esiste una vera giunzione $p\text{-}n$. Possiamo applicare solo $V_{SB} > 0$ (*Reverse Body Bias* per alzare la soglia). Se tentassimo un *Forward Body Bias* ($V_{BS} > 0$, cioè $V_{SB} < 0$) per abbassare la soglia e accelerare il dispositivo, appena superati $0.3 - 0.4\,\text{V}$ la giunzione Source-Substrato si accenderebbe in diretta conducendo correnti parassite enormi e innescando il **latch-up**.
> Per superare questo limite e consentire una sintonizzazione dinamica bidirezionale della soglia (sia Turbo FBB che Sleep RBB) senza rischi di conduzione di giunzione, si adotta la tecnologia [UTBB FD-SOI](./SOI.md), dove l'ossido sepolto (BOX) isola completamente il canale dal Back-Gate.

---

### 5. La Deriva Termica della Soglia $V_{th}(T)$

All'aumentare della temperatura $T$, la concentrazione intrinseca $n_i(T)$ cresce in modo esponenziale:
$$n_i(T) \propto T^{3/2} \, e^{-\frac{E_g}{2 k_B T}}$$

Poiché il potenziale di Fermi vale $\Phi_F(T) = \frac{k_B T}{q} \ln\left(\frac{N_A}{n_i(T)}\right)$, all'aumentare di $T$ il potenziale $\Phi_F$ **cala vistosamente** (il livello di Fermi $E_F$ si sposta verso il centro del gap $E_i$). Per raggiungere la forte inversione serve meno curvatura di banda superficiale ($2\Phi_F$) e una minore carica fissa di svuotamento $Q_{d,MAX}$.

* **Transistor nMOS:** $\frac{\partial V_{Tn}}{\partial T} \approx -1\text{ mV/K}$ (la soglia scende).
* **Transistor pMOS:** $\frac{\partial V_{Tp}}{\partial T} \approx +2\text{ mV/K}$ (la soglia sale verso 0 V).
* **Conclusione:** **In modulo $|V_{th}|$ cala per entrambi i tipi di transistor**, che diventano più conduttivi e facili da accendere alle alte temperature.

---

### 6. L'Effetto Body nelle Serie di Transistor e nel Folded MOS

Quando transistor MOS sono posti in serie (come nelle catene di pull-down delle porte logiche NAND o nei transistor lunghi ripiegati [Folded MOS](./Layout%20e%20Tecniche%20di%20Progettazione%20dei%20MOS.md)):
* Il dispositivo con Source a massa ha $V_{SB1} = 0\text{ V}$ e soglia nominale $V_{th0}$.
* I transistor sovrastanti vedono il proprio Source a tensioni via via crescenti ($V_S > 0\text{ V}$), imponendo **$V_{SB} > 0\text{ V}$**.
* **La soglia $V_{th}$ aumenta progressivamente salendo verso il Drain**, riducendo la corrente e aumentando la resistenza dinamica di canale.
* **Nei riferimenti di corrente integrati:** Come analizzato in [Riferimenti di Corrente e Circuiti di Start-Up](./Riferimenti%20di%20Corrente%20e%20Start-Up.md), inserire un resistore di degenerazione $R_S$ al source di un NMOS solleva $V_S = R_S I_{out} > 0\text{ V}$, provocando $V_{SB} > 0\text{ V}$ e distorcendo il bilanciamento delle soglie tra i rami dello specchio.

---

### 7. Cosa succede quando scendiamo di dimensioni? (Effetti 2D/3D)

La formula classica monodimensionale a canale lungo assume che $V_{th}$ non dipenda né da $W$ né da $L$. Nei dispositivi nanometrici reali intervengono invece:

1. **La variabilità statistica di processo (Legge di Pelgrom & RDF):** A causa del numero finito di atomi di drogante nel canale (*Random Dopant Fluctuation*), la soglia oscilla casualmente tra transistor vicini: $\sigma(\Delta V_{th}) = \frac{A_{Vth}}{\sqrt{W \cdot L}}$.
2. **L'abbassamento deterministico della soglia ($V_{th}$ Roll-Off):** Nei canali corti, le sacche di svuotamento laterali di Source e Drain condividono la carica del canale (*charge sharing*), facendo crollare $V_{th}$ al calare di $L$.
   👉 Approfondimento: [Vth Roll-Off](../Effetti%20di%20Canale%20Corto/Vth%20roll%20off.md)
3. **L'effetto del potenziale di Drain (DIBL):** La tensione applicata al Drain abbassa la barriera elettrostatica all'ingresso del canale: $V_{th}(V_{DS}) = V_{th0} - \eta V_{DS}$.
   👉 Approfondimento: [DIBL](../Effetti%20di%20Canale%20Corto/DIBL.md)

---

*Pagine correlate:*
- [Riferimenti di Corrente e Circuiti di Start-Up](./Riferimenti%20di%20Corrente%20e%20Start-Up.md)
- [Overdrive e Regioni di Inversione](./Overdrive%20e%20Regioni%20di%20Inversione.md)
- [Layout e Tecniche di Progettazione dei MOS](./Layout%20e%20Tecniche%20di%20Progettazione%20dei%20MOS.md)
- [MOS](./MOS.md)
- [Capacità parassite nel MOSFET](./Capacit%C3%A0%20parassite%20nel%20MOSFET.md)
- [Matching e Variabilita nei Componenti Integrati](./Matching%20e%20Variabilita%20nei%20Componenti%20Integrati.md)
- [Condensatori](./Condensatori.md)
- [Vth Roll-Off](../Effetti%20di%20Canale%20Corto/Vth%20roll%20off.md)
- [DIBL](../Effetti%20di%20Canale%20Corto/DIBL.md)
- [Conduzione di Sottosoglia e Rapporto Ion/Ioff](../Effetti%20di%20Canale%20Corto/Rapporto%20Ion%20Ioff%20e%20sottosoglia.md)
- [Analogico non si scende di dimensioni](../Scaling%20e%20Limiti%20Fisici/Analogico%20non%20si%20scende%20di%20dimensioni.md)



