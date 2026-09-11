# Portatori Caldi (*Hot Carrier Injection - HCI*)

### Cos'è l'effetto Hot Carriers?
Quando il MOSFET lavora in saturazione, il canale si strizza (*pinch-off*) prima di raggiungere il Drain.
Tutta la differenza di potenziale $(V_{DS} - V_{DS,sat})$ cade in una minuscola regione spaziale $\Delta L$ adiacente al Drain.

Questo genera un **picco di campo elettrico locale spaventoso**:
$$E_{peak} > 10^5 - 10^6\,\text{V/cm}$$

Gli elettroni che attraversano questa zona vengono accelerati violentemente, accumulando un'energia cinetica molto superiore all'energia termica media: diventano **"portatori caldi"** (*hot carriers*).

---

### Meccanismi di degrado fisico


1. **Iniezione nell'ossido:** Alcuni elettroni hanno energia cinetica sufficiente per superare la barriera di potenziale silicio-ossido ($\approx 3.1\text{ eV}$) e vengono sparati direttamente nel dielettrico di Gate ($\text{SiO}_2$).
2. **Generazione di trappole interfacciali:** L'impatto ad alta energia rompe i legami $\text{Si-H}$ o $\text{Si-O}$ all'interfaccia, creando nuove trappole energetiche permanenti.
3. **Ionizzazione per impatto (Effetto Valanga):** I portatori caldi collidono violentemente con gli atomi del reticolo di silicio, rompendo legami covalenti e liberando nuove coppie elettrone-lacuna secondarie.

---

### Separazione delle Cariche Secondarie e Corrente di Substrato ($I_B$)

Nella regione di pinch-off al Drain, il campo elettrico separa istantaneamente le cariche secondarie generate per impatto:
* **Gli elettroni secondari** vengono attratti dal potenziale positivo del Drain $\implies$ vanno a sommarsi alla corrente utile $\Delta I_D$, facendo impennare la caratteristica $I_D(V_{DS})$ ad alti voltaggi.
* **Le lacune secondarie** vengono respinte dal Drain verso il potenziale più basso (il substrato $P$) $\implies$ fluiscono verso la presa di massa del Bulk dando origine a una **corrente di substrato $I_B$** (o $I_{sub}$).

---

### I 4 Gravi Pericoli Circuitali

1. **Innesco del Latch-Up (Pericolo Distruttivo!):**  
   La corrente di substrato $I_B$ scorre lungo il bulk per raggiungere i contatti metallici di massa. Attraversando la resistenza distribuita del silicio ($R_{sub}$), genera una caduta ohmica localizzata:
   $$\Delta V = R_{sub} \cdot I_B$$
   Se questa caduta supera $\approx 0.6 \div 0.7\,\text{V}$, polarizza in diretta la giunzione base-emettitore del transistore parassita NPN, accendendo la struttura tiristore a 4 strati SCR e causando il **latch-up distruttivo** (corto-circuito permanente tra alimentazione e massa).
2. **Crollo della Resistenza di Uscita ($r_o \to 0$):**  
   L'impennata di corrente a valanga fa esplodere la conduttanza differenziale $g_{ds} = \frac{\partial I_D}{\partial V_{DS}}$, abbattendo drasticamente $r_o$ e annullando il guadagno di tensione degli stadi analogici ($A_0 = g_m r_o$, vedi [Crollo della Resistenza di Uscita (ro)](./Crollo%20di%20ro.md)).
3. **Aumento del Rumore (Shot Noise):**  
   Gli eventi casuali e quantistici di ionizzazione per impatto generano forte rumore a valanga ($\overline{i_{nav}^2}/\Delta f = 2qI_{av}$), degradando il rapporto segnale/rumore (vedi [Rumore nel MOSFET](../Dispositivi%20e%20Componenti/Rumore%20nel%20MOSFET.md)).
4. **Deriva Temporale della Soglia ($V_{Th}$ Shift / Aging):**  
   Le cariche intrappolate stabilmente nell'ossido modificano la carica totale $Q_{ox}$. Con l'accumularsi delle ore di funzionamento, la tensione di soglia $V_{th}$ slitta progressivamente nel tempo ($\Delta V_{th}(t)$), la transconduttanza $g_m$ crolla e il chip finisce **fuori specifica**.

---

### Perché l'Effetto è Molto Peggiore nell'NMOS rispetto al PMOS?

Il coefficiente di ionizzazione $\alpha$ (numero di coppie generate per centimetro di percorso) è legato al campo elettrico $E$:
$$\alpha_n \gg \alpha_p$$

* Gli **elettroni** (portatori dei canali N) hanno una massa efficace notevolmente inferiore rispetto alle lacune e una mobilità circa 2-3 volte superiore.
* Nel silicio, tra due collisioni reticolari gli elettroni riescono ad accumulare molta più energia cinetica rispetto alle lacune prima di essere rallentati.
* **Nei PMOS**, la probabilità di ionizzazione per urto $\alpha_p$ è molto più bassa: il transistor a canale P è intrinsecamente molto più immune all'effetto valanga e all'iniezione di portatori caldi.

---

*Pagine correlate:*
- [Crollo della Resistenza di Uscita (ro)](./Crollo%20di%20ro.md)
- [Rumore nel MOSFET](../Dispositivi%20e%20Componenti/Rumore%20nel%20MOSFET.md)
- [Breakdown e Diodo Zener](../Dispositivi%20e%20Componenti/Breakdown%20e%20Diodo%20Zener.md)
- [Latchup nei circuiti CMOS](../Famiglie%20Logiche/Latchup%20nei%20circuiti%20CMOS.md)
- [1_f non va a braccetto con lo scaling](../Scaling%20e%20Limiti%20Fisici/1_f%20non%20va%20a%20braccetto%20con%20lo%20scaling.md)
- [Saturazione di velocita](./Saturazione%20di%20velocita.md)
- [Analogico non si scende di dimensioni](../Scaling%20e%20Limiti%20Fisici/Analogico%20non%20si%20scende%20di%20dimensioni.md)
