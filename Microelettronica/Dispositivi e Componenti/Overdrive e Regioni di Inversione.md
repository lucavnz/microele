# Overdrive $V_{ov}$, Tensione di Saturazione $V_{dsat}$ e Regioni di Inversione

L'**overdrive** ($V_{ov} = V_{GS} - V_{th}$) quantifica quanto stiamo spingendo il gate sopra la soglia per accendere il canale. Tuttavia, la classica uguaglianza $V_{dsat} = V_{GS} - V_{th}$ e la formula $g_m = \frac{2I_D}{V_{ov}}$ sono approssimazioni che valgono solo in determinate condizioni fisiche.

---

### 1. $V_{dsat} = V_{GS} - V_{th}$ è un'approssimazione?

**Sì, è un'approssimazione** valida rigorosamente solo nel modello a canale lungo in **forte inversione**.

La tensione minima di drain necessaria a mandare il transistor in saturazione ($V_{dsat}$) dipende dal regime fisico di trasporto:

#### A) Forte Inversione (Drift / Deriva dominante)
* **Condizione:** $V_{GS} \gg V_{th}$.
* La densità di carica mobile nel canale è abbondante: $Q_I(x) \approx -C_{ox}(V_{GS} - V_{th} - V(x))$.
* Il trasporto è dominato dal campo elettrico (**drift**).
* La saturazione avviene per **pinch-off** (strozzamento geometrico della carica al drain, $Q_I(L) = 0$).
* **Risultato:** $V_{dsat} = V_{GS} - V_{th} = V_{ov}$.
*(Nei canali corti subentra prima la [saturazione di velocità](../Effetti%20di%20Canale%20Corto/Saturazione%20di%20velocita.md), per cui $V_{dsat} < V_{ov}$)*.

#### B) Debole Inversione / Sottosoglia (Diffusione dominante)
* **Condizione:** $V_{GS} < V_{th}$ (vedi [Conduzione di Sottosoglia e Rapporto Ion/Ioff](../Effetti%20di%20Canale%20Corto/Rapporto%20Ion%20Ioff%20e%20sottosoglia.md)).
* La densità di portatori è minima: il trasporto avviene per **diffusione** (come nei [BJT](./BJT.md)).
* La corrente vale:
  $$I_D \propto \exp\left(\frac{V_{GS}-V_{th}}{n V_T}\right) \left( 1 - \exp\left(-\frac{V_{DS}}{V_T}\right) \right)$$
  dove $V_T = \frac{k_B T}{q} \approx 26\,\text{mV}$ e $n \approx 1.2 \div 1.5$.
* Per saturare la corrente basta annullare il termine esponenziale di ritorno dal drain: è sufficiente che $V_{DS} \ge 3 \div 4 V_T \approx 75 \div 100\,\text{mV}$.
* **Risultato:** In debole inversione $V_{dsat} \approx 3\div 4 V_T \approx 100\,\text{mV}$, ed è **completamente indipendente dall'overdrive $V_{GS} - V_{th}$**.

#### C) Moderata Inversione (Regione di transizione)
* **Condizione:** $V_{GS} \approx V_{th}$.
* Il trasporto è un mix continuo di diffusione e deriva.
* Non valgono né il modello esponenziale puro né quello quadratico: $V_{dsat}$ transita gradualmente da $\approx 3 V_T$ a $V_{ov}$. Dire che $V_{dsat} = V_{ov}$ è una sovrastima grossolana.

---

### 2. A Corrente Fissata ($I_D$), cosa decide l'Overdrive $V_{ov}$?

Se imponiamo una corrente di polarizzazione $I_D$ (es. tramite uno specchio di corrente o un generatore di bias), il transistor non "sceglie" da solo il suo overdrive: **è il progettista a determinarlo attraverso le dimensioni geometriche $W/L$** e i parametri tecnologici del processo ($\mu C_{ox}$).

In forte inversione:
$$I_D = \frac{1}{2} \mu C_{ox} \left(\frac{W}{L}\right) V_{ov}^2 \implies V_{ov} = \sqrt{\frac{2 I_D}{\mu C_{ox} \left(\frac{W}{L}\right)}}$$

#### Intuizione fisica:
$V_{ov}$ misura **quanta densità di carica superficiale** dobbiamo accumulare nel canale per permettere il transito della corrente $I_D$:

1. **Se scegliamo $W/L$ molto grande (transistor largo):**
   * Il canale offre una sezione enorme al passaggio dei portatori.
   * Serve pochissima carica per unità di superficie per far scorrere $I_D$.
   * Il transistor si polarizza con un **$V_{ov}$ piccolissimo**, spostandosi verso la moderata o debole inversione.
2. **Se scegliamo $W/L$ piccolo (transistor stretto o lungo):**
   * Il canale è un collo di bottiglia.
   * Per far passare la stessa corrente $I_D$, serve un forte campo di gate e un'alta densità di portatori.
   * Il circuito impone un **$V_{ov}$ elevato** (forte inversione profonda).

---

### 3. La Transconduttanza $g_m$ e il Trade-off $g_m / I_D$

La transconduttanza $g_m = \frac{\partial I_D}{\partial V_{GS}}$ rappresenta il guadagno del transistor (conversione tensione-corrente):
* In forte inversione: $g_m = \frac{2 I_D}{V_{ov}} = \sqrt{2 \mu C_{ox} \frac{W}{L} I_D}$.
* In debole inversione: $g_m = \frac{I_D}{n V_T}$ (massima efficienza, indipendente da $W/L$).

L'indice di merito **$g_m / I_D$** (efficienza di transconduttanza) guida il dimensionamento in analogico:

| Parametro | $V_{ov}$ Piccolo (Grande $W/L$ - Moderata/Debole Inv.) | $V_{ov}$ Grande (Piccolo $W/L$ - Forte Inv.) |
| :--- | :--- | :--- |
| **Efficienza $\frac{g_m}{I_D}$** | **Massima** ($\approx \frac{1}{n V_T} \approx 25\,\text{V}^{-1}$) $\rightarrow$ Massimo guadagno a parità di corrente | **Bassa** ($= \frac{2}{V_{ov}} \approx 5 \div 10\,\text{V}^{-1}$) |
| **Velocità / Banda ($f_T$)** | Minore (capacità parassite [Cgg](./Capacit%C3%A0%20parassite%20nel%20MOSFET.md) elevate per via dell'ampio $W$) | **Molto elevata** ($f_T \propto \frac{V_{ov}}{L^2}$) |
| **Tensione $V_{dsat}$** | Piccola ($\approx 80 \div 150\,\text{mV}$) $\rightarrow$ Massimo **voltage headroom** (dinamica di segnale) | Grande ($\ge 200 \div 400\,\text{mV}$) $\rightarrow$ Minore dinamica di uscita |
| **Matching di Corrente** | Peggiore a parità di $\Delta V_{th}$ ($\frac{\Delta I_D}{I_D} = \frac{2\Delta V_{th}}{V_{ov}}$) | Migliore mismatch relativo di corrente (perché $V_{ov}$ è alto al denominatore) |

👉 Approfondimento sulla variabilità: [Matching e Variabilità nei Componenti Integrati](./Matching%20e%20Variabilita%20nei%20Componenti%20Integrati.md)

---

*Pagine correlate:*
- [La soglia da cosa dipende](./La%20soglia%20da%20cosa%20dipende.md)
- [MOS](./MOS.md)
- [Conduzione di Sottosoglia e Rapporto Ion/Ioff](../Effetti%20di%20Canale%20Corto/Rapporto%20Ion%20Ioff%20e%20sottosoglia.md)
- [Saturazione di velocità](../Effetti%20di%20Canale%20Corto/Saturazione%20di%20velocita.md)
- [Matching e Variabilita nei Componenti Integrati](./Matching%20e%20Variabilita%20nei%20Componenti%20Integrati.md)
- [Capacità parassite nel MOSFET](./Capacit%C3%A0%20parassite%20nel%20MOSFET.md)
- [Layout e Tecniche di Progettazione dei MOS](./Layout%20e%20Tecniche%20di%20Progettazione%20dei%20MOS.md)
- [Analogico non si scende di dimensioni](../Scaling%20e%20Limiti%20Fisici/Analogico%20non%20si%20scende%20di%20dimensioni.md)
- [BJT](./BJT.md)
