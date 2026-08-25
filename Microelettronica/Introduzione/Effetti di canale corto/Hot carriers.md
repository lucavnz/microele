# Portatori Caldi (*Hot Carrier Injection - HCI*)

### Cos'è l'effetto Hot Carriers?
Quando il MOSFET lavora in saturazione, il canale si strizza (*pinch-off*) prima di raggiungere il Drain.
Tutta la differenza di potenziale $(V_{DS} - V_{DS,sat})$ cade in una minuscola regione spaziale $\Delta L$ adiacente al Drain.

Questo genera un **picco di campo elettrico locale spaventoso**:
$$E_{peak} > 10^5 - 10^6\,\text{V/cm}$$

Gli elettroni che attraversano questa zona vengono accelerati violentemente, accumulando un'energia cinetica molto superiore all'energia termica media: diventano **"portatori caldi"** (*hot carriers*).

---

### Meccanismi di degrado fisico

1. **Iniezione nell'ossido:** Alcuni elettroni hanno energia sufficiente per superare la barriera di potenziale silicio-ossido ($\approx 3.1\text{ eV}$) e vengono iniettati direttamente nel dielettrico di Gate ($\text{SiO}_2$).
2. **Generazione di trappole interfacciali:** L'impatto ad alta energia rompe i legami $\text{Si-H}$ o $\text{Si-O}$ all'interfaccia, creando nuove trappole energetiche permanenti.
3. **Ionizzazione per impatto:** I portatori caldi collidono con gli atomi del reticolo di silicio, generando coppie elettrone-lacuna secondarie che creano corrente parassita nel substrato ($I_{sub}$).

---

### Perché distrugge le prestazioni in Analogico?

* **Deriva Temporale (Aging / Invecchiamento del circuito):**
  A mano a mano che le cariche si accumulano nell'ossido e le trappole aumentano:
  * La tensione di soglia $V_{th}$ scivola lentamente nel tempo ($\Delta V_{th}(t)$).
  * La transconduttanza $g_m$ diminuisce per via della minore mobilità superficiale.
  * In circuiti analogici di precisione (es. riferimenti di tensione Bandgap, amplificatori a basso rumore), il chip dopo 1 anno di funzionamento finisce **completamente fuori specifica**.

* **Aumento del Rumore Flicker $1/f$:**
  Poiché il rumore $1/f$ nasce proprio dal trapping/detrapping all'interfaccia, creare nuove trappole con gli Hot Carriers significa **peggiorare costantemente il rumore $1/f$** durante la vita utile del dispositivo.

---
*Pagine correlate:*
- [Analogico non si scende di dimensioni](../Analogico%20non%20si%20scende%20di%20dimensioni.md)
- [1_f non va a braccetto con lo scaling](<../1_f on va a braccietto con lo scaling.md>)
- [Saturazione di velocita](./Saturazione%20di%20velocita.md)
