La famiglia **RTL (*Resistor-Transistor Logic*)** è la prima famiglia logica integrata della storia, basata su un invertitore a singolo [BJT](../Dispositivi%20e%20Componenti/BJT.md) con resistore di pull-up $R_C$ e resistore di base $R_B$.

---

### 1. Dissipazione Statica ($P_s$): Il Caso Peggiore a Regime

Per definizione, la **potenza statica dissipata $P_s$** di una porta logica è il **valore massimo (caso peggiore)** tra tutte le combinazioni logiche degli ingressi in condizioni stazionarie (post-transitorio):

$$P_s = \max[P_{sL}, P_{sH}]$$

In un invertitore RTL ($V_{CC} = 3\text{ V}$, $R_C = 640\ \Omega$, $R_B = 450\ \Omega$):
* **Ingresso BASSO ($V_I = 0\text{ V}$):** il BJT è interdetto (spento). Non scorre corrente né da $V_{CC}$ né in base $\implies \mathbf{P_{sL} = 0\text{ W}}$.
* **Ingresso ALTO ($V_I = 3\text{ V}$):** il BJT è saturo (acceso a massa). Scorre corrente continua sia sul ramo di collettore che sul ramo di base:
  $$I_C = \frac{V_{CC} - V_{OL}}{R_C} \approx 4.57\text{ mA}, \quad I_B = \frac{V_I - V_{BE}}{R_B} \approx 5.13\text{ mA}$$
  $$P_{sH} = V_{CC} I_C + V_I I_B = 3\text{ V} (4.57\text{ mA}) + 3\text{ V} (5.13\text{ mA}) \approx \mathbf{29.1\text{ mW}}$$
* **Risultato:** $P_s = P_{sH} \approx 29.1\text{ mW}$ (disastroso consumo continuo a vuoto finché l'ingresso resta alto).

---

### 2. Asimmetria nei Tempi di Commutazione ($t_{pHL} \ll t_{pLH}$)

Quando l'uscita pilota una [capacità parassita di carico](../Dispositivi%20e%20Componenti/Capacit%C3%A0%20parassite%20nel%20MOSFET.md) $C$:

* **Transizione Alto $\to$ Basso ($t_{pHL} \approx 13\text{ ps}$):**  
  Il BJT si accende ed entra in forte conduzione attiva/saturazione, comportandosi come un generatore di corrente elevata che **scarica attivamente la capacità $C$ quasi istantaneamente**.
* **Transizione Basso $\to$ Alto ($t_{pLH} \approx 855\text{ ps}$):**  
  Il BJT si spegne. La capacità $C$ deve essere **caricata passivamente solo attraverso il [resistore](../Dispositivi%20e%20Componenti/Resistore.md) $R_C$**, con costante di tempo $\tau = R_C \cdot C$. La salita della tensione è molto lenta.

#### Il Tempo di Propagazione Medio ($t_p$)
Il tempo di propagazione caratteristico di una porta non è solo il caso peggiore, ma la **media aritmetica** tra i due fronti:

$$t_p = \frac{t_{pHL} + t_{pLH}}{2}$$

> **Perché la media?**  
> In una catena di porte in cascata, a ogni stadio i fronti si alternano ($H \to L \to H \to L$). Il ritardo medio per singolo stadio lungo la catena è esattamente la media dei due tempi.  
> Tuttavia, poiché in RTL $t_{pLH} \gg t_{pHL}$, il ritardo complessivo è **dominato quasi per intero dal fronte lento di salita**:
> $$t_p \approx \frac{t_{pLH}}{2} \approx 434\text{ ps}$$

---

### 3. Il Trade-off di $R_C$ e il Prodotto Ritardo-Consumo ($PDP \approx \text{costante}$)

Il **Power-Delay Product ($PDP$)** rappresenta l'energia media spesa per singola commutazione:

$$PDP = P_{\text{MED}} \times t_p$$

Poiché in RTL la potenza statica domina su quella dinamica ($P_{\text{MED}} \approx P_s$):
$$P_s \approx V_{CC}^2 \left( \frac{1}{R_C} + \frac{1}{R_B} \right) \propto \frac{1}{R_C}$$
$$t_p \approx \frac{R_C C}{2} \ln\left(\frac{V_{CC} - V_{OL}}{V_{CC} - V_{O50\%}}\right) \propto R_C$$

Moltiplicando i due termini:

$$PDP \approx P_s \cdot t_p \approx \left( 1 + \frac{R_C}{R_B} \right) \frac{V_{CC}^2 C}{2} \ln(\dots) \approx \mathbf{\text{costante}} \approx 600\text{ pJ}$$

* Se **diminuisci $R_C$**: carichi la capacità più velocemente ($t_p \downarrow$), ma aumenti la corrente statica e dissipi più potenza ($P_s \uparrow$).
* Se **aumenti $R_C$**: consumi meno corrente ($P_s \downarrow$), ma la porta diventa lentissima a salire ($t_p \uparrow$).
* **Conclusione ed Evoluzione:** in RTL non è possibile ottimizzare velocità e consumi contemporaneamente. Per superare questi limiti si sono sviluppate diverse architetture bipolari ([DCTL](./DCTL%20e%20Current%20Hogging.md), [I2L](./I2L%20%28Integrated%20Injection%20Logic%29.md), [DTL](./DTL%20%28Diode-Transistor%20Logic%29.md), [TTL](./TTL%20%28Transistor-Transistor%20Logic%29.md), [ECL](./ECL%20%28Emitter-Coupled%20Logic%29.md)) fino al definitivo trionfo della tecnologia CMOS (dove sia $P_{sL}$ che $P_{sH}$ sono nulli).

---

*Pagine correlate:*
- [DCTL e Current Hogging](./DCTL%20e%20Current%20Hogging.md)
- [I2L (Integrated Injection Logic)](./I2L%20%28Integrated%20Injection%20Logic%29.md)
- [DTL (Diode-Transistor Logic)](./DTL%20%28Diode-Transistor%20Logic%29.md)
- [TTL (Transistor-Transistor Logic)](./TTL%20%28Transistor-Transistor%20Logic%29.md)
- [ECL (Emitter-Coupled Logic)](./ECL%20%28Emitter-Coupled%20Logic%29.md)
- [Famiglia Logica e Costo per Bit](./Famiglia%20Logica%20e%20Costo%20per%20Bit.md)
- [Potenza Dinamica e Dissipazione di Carica](./Potenza%20Dinamica%20e%20Dissipazione%20di%20Carica.md)
- [Soglia Logica e Margine di Rumore](./Soglia%20Logica%20e%20Margine%20di%20Rumore.md)
- [Caratteristica di Trasferimento e Rigenerazione](./Caratteristica%20di%20Trasferimento%20e%20Rigenerazione.md)
- [BJT](../Dispositivi%20e%20Componenti/BJT.md)
- [Resistore](../Dispositivi%20e%20Componenti/Resistore.md)
- [Capacità parassite nel MOSFET](../Dispositivi%20e%20Componenti/Capacit%C3%A0%20parassite%20nel%20MOSFET.md)
- [Analogico non si scende di dimensioni](../Scaling%20e%20Limiti%20Fisici/Analogico%20non%20si%20scende%20di%20dimensioni.md)
