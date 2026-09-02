Searched for "Caratteristica di Trasferimento"
Viewed Caratteristica%20di%20Trasferimento%20e%20Rigenerazione.md:1-46
Listed directory Famiglie%20Logiche
Viewed TTL%20%28Transistor-Transistor%20Logic%29.md:1-60

Per calcolare i **Margini di Rumore** di una qualsiasi porta logica (inclusa l'ECL), si segue un procedimento preciso diviso in **3 passi**:

---

### PASSO 1: Individuare i 4 Valori Chiave

Per calcolare i margini di rumore servono **4 tensioni fondamentali**:

| Simbolo | Nome | Cosa rappresenta fisicamente |
| :--- | :--- | :--- |
| **$V_{OH}$** | *Output High* | La tensione **massima/nominale** che la porta eroga quando spara un **1**. |
| **$V_{OL}$** | *Output Low* | La tensione **minima/nominale** che la porta eroga quando spara uno **0**. |
| **$V_{IH}$** | *Input High* | La tensione minima che una porta deve ricevere per essere **sicura al 100%** che sia un **1**. |
| **$V_{IL}$** | *Input Low* | La tensione massima che una porta può ricevere per essere **sicura al 100%** che sia uno **0**. |

---

### PASSO 2: Come si calcolano $V_{IL}$ e $V_{IH}$? (La regola della pendenza $-1$)

I valori di uscita $V_{OH}$ e $V_{OL}$ si calcolano banalmente analizzando il circuito agli stati estremi (transistor spento o acceso a fondo). 

Ma **come si stabiliscono matematicamente $V_{IL}$ e $V_{IH}$** sulla Caratteristica di Trasferimento ($V_O = f(V_I)$)?

Si cercano i punti in cui la derivata della curva (cioè il guadagno differenziale $A_v$) vale esattamente **$-1$**:

$$\frac{dV_O}{dV_I} = -1$$

```
V_O ^
    │ ══════════ (V_OH)
    │           \
    │            \  <- Punto A: dVo/dVi = -1  ===> QUI STA V_IL
    │             \
    │              \  <- ZONA DI ALTO GUADAGNO (|Av| > 1): transizione ripida
    │               \
    │                \ <- Punto B: dVo/dVi = -1 ===> QUI STA V_IH
    │                 \
    │                  ══════════ (V_OL)
    └─────────────────────────────────────> V_I
                  V_IL        V_IH
```

#### Perché proprio dove la derivata vale $-1$?
* **Nelle zone piatte ($|A_v| < 1$):** il circuito è un **attenuatore di rumore** (se l'ingresso oscilla di $\pm 10\text{ mV}$, l'uscita oscilla di soli $\pm 2\text{ mV}$, smorzando il disturbo).
* **Nella zona centrale ($|A_v| > 1$):** il circuito è un **amplificatore** (un disturbo di $\pm 10\text{ mV}$ viene moltiplicato e crea un errore).
* I punti con pendenza **$-1$** sono il confine esatto tra la zona sicura (che uccide il rumore) e la zona instabile.

---

### PASSO 3: Applicare le Formule dei Margini

Una volta noti i 4 valori, i margini di rumore sono semplicemente le distanze tra ciò che **esce** da una porta e ciò che è **richiesto** dalla porta successiva:

$$NM_H = V_{OH} - V_{IH}$$
$$NM_L = V_{IL} - V_{OL}$$

Il **margine di rumore complessivo della famiglia** è il caso peggiore tra i due:
$$NM = \min(NM_H, NM_L)$$

---

### Esempio Pratico e Reale: Calcolo dei Margini in ECL

Facciamo i conti reali sulla classica porta **ECL 10K** alimentata con:
* $V_{CC} = 0\text{ V}$ (Massa)
* $V_{EE} = -5.2\text{ V}$
* Resistenza di carico $R_C = 220\ \Omega$
* Corrente di coda $I_0 = 4\text{ mA}$
* Tensione di riferimento $V_{ref} = -1.29\text{ V}$
* Caduta base-emettitore $V_{BE} \approx 0.85\text{ V}$

```
                      Vcc = 0V
                   ┌─────┴─────┐
                  [Rc]        [Rc]
                   │           │
                   ├───────────┼──────── (Basi degli Emitter Follower)
                  ┌┴┐         ┌┴┐
            Vi o──┤ │ Q1   Q2 │ ├──o Vref (-1.29V)
                  └┬┘         └┬┘
                   └───┬───────┘
                       │
                      (↓) I0 = 4 mA
                       │
                      Vee = -5.2V
```

---

#### 1. Calcolo di $V_{OH}$ (Uscita Alta)
Quando l'ingresso $V_I$ è basso, $Q_1$ è spento e non assorbe corrente.
* Tensione sul collettore di $Q_1$: $V_C = 0\text{ V}$ (nessuna caduta su $R_C$).
* L'uscita passa attraverso l'emitter follower ($Q_3$):
  $$V_{OH} = 0\text{ V} - V_{BE} = 0 - 0.85\text{ V} = \mathbf{-0.85\text{ V}}$$

---

#### 2. Calcolo di $V_{OL}$ (Uscita Bassa)
Quando l'ingresso $V_I$ è alto, tutta la corrente $I_0 = 4\text{ mA}$ passa dentro $Q_1$.
* Caduta sul resistore $R_C$: $\Delta V = R_C \cdot I_0 = 220\ \Omega \cdot 4\text{ mA} = 0.88\text{ V}$.
* Tensione sul collettore: $V_C = 0\text{ V} - 0.88\text{ V} = -0.88\text{ V}$.
* L'uscita dopo l'emitter follower:
  $$V_{OL} = -0.88\text{ V} - V_{BE} = -0.88 - 0.85\text{ V} = \mathbf{-1.73\text{ V}}$$

Lo **swing logico** totale è: $\Delta V = V_{OH} - V_{OL} = -0.85 - (-1.73) = \mathbf{0.88\text{ V}}$.

---

#### 3. Calcolo di $V_{IL}$ e $V_{IH}$
La coppia differenziale a BJT sposta la corrente $I_0$ secondo la caratteristica a tangente iperbolica:
$$I_{C1} = \frac{I_0}{1 + e^{-(V_I - V_{ref})/V_T}}$$

La tensione di uscita è:
$$V_O(V_I) = - R_C I_{C1} - V_{BE} = - \frac{R_C I_0}{1 + e^{-(V_I - V_{ref})/V_T}} - V_{BE}$$

Derivando rispetto a $V_I$ e imponendo la pendenza unitaria $\frac{dV_O}{dV_I} = -1$, grazie all'elevata transconduttanza del BJT ($V_T \approx 26\text{ mV}$) si ottiene che la transizione avviene in una finestrella simmetrica di circa $\pm 120\text{ mV}$ attorno a $V_{ref}$:

* **$V_{IH}$ (Ingresso Alto Minimo):**
  $$V_{IH} = V_{ref} + 0.12\text{ V} = -1.29\text{ V} + 0.12\text{ V} = \mathbf{-1.17\text{ V}}$$
* **$V_{IL}$ (Ingresso Basso Massimo):**
  $$V_{IL} = V_{ref} - 0.12\text{ V} = -1.29\text{ V} - 0.12\text{ V} = \mathbf{-1.41\text{ V}}$$

---

#### 4. Calcolo Finale dei Margini di Rumore

Applichiamo le definizioni:

* **Margine di Rumore Alto ($NM_H$):**
  $$NM_H = V_{OH} - V_{IH} = -0.85\text{ V} - (-1.17\text{ V}) = \mathbf{+0.32\text{ V} = 320\text{ mV}}$$

* **Margine di Rumore Basso ($NM_L$):**
  $$NM_L = V_{IL} - V_{OL} = -1.41\text{ V} - (-1.73\text{ V}) = \mathbf{+0.32\text{ V} = 320\text{ mV}}$$

---

### Cosa significano questi numeri nella pratica?

1. **Se una porta trasmette un $1$ ($V_{OH} = -0.85\text{ V}$):**  
   Lungo la pista di rame può sommarsi un disturbo o caduta di potenziale negativa fino a **$320\text{ mV}$**. Finché la tensione che arriva all'ingresso non scende sotto $-1.17\text{ V}$, la porta ricevente interpreterà il dato come un **1 perfetto senza errori**.

2. **Se una porta trasmette uno $0$ ($V_{OL} = -1.73\text{ V}$):**  
   Può sovrapporsi un picco di rumore positivo fino a **$320\text{ mV}$**. Finché non supera $-1.41\text{ V}$, la porta ricevente leggerà un **0 perfetto**.