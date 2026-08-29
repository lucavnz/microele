L'**elettromigrazione** è il fenomeno per cui un'eccessiva densità di corrente provoca lo spostamento fisico graduale degli atomi del conduttore. Non è l'energia del singolo elettrone a muovere il metallo, ma il cosiddetto **vento elettronico** (*electron wind*): l'urto continuo di miliardi di elettroni contro gli ioni del reticolo metallico.

---

### 1. I 3 Limiti Fisici alla Densità di Corrente nelle Piste

Non è possibile aumentare a piacere la corrente nelle interconnessioni integrate per 3 vincoli fisici fondamentali:
1. **Caduta di tensione ohmica ($IR$):** la resistenza finita delle linee metalliche produce cadute di potenziale che distorcono i livelli logici ed eliminano l'equipotenzialità delle reti di alimentazione ($V_{DD}$ e massa).
2. **Elettromigrazione:** usura cumulativa e trasporto di materia che compromettono l'affidabilità a lungo termine del circuito.
3. **Dissipazione termica (Effetto Joule $\propto J^2$):** il riscaldamento locale crea stress meccanico da dilatazione, accelera esponenzialmente l'elettromigrazione e causa l'ulteriore diffusione termica indesiderata dei droganti nel silicio.

---

### 2. La Legge di Black e il Vero Significato di $J_{\text{max}}$

La durata nel tempo di una pista metallica prima di rompersi per elettromigrazione è quantificata dalla **Legge di Black**:

$$\text{MTTF} = \frac{A}{J^n} \exp\left(\frac{E_a}{k_B T}\right)$$

Dove:
* $\text{MTTF}$ (*Mean Time To Failure*): è il **tempo medio prima del guasto** della pista metallica.
* $J = \frac{I}{\text{Area}}$: è la **densità di corrente** ($\text{A/cm}^2$).
* $n \approx 2$: esponente empirico legato sia all'urto del vento elettronico sia all'effetto Joule ($\Delta T \propto J^2$).
* $E_a$: è l'**Energia di Attivazione per l'autodiffusione atomica** (espressa in $\text{eV}$). Rappresenta la barriera energetica che un atomo deve superare per staccarsi dalla propria posizione nel reticolo metallico.
* $k_B T$: energia termica disponibile.

#### Cosa rappresenta davvero $J_{\text{max}}$?
L'elettromigrazione non è una rottura istantanea per fusione, ma un processo di **usura progressiva nel tempo**:
* La fonderia fissa un target di affidabilità del prodotto (es. $\text{MTTF} \ge 10\text{–}20\text{ anni}$ a $105^\circ\text{C}$ con tasso di guasto $< 0.1\%$).
* Invertendo la Legge di Black, si ricava la **$J_{\text{max}}$**: la massima densità di corrente consentita dalle regole di layout (DRC) per garantire quella specifica vita utile. Se si supera $J_{\text{max}}$, il circuito non fonde all'istante, ma si romperà dopo pochi mesi anziché dopo anni.
* **Unità pratica di layout ($\text{mA}/\mu\text{m}$):** poiché lo spessore $H$ della metallizzazione è fissato dal processo tecnologico, le fonderie esprimono spesso $J_{\text{max}}$ come corrente massima per unità di larghezza (es. per l'alluminio $J_{\text{max}} \approx 1\text{ mA}/\mu\text{m} \implies$ per portare $3\text{ mA}$ serve una pista larga almeno $W = 3\,\mu\text{m}$).

I guasti provocati dall'elettromigrazione sono di due tipi:
1. **Circuito Aperto (CA - *Voids*):** a monte del flusso elettronico gli atomi vengono spazzati via creando cavità che finiscono per spezzare la linea.
2. **Cortocircuito (CC - *Hillocks/Whiskers*):** a valle gli atomi si accumulano creando cumuli e aghi metallici che perforano il dielettrico intermetallico toccando piste adiacenti.

---

### 3. Alluminio vs Rame: Il Ruolo dell'Autodiffusione Atomica

Perché il Rame ($\text{Cu}$) ha sostituito l'Alluminio ($\text{Al}$) nelle tecnologie avanzate?

La velocità con cui gli atomi del metallo si muovono lungo la pista sotto la spinta della corrente è regolata dal **coefficiente di autodiffusione**:
$$D = D_0 \exp\left(-\frac{E_a}{k_B T}\right)$$

* **Alluminio ($\text{Al}$):** fonde a $660^\circ\text{C}$ e ha legami metallici deboli con bassa energia di attivazione ($E_a \approx 0.5\text{ eV}$). Gli atomi di alluminio scivolano e diffondono con estrema facilità lungo i bordi di grano a temperature ordinarie ($80\text{–}100^\circ\text{C}$) e basse correnti.
  * Per mitigare il problema nelle vecchie tecnologie si usava una **lega $\text{Al:Cu } 4\%$**: le piccole quantità di rame precipitano sui bordi di grano dell'alluminio bloccando lo scivolamento degli atomi.
* **Rame ($\text{Cu}$):** fonde a $1085^\circ\text{C}$ e possiede legami molto più forti ed energetici ($E_a \approx 1.25\text{ eV}$). 
  * Inserendo l'energia di attivazione nell'esponenziale di Arrhenius, gli atomi di rame **diffondono lungo la pista 3–4 ordini di grandezza più lentamente ($1.000\text{–}10.000$ volte più lentamente)** rispetto all'alluminio.
  * Il rame è quindi quasi immune all'elettromigrazione fino a oltre $250^\circ\text{C}$.

> ⚠️ **Distinzione Fondamentale sulla "Diffusione":**
> 1. **Autodiffusione del Rame nel proprio reticolo metallico:** è lentissima ($10^4$ volte più lenta di $\text{Al}$) $\implies$ **Pregio Straordinario** contro l'elettromigrazione.
> 2. **Diffusione del Rame nel Silicio e nel $\text{SiO}_2$:** è rapidissima $\implies$ **Grave Rischio di Contaminazione** (il rame agisce da veleno).

---

### 4. Il Collo di Bottiglia di Contatti e Vias

Nei fori di contatto verticali tra metalli ([Vias]Vias](./Vias.md)), la corrente compie una svolta a $90^\circ$ e deve risalire pareti sottili, concentrandosi sul perimetro:
* La densità perimetrale massima è molto limitata ($J_{\text{MAX, perim}} \approx 0.05\text{ mA}/\mu\text{m}$).
* La massima corrente sopportabile da un singolo via è limitata a circa **$I_{\text{max}} \approx 0.4\text{ mA/contatto}$**.
* **Regola di Layout:** per trasportare correnti elevate (es. piste di alimentazione $V_{DD}$ o nodi di potenza) è vietato fare affidamento su un solo via allargato; si impiegano sempre **matrici di tanti vias in parallelo** (*Via Arrays* $3\times 3, 4\times 4, \dots$).
  👉 Vedi: [Vias]Vias](./Vias.md) per l'anatomia dei contatti verticali e la gestione dello stress termomeccanico.

---

### 5. Perché i Metalli Elettromigrano e il Silicio (anche Degenere) NO?

La differenza risiede nella **natura chimica del legame**:

* **Nei Metalli (Legame Metallico):**
  Gli ioni positivi sono immersi in un "mare" di elettroni delocalizzati. Il legame è **non direzionale**: gli ioni possono scivolare facilmente se spinti dal vento elettronico ($E_a \approx 0.5 - 1.25\text{ eV}$). Metalli a punto di fusione altissimo come il Tungsteno ($3422^\circ\text{C}$) hanno legami fortissimi ($E_a > 1.6\text{ eV}$) e sono impiegati proprio nei contatti verticali per questa immunità.
* **Nel Silicio (Legame Covalente $sp^3$):**
  Gli atomi di silicio sono bloccati in un reticolo a diamante con legami covalenti rigidi e fortemente direzionali ($E_a \approx 4 - 5\text{ eV}$).
  *Anche se droghiamo il silicio fino a farlo diventare **degenere** ($N^+$ o $P^+$)*, la conduzione aumenta ma la struttura fisica rimane un cristallo covalente: il vento elettronico rimbalza sugli atomi senza riuscire a spostarli.

---

### 6. Tossicità dei Metalli a Contatto con il Silicio

Mettere metalli puri a contatto diretto con il silicio causa gravi degradazioni:

* **Alluminio e lo Spiking (*Junction Spiking*):**
  L'alluminio fonde a $660^\circ\text{C}$ e a temperature di processo ($400^\circ\text{C}-450^\circ\text{C}$) il silicio si scioglie nell'alluminio ($\approx 1\%$). Il silicio migra nella pista lasciando cavità che l'alluminio riempie formando "chiodi" verticali (*spikes*) che cortocircuitano le giunzioni sottili di Source e Drain.
* **Rame: Il "Veleno Assoluto" per il Silicio:**
  Il rame diffonde con estrema rapidità nel silicio anche a basse temperature ($100^\circ\text{C}$) e crea stati energetici a centro banda (*deep-level traps*). Questi stati agiscono come centri di ricombinazione micidiali, **azzerando il tempo di vita dei portatori minoritari ($\tau \to 0$)** e facendo esplodere la corrente di perdita da spento ($I_{\text{off}}$).
  Per poter usare il rame è indispensabile rivestire ogni trincea con barriere anti-diffusione impermeabili (come nitruro di tantalio $\text{TaN}$ o nitruro di titanio $\text{TiN}$) tramite processo *Damascene*.

---

*Pagine correlate:*
- [Vias]Vias](./Vias.md)
- [Siliciuro]Siliciuro](./Siliciuro.md)
- [Resistore]Resistore](../Dispositivi%20e%20Componenti/Resistore.md)
- [PVD]PVD](./PVD.md)
- [CVD]CVD](./CVD.md)
- [MOS]MOS](../Dispositivi%20e%20Componenti/MOS.md)
- [Difficoltà nel fare un componente ideale]Difficoltà nel fare un componente ideale](../Scaling%20e%20Limiti%20Fisici/Difficolt%C3%A0%20nel%20fare%20un%20componente%20ideale.md)
