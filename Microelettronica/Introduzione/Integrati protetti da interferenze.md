# Perché i Circuiti Integrati sono Protetti dalle Interferenze Elettromagnetiche?

Non è la plastica nera dell'involucro a schermare i chip (la plastica è un isolante trasparente alle onde radio), ma la loro **geometria microscopica**.

---

### 1. La regola dell'antenna e la lunghezza d'onda ($\lambda$)
Perché un circuito faccia da antenna — cioè capti onde elettromagnetiche e "ciucci" potenza dall'ambiente — le dimensioni fisiche del conduttore devono essere **confrontabili con la lunghezza d'onda** ($\lambda = \frac{c}{f}$):
* Se le piste sono lunghe diversi centimetri (come sulle schede PCB verdi), risuonano perfettamente con i disturbi ambientali come Wi-Fi ($2.4\text{ GHz} \implies \lambda \approx 12.5\text{ cm}$) o reti cellulari.
* Nei circuiti integrati i conduttori sono microscopici (da pochi $\mu\text{m}$ a massimo $1\text{ mm}$): le dimensioni minuscole agiscono da "filtro spaziale" naturale su una grandissima banda di frequenze, rendendo il chip **praticamente invisibile** alle onde radio ($P_{captata} \propto (L/\lambda)^2 \to 0$).

---

### 2. Come il circuito capta Campo Elettrico ($\vec{E}$) vs Campo Magnetico ($\vec{B}$)

Un circuito capta le due componenti dell'onda elettromagnetica in modo diverso:

#### A. Il Campo Elettrico ($\vec{E}$) sente la LUNGHEZZA del filo ($L$)
Il campo elettrico agisce lungo la direzione del conduttore spingendo gli elettroni e creando una differenza di potenziale:
$$V_{disturbo} \approx E \cdot L$$
Poiché dentro il silicio le lunghezze $L$ sono minuscole, la porzione d'onda convertita in tensione di disturbo nel circuito è praticamente trascurabile.

#### B. Il Campo Magnetico ($\vec{B}$) sente l'AREA della spira ($A$)
Il segnale e il suo ritorno di massa formano una spira chiusa. Le linee di campo magnetico che entrano nell'area racchiusa inducono una forza elettromotrice per la legge di Faraday-Neumann:
$$V_{disturbo} = - A \cdot \frac{dB}{dt} = - (L \cdot d) \cdot \frac{dB}{dt}$$
*(dove $d$ è la distanza tra la pista di segnale e il piano di massa)*.

Nel microchip i fili viaggiano a distanze sub-micrometriche ($d < 1\,\mu\text{m}$) dalla massa: l'area $A$ racchiusa è nell'ordine dei $\mu\text{m}^2$ (milioni di volte più piccola rispetto a una scheda PCB), azzerando la tensione indotta.

---

### In sintesi:
* **Il campo elettrico** sente la **lunghezza** del filo ($L \to 0 \implies V_{disturbo} \to 0$).
* **Il campo magnetico** sente l'**area** della spira ($A \to 0 \implies V_{disturbo} \to 0$).

---

*Pagine correlate:*
- [Difficoltà nel fare un componente ideale](../Tecnologie/Difficolt%C3%A0%20nel%20fare%20un%20componente%20ideale.md)
- [Analogico non si scende di dimensioni](./Analogico%20non%20si%20scende%20di%20dimensioni.md)
