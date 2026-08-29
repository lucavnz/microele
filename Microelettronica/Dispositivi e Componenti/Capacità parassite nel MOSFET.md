# Capacità Parassite e Intrinseche nel MOSFET

Nel transistor MOSFET reale le capacità non sono componenti lineari ideali a valore fisso: si dividono tra **capacità estrinseche/parassite geometriche** (fisse o di giunzione) e **capacità intrinseche di canale** (fortemente dipendenti dal potenziale e dal regime di funzionamento).

---

### 1. Perché Due Isolanti a Contatto sono "in Serie" e non semplicemente $d_1 + d_2$?

Quando si analizza la struttura di Gate del MOS prima dell'accensione ($V_{FB} < V_{GS} < V_{th}$), sotto il Gate si trovano a contatto due strati isolanti: l'ossido di silicio ($\text{SiO}_2$) e lo strato di silicio svuotato dalle lacune ($\text{SCR}$).

```
Gate (Polisilicio/Metallo)  ─────────────────────────────────
                            │  Ossido SiO2 (ε_ox,  tox)     │  Caduta V_ox
Interfaccia Silicio-Ossido  ─────────────────────────────────
                            │  Silicio svuotato (ε_si, Wd)  │  Caduta Φ_s
Bulk (Silicio Neutro p)     ─────────────────────────────────
```

#### A) Se i materiali fossero identici ($\varepsilon_1 = \varepsilon_2 = \varepsilon$)
Se unissimo due blocchi dello stesso isolante di spessore $d_1$ e $d_2$, la formula della serie circuitale darebbe:
$$\frac{1}{C_{tot}} = \frac{1}{C_1} + \frac{1}{C_2} = \frac{d_1}{\varepsilon A} + \frac{d_2}{\varepsilon A} = \frac{d_1 + d_2}{\varepsilon A} \implies C_{tot} = \frac{\varepsilon A}{d_1 + d_2}$$
> **La formula della serie è esattamente la somma degli spessori!** Dire che due dielettrici sono in serie è la traduzione matematica di calcolare la capacità di un blocco unico di spessore totale $(d_1 + d_2)$.

#### B) Nel MOS i materiali sono diversi ($\varepsilon_{ox} \neq \varepsilon_{si}$)
L'ossido ha permittività $\varepsilon_{ox} \approx 3.9 \cdot \varepsilon_0$, mentre il silicio ha $\varepsilon_{si} \approx 11.7 \cdot \varepsilon_0$ (è **3 volte più permissivo**).
Poiché il vettore spostamento elettrico è continuo ($D = \frac{Q}{A}$), la caduta di tensione totale è la somma delle cadute nei singoli strati:
$$V_{tot} = V_{ox} + \Phi_s = E_{ox} t_{ox} + E_{si} W_d = \frac{Q}{A} \left( \frac{t_{ox}}{\varepsilon_{ox}} + \frac{W_d}{\varepsilon_{si}} \right)$$

Dividendo per $Q$:
$$\frac{1}{C_{tot}} = \frac{V_{tot}}{Q} = \frac{t_{ox}}{\varepsilon_{ox} A} + \frac{W_d}{\varepsilon_{si} A} = \frac{1}{C_{ox}} + \frac{1}{C_{dep}}$$

#### C) Lo Spessore Equivalente di Ossido (EOT)
Possiamo vedere la serie come un unico strato di ossido equivalente (**EOT**):
$$d_{eq} = t_{ox} + W_d \cdot \frac{\varepsilon_{ox}}{\varepsilon_{si}} \approx t_{ox} + \frac{W_d}{3}$$
$$C_{tot} = \frac{\varepsilon_{ox} A}{d_{eq}}$$

👉 Approfondimento sul partitore capacitivo e la soglia: [La soglia da cosa dipende](./La%20soglia%20da%20cosa%20dipende.md)

---

### 2. Perché le Sacche di Drain e Source NON fanno la Serie con lo Svuotamento?

Sorge spontaneo chiedersi: *«Se sotto il Gate c'è la serie $C_{ox} \leftrightarrow C_{dep}$, perché sulle sovrapposizioni con Drain e Source no?»*

La differenza fisica sta nel **livello di drogaggio**:
* **Nel Canale (Substrato $p$):** drogaggio moderato ($N_A \approx 10^{16}-10^{17}\text{ cm}^{-3}$). Il campo elettrico scava una zona di svuotamento profonda centinaia di nanometri ($W_d$), che agisce da secondo isolante.
* **Nelle sacche di Source e Drain ($n^+$):** drogaggio degenerato altissimo ($N_D \approx 10^{20}\text{ cm}^{-3}$). La lunghezza di schermatura di Debye all'interfaccia con l'ossido è microscopica (frazioni di nanometro): **il silicio $n^+$ si comporta a tutti gli effetti come un metallo conduttore ideale**.

Di conseguenza, le capacità di sovrapposizione (**Overlap**) sono condensatori a facce piane ideali con dielettrico d'ossido puro:
$$C_{gso} = C_{ox}' \cdot W \cdot L_{ov} = \frac{\varepsilon_{ox}}{t_{ox}} W L_{ov}$$
$$C_{gdo} = C_{ox}' \cdot W \cdot L_{ov} = \frac{\varepsilon_{ox}}{t_{ox}} W L_{ov}$$
dove $L_{ov}$ è l'infiltrazione laterale delle diffusioni sotto il Gate.

---

### 3. La Formula Completa: Overlap Geometrico ($O$) + Canale Intrinseco ($C$)

Ogni capacità vista dal terminale di Gate è la somma di due contributi:

$$\begin{aligned}
C_{GS} &= \underbrace{C_{gso}}_{\text{Overlap fisso}} + \underbrace{C_{gsc}}_{\text{Carica di Canale}} \\
C_{GD} &= \underbrace{C_{gdo}}_{\text{Overlap fisso}} + \underbrace{C_{gdc}}_{\text{Carica di Canale}} \\
C_{GB} &= \underbrace{C_{gbo}}_{\text{Overlap perimetrale}} + \underbrace{C_{gbc}}_{\text{Accoppiamento Bulk}}
\end{aligned}$$

```
                ┌────────────── Gate ──────────────┐
                │                                  │
          ┌─────┴──────┐                    ┌──────┴─────┐
          │   C_gso    │                    │   C_gdo    │   (Overlap geometrico puro: Cox' * W * Lov)
          └─────┬──────┘                    └──────┬─────┘
                ▼                                  ▼
      ┌──────────────────┐  C_gsc    C_gdc  ┌──────────────────┐
      │   Source (n+)    ├────────┬─────────┤    Drain (n+)    │
      └──────────────────┘        │         └──────────────────┘
                                  ▼
                        Canale di Inversione (Qi)
                                  │
                                C_gbc
                                  ▼
                           Substrato Bulk (p)
```

#### Cosa succede al variare del regime di polarizzazione?

1. **A Transistor Spento / Sottosoglia ($V_{GS} < V_{th}$):**
   * Non ci sono elettroni liberi nel canale ($Q_i = 0 \implies C_{gsc} = 0, C_{gdc} = 0$).
   * Il Gate vede direttamente il Bulk attraverso la serie ossido-svuotamento: $C_{gbc} = \frac{C_{ox} C_{dep}}{C_{ox} + C_{dep}} W L$.
   * $C_{GS} = C_{gso}$ e $C_{GD} = C_{gdo}$.

2. **A Transistor Acceso in Triodo / Zona Lineare ($V_{GS} > V_{th}$, $V_{DS} \approx 0$):**
   * Si forma lo strato di inversione con carica totale $Q_i = -W L C_{ox}' (V_{GS} - V_{th})$.
   * **Schermo Elettrostatico:** il denso strato di elettroni liberi funge da gabbia di Faraday tra Gate e Bulk, bloccando le linee di campo verso il substrato $\implies \mathbf{C_{gbc} \to 0}$.
   * La capacità di canale $C_{ox,tot} = C_{ox}' W L$ si ripartisce equamente tra i due terminali:
     $$C_{gsc} \approx \frac{1}{2} C_{ox}' W L, \quad C_{gdc} \approx \frac{1}{2} C_{ox}' W L$$

3. **In Saturazione ($V_{DS} \ge V_{GS} - V_{th}$):**
   * Il canale subisce la strozzatura (**pinch-off**) al Drain: la carica di canale termina prima di raggiungere la sacca di Drain ed è agganciata elettrostaticamente solo al Source.
   * Di conseguenza:
     $$C_{gsc} \approx \frac{2}{3} C_{ox}' W L, \quad \mathbf{C_{gdc} \approx 0}$$
   * La capacità totale Drain-Gate crolla al **solo contributo parassita di overlap**:
     $$\mathbf{C_{GD} = C_{gdo}}$$

> [!NOTE]
> In saturazione il crollo di $C_{GD}$ al solo overlap $C_{gdo}$ è di fondamentale importanza nei circuiti analogici: $C_{GD}$ costituisce la capacità di retroazione ingresso-uscita che viene amplificata dal guadagno dello stadio per **Effetto Miller** ($C_{in,Miller} \approx C_{GS} + (1 + |A_v|) C_{GD}$).

---

### 4. Tabella Riassuntiva dei Regimi di Funzionamento

| Regime | Canale ($Q_i$) | $C_{GS}$ | $C_{GD}$ | $C_{GB}$ |
| :--- | :--- | :--- | :--- | :--- |
| **Interdizione / Off** ($V_{GS} < V_{th}$) | $0$ (Assente) | $C_{gso}$ | $C_{gdo}$ | $C_{gbo} + \frac{C_{ox} C_{dep}}{C_{ox} + C_{dep}} W L$ |
| **Triodo / Lineare** ($V_{DS} \approx 0$) | Uniforme | $C_{gso} + \frac{1}{2} C_{ox}' W L$ | $C_{gso} + \frac{1}{2} C_{ox}' W L$ | $C_{gbo} \approx 0$ |
| **Saturazione** ($V_{DS} \ge V_{ov}$) | Strozzato (*Pinch-off*) | $C_{gso} + \frac{2}{3} C_{ox}' W L$ | **$C_{gdo}$ (Solo overlap!)** | $C_{gbo} \approx 0$ |

---

### 5. Le Capacità di Giunzione verso il Bulk ($C_{DB}$ e $C_{SB}$)

Le tasche di Source ($n^+$) e Drain ($n^+$) immerse nel substrato $p$ formano due **diodi a giunzione $pn$ polarizzati inversamente**. 

Le loro capacità parassite dipendono dalla tensione inversa applicata $V_R$ secondo la legge delle giunzioni:
$$C_j(V_R) = \frac{C_{j0}}{\left(1 + \frac{V_R}{\Phi_0}\right)^m}$$

Ciascuna si scompone in due parti geometriche:
1. **Capacità di Fondo (*Bottom Plate*):** dovuta all'area piana inferiore della sacca ($Area = W \cdot L_{diff}$).
2. **Capacità Perimetrale (*Sidewall*):** dovuta al perimetro laterale a contatto con l'ossido di isolamento ([STI/LOCOS]STI/LOCOS](./MOS.md)) e con il canale.

👉 Per abbattere drasticamente $C_{DB}$ e $C_{SB}$ si impiega la tecnologia [SOI (Silicon On Insulator)]SOI (Silicon On Insulator)](./SOI.md), dove l'ossido sepolto BOX sostituisce il silicio massivo.

---

### 6. Sintesi Circuitale dei Modelli Equivalenti

```text
Transistor SPENTO (Vgs < Vth):
  Gate ───┬────────[ Cox ]───────┬──────[ Cdep ]───── Bulk  (C_GB attiva)
          │                      │
          ├──[ C_gso (Overlap) ]─┴── Source
          │
          └──[ C_gdo (Overlap) ]──── Drain

Transistor ACCESO in Saturazione (Vgs > Vth, Vds >= Vov):
  Gate ───┬──[ 2/3 Cox*W*L ]─────── Canale/Source
          │
          ├──[ C_gso (Overlap) ]─── Source
          │
          └──[ C_gdo (Overlap) ]─── Drain (il canale è staccato dal pinch-off!)
```

---

*Pagine correlate:*
- [Famiglia Logica e Costo per Bit](../Famiglie%20Logiche/Famiglia%20Logica%20e%20Costo%20per%20Bit.md)
- [MOS](./MOS.md)
- [Condensatori](./Condensatori.md)
- [La soglia da cosa dipende](./La%20soglia%20da%20cosa%20dipende.md)
- [Transitori del diodo e capacita](./Transitori%20del%20diodo%20e%20capacita.md)
- [SOI](./SOI.md)
- [Difficoltà nel fare un componente ideale](../Scaling%20e%20Limiti%20Fisici/Difficolt%C3%A0%20nel%20fare%20un%20componente%20ideale.md)
- [Rapporto Ion Ioff e sottosoglia](../Effetti%20di%20Canale%20Corto/Rapporto%20Ion%20Ioff%20e%20sottosoglia.md)
- [DIBL](../Effetti%20di%20Canale%20Corto/DIBL.md)
