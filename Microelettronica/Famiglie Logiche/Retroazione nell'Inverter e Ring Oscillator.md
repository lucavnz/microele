Quando si parla di **retroazione in un invertitore logico** si fa riferimento al collegamento dell'uscita verso il proprio ingresso (o in un anello chiuso di porte). Il comportamento del circuito cambia radicalmente tra il regime **statico (continua, DC)** e il regime **dinamico (con ritardo di commutazione)**.

---

### 1. Retroazione di un Singolo Invertitore in DC: La Soglia Logica $V_M$

Se colleghiamo direttamente l'uscita dell'invertitore al suo ingresso ($V_O = V_I$):

```
        ┌────────────────┐
        │                │
        └───►[ INVERTER ]─┴──► V_O (= V_I)
```

In condizioni statiche a regime, il circuito deve soddisfare simultaneamente due vincoli:
1. La caratteristica di trasferimento: $V_O = f(V_I)$
2. Il cortocircuito: $V_O = V_I$

L'unico punto di lavoro possibile è l'intersezione tra la curva di trasferimento e la retta bisettrice, ovvero la **[Soglia Logica $V_M$](./Soglia%20Logica%20e%20Margine%20di%20Rumore.md)**:
$$V_O = V_I = V_M \approx \frac{V_{DD}}{2}$$

* **Retroazione negativa in continua:** se la tensione $V_I$ tenta di salire sopra $V_M$, l'uscita tende a scendere e tira verso il basso l'ingresso; viceversa, se $V_I$ scende sotto $V_M$, l'uscita sale e lo ritira su.
* **Stato dei transistor:** nel punto $V_M$ i transistor **non sono spenti**:
  * Nei [MOS](../Dispositivi%20e%20Componenti/MOS.md), sia NMOS che PMOS sono simultaneamente accesi in saturazione (vedi [Inverter CMOS e Regioni di Funzionamento](./Inverter%20CMOS%20e%20Regioni%20di%20Funzionamento.md)).
  * Nei [BJT](../Dispositivi%20e%20Componenti/BJT.md), il transistor lavora in zona attiva diretta.
* In questa condizione il guadagno differenziale in modulo è massimo ($|A_v| \gg 1$) e scorre la massima corrente di cortocircuito tra alimentazione e massa: l'inverter opera come un **amplificatore lineare analogico auto-polarizzato**.

---

### 2. Il Ritardo di Propagazione ($t_p$) e l'Oscillazione

La stabilità statica su $V_M$ presuppone un segnale istantaneo. Nella realtà fisica, ogni porta possiede un [tempo di propagazione $t_p$](./RTL%20e%20Prodotto%20Ritardo-Consumo%20%28PDP%29.md) non nullo:

```
t = 0:    Ingresso = 0  ──►  (attesa tp)  ──►  Uscita = 1
              ▲                                   │
              └───────────── riporto a monte ─────┘
t = tp:   Ingresso = 1  ──►  (attesa tp)  ──►  Uscita = 0
              ▲                                   │
              └───────────── riporto a monte ─────┘
t = 2tp:  Ingresso = 0  ──►  (attesa tp)  ──►  Uscita = 1 ... (si ripete)
```

1. Se l'ingresso si trova a livello logico basso (`0`), l'uscita deve andare ad alto (`1`), ma impiega un intervallo $t_p$ per caricare le capacità di nodo.
2. Appena l'uscita raggiunge il valore alto, questo livello si ritrova immediatamente all'ingresso.
3. Riconoscendo l'ingresso alto, la porta commuta per portare l'uscita a basso (`0`), impiegando un altro tempo $t_p$.
4. L'uscita scende a `0`, ritorna all'ingresso e il ciclo ricomincia da capo.

Il circuito **insegue all'infinito la propria negazione**: non potendo fermarsi in uno stato logico stabile, entra in **auto-oscillazione permanente**, generando un'onda quadra.

---

### 3. Il Ring Oscillator (Oscillatore ad Anello a $N$ Dispari)

In un singolo invertitore integrato, se il ritardo $t_p$ è troppo ridotto rispetto alle costanti di tempo interne, il segnale rischia di smorzarsi e adagiarsi sul punto analogico $V_M$.

Per ottenere un'oscillazione periodica stabile con swing logico pieno da $0$ a $V_{DD}$, si collegano in anello chiuso un **numero dispari $N$ di invertitori** ($N = 3, 5, 7\dots$):

```
┌────────────────────────────────────────────────────────┐
│                                                        │
└──►[ NOT 1 ]──(tp)──►[ NOT 2 ]──(tp)──►[ NOT 3 ]──(tp)──┴──► f_osc
```

#### Formula del Periodo e Frequenza
Il fronte logico deve attraversare l'intera catena di $N$ stadi per **due volte consecutive** (una prima volta per la transizione $0 \to 1$ e una seconda volta per la transizione $1 \to 0$):

$$T = 2 \cdot N \cdot t_p$$
$$f = \frac{1}{2 \cdot N \cdot t_p}$$

#### Cosa cambia tra TANTI inverter e POCHI inverter?

| Parametro | POCHI inverter (es. $N = 3$) | TANTI inverter (es. $N = 31, 65, 101$) |
| :--- | :--- | :--- |
| **Frequenza di oscillazione** | **Altissima** (decine di GHz) | **Moderata / Bassa** (decine/centinaia di MHz) |
| **Periodo $T$** | Brevissimo | Molto lungo |
| **Forma d'onda** | Rischia di essere smussata (quasi sinusoidale) | **Onda quadra perfetta rail-to-rail** ($0\text{ V} \leftrightarrow V_{DD}$) |
| **Stabilità di oscillazione** | Più sensibile al guadagno | **Robustissima** |

* **Perché $N = 1$ non oscilla e $N = 3$ è il minimo fisico:**  
  Un singolo invertitore con uscita collegata all'ingresso non ha uno sfasamento di fase sufficiente a soddisfare il criterio di Barkhausen prima che il guadagno cali: finisce per "sedersi" a riposo sul punto statico $V_M \approx V_{DD}/2$. Con $N = 3$ (tre stadi con polo RC che introducono ciascuno $60^\circ$ di ritardo oltre all'inversione) si raggiunge lo sfasamento necessario per innescare l'oscillazione permanente.
* **Forma d'onda piena:** con una catena lunga, il fronte ha tutto il tempo di saturare completamente a massa e ad alimentazione prima dell'arrivo della transizione successiva, eliminando incertezze logiche.

> [!TIP]
> **Lo strumento industriale "Process Monitor" (Test Chip):**  
> Misurare direttamente il ritardo $t_p$ di una singola porta logica (spesso dell'ordine di $10\text{ ps}$) è tecnicamente impossibile con strumenti esterni a causa delle capacità parassite delle sonde.  
> Fonderie come TSMC o Intel inseriscono sui wafer un Ring Oscillator con **$N = 101$ stadi**: la frequenza scende a valori comodamente leggibili con un normale frequenzimetro (es. $50\text{ MHz}$) e da essa si estrae con precisione assoluta il ritardo medio del singolo transistor della tecnologia:
> $$t_p = \frac{T}{2 \cdot N} = \frac{1}{2 \cdot N \cdot f}$$

---

### 4. Confronto Fondamentale: Anello Dispari vs Anello Pari

La tipologia di circuito dipende unicamente dal fatto che il numero di inversioni nel loop sia dispari o pari:

| Configurazione | Tipo di retroazione | Comportamento del circuito | Funzione logica |
| :--- | :--- | :--- | :--- |
| **$N$ Dispari ($1, 3, 5\dots$)** | Retroazione **negativa con ritardo** | Il circuito non ha punti stabili estremi e **oscilla continuamente**. | **Ring Oscillator** (generazione di clock, test $t_p$). |
| **$N$ Pari ($2, 4\dots$)** | Retroazione **positiva (rigenerativa)** | Il segnale si blocca in uno dei due stati ($0$ o $1$) rinforzandosi da solo. | **Bistabile / Cella SRAM** (memoria statica). |

👉 Approfondimento sulla memoria statica, la bistabilità e la metastabilità: [Bistabilità, Metastabilità e Latch Statici](../Circuiti%20Sequenziali%20CMOS/Bistabilit%C3%A0,%20Metastabilit%C3%A0%20e%20Latch%20Statici.md).  
👉 Approfondimento sulla rigenerazione dei livelli logici: [Caratteristica di Trasferimento e Rigenerazione](./Caratteristica%20di%20Trasferimento%20e%20Rigenerazione.md).

---

### 5. Multivibratori e Altri Generatori di Clock

Nel panorama dei circuiti sequenziali, i multivibratori si classificano in tre categorie (metafora dell'altalena):

```
    BISTABILE (Flip-Flop)            MONOSTABILE (One-Shot)            ASTABILE (Oscillatore)
    
       S              R                     T
       ▼              ▼                     ▼
      ══════▲══════════                    ══════▲══════════                 ══════▲══════════
    (2 posizioni stabili:                (1 stato stabile:                 (Nessuno stato stabile:
     memorizza 0 o 1)                     la molla lo richiama)             molle sui due lati, oscilla!)
```

1. **Monostabili (One-Shot):**  
   Possiedono un solo stato stabile. Un impulso di trigger li porta temporaneamente nello stato instabile per un tempo prefissato $t_d$ (determinato da una linea di ritardo logica o da una rete $RC$, con $t_d \propto RC$), dopodiché il circuito torna da solo allo stato di riposo.
2. **Oscillatore a Rilassamento (Relaxation Oscillator):**  
   Due invertitori con retroazione tramite resistenza $R$ e capacità $C$. Il condensatore si carica e scarica ciclicamente attraverso $R$, con periodo legato ai componenti passivi:
   $$T = 2 \ln(3) \cdot RC \approx 2.2 \cdot RC$$
3. **VCO (Voltage-Controlled Oscillator):**  
   Permette di variare la frequenza di oscillazione agendo su una tensione di controllo continua $V_{contr}$.
   * Si utilizza un **Current-Starved Inverter** (inverter a corrente affamata): transistor ausiliari limitano la corrente $I_{ref}$ di carica/scarica del nodo in base a $V_{contr}$, variando a comando il ritardo $t_p$.
   * **Il ruolo dello Schmitt Trigger a valle:** poiché la corrente limitata rende le transizioni di tensione lentissime (rampe "mosce"), lo Schmitt Trigger con la sua soglia a isteresi **ripristina la ripidità dei fronti (*restores signal slopes*)**, rigenerando un'onda quadra netta a basso consumo statico.

---

### 6. Unilateralità e Retroazioni Parassite Indesiderate

Nelle specifiche ideali delle famiglie logiche si richiede che le porte siano **unilaterali** (Slide 5 di [famiglie.pdf](../../famiglie.pdf)):

* **Comportamento ideale a senso unico:** il segnale deve propagarsi esclusivamente dall'ingresso verso l'uscita, senza che le variazioni sull'uscita alterino le tensioni a monte.
* **Retroazione parassita nei dispositivi reali:** nei transistor integrati esistono accoppiamenti capacitivi non eliminabili, come la capacità parassita $C_{gd}$ nel MOS o $C_{bc}$ nel BJT, amplificata per [Effetto Miller](../Dispositivi%20e%20Componenti/Effetto%20Miller.md) (vedi anche [Capacità parassite nel MOSFET](../Dispositivi%20e%20Componenti/Capacit%C3%A0%20parassite%20nel%20MOSFET.md)). Durante una rapida transizione in uscita, una frazione di carica viene iniettata a ritroso sul nodo di ingresso.
* **Effetti deleteri:** se la porta non garantisse una sufficiente unilateralità, la retroazione parassita corromperebbe la tensione del nodo pilota precedente, riducendo i [margini di rumore](./Soglia%20Logica%20e%20Margine%20di%20Rumore.md) o innescando oscillazioni spurie ad alta frequenza.

---

*Pagine correlate:*
- [Bistabilità, Metastabilità e Latch Statici](../Circuiti%20Sequenziali%20CMOS/Bistabilit%C3%A0,%20Metastabilit%C3%A0%20e%20Latch%20Statici.md)
- [Logica Sequenziale e Temporizzazione](../Circuiti%20Sequenziali%20CMOS/Logica%20Sequenziale%20e%20Temporizzazione.md)
- [Caratteristica di Trasferimento e Rigenerazione](./Caratteristica%20di%20Trasferimento%20e%20Rigenerazione.md)
- [Inverter CMOS e Regioni di Funzionamento](./Inverter%20CMOS%20e%20Regioni%20di%20Funzionamento.md)
- [Soglia Logica e Margine di Rumore](./Soglia%20Logica%20e%20Margine%20di%20Rumore.md)
- [Effetto Miller](../Dispositivi%20e%20Componenti/Effetto%20Miller.md)
- [RTL e Prodotto Ritardo-Consumo (PDP)](./RTL%20e%20Prodotto%20Ritardo-Consumo%20%28PDP%29.md)
- [Potenza Dinamica e Dissipazione di Carica](./Potenza%20Dinamica%20e%20Dissipazione%20di%20Carica.md)
- [Capacità parassite nel MOSFET](../Dispositivi%20e%20Componenti/Capacit%C3%A0%20parassite%20nel%20MOSFET.md)
- [MOS](../Dispositivi%20e%20Componenti/MOS.md)
- [BJT](../Dispositivi%20e%20Componenti/BJT.md)
