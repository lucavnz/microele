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
* Nelle vecchie tecnologie bastavano uno o due stadi semplici o una struttura cascode: [Coppia Differenziale e Cascode Telescopico](../Dispositivi%20e%20Componenti/Coppia%20Differenziale%20e%20Cascode%20Telescopico.md), eventualmente evoluta in [Folded Cascode e Recycling](../Dispositivi%20e%20Componenti/Folded%20Cascode%20e%20Recycling.md) o potenziata tramite [Gain Boosting (Regulated Cascode)](../Dispositivi%20e%20Componenti/Gain%20Boosting.md) per ripristinare $R_{out}$ elevatissime senza perdere swing.
* Nelle tecnologie nanometriche avanzate siamo altrimenti costretti a progettare **amplificatori complessi multistadio** (3 o più stadi), che introducono poli multipli, rendendo molto difficile la stabilizzazione ad anello chiuso e la compensazione in frequenza.

---

### 4. L'Espressione Completa della Conduttanza di Uscita $g_{ds}$ (Canale Corto)

Nel modello semplificato del primo ordine si assume che $g_{ds} = \lambda I_D$.  
Nella realtà di un canale corto avanzato, la corrente $I_D$ risente di $V_{DS}$ attraverso **quattro meccanismi fisici simultanei**:
1. L'accorciamento geometrico del canale $\Delta L$ (**CLM**).
2. L'abbassamento della soglia indotto dal drain (**DIBL**, $V_{Th}(V_{DS})$).
3. La degradazione della mobilità con il campo elettrico laterale (**saturazione di velocità**, $\mu(V_{DS})$).
4. La corrente secondaria di ionizzazione per impatto (**valanga**, $I_S(V_{DS})$).

Differenziando totalmente la corrente di Drain rispetto a $V_{DS}$, si ottiene l'**espressione accurata della conduttanza di uscita**:

$$g_{ds} = \frac{\partial I_D}{\partial V_{DS}} = \mathbf{\lambda I_D} \;-\; \mathbf{g_m \frac{\partial V_{Th}}{\partial V_{DS}}} \;+\; \mathbf{\frac{I_D}{\mu} \frac{\partial \mu}{\partial V_{DS}}} \;+\; \mathbf{\frac{\partial I_S}{\partial V_{DS}}}$$

Analisi dettagliata dei quattro contributi:

| Termine | Meccanismo Fisico | Segno ed Effetto su $g_{ds}$ e $r_o$ |
| :--- | :--- | :--- |
| **$\lambda I_D$** | **Modulazione di Canale (CLM - 1° ordine):** pendenza classica dovuta all'arretramento del pinch-off $\Delta L$. | Termine base di saturazione ($r_o \approx \frac{1}{\lambda I_D}$). |
| **$- g_m \frac{\partial V_{Th}}{\partial V_{DS}}$** | **Effetto DIBL (Canale Corto):** poiché per DIBL la soglia cala con $V_{DS}$ ($\frac{\partial V_{Th}}{\partial V_{DS}} < 0$), con il segno meno davanti questo termine diventa **POSITIVO**. | **Distrugge $r_o$**: all'aumentare di $V_{DS}$ il canale conduce di più perché si abbassa la soglia, aumentando vistosamente la pendenza della curva! |
| **$+ \frac{I_D}{\mu} \frac{\partial \mu}{\partial V_{DS}}$** | **Saturazione di Velocità:** modula la mobilità efficace con il campo medio orizzontale $V_{DS}/L$. | Riduce la transconduttanza efficace e altera la pendenza dinamica. |
| **$+ \frac{\partial I_S}{\partial V_{DS}}$** | **Moltiplicazione a Valanga (Avalanching):** generazione di coppie elettrone-lacuna per ionizzazione per impatto nella zona svuotata al Drain. | Fa impennare drasticamente $g_{ds}$ verso l'alto a tensioni $V_{DS}$ elevate (fino al breakdown). |

---

### 5. Effetti di Secondo Ordine su $\Delta L$ (Modello Bidimensionale 2D)

Nel modello monodimensionale si assume che l'accorciamento $\Delta L$ dipenda solo dalla caduta di tensione orizzontale $(V_{DS} - V_{sat})$.  
Nella realtà, la vicinanza dell'elettrodo di Gate genera un campo elettrico di bordo (*fringing field*) che interagisce con la giunzione di Drain in modo bidimensionale. Un'analisi accurata fornisce:

$$\frac{1}{\Delta L} \cong \frac{1}{\Delta L_{\text{(1st order)}}} + \frac{C_{ox}}{\varepsilon_S} \left[ \frac{\alpha(V_{DS} - V_{GS}) + \beta(V_{GS} - V_{sat})}{V_{DS} - V_{sat}} \right]$$

* La contrazione del canale non è decisa solo dal Drain, ma è **modulata attivamente dal potenziale del Gate ($V_{GS}$)** attraverso la capacità di ossido $C_{ox}$.

---

*Pagine correlate:*
- [Gain Boosting (Regulated Cascode)](../Dispositivi%20e%20Componenti/Gain%20Boosting.md)
- [Folded Cascode e Recycling](../Dispositivi%20e%20Componenti/Folded%20Cascode%20e%20Recycling.md)
- [Coppia Differenziale e Cascode Telescopico](../Dispositivi%20e%20Componenti/Coppia%20Differenziale%20e%20Cascode%20Telescopico.md)
- [DIBL](./DIBL.md)
- [Saturazione di velocita](./Saturazione%20di%20velocita.md)
- [Portatori Caldi (Hot Carriers)](./Hot%20carriers.md)
- [Rumore nel MOSFET](../Dispositivi%20e%20Componenti/Rumore%20nel%20MOSFET.md)
- [Overdrive e Regioni di Inversione](../Dispositivi%20e%20Componenti/Overdrive%20e%20Regioni%20di%20Inversione.md)
- [Analogico non si scende di dimensioni](../Scaling%20e%20Limiti%20Fisici/Analogico%20non%20si%20scende%20di%20dimensioni.md)
- [Inverter CMOS e Regioni di Funzionamento](../Famiglie%20Logiche/Inverter%20CMOS%20e%20Regioni%20di%20Funzionamento.md)
