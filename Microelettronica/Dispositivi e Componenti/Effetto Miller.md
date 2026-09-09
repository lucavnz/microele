# Effetto Miller e Capacità di Retroazione

L'**Effetto Miller** è il fenomeno circuitale per cui un'impedenza (tipicamente una capacità parassita $C$) collegata a cavallo tra l'ingresso e l'uscita di uno stadio invertente viene vista dai singoli nodi come se fosse una **capacità riferita a massa di valore molto più grande**.

Non cambia il componente fisico: cambia la **quantità di carica** che il circuito deve iniettare per far variare la tensione, perché i due capi del condensatore si muovono in direzioni opposte.

---

### 1. Il Principio Fisico: Perché la Capacità "Appare Più Grande"?

Un condensatore fisico reale non modifica le sue armature né il suo dielettrico. La corrente e la carica scambiata dipendono unicamente dalla **differenza di potenziale ai suoi capi**:
$$i(t) = C \frac{d(V_1 - V_2)}{dt} \iff \Delta Q = C \cdot \Delta V_C$$

```text
Caso A: Condensatore a Massa            Caso B: Condensatore tra nodi in controfase
         V1                GND                   V1                V2
         o-------||--------o                     o-------||--------o
                 C                                       C
   ΔV1 = +1V          V2 = 0V              ΔV1 = +1V          ΔV2 = -1V
   ──────────────────────────              ──────────────────────────
   ΔVc = 1V - 0V = 1V                      ΔVc = (+1V) - (-1V) = 2V
   ΔQ  = C * 1V                            ΔQ  = C * 2V = (2C) * 1V
```

* **Riferito a massa (Caso A):** se sposti il nodo 1 di $+1\text{ V}$, ai capi del condensatore c'è una variazione di $1\text{ V}$. Il nodo deve erogare una carica $\Delta Q = C \cdot 1\text{ V}$.
* **A cavallo di nodi in controfase (Caso B):** se mentre alzi il nodo 1 di $+1\text{ V}$, dall'altra parte il circuito abbassa il nodo 2 di $-1\text{ V}$, il condensatore vede una caduta complessiva di **$2\text{ V}$**.
* Per muovere il nodo 1 di solo $1\text{ V}$, hai dovuto pompare **il doppio della carica**: dal punto di vista del nodo 1, il condensatore "pesa" come se fosse a massa con valore **$2C$**.

---

### 2. Il Teorema di Miller: Sdoppiamento verso Massa e Formule Universali

Invece di portarsi dietro un condensatore flottante a cavallo tra due nodi, il **Teorema di Miller** permette di eliminarlo e sostituirlo con **due capacità separate, entrambe riferite a massa**.

```text
Circuito REALE:
          Nodo 1 (Ingresso) ──────────||────────── Nodo 2 (Uscita)
                                       C

Circuito Equivalente di MILLER:
          Nodo 1 (Ingresso)                        Nodo 2 (Uscita)
                  │                                       │
                 === C_1                                 === C_2
                  │                                       │
                 GND                                     GND
```

#### Perché ci sono SEMPRE due capacità? (La regola fisica di Kirchhoff)
Un condensatore tocca **due nodi fisici**:
* Se una corrente esce dal Nodo 1, la stessa identica corrente **arriva nel Nodo 2**.
* Se tu mettessi l'equivalente a massa solo sul Nodo 1, il Nodo 2 "verrebbe imbrogliato": vedrebbe un circuito aperto e perderebbe tutta la corrente che prima il condensatore gli scaricava addosso, violando la legge di Kirchhoff!
* **Regola d'oro:** quando spezzi un componente a due terminali, **DEVI SEMPRE mettere un equivalente sul Nodo 1 E uno sul Nodo 2**.

#### Le Due Uniche Formule Universali
Definendo il rapporto di guadagno tra il secondo nodo e il primo:
$$K = \frac{\Delta V_2}{\Delta V_1} = \frac{\text{variazione di potenziale sul nodo 2}}{\text{variazione di potenziale sul nodo 1}}$$

Le due capacità equivalenti verso massa valgono **sempre ed esclusivamente**:
$$\mathbf{C_1 = C \cdot (1 - K)}$$
$$\mathbf{C_2 = C \cdot \left(1 - \frac{1}{K}\right)}$$

Queste due formule governano all'unisono **sia il mondo analogico sia quello digitale**:
* **In Analogico (Source Comune):** $K = -A_v = -50 \implies C_1 = C(1 - (-50)) = \mathbf{51C}$, mentre $C_2 = C(1 - (-1/50)) = \mathbf{1.02C}$.
* **In Digitale (Inverter CMOS):** $K = \frac{\Delta V_O}{\Delta V_I} = \frac{-V_{DD}}{+V_{DD}} = \mathbf{-1} \implies C_1 = C(1 - (-1)) = \mathbf{2C}$, e $C_2 = C(1 - (-1/(-1))) = \mathbf{2C}$. In digitale il fattore è identico e raddoppia su entrambi i lati!

---

### 3. In Analogico (Piccoli Segnali, es. Source Comune)

Nel circuito analogico lineare a piccoli segnali (come il [MOS](./MOS.md) a Source Comune):
* L'ingresso ha una piccola escursione $v_i$.
* L'uscita ha un'escursione invertita amplificata: $v_o = -A_v v_i$ con $A_v = g_m R_L'$ (es. $A_v = 50$).
* La [capacità parassita di overlap](./Capacit%C3%A0%20parassite%20nel%20MOSFET.md) $C_{gd}$ si sdoppia:
  * **All'ingresso:** $C_{in} = C_{gd}(1 - (-A_v)) = \mathbf{C_{gd}(1 + |A_v|)}$. Con $A_v = 50$, all'ingresso vedi **$51 \cdot C_{gd}$**!
  * **All'uscita:** $C_{out} = C_{gd}\left(1 - \left(-\frac{1}{A_v}\right)\right) = C_{gd}\left(1 + \frac{1}{|A_v|}\right) \approx \mathbf{C_{gd}}$.

#### L'Impatto sui Poli della Funzione di Trasferimento
* La capacità di ingresso gigante $C_{in}$ vede la resistenza interna del generatore $R_{sig}$:
  $$\tau_{in} = R_{sig} \cdot C_{in} = R_{sig} \cdot [C_{gd}(1 + |A_v|)] \implies \mathbf{\omega_{p1} = \frac{1}{\tau_{in}}}$$
  Questo genera il **polo dominante a bassa frequenza**, che abbatte drasticamente la banda passante dell'amplificatore.
* Al nodo di uscita c'è il secondo polo $\omega_{p2} \approx \frac{1}{R_L' C_{out}}$, posizionato a frequenza molto più alta.
* 👉 Per eliminare questo accoppiamento e recuperare banda si usa la configurazione a [Coppia Differenziale e Cascode Telescopico](./Coppia%20Differenziale%20e%20Cascode%20Telescopico.md), dove lo stadio Cascode disaccoppia il Drain del transistore di ingresso abbattendo il guadagno locale a circa $-1$ e annullando l'effetto Miller.

---

### 4. Il Paradosso dei Due Poli: Perché 1 Capacità Sembra Dare 2 Poli?

Se un circuito ha un'unica capacità parassita $C_{gd}$ e nessuna capacità a massa, la teoria delle reti impone che ci sia **al massimo 1 solo polo** (il denominatore di $H(s)$ può essere solo di primo grado). Perché Miller ne fa spuntare due?

> [!NOTE]
> Il Teorema di Miller classico è un'**approssimazione quasi-statica**: assume che il guadagno $A_v$ sia una costante reale fissa a tutte le frequenze ($A_{v0} = -g_m R_L'$).  
> In realtà, all'aumentare della frequenza, il guadagno reale $A_v(s)$ crolla proprio per effetto di $C_{gd}$.  
> * Il **polo dominante** $\omega_{p1}$ calcolato con $C_{in}$ è **estremamente accurato** e coincide quasi perfettamente con il vero polo del circuito.
> * Il secondo polo $\omega_{p2}$ calcolato con $C_{out}$ è un **polo fittizio** (un artefatto dell'aver assunto $A_v$ costante anche a frequenza infinita).
> Nei circuiti reali, tuttavia, ci sono sempre anche le capacità fisiche a massa $C_{gs}$ (all'ingresso) e $C_{db} + C_L$ (all'uscita), quindi il sistema fisico reale ha effettivamente due o tre poli distinti.

---

### 5. In Digitale (Grandi Segnali, Inverter CMOS)

Nelle porte logiche digitali (come l'[Inverter CMOS](../Famiglie%20Logiche/Inverter%20CMOS%20e%20Regioni%20di%20Funzionamento.md)) non siamo a piccoli segnali: le tensioni commutano su tutta la dinamica di alimentazione $V_{DD}$ (**rail-to-rail**).

Non si usano i poli di Laplace, ma il **bilancio di carica netta scambiata $\Delta Q$** per calcolare il ritardo di propagazione $t_p$.

```text
Ingresso VI:   0V ──────────> VDD   (Salto ΔVI = +VDD)
Uscita   VO:  VDD ──────────> 0V    (Salto ΔVO = -VDD)
```

#### A) Calcolo della Carica Scambiata $\Delta Q$
La capacità parassita di overlap tra gate e drain dei due MOS dell'inverter vale $C = C_{GD12} = W_1 C_{On} + W_2 C_{Op}$.
1. **Prima della commutazione ($t = 0^-$):** $V_I = 0\text{ V}$, $V_O = V_{DD} \implies V_C = 0 - V_{DD} = -V_{DD}$.
2. **A transizione completata ($t \to \infty$):** $V_I = V_{DD}$, $V_O = 0\text{ V} \implies V_C = V_{DD} - 0 = +V_{DD}$.
3. **Variazione di tensione sulle armature:** $\Delta V_C = (+V_{DD}) - (-V_{DD}) = \mathbf{2 V_{DD}}$.
$$\Delta Q = C \cdot 2 V_{DD}$$

#### B) Perché la Capacità Equivalente è $2C$?
Per ricondurre l'analisi manuale a un circuito semplice con una sola capacità di carico $C_L$ a massa sull'uscita:
* La tensione del nodo di uscita varia di $\Delta V_O = V_{DD}$.
* La capacità equivalente a massa che assorbe la stessa carica $\Delta Q$ vale:
  $$C_{out} = \frac{\Delta Q}{\Delta V_O} = \frac{2 C \cdot V_{DD}}{V_{DD}} = \mathbf{2 C}$$
* Lo stesso vale per la porta a monte che pilota l'ingresso:
  $$C_{in} = \frac{\Delta Q}{\Delta V_I} = \frac{2 C \cdot V_{DD}}{V_{DD}} = \mathbf{2 C}$$

In digitale il "guadagno a grandi segnali" vale in modulo $A = \left|\frac{\Delta V_O}{\Delta V_I}\right| = \frac{V_{DD}}{V_{DD}} = 1$.  
Di conseguenza la formula di Miller diventa simmetrica: $1 + |A| = 1 + 1 = \mathbf{2}$.

---

### 6. Analisi Dinamica della Commutazione: 50% vs 90%

```text
  VO [V]
   6 |    /\  <- Capacitive feedthrough (spike iniziale oltre VDD)
   5 |---/  \
   4 |       \  Curva reale (con C tra IN e OUT)
   3 |        \
 2.5 |---------\----------- <- 50% di VDD: interseca CL = 2C (tpHL)
   2 |          \
   1 |           \
 0.5 |------------\-------- <- 90% di scarica: interseca CL = 1.5C
   0 |_____________\_____ t
```

1. **Capacitive Feedthrough (Spike oltre $V_{DD}$):**  
   Quando $V_I$ compie il gradino da $0$ a $V_{DD}$, i transistor non hanno ancora scaricato il nodo di uscita: il salto rapido di $V_I$ si accoppia direttamente su $V_O$ tramite $C_{GD}$, spingendo istantaneamente l'uscita **al di sopra di $V_{DD}$** (fino a oltre $6\text{ V}$).
2. **Al 50% della Transizione ($V_O = V_{DD}/2$):**  
   A causa della carica extra introdotta dallo spike iniziale e della forte controfase iniziale, la curva reale impiega esattamente lo stesso tempo della curva con carico a massa:
   $$\mathbf{V_O(t)\big|_{50\%} \implies C_L \approx 2C}$$
3. **Al 90% della Scarica ($V_O \approx 0.1 V_{DD}$):**  
   Verso la fine del transitorio, l'ingresso è fermo a $V_{DD}$ da tempo ($dV_I/dt = 0$). Il gate è diventato una massa dinamica: il condensatore $C$ si comporta come una capacità verso tensione fissa, pesando solo **$1 \cdot C$**. Mediando l'intero transitorio si ottiene:
   $$V_O(t)\big|_{90\%} \implies C_L \approx 1.5C$$
4. **Regola di Progetto:**  
   Poiché il ritardo di propagazione $t_{pHL}$ è convenzionalmente misurato al **50% dell'escursione**, nei calcoli del ritardo si adotta rigorosamente il fattore **2**:
   $$\mathbf{\Delta C_L \approx 2 \, C_{GD12} = 2 (W_1 + W_2) C_{GDO}}$$

---

### 7. Sintesi Comparativa

| Parametro | In Elettronica Analogica | In Elettronica Digitale (CMOS) |
| :--- | :--- | :--- |
| **Regime** | Piccoli segnali sinusoidali lineari | Grandi segnali non lineari ($0 \leftrightarrow V_{DD}$) |
| **Obiettivo** | Trovare banda passante e poli in frequenza | Trovare il tempo di propagazione $t_p$ |
| **Guadagno $A$** | $A_v = -g_m R_L'$ (elevato, es. $30-100$) | $A = \left\|\frac{\Delta V_O}{\Delta V_I}\right\| = 1$ (escursioni uguali) |
| **Capacità all'Ingresso** | $C_{in} = C(1 + \|A_v\|) \gg C$ | $C_{in} = 2C$ |
| **Capacità all'Uscita** | $C_{out} \approx C$ | $C_{out} = 2C$ (misurato al $50\%$) |
| **Effetto Principale** | Crea il polo dominante $\omega_{p1}$ a bassa frequenza | Raddoppia il carico capacitivo di scarica su $C_L$ |

---

*Pagine correlate:*
- [Capacità parassite nel MOSFET](./Capacit%C3%A0%20parassite%20nel%20MOSFET.md)
- [Coppia Differenziale e Cascode Telescopico](./Coppia%20Differenziale%20e%20Cascode%20Telescopico.md)
- [Inverter CMOS e Regioni di Funzionamento](../Famiglie%20Logiche/Inverter%20CMOS%20e%20Regioni%20di%20Funzionamento.md)
- [Potenza Dinamica e Dissipazione di Carica](../Famiglie%20Logiche/Potenza%20Dinamica%20e%20Dissipazione%20di%20Carica.md)
- [Retroazione nell'Inverter e Ring Oscillator](../Famiglie%20Logiche/Retroazione%20nell'Inverter%20e%20Ring%20Oscillator.md)
- [MOS](./MOS.md)
- [Condensatori](./Condensatori.md)
- [RTL e Prodotto Ritardo-Consumo (PDP)](../Famiglie%20Logiche/RTL%20e%20Prodotto%20Ritardo-Consumo%20(PDP).md)
