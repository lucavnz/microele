L'**elettromigrazione** è il fenomeno per cui un'eccessiva densità di corrente provoca lo spostamento fisico graduale degli atomi del conduttore. Non è l'energia del singolo elettrone a muovere il metallo, ma il cosiddetto **vento elettronico** (*electron wind*): l'urto continuo di miliardi di elettroni contro gli ioni del reticolo.

---

### 1. La Legge di Black e il Tempo Medio al Guasto (MTTF)

La durata nel tempo di una pista metallica prima di rompersi per elettromigrazione è quantificata dalla **Legge di Black**:

$$\text{MTTF} = \frac{A}{J^n} \exp\left(\frac{E_a}{k_B T}\right)$$

Dove:
* $\text{MTTF}$ (*Mean Time To Failure*): è il **tempo medio prima del guasto** della pista metallica.
* $J = \frac{I}{\text{Area}}$: è la **densità di corrente** ($\text{A/cm}^2$).
* $n \approx 2$: esponente empirico legato sia all'urto del vento elettronico sia al riscaldamento per effetto Joule ($\Delta T \propto J^2$).
* $E_a$: è l'**Energia di Attivazione per l'autodiffusione atomica** (espressa in $\text{eV}$). Rappresenta la barriera energetica che un atomo deve superare per staccarsi dal reticolo.

I guasti da elettromigrazione provocano due problemi:
1. **Circuito Aperto (CA - *Voids*):** a monte del flusso elettronico gli atomi vengono spazzati via creando cavità che interrompono la linea.
2. **Cortocircuito (CC - *Hillocks/Whiskers*):** a valle gli atomi si accumulano creando cumuli e aghi metallici che perforano l'isolante toccando piste adiacenti.

---

### 2. Perché i Metalli Elettromigrano e il Silicio (anche Degenere) NO?

La differenza risiede nella **natura chimica del legame**:

* **Nei Metalli (Legame Metallico):**
  Gli ioni positivi sono immersi in un "mare" di elettroni condivisi. Il legame è **non direzionale e delocalizzato**: gli ioni possono scivolare facilmente se spinti dal vento elettronico ($E_a \approx 0.6 - 1.0\text{ eV}$). Metalli a punto di fusione altissimo come il Tungsteno ($3422^\circ\text{C}$) hanno legami fortissimi ($E_a > 1.6\text{ eV}$) e sono quasi immuni.
* **Nel Silicio (Legame Covalente $sp^3$):**
  Gli atomi di silicio sono bloccati in un reticolo a diamante con legami covalenti rigidi e direzionali. Per spostare un atomo servono $E_a \approx 4 - 5\text{ eV}$.
  *Anche se droghiamo il silicio fino a farlo diventare **degenere** ($N^+$ o $P^+$)*, la conduzione aumenta ma la struttura fisica rimane un cristallo covalente: il vento elettronico rimbalza sugli atomi senza riuscire a spostarli.

---

### 3. Tossicità dei Metalli a Contatto con il Silicio

Mettere metalli puri a contatto diretto con il silicio causa gravi degradazioni:

* **Alluminio e lo Spiking (*Junction Spiking*):**
  L'alluminio fonde a $660^\circ\text{C}$ e a temperature di processo ($400^\circ\text{C}-450^\circ\text{C}$) il silicio si scioglie nell'alluminio ($\approx 1\%$). Il silicio migra nella pista lasciando cavità che l'alluminio riempie formando "chiodi" verticali (*spikes*) che cortocircuitano le giunzioni sottili di Source e Drain.
* **Rame: Il "Veleno Assoluto" per il Silicio:**
  Il rame diffonde con estrema rapidità nel silicio anche a basse temperature ($100^\circ\text{C}$) e crea stati energetici a centro banda (*deep-level traps*). Questi stati agiscono come centri di ricombinazione micidiali, **azzerando il tempo di vita dei portatori minoritari ($\tau \to 0$)** e facendo esplodere la corrente di perdita da spento ($I_{OFF}$).

Per evitare questi problemi si impiegano strati intermedi protettivi:
👉 Vedi: [Siliciuro](./Siliciuro.md) e [Vias](./Vias.md)

---

*Pagine correlate:*
- [Vias](./Vias.md)
- [Siliciuro](./Siliciuro.md)
- [PVD](./PVD.md)
- [CVD](./CVD.md)
- [MOS](./MOS.md)
