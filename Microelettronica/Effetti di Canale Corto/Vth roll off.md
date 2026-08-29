# $V_{th}$ Roll-Off

### Cos'è il $V_{th}$ Roll-Off?
Il **$V_{th}$ Roll-Off** è la riduzione deterministica del valore nominale della tensione di soglia $V_{th}$ che si verifica quando si accorcia la lunghezza di canale $L$ del MOSFET.

---

### Meccanismo Fisico: Il modello di *Charge Sharing* (Modello a trapezio di Yau)

Nella teoria a canale lungo (1D), si assume che tutta la carica della zona di svuotamento sotto il Gate ($Q_{dep}$) debba essere sostenuta dal campo elettrico generato dalla tensione di Gate.

Quando $L$ diventa molto corta (2D):
1. Le giunzioni PN di Source e Drain creano attorno a sé delle regioni di svuotamento (*depletion regions*) che si allargano lateralmente nel canale.
2. Queste regioni laterali supportano già una frazione significativa della carica di svuotamento totale sotto il Gate.
3. Il Gate deve quindi fornire **meno carica superficiale** per raggiungere la condizione di forte inversione.

$$\Delta Q_{gate} < Q_{dep,1D} \implies V_{th} \text{ crolla al diminuire di } L$$

---

### Differenza fondamentale: $V_{th}$ Roll-Off vs Legge di Pelgrom

È fondamentale non confondere questi due concetti:

| Caratteristica | $V_{th}$ Roll-Off | Legge di Pelgrom (Mismatch) |
| :--- | :--- | :--- |
| **Natura** | **Deterministica** (Fisica del dispositivo) | **Statistica** (Dispersione / Variabilità) |
| **Cosa descrive** | Come cambia il valore *medio/nominale* di $V_{th}$ al variare di $L$ | Quanto differiscono tra loro due transistor vicini nominalmente identici |
| **Formula** | $V_{th}(L) = V_{th0} - \Delta V_{th,SCE}(L)$ | $\sigma(\Delta V_{th}) = \frac{A_{Vth}}{\sqrt{W \cdot L}}$ |

> **Il legame tra i due:** Nella zona di forte Roll-Off, la curva $V_{th}(L)$ è estremamente ripida ($\frac{\partial V_{th}}{\partial L}$ gigante). Se la litografia di produzione sbaglia di appena $\Delta L = \pm 0.5\,\text{nm}$, due transistor adiacenti avranno una differenza di $V_{th}$ mostruosa, peggiorando drasticamente il mismatch di Pelgrom!

---
*Pagine correlate:*
- [La soglia da cosa dipende](../Dispositivi%20e%20Componenti/La%20soglia%20da%20cosa%20dipende.md)
- [Analogico non si scende di dimensioni](../Scaling%20e%20Limiti%20Fisici/Analogico%20non%20si%20scende%20di%20dimensioni.md)
- [DIBL](./DIBL.md)
