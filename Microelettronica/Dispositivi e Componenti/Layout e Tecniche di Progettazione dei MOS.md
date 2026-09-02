# Layout del Transistor MOS e Tecniche di Progettazione

Nella progettazione dei circuiti integrati moderni (sia digitali che analogici ad alte prestazioni), il layout fisico del transistor MOS è cruciale per minimizzare le capacità parassite, abbattere i ritardi RC, garantire il matching statistico e gestire gli effetti termici e di affidabilità.

---

### 1. Parametri Fisici e Variabilità del MOS

I parametri tecnologici di base di un processo CMOS governano sia il punto di lavoro che i limiti operativi del dispositivo:

```
                            PARAMETRI OPERATIVI FONDAMENTALI
  ┌───────────────────────┬─────────────────────────────────────────────────────────┐
  │ Parametro             │ Significato Fisico e Dipendenze                          │
  ├───────────────────────┼─────────────────────────────────────────────────────────┤
  │ V_T (Tensione Soglia) │ Deriva termica: -1 mV/K (nMOS), +2 mV/K (pMOS)          │
  │ k' = μ · Cox          │ Transconduttanza di processo (k'_n ≈ 3 · k'_p)          │
  │ Isat / μm             │ Massima densità di corrente per larghezza di canale     │
  │ Isub                  │ Corrente di sottosoglia e perdite parassite (Leakage)   │
  │ V_B                   │ Tensione di rottura (Breakdown di giunzione o ossido)   │
  └───────────────────────┴─────────────────────────────────────────────────────────┘
```

#### A) Deriva Termica della Tensione di Soglia $V_T(T)$
Al crescere della temperatura $T$, la concentrazione intrinseca $n_i(T)$ cresce esponenzialmente:
$$n_i(T) = \sqrt{N_c N_v} \, e^{-\frac{E_g}{2 k_B T}}$$
Di conseguenza, il potenziale di Fermi $\phi_F(T) = \frac{k_B T}{q} \ln\left(\frac{N_A}{n_i(T)}\right)$ **diminuisce** (il livello di Fermi $E_F$ si avvicina al centro della banda proibita $E_i$). Serve meno curvatura di banda superficiale ($2\phi_F$) e meno carica fissa di svuotamento per creare il canale:
* **Per l'nMOS:** la soglia $V_{Tn}$ scende con pendenza $\frac{\partial V_{Tn}}{\partial T} \approx -1\text{ mV/K}$.
* **Per il pMOS:** la soglia $V_{Tp}$ (originariamente negativa) sale verso lo zero con pendenza $\frac{\partial V_{Tp}}{\partial T} \approx +2\text{ mV/K}$.
* **In modulo:** **sia per l'nMOS che per il pMOS, $|V_T|$ cala all'aumentare della temperatura**, rendendo i transistor più facili da accendere a caldo.

#### B) Massima Corrente $I_{sat}/\mu\text{m}$ ed Elettromigrazione
Il parametro $I_{sat}/\mu\text{m}$ indica la massima corrente erogabile per micrometro di larghezza $W$:
* Fissa la densità di corrente massima ammissibile nelle piste metalliche e nei contatti per evitare l'**elettromigrazione** (secondo la Legge di Black per il tempo medio di guasto $\text{MTTF}$).
* Stabilisce il dimensionamento minimo delle piste di metallo e del numero di contatti/vias da disporre sulle sacche di Source e Drain.

---

### 2. Struttura Fisica Bulk: Isolamento STI, Pareti e Channel-Stop $P^+$

Nei processi avanzati sub-micrometrici l'isolamento è garantito da trincee **STI** (*Shallow Trench Isolation*):

![Struttura Bulk CMOS con STI e Channel-Stop](../../Immagini/mos_sti_bulk_cross_section.png)

* **Contatto Diretto:** Le sacche di Source e Drain $N^+$ sono autoallineate e **sbattono a filo direttamente contro la parete di ossido $\text{SiO}_2$ dello STI** (profondo $0.4\,\mu\text{m} > x_j = 0.2\,\mu\text{m}$).
* **Anello $P^+$ Channel-Stop:** Alla base della trincea STI è presente un'impiantazione $P^+$ ad alta concentrazione per evitare l'inversione parassita del silicio sotto l'ossido spesso.
* **Capacità Parassite di Giunzione:**
  $$C_{\text{giunzione}} = \underbrace{c_j \cdot (W \cdot L_D)}_{\text{Fondo (Area)}} + \underbrace{c_{jsw} \cdot (2W + 2L_D)}_{\text{Pareti Laterali (Perimetro STI / Channel-stop)}}$$

---

### 3. MOS Largo: Fingering e Condivisione delle Diffusioni

Nei transistor con larghezza elevata ($W \gg L$, es. $W = 40\,\mu\text{m}$), realizzare un unico nastro rettilineo di Gate introduce gravi limitazioni:
1. **Resistenza distribuita di Gate ($R_G$):** Il polisilicio ha resistenza di strato non trascurabile ($R_\square \approx 10-30\,\Omega/\square$). Un gate lungo e stretto crea una linea di trasmissione RC distribuita che rallenta la commutazione del canale.
2. **Capacità parassita di Drain ($C_{DB}$):** Una singola sacca di Drain estesa su tutta la larghezza $W$ crea un'area di fondo e un perimetro considerevoli.

![Confronto Layout Singolo Dito vs Interdigitato](../../Immagini/mos_fingering_layout_comparison.png)

#### A) La Tecnica del Fingering ($N$ dita in parallelo)
Dividendo il transistor in $N$ dita parallele ciascuna di larghezza $W_f = W/N$:
* La resistenza del singolo dito si riduce di $N$ volte ($R_{G,dito} = R_\square \frac{W/N}{L} = \frac{R_G}{N}$).
* Essendo le $N$ dita collegate in parallelo da una barra metallica comune, la resistenza totale equivalente di Gate crolla quadraticamente:
  $$\mathbf{R_{G,\text{tot}} = \frac{R_G}{N^2}}$$
* Se il gate viene contattato da **entrambe le estremità**, si guadagna un ulteriore fattore 4: $R_{G,\text{tot}} = \frac{R_G}{4 N^2}$.

#### B) Condivisione delle Diffusioni ($\mathbf{S - G - D - G - S}$)
Disponendo le dita in configurazione interdigitata simmetrica:
* **I Drain interni sono condivisi:** due dita adiacenti condividono la stessa sacca di Drain.
* Per un numero pari di dita $N$, si hanno solo $N/2$ sacche di Drain (con $N/2 + 1$ sacche di Source poste alle estremità esterne).
* **Risultato:** **L'area totale di Drain si DIMEZZA**, abbattendo la capacità parassita $C_{DB}$ del $40\% \div 50\%$.

#### C) L'Analisi dello "Sweet Spot" (Perché la grana iper-fine peggiora le cose)
Frazionare in un numero eccessivo di finger microscopici ($N \ge 40$, $W_f \le 1\,\mu\text{m}$) diventa controproducente:
* **Esplosione del perimetro laterale:** Ciascuna nuova sacca aggiunge due testate perimetrali affacciate sullo STI ($c_{jsw}$).
* **Capacità di instradamento metallico ($C_{\text{metal}}$):** Il fitto pettine di piste in Metallo 1 e Metallo 2 necessario per collegare decine di sacche sparse aggiunge capacità parassita verso il substrato.

| Configurazione | Dita ($N$) | Area Drain | Perimetro Drain | $C_{\text{giunz}}$ | $C_{\text{metallo}}$ | $C_{\text{tot}}$ | Resistenza $R_G$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Singolo Dito** | 1 | $40\,\mu\text{m}^2$ | $82\,\mu\text{m}$ | $81\text{ fF}$ | $0\text{ fF}$ | **$81\text{ fF}$** | $114\,R_\square$ (Lentissimo) |
| **Ottimo (Fingered)** | **4** | **$20\,\mu\text{m}^2$** | **$44\,\mu\text{m}$** | **$42\text{ fF}$** | **$4\text{ fF}$** | **$46\text{ fF}$** 🚀 | **$7.1\,R_\square$ (Velocissimo)** |
| **Grana Iper-fine** | 40 | $20\,\mu\text{m}^2$ | $80\,\mu\text{m}$ | $60\text{ fF}$ | $35\text{ fF}$ | **$95\text{ fF}$** ❌ | $0.07\,R_\square$ (Inutile) |

---

### 4. MOS Lungo e "Folded MOS" ($W/L \ll 1$)

Nelle applicazioni analogiche di precisione e a bassissima potenza (*Ultra-Low Power*), è spesso necessario realizzare transistor con $W/L \ll 1$ (es. $W = 1\,\mu\text{m}, L = 40\,\mu\text{m}$):
1. **Generazione di correnti ultra-basse ($10\text{ nA}$):** Per circuiti sempre accesi alimentati a batteria (IoT, biomedicale).
2. **Resistenze equivalenti gigantesche ($> 10\text{ M}\Omega$):** In zona lineare, senza sprecare l'enorme area richiesta da un resistore in polisilicio.
3. **Guadagno intrinseco elevatissimo ed eliminazione dell'effetto Early:** La resistenza di uscita vale $r_o = \frac{1}{\lambda I_D} \propto L$.

```
              REALIZZAZIONE DI UN TRANSISTOR LUNGO A MEANDRO (FOLDED MOS)
              
                 ┌────────────────────────────────────────────────────────┐
                 │                       PIANO DI GATE                    │ (Polisilicio comune)
                 └──────┬──────────────┬──────────────┬──────────────┬────┘
                        │              │              │              │
                    ┌───┴───┐      ┌───┴───┐      ┌───┴───┐      ┌───┴───┐
                    │  M1   │      │  M2   │      │  M3   │      │  M4   │
                    └───┬───┘      └───┬───┘      └───┬───┘      └───┬───┘
                        │              │              │              │
                   [Source = 0V]    [Nodo 1]       [Nodo 2]     [Drain = VDD]
                                   (V1 = 0.2V)    (V2 = 0.5V)
                                   (VSB2 > 0)     (VSB3 > 0)
```

#### A) Perché non fare una striscia rettilinea lunga?
* **Altezza delle Standard Cells:** Le righe di layout hanno altezza fissa ($3 \div 5\,\mu\text{m}$). Una striscia da $40\,\mu\text{m}$ romperebbe la continuità dell'alimentazione e del routing.
* **Gradienti Termici e Meccanici:** Una serpentina compatta ($5 \times 4\,\mu\text{m}$) confina il dispositivo nello stesso micro-ambiente termico.
* **Piste di Drain lontane:** Riduce le capacità e i disturbi captati dai metalli di collegamento.

#### B) L'Effetto Body nella Catena in Serie
Quando scorre corrente nella serie dei canali:
* Il transistor in basso ha $V_{SB1} = 0\text{ V} \implies V_{T1} = V_{T0}$.
* I nodi intermedi salgono a potenziale positivo ($V_X > 0\text{ V}$), imponendo **$V_{SB} > 0\text{ V}$** per tutti i transistor superiori:
  $$V_T = V_{T0} + \gamma\left(\sqrt{2\phi_F + V_{SB}} - \sqrt{2\phi_F}\right)$$
* **La tensione di soglia $V_T$ sale progressivamente salendo verso il Drain**, riducendo la corrente erogata rispetto al calcolo ideale (lo stesso identico fenomeno si osserva nelle pile di pull-down delle porte logiche NAND/NOR).
* *Nota fisica:* Questo effetto Body distribuito $V_{CB}(y) = V(y) - V_B > 0$ è intrinseco nel silicio ed è presente in modo identico anche all'interno del canale di un transistor rettilineo continuo.

---

### 5. Matching Avanzato nei Transistor MOS

Nelle coppie differenziali e negli specchi di corrente di precisione, la variabilità statistica è descritta dalla **Legge di Pelgrom**:
$$\sigma(V_T) = \frac{C_{VT}}{\sqrt{W_{\text{eff}} \cdot L_{\text{eff}}}} \qquad \frac{\sigma(k)}{k} = \frac{C_k}{\sqrt{W_{\text{eff}} \cdot L_{\text{eff}}}}$$

#### A) Confronto Matching: nMOS vs pMOS
A livello di tecnologia microscopica $C_{VT}$ è simile, ma **a parità di prestazioni circuitali ($I_D$ o $g_m$) il pMOS è nettamente superiore**:
* Poiché $\mu_p \approx \frac{1}{3}\mu_n$, per avere la stessa transconduttanza il pMOS richiede una larghezza $W_p \approx 3 W_n$.
* L'area fisica risulta 3 volte superiore ($3 \cdot W_n L$).
* Per la legge di Pelgrom:
  $$\sigma(\Delta V_{T,p}) = \frac{C_{VT}}{\sqrt{3 \cdot W_n L}} \approx \mathbf{0.58 \cdot \sigma(\Delta V_{T,n})} \quad (\mathbf{-42\% \text{ di mismatch!}})$$
* Inoltre il pMOS presenta un **rumore $1/f$ (flicker noise)** molto inferiore grazie al canale leggermente sepolto (*buried channel*). Per questo le coppie differenziali di ingresso di amplificatori operazionali a basso rumore/offset sono quasi sempre realizzate con **pMOS**.

#### B) Orientazione Rigorosa anche per Polisilicio e Diffusioni
Tutti i transistor e i resistori da accoppiare devono avere **identica orientazione geometrica**:
1. **Stress Meccanico del Package:** La contrazione anisotropa della resina ($\sigma_x \neq \sigma_y$) si trasmette attraverso l'ossido alterando la mobilità e la piezoresistività ($\pi_l \neq \pi_t$).
2. **Asimmetria di Incisione (Etching Bias):** La fotolitografia e l'attacco al plasma generano larghezze effettive diverse tra linee orizzontali e verticali ($W_X \neq W_Y$).
3. **Tilt Angle dell'Impiantazione ($7^\circ$):** Genera ombre asimmetriche nel drogaggio del canale e delle sacche.

#### C) Bilanciamento delle Sacche di Drain nelle Coppie Differenziali (1D vs 2D)
Nelle coppie differenziali interdigitate, la simmetria capacitiva delle uscite $V_{\text{out}+}$ (C) e $V_{\text{out}-}$ (D) è cruciale:

```
          LAYOUT 1D ASIMMETRICO (A-A-B-B)                LAYOUT 2D COMMON CENTROID
          
     ┌───┐  Gate A  ┌───┐  Gate B  ┌───┐            Riga 1: [D] [A] [B] [B] [A] [D]  (A=3, B=2 sacche)
     │ S │   [G]    │ D │   [G]    │ D │            Riga 2: [D] [B] [A] [A] [B] [D]  (A=2, B=3 sacche)
     └───┘          └───┘          └───┘                    ───────────────────────
       │              │              │              TOTALE:  A = 5 sacche, B = 5 sacche!
      [E]            [C]            [D] (Doppia!)            (Capacità parassite perfettamente bilanciate)
```

* **Errore nel layout 1D asimmetrico ($A-A-B-B$):** Il transistor A possiede 1 sola sacca di Drain condivisa (C), mentre il transistor B possiede 2 sacche di Drain (D) $\implies \mathbf{C_D \approx 2 \cdot C_C}$. Questo sbilanciamento capacitivo distrugge il bilanciamento dinamico e il **CMRR ad alta frequenza**.
* **Soluzione 2D Common Centroid (a scacchiera):** La seconda riga inverte il pattern, pareggiando perfettamente il numero di sacche di diffusione ($5 + 5$) e garantendo risposte in frequenza identiche su entrambi i rami differenziali.

---

*Pagine correlate:*
- [MOS](./MOS.md)
- [Capacità parassite nel MOSFET](./Capacit%C3%A0%20parassite%20nel%20MOSFET.md)
- [Matching e Variabilita nei Componenti Integrati](./Matching%20e%20Variabilita%20nei%20Componenti%20Integrati.md)
- [La soglia da cosa dipende](./La%20soglia%20da%20cosa%20dipende.md)
- [SOI](./SOI.md)
- [Resistore](./Resistore.md)
- [Condensatori](./Condensatori.md)
- [Elettromigrazione e tossicità dei metalli](../Tecnologia%20e%20Fabbricazione/Elettromigrazione%20e%20tossicit%C3%A0%20dei%20metalli.md)
