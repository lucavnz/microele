# Crollo della Resistenza di Uscita ($r_o$) e Guadagno Intrinseco

### Cos'è il Guadagno Intrinseco $A_0$?
Il **guadagno intrinseco** $A_0$ rappresenta il limite superiore teorico del guadagno di tensione che un singolo transistor può fornire al mondo circostante.

Si calcola considerando uno stadio amplificatore elementare a **Source comune** polarizzato con un generatore di corrente ideale come carico ($R_L = \infty$):
$$A_v = -g_m \cdot (r_o \parallel R_L) \xrightarrow{R_L = \infty} A_0 = -g_m \cdot r_o$$

---

### Perché $r_o \approx \frac{1}{\lambda I_D}$?

Nel modello a piccoli segnali, la resistenza dinamica di uscita $r_o$ (o $r_{ds}$) è definita come **l'inverso della pendenza della caratteristica $I_D(V_{DS})$** a $V_{GS}$ costante quando il MOS è in saturazione:
$$r_o \triangleq \left( \left. \frac{\partial I_D}{\partial V_{DS}} \right|_{V_{GS}} \right)^{-1} = \frac{1}{g_{ds}}$$

* **Senza modulazione (caso ideale):** in saturazione la corrente non dipenderebbe da $V_{DS}$, la pendenza sarebbe zero e $r_o = \infty$ (generatore di corrente ideale).
* **Con la Modulazione di Canale (CLM):** quando $V_{DS} \ge V_{DS,\text{sat}}$, il canale si strozza (*pinch-off*) e all'aumentare di $V_{DS}$ la zona di svuotamento al Drain si allarga, arretrando il punto di strozzamento di $\Delta L$. La lunghezza effettiva diventa $L_{\text{eff}} = L - \Delta L$.
  Poiché la corrente è inversamente proporzionale alla lunghezza del canale:
  $$I_D \propto \frac{1}{L - \Delta L} = \frac{1}{L \left(1 - \frac{\Delta L}{L}\right)} \approx I_{D0} \left(1 + \frac{\Delta L}{L}\right)$$
  Modellando $\frac{\Delta L}{L} \approx \lambda V_{DS}$, si ottiene la classica espressione di saturazione reale:
  $$I_D = I_{D0} \cdot (1 + \lambda V_{DS})$$

#### Derivata e passaggio a $I_D$
Calcolando la conduttanza differenziale di canale:
$$g_{ds} = \frac{\partial I_D}{\partial V_{DS}} = \lambda I_{D0} \implies r_o = \frac{1}{\lambda I_{D0}}$$

Poiché l'effetto della modulazione di canale produce una variazione modesta ($\lambda V_{DS} \ll 1$), in saturazione la corrente reale vale $I_D \approx I_{D0}$. Di conseguenza si approssima:
$$\mathbf{r_o \approx \frac{1}{\lambda I_D}}$$

#### Interpretazione geometrica (Tensione di Early $V_A$)
Estrapolando all'indietro le rette della caratteristica $I_D - V_{DS}$ in saturazione, esse convergono tutte sull'asse delle tensioni negative nel punto $-V_A = -1/\lambda$:
$$r_o = \frac{V_A + V_{DS}}{I_D} \approx \frac{V_A}{I_D} = \frac{1}{\lambda I_D}$$

---

### Perché rimpicciolire $L$ distrugge $r_o$ e $A_0$?

Il parametro $\lambda$ descrive la quota di canale "mangiata" dalla strozzatura rispetto alla lunghezza totale:
$$\lambda \propto \frac{\Delta L}{L} \propto \frac{1}{L} \implies r_o \propto \frac{L}{I_D}$$

Sostituendo nel guadagno intrinseco:
$$A_0 = g_m \cdot r_o \propto L$$

* **Canale lungo (es. $0.35\,\mu\text{m}$ o $0.18\,\mu\text{m}$):** $\lambda$ è piccolissimo, $r_o$ è alta e un singolo transistor fornisce un guadagno di **$50 - 100$** ($34 - 40\,\text{dB}$).
* **Canale nanometrico (es. $40\,\text{nm}$):** $\lambda$ è enorme per via degli effetti di canale corto e del DIBL. $r_o$ crolla a valori bassissimi e il guadagno scende a **$5 - 10$** ($14 - 20\,\text{dB}$)!

---

### Impatto sulla progettazione analogica:
Per ottenere amplificatori ad alto guadagno (es. operazionali con $A_{v0} \ge 80\,\text{dB}$):
* Nelle vecchie tecnologie bastavano uno o due stadi semplici o una struttura cascode: [Coppia Differenziale e Cascode Telescopico](../Dispositivi%20e%20Componenti/Coppia%20Differenziale%20e%20Cascode%20Telescopico.md).
* Nelle tecnologie nanometriche avanzate siamo costretti a progettare **amplificatori complessi multistadio** (3 o più stadi), che introducono poli multipli, rendendo molto difficile la stabilizzazione ad anello chiuso e la compensazione in frequenza.

---
*Pagine correlate:*
- [Analogico non si scende di dimensioni](../Scaling%20e%20Limiti%20Fisici/Analogico%20non%20si%20scende%20di%20dimensioni.md)
- [Coppia Differenziale e Cascode Telescopico](../Dispositivi%20e%20Componenti/Coppia%20Differenziale%20e%20Cascode%20Telescopico.md)
- [DIBL](./DIBL.md)
- [Saturazione di velocita](./Saturazione%20di%20velocita.md)
- [Inverter CMOS e Regioni di Funzionamento](../Famiglie%20Logiche/Inverter%20CMOS%20e%20Regioni%20di%20Funzionamento.md)
