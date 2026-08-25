# Crollo della Resistenza di Uscita ($r_o$) e Guadagno Intrinseco

### Cos'è il Guadagno Intrinseco $A_0$?
Il **guadagno intrinseco** $A_0$ rappresenta il limite superiore teorico del guadagno di tensione che un singolo transistor può fornire al mondo circostante.

Si calcola considerando uno stadio amplificatore elementare a **Source comune** polarizzato con un generatore di corrente ideale come carico ($R_L = \infty$):
$$A_v = -g_m \cdot (r_o \parallel R_L) \xrightarrow{R_L = \infty} A_0 = -g_m \cdot r_o$$

---

### Perché $r_o \approx \frac{1}{\lambda I_D}$?

A causa della modulazione della lunghezza di canale (CLM), la corrente reale in saturazione sale leggermente con $V_{DS}$:
$$I_D = I_{D0} \cdot (1 + \lambda V_{DS})$$

La resistenza dinamica di uscita $r_o$ è l'inverso della pendenza della caratteristica $I_D - V_{DS}$:
$$r_o = \left( \frac{\partial I_D}{\partial V_{DS}} \right)^{-1} = \frac{1}{\lambda I_{D0}} \approx \frac{1}{\lambda I_D}$$

---

### Perché rimpicciolire $L$ distrugge $r_o$ e $A_0$?

Il parametro $\lambda$ è inversamente proporzionale alla lunghezza del canale:
$$\lambda \propto \frac{1}{L} \implies r_o \propto L$$

Sostituendo nel guadagno intrinseco:
$$A_0 = g_m \cdot r_o \propto L$$

* **Canale lungo (es. $0.35\,\mu\text{m}$ o $0.18\,\mu\text{m}$):** $\lambda$ è piccolissimo, $r_o$ è alta e un singolo transistor fornisce un guadagno di **$50 - 100$** ($34 - 40\,\text{dB}$).
* **Canale nanometrico (es. $40\,\text{nm}$):** $\lambda$ è enorme per via degli effetti di canale corto e del DIBL. $r_o$ crolla a valori bassissimi e il guadagno scende a **$5 - 10$** ($14 - 20\,\text{dB}$)!

---

### Impatto sulla progettazione analogica:
Per ottenere amplificatori ad alto guadagno (es. operazionali con $A_{v0} \ge 80\,\text{dB}$):
* Nelle vecchie tecnologie bastavano uno o due stadi semplici o una struttura cascode.
* Nelle tecnologie nanometriche avanzate siamo costretti a progettare **amplificatori complessi multistadio** (3 o più stadi), che introducono poli multipli, rendendo molto difficile la stabilizzazione ad anello chiuso e la compensazione in frequenza.

---
*Pagine correlate:*
- [Analogico non si scende di dimensioni](../Analogico%20non%20si%20scende%20di%20dimensioni.md)
- [DIBL](./DIBL.md)
- [Saturazione di velocita](./Saturazione%20di%20velocita.md)
