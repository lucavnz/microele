In analogico **non si può scalare troppo di dimensioni**, perché rimpicciolire i transistor distrugge le prestazioni dei circuiti. I problemi principali sono:

---

### 1. Il Mismatch e la Legge di Pelgrom
In analogico è fondamentale creare coppie di transistor identici (per specchi di corrente e coppie differenziali). 
La **Legge di Pelgrom** dice che la deviazione standard della differenza di tensione di soglia $\Delta V_{th}$ tra due transistor adiacenti è inversamente proporzionale alla radice dell'area:

$$\sigma(\Delta V_{th}) = \frac{A_{Vth}}{\sqrt{W \cdot L}}$$

> Più scendiamo con l'area ($W \cdot L$), più i transistor diventano asimmetrici per le fluttuazioni microscopiche di processo $\implies$ **offset gigante e forte sbilanciamento**.

---

### 2. Il Guadagno Intrinseco e il crollo di $r_o$
Il **guadagno intrinseco** $A_0$ è il massimo guadagno di tensione teorico ottenibile da un singolo transistor (configurato a Source comune con carico ideale $R_L = \infty$):
$$A_0 = g_m \cdot r_o$$

Dato che la resistenza di uscita vale $r_o \approx \frac{1}{\lambda I_D}$ e il coefficiente di modulazione di canale è $\lambda \propto \frac{1}{L}$, abbiamo che:
$$A_0 \propto L$$

Se usiamo transistor corti ($L$ piccolo), $r_o$ crolla miseramente. Se vogliamo avere un guadagno elevato in analogico siamo costretti a ricorrere a **complessi circuiti multistadio**, che complicano la stabilità e la compensazione in frequenza!

👉 Approfondimento: [Crollo di ro](../Effetti%20di%20Canale%20Corto/Crollo%20di%20ro.md)

---

### 3. Gli Effetti di Canale Corto (SCE)
Quando $L$ scende a livelli nanometrici, il Drain e il Source interferiscono pesantemente con il controllo del Gate sul canale:

* **[DIBL (Drain-Induced Barrier Lowering)](../Effetti%20di%20Canale%20Corto/DIBL.md):** la soglia diventa $V_{th}(V_{DS}) = V_{th0} - \eta V_{DS}$. Se la tensione sul Drain oscilla con il segnale analogico, oscilla anche la $V_{th}$, introducendo **forte distorsione non lineare** (fondamentale da evitare in analogico dove dobbiamo seguire fedelmente il segnale).
* **[Saturazione di Velocità](../Effetti%20di%20Canale%20Corto/Saturazione%20di%20velocita.md):** gli elettroni raggiungono la velocità limite $v_{sat}$, muore il modello quadratico e la transconduttanza $g_m$ non cresce più aumentando la corrente.
* **[$V_{th}$ Roll-Off](../Effetti%20di%20Canale%20Corto/Vth%20roll%20off.md):** le sacche di svuotamento delle giunzioni riducono la soglia nominale al calare di $L$.
* **[Hot Carriers (HCI)](../Effetti%20di%20Canale%20Corto/Hot%20carriers.md):** elettroni ad altissima energia che danneggiano l'ossido, creando deriva temporale di $V_{th}$ (invecchiamento) e peggiorando il rumore.
* **[Rapporto Ion/Ioff e Sottosoglia](../Effetti%20di%20Canale%20Corto/Rapporto%20Ion%20Ioff%20e%20sottosoglia.md):** la corrente di perdita da spento esplode, scaricando i nodi capacitivi nei circuiti di campionamento (*Sample & Hold*).

---

### 4. Rumore Flicker $1/f$
Nei transistor piccoli il rumore $1/f$ esplode con $1/(W \cdot L)$, soffocando i piccoli segnali analogici.

👉 Approfondimento: [1_f non va a braccetto con lo scaling](./1_f%20non%20va%20a%20braccetto%20con%20lo%20scaling.md)

---

### 5. Il Contrasto con il Digitale
Mentre l'analogico soffre drammaticamente la riduzione delle dimensioni per perdita di linearità e guadagno intrinseco, il **digitale trae il massimo beneficio dallo scaling**:
* Le non linearità estreme e l'alto guadagno differenziale sono sfruttati positivamente per creare porte logiche bistabili e rigenerative ([Caratteristica di Trasferimento e Rigenerazione](../Famiglie%20Logiche/Caratteristica%20di%20Trasferimento%20e%20Rigenerazione.md)).
* La riduzione d'area abbatte le capacità parassite, aumentando la velocità e riducendo il costo per porta ([Famiglia Logica e Costo per Bit](../Famiglie%20Logiche/Famiglia%20Logica%20e%20Costo%20per%20Bit.md)).

---

*Pagine correlate:*
- [Matching e Variabilita nei Componenti Integrati](../Dispositivi%20e%20Componenti/Matching%20e%20Variabilita%20nei%20Componenti%20Integrati.md)
- [Resistore](../Dispositivi%20e%20Componenti/Resistore.md)
- [Condensatori](../Dispositivi%20e%20Componenti/Condensatori.md)
- [Famiglia Logica e Costo per Bit](../Famiglie%20Logiche/Famiglia%20Logica%20e%20Costo%20per%20Bit.md)
- [Caratteristica di Trasferimento e Rigenerazione](../Famiglie%20Logiche/Caratteristica%20di%20Trasferimento%20e%20Rigenerazione.md)
- [Soglia Logica e Margine di Rumore](../Famiglie%20Logiche/Soglia%20Logica%20e%20Margine%20di%20Rumore.md)
- [La soglia da cosa dipende](../Dispositivi%20e%20Componenti/La%20soglia%20da%20cosa%20dipende.md)
- [BJT](../Dispositivi%20e%20Componenti/BJT.md)
- [Diodo](../Dispositivi%20e%20Componenti/Diodo.md)
- [MOS](../Dispositivi%20e%20Componenti/MOS.md)
- [Difficoltà nel fare un componente ideale](./Difficolt%C3%A0%20nel%20fare%20un%20componente%20ideale.md)
- [Crollo di ro](../Effetti%20di%20Canale%20Corto/Crollo%20di%20ro.md)
- [DIBL](../Effetti%20di%20Canale%20Corto/DIBL.md)
- [Rapporto Ion Ioff e sottosoglia](../Effetti%20di%20Canale%20Corto/Rapporto%20Ion%20Ioff%20e%20sottosoglia.md)