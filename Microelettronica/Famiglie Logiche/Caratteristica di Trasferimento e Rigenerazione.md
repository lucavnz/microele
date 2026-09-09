La **Caratteristica Statica di Trasferimento (VTC)** di un invertitore digitale ($V_O = f(V_I)$) presenta tipicamente un profilo non lineare con tre zone distinte:
1. Una **zona alta quasi piatta** (ingresso basso, uscita vicina a $V_{OH}$).
2. Una **zona centrale di transizione a fortissima pendenza** (alto guadagno in modulo $|A_v| \gg 1$).
3. Una **zona bassa quasi piatta** (ingresso alto, uscita vicina a $V_{OL}$).

---

### 1. Le Zone Piatte ($|A_v| < 1$): Gli Ammortizzatori di Rumore

Le zone orizzontali all'inizio e alla fine della curva non sono matematicamente piatte al $100\%$, ma possiedono una derivata (guadagno differenziale) con modulo strettamente minore di $1$:
$$|A_v| = \left| \frac{dV_O}{dV_I} \right| < 1$$

* **Come agiscono:** fungono da veri e propri **"ammortizzatori" che uccidono il rumore**. 
* Se al segnale di ingresso nominale si somma una fluttuazione di disturbo $\Delta V_I$, la variazione trasferita sull'uscita sarà attenuata:
  $$\Delta V_O \approx A_v \cdot \Delta V_I \implies |\Delta V_O| < |\Delta V_I|$$
* **Comportamento in cascata:** propagando il segnale lungo una catena di invertitori, il disturbo non cresce, ma viene via via progressivamente **smorzato e azzerato** ad ogni stadio successivo.

---

### 2. La Zona Centrale ad Alto Guadagno ($|A_v| > 1$): Rigenerazione dei Livelli

Tra i punti a pendenza unitaria ($|A_v| = 1$, punti $A$ e $B$) la caratteristica precipita verticalmente:

* **Rigenerazione di segnali degradati:** se a un invertitore arriva un livello logico parzialmente corrotto o indebolito (ad esempio un *"1 moscio"* o uno *"0 sporco"* causato da cadute parassite o accoppiamenti capacitivi), l'elevato guadagno differenziale amplifica la differenza rispetto al punto di commutazione.
* **Ripristino dei livelli pieni:** passando attraverso la cascata di porte, il segnale viene forzato a convergere rapidamente verso i livelli logici nominali pieni ($V_{OH}$ o $V_{OL}$), rigenerando l'integrità del dato logico originario.

---

### 3. Senza Alto Guadagno: Niente Digitale, Solo Analogico Lineare

L'elevato guadagno $|A_v| \gg 1$ nella regione di transizione è il **"motore decisionale"** indispensabile di ogni circuito digitale:

* **Se il guadagno fosse ovunque $|A_v| \le 1$:** il circuito si comporterebbe come un sistema analogico lineare. Le transizioni temporali tra alto e basso sarebbero lentissime e un segnale che si trova a metà strada rimarrebbe intrappolato a metà strada, accumulando degrado e rumore ad ogni stadio.
* **La natura bistabile del digitale:** l'alto guadagno al centro combinato con l'attenuazione ($|A_v| < 1$) agli estremi crea due stati di equilibrio stabili ($V_{OH}$ e $V_{OL}$) e forza il circuito a **prendere una decisione drastica**: o $0$ o $1$, senza vie di mezzo.

👉 Approfondimento sulla retroazione bistabile (anelli pari) vs oscillatori ad anello (anelli dispari): [Retroazione nell'Inverter e Ring Oscillator](./Retroazione%20nell%27Inverter%20e%20Ring%20Oscillator.md).
👉 Approfondimento sull'analisi analitica delle regioni dell'inverter complementare: [Inverter CMOS e Regioni di Funzionamento](./Inverter%20CMOS%20e%20Regioni%20di%20Funzionamento.md).

---

*Pagine correlate:*
- [Inverter CMOS e Regioni di Funzionamento](./Inverter%20CMOS%20e%20Regioni%20di%20Funzionamento.md)
- [Retroazione nell'Inverter e Ring Oscillator](./Retroazione%20nell%27Inverter%20e%20Ring%20Oscillator.md)
- [Famiglia Logica e Costo per Bit](./Famiglia%20Logica%20e%20Costo%20per%20Bit.md)
- [Potenza Dinamica e Dissipazione di Carica](./Potenza%20Dinamica%20e%20Dissipazione%20di%20Carica.md)
- [Soglia Logica e Margine di Rumore](./Soglia%20Logica%20e%20Margine%20di%20Rumore.md)
- [Analogico non si scende di dimensioni](../Scaling%20e%20Limiti%20Fisici/Analogico%20non%20si%20scende%20di%20dimensioni.md)
- [Difficoltà nel fare un componente ideale](../Scaling%20e%20Limiti%20Fisici/Difficolt%C3%A0%20nel%20fare%20un%20componente%20ideale.md)
- [MOS](../Dispositivi%20e%20Componenti/MOS.md)
- [BJT](../Dispositivi%20e%20Componenti/BJT.md)
