Ran command: `python -c "
import fitz, sys
sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open(r'c:\Users\Accetazione\Downloads\microele\modelli.pdf')

for page_idx in range(143, min(154, len(doc))):
    print(f'==============================')
    print(f'=== SLIDE {page_idx+1} (Page {page_idx+1}) ===')
    print(f'==============================')
    print(doc[page_idx].get_text())
"`

Ecco una spiegazione completa, fisica e numerica della **Slide 146** e del funzionamento in sottosoglia del MOS.

---

### 1. Cosa succede in Sottosoglia? (Slide 146)

Nel modello circuitale semplificato si insegna che se $V_{GS} < V_T$ il transistore è spento ($I_D = 0$). 
**Nella realtà fisica non è così**: quando $V_{GS} < V_T$, il silicio si trova in **debole inversione** ($V_{FB} < V_{GS} < V_T$). 

* All'interfaccia non c'è ancora un canale continuo e denso di elettroni, ma c'è già una **piccola densità di elettroni liberi**:
  $$n(0) \propto e^{\frac{q\Phi_S}{k_B T}}$$
* La corrente $I_D$ non è zero: **scorre una corrente che varia in modo puramente ESPONENZIALE con $V_{GS}$**, esattamente come in un diodo o in un BJT!

```
     Corrente I_D (Scala Logaritmica)
           ^
    1 mA   │                         / (Forte inversione: curva parabolica/lineare)
           │                        /
    1 μA   │                       /
           │                      /  <── V_GS = V_T
    1 nA   │                     /
           │                    /
    1 pA   │                   /   (Sottosoglia: retta esponenziale a pendenza costante!)
           │                  /
           └─────────────────┴────────────────────────► V_GS
                             V_T
```

---

### 2. Perché si comporta "simil-BJT"? (Diffusione vs Deriva)

La differenza fondamentale tra il funzionamento normale e quello in sottosoglia sta nel **meccanismo fisico con cui si muovono gli elettroni**:

| Regime | Come si muovono le cariche | Formula Corrente | Come in... |
| :--- | :--- | :--- | :--- |
| **Forte Inversione ($V_{GS} > V_T$)** | **Deriva (Drift):** C'è una pista conduttiva (il canale). Il campo elettrico tra Drain e Source trascina gli elettroni con una velocità $v = \mu E$. | $I_D \propto (V_{GS} - V_T)^2$ | Resistore controllato |
| **Sottosoglia ($V_{GS} < V_T$)** | **Diffusione (Diffusion):** Non c'è un canale continuo. Gli elettroni saltano la barriera di potenziale termicamente e **diffondono** per gradiente di concentrazione dal Source al Drain. | $I_D \propto e^{\frac{q V_{GS}}{n k_B T}}$ | **BJT** ($I_C \propto e^{\frac{q V_{BE}}{k_B T}}$) |

Fisicamente, la struttura $n^+ (\text{Source}) - p (\text{Substrato}) - n^+ (\text{Drain})$ in debole inversione funziona esattamente come un **transistore BJT NPN laterale**, dove:
* Il **Source** fa da *Emettitore* (inietta elettroni).
* La regione sotto l'ossido fa da *Base* (attraversata per diffusione).
* Il **Drain** fa da *Collettore* (raccoglie gli elettroni).
* Il **Gate** fa da morsetto che abbassa la barriera di potenziale della base elettrostaticamente.

---

### 3. Da dove saltano fuori i "$60\text{ mV/decade}$"? (Subthreshold Swing $S$)

La **pendenza di sottosoglia** (o *Subthreshold Swing*, $S$) indica:
> *"Di quanti millivolt devo aumentare $V_{GS}$ per far decuplicare ($10\times$, cioè 1 decade) la corrente $I_D$?"*

#### A) Il calcolo teorico ideale
La corrente è $I_D \propto e^{\frac{q \Phi_S}{k_B T}} = 10^{\frac{q \Phi_S}{\ln(10) k_B T}}$.
Se ogni variazione di Gate si trasferisse interamente alla superficie ($\Delta\Phi_S = \Delta V_{GS}$), la pendenza ideale sarebbe:

$$S_{ideale} = \ln(10) \cdot \frac{k_B T}{q} = \ln(10) \cdot \Phi_T$$

A temperatura ambiente ($T = 300\text{ K}$), il potenziale termico è $\Phi_T = \frac{k_B T}{q} \approx 25.86\text{ mV}$:
$$S_{ideale} = 2.3026 \times 25.86\text{ mV} \approx \mathbf{59.6\text{ mV/decade} \approx 60\text{ mV/decade}}$$

#### B) Nei dispositivi reali (il partitore capacitivo $\alpha$)
Come visto prima, tra il Gate e il silicio c'è il partitore capacitivo tra l'ossido $C_{ox}$ e la capacità di svuotamento $C_d$:
$$d\Phi_S = \frac{C_{ox}}{C_{ox} + C_d} dV_{GS} = \frac{1}{1 + \alpha} dV_{GS} \quad \text{con } \alpha = \frac{C_d}{C_{ox}}$$

Quindi nei dispositivi reali (Slide 146):
$$S = \frac{d V_{GS}}{d(\log_{10} I_D)} = \ln(10) \frac{k_B T}{q} (1 + \alpha) = 60\text{ mV} \cdot (1 + \alpha)$$

Poiché $\alpha > 0$, nei MOS reali servono tipicamente **$70\text{–}90\text{ mV}$** per aumentare la corrente di una decade.

> 🔋 **Perché è fondamentale nei chip moderni?**
> Se hai una corrente di perdita (*leakage*) a riposo e vuoi ridurla di un milione di volte ($10^6$, cioè 6 decadi), devi dare al Gate almeno $6 \times 80\text{ mV} = 480\text{ mV}$ di margine sotto la soglia. È per questo che non si può abbassare la tensione di alimentazione dei microprocessori a piacere senza avere dispersioni di batteria enormi!

---

### 4. Debole, Moderata e Forte Inversione: esistono confini netti?

Hai colto un punto cruciale di microelettronica: **la fisica è continua**, la transizione tra spento e acceso non è un interruttore a scatto a $V_T$.

Si definiscono convenzionalmente 3 regioni in base alla tensione di **Overdrive ($V_{ov} = V_{GS} - V_T$)**:

```
        DEBOLE INVERSIONE         MODERATA INVERSIONE            FORTE INVERSIONE
         (Sottosoglia)              (Transizione)
◄──────────────────────────────┼────────────────────────┼────────────────────────►
     V_GS - V_T < -50 mV        -50 mV < V_ov < +150 mV       V_GS - V_T > 200 mV
```

1. **Debole Inversione (Weak Inversion / Sottosoglia):**
   * Corrisponde a $V_{GS} \le V_T - 50\text{ mV}$ (Overdrive negativo).
   * La carica mobile $Q_i$ è trascurabile rispetto alla carica fissa $Q_d$.
   * Trasporto: **Diffusione pura**.
   * Relazione $I_D(V_{GS})$: **Puro esponenziale** ($I_D \propto e^{V_{GS}}$).
   * Massima efficienza energetica: altissimo rapporto transconduttanza/corrente ($g_m/I_D \approx 25\text{--}28\text{ V}^{-1}$, usato nei circuiti ultra-low-power come gli smartwatch o i pacemaker).

2. **Moderata Inversione (Moderate Inversion):**
   * Intervallo a cavallo della soglia: da circa **$-50\text{ mV}$ a $+150\text{ mV}$** di Overdrive.
   * La carica mobile e la carica fissa sono confrontabili ($Q_i \approx Q_d$).
   * Trasporto: coesistono sia deriva che diffusione.
   * La formula non è né puramente esponenziale né puramente quadratica (è la zona di raccordo).

3. **Forte Inversione (Strong Inversion):**
   * Corrisponde a un Overdrive sicuro **$V_{ov} = V_{GS} - V_T \ge 150\text{--}200\text{ mV}$**.
   * La carica mobile di canale $Q_i$ sovrasta totalmente la carica di svuotamento.
   * Trasporto: **Deriva (Drift)**.
   * Relazione $I_D(V_{GS})$: **Quadratica** a canale lungo ($I_D \propto V_{ov}^2$) o **Lineare** a canale corto (per saturazione della velocità).

Quindi la tua intuizione è esattissima: quando in progettazione analogica vogliamo essere **sicuri** di essere in piena forte inversione (dove valgono le formule quadratiche classiche), imponiamo un Overdrive di almeno **$150\text{--}200\text{ mV}$**.