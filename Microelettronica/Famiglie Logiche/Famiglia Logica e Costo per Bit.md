Una **famiglia logica** è l'insieme di tutte le topologie circuitali che realizzano diverse funzioni logiche condividendo:
1. Il **nucleo topologico di base** (es. logica complementare con [MOS](../Dispositivi%20e%20Componenti/MOS.md) a canale $p$ per il pull-up e a canale $n$ per il pull-down, oppure [BJT](../Dispositivi%20e%20Componenti/BJT.md) con carico resistivo come in RTL).
2. Gli **stessi livelli di tensione** (alimentazione $V_{CC}/V_{DD}$ e livelli logici $V_{OH}, V_{OL}, V_{IH}, V_{IL}$), garantendo che l'uscita di una porta possa pilotare direttamente l'ingresso di un'altra senza convertitori di livello.
3. Il **medesimo processo tecnologico di fonderia** (stesso numero di maschere, drogaggi e litografia).

---

### 1. Il Costo "Per Bit" e le Porte Elementari Universali

Nei circuiti integrati digitali il costo di produzione viene valutato **per bit** (o per porta logica elementare / *gate equivalent*):
* **L'unità di misura base:** per convenzione si prende come riferimento la porta logica elementare più semplice (come una porta NAND o NOR a 2 ingressi, oppure l'inverter).
* **Universalità:** NAND e NOR sono **porte logiche universali**; questo significa che un intero chip (anche un microprocessore complesso) può essere teoricamente e praticamente realizzato combinando solo porte elementari dello stesso tipo.
* **Calcolo del costo:** se trattare un'area di wafer costa $20.000\text{ €}$ e su quell'area stampiamo $1\text{ miliardo}$ di porte logiche funzionanti, il costo per porta è:
  $$\text{Costo per bit} = \frac{20.000\text{ €}}{10^9\text{ porte}} = 0.00002\text{ €/porta}$$

---

### 2. Perché l'Area Comanda: Costo e Resa (*Yield*) del Wafer

Una famiglia logica è tanto più **pregiata** quanto **minore è l'occupazione di area** del circuito a parità di funzione:

1. **L'impatto micidiale sulla Resa (*Yield*):**
   * Durante la [lavorazione del wafer](../Tecnologia%20e%20Fabbricazione/Wafer%20produzione.md) si generano inevitabilmente difetti microscopici casuali sparsi sulla superficie.
   * **Se stampi chip giganti:** su un wafer ci stanno solo $10$ chip; con $3$ difetti sparsi rischi di contaminare $3$ chip diversi, buttando via il $30\%$ dell'intera produzione (resa del $70\%$).
   * **Se stampi chip minuscoli:** sullo stesso wafer ci stanno $100$ chip; quegli stessi $3$ difetti colpiscono solo $3$ chip, ottenendo una **resa del $97\%$**!
   * Più l'area del singolo die si riduce, più la percentuale di chip sani che passano il collaudo esplode verso l'alto.

2. **Miniaturizzazione (Scaling): Più Veloce e Meno Consumo:**
   * **Capacità parassite:** riducendo l'area geometrica dei transistor, le [capacità parassite](../Dispositivi%20e%20Componenti/Capacit%C3%A0%20parassite%20nel%20MOSFET.md) diminuiscono drasticamente ($C \propto \text{Area}$).
   * **Maggiore velocità:** il ritardo di commutazione vale $t_p \propto R \cdot C$, quindi capacità minori significano commutazioni più rapide e frequenze di clock più elevate.
   * **Minori consumi:** la potenza dinamica spesa per caricare e scaricare i nodi vale:
     $$P_d = C \cdot V_{DD}^2 \cdot f$$
     A parità di frequenza $f$, una capacità $C$ inferiore riduce direttamente l'energia dissipata ad ogni commutazione ([Potenza Dinamica e Dissipazione di Carica](./Potenza%20Dinamica%20e%20Dissipazione%20di%20Carica.md)).

---

### 3. Famiglie Statiche vs Dinamiche

* **Famiglie statiche (es. CMOS statica, RTL, TTL):** il valore logico in uscita dipende esclusivamente dai valori attuali degli ingressi (a transitorio esaurito) e rimane stabile indefinitamente nel tempo.
* **Famiglie dinamiche:** il dato viene memorizzato temporaneamente su nodi capacitivi; l'uscita permane corretta solo per un intervallo di tempo limitato prima che le correnti di perdita scarichino le capacità, richiedendo un clock continuo di refresh.

---

*Pagine correlate:*
- [RTL e Prodotto Ritardo-Consumo (PDP)](./RTL%20e%20Prodotto%20Ritardo-Consumo%20%28PDP%29.md)
- [Potenza Dinamica e Dissipazione di Carica](./Potenza%20Dinamica%20e%20Dissipazione%20di%20Carica.md)
- [Caratteristica di Trasferimento e Rigenerazione](./Caratteristica%20di%20Trasferimento%20e%20Rigenerazione.md)
- [Soglia Logica e Margine di Rumore](./Soglia%20Logica%20e%20Margine%20di%20Rumore.md)
- [Wafer produzione](../Tecnologia%20e%20Fabbricazione/Wafer%20produzione.md)
- [Capacità parassite nel MOSFET](../Dispositivi%20e%20Componenti/Capacit%C3%A0%20parassite%20nel%20MOSFET.md)
- [Analogico non si scende di dimensioni](../Scaling%20e%20Limiti%20Fisici/Analogico%20non%20si%20scende%20di%20dimensioni.md)
- [MOS](../Dispositivi%20e%20Componenti/MOS.md)
- [BJT](../Dispositivi%20e%20Componenti/BJT.md)
