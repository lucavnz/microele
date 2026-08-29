# Saturazione di Velocità (*Velocity Saturation*)

### Cos'è fisicamente?
Nei transistor a canale lungo la velocità di deriva degli elettroni è proporzionale al campo elettrico:
$$v = \mu_n \cdot E$$

Quando rimpiccioliamo $L$ fino a pochi nanometri, il campo elettrico longitudinale lungo il canale ($E \approx \frac{V_{DS,sat}}{L}$) supera facilmente il valore critico $E_{crit} \approx 10 - 20\,\text{kV/cm}$.
In questo regime, gli elettroni collidono così violentemente e frequentemente con i fononi del reticolo di silicio da raggiungere una **velocità limite massima**:
$$v_{sat} \approx 10^7\,\text{cm/s} = 10^5\,\text{m/s}$$

Anche se aumentiamo ancora il campo elettrico o la tensione di Drain, gli elettroni **non possono andare più veloci di $v_{sat}$**.

---

### Morte della formula quadratica
La classica legge quadratica in saturazione:
$$I_D = \frac{1}{2} \mu_n C_{ox} \frac{W}{L} (V_{GS} - V_{th})^2 \quad \text{(NON VALE PIÙ)}$$

Viene sostituita dal modello di forte saturazione di velocità, in cui la corrente diventa **lineare** con l'overdrive:
$$I_D \approx W \cdot C_{ox} \cdot v_{sat} \cdot (V_{GS} - V_{th})$$

---

### Perché distrugge le prestazioni in Analogico?

1. **La transconduttanza $g_m$ non sale più:**
   Nel modello classico, $g_m = \sqrt{2 \mu_n C_{ox} \frac{W}{L} I_D} \propto \sqrt{I_D}$. Potevi aumentare la corrente $I_D$ per ottenere più guadagno $g_m$.
   In velocità satura:
   $$g_m = \frac{\partial I_D}{\partial V_{GS}} \approx W \cdot C_{ox} \cdot v_{sat} = \text{costante}$$
   Aumentare la corrente di polarizzazione $I_D$ è del tutto inutile: $g_m$ resta bloccata al valore limite!

2. **Crollo dell'efficienza $g_m/I_D$:**
   L'efficienza di transconduttanza $g_m/I_D$ misura quanto guadagno ottieni per ogni milliampere di corrente speso. Nei nodi nanometrici saturi questa efficienza scende drasticamente, costringendo a sprecare potenza statica per ottenere prestazioni analogiche mediocri.

---
*Pagine correlate:*
- [Analogico non si scende di dimensioni](../Scaling%20e%20Limiti%20Fisici/Analogico%20non%20si%20scende%20di%20dimensioni.md)
- [Crollo di ro](./Crollo%20di%20ro.md)
- [Hot carriers](./Hot%20carriers.md)
