# Sintesi delle Lezioni: Rail-to-Rail, Fully-Differential, CMFB ed Immunità alle EMI

Questo documento raccoglie la sintesi concettuale delle discussioni e delle dispense della Prof.ssa Anna Richelli (`richelli_rail_to_rail_5.pdf` e `richelli_CMFB_rail_6.pdf`).

Gli appunti completi e dettagliati sono stati organizzati e integrati nelle rispettive sezioni della cartella `Microelettronica/Dispositivi e Componenti/`:

---

### 1. [Amplificatori Operazionali Rail-to-Rail](../Microelettronica/Dispositivi%20e%20Componenti/Amplificatori%20Rail-to-Rail.md)
* **Il problema dell'ICMR a bassa tensione:** La coppia differenziale NMOS si spegne vicino a $V_{SS}$ ($V_{in,CM} < V_{SS} + 1.1\,\text{V}$), mentre la coppia PMOS si spegne vicino a $V_{DD}$ ($V_{in,CM} > V_{DD} - 1.1\,\text{V}$). A basse tensioni d'alimentazione (es. $1.8\,\text{V}$) nessuna delle due copre l'intervallo necessario per un inseguitore unitario (buffer $V_{out} = V_{in}$).
* **La doppia coppia complementare:** Si mettono in parallelo una coppia NMOS e una PMOS con ingressi condivisi.
* **Il raddoppio di $g_m$ a centro scala:** Nella regione intermedia conducono entrambe $\implies g_{m,\text{tot}} \approx 2g_m$. Questo raddoppia la banda a guadagno unitario ($GBW = g_m / 2\pi C_c$), fa crollare il margine di fase (rischio oscillazioni e instabilità) e genera forte distorsione armonica.
* **Equalizzatore di transconduttanza ($g_m$ Equalizer):** Un circuito di monitoraggio misura la corrente condotta e modula i generatori di coda affinché la somma delle correnti (o la somma delle radici) resti costante ($I_n + I_p \approx \text{costante}$).
* **Folded Cascode come ambiente naturale:** Le correnti delle due coppie d'ingresso vengono iniettate direttamente nei nodi di sorgente a bassa impedenza ($1/g_m$) dei cascode PMOS (in alto) e NMOS (in basso), sommandosi sull'uscita ad alta impedenza senza creare poli parassiti lenti.

👉 Schemi, equazioni e analisi completa: [Amplificatori Rail-to-Rail](../Microelettronica/Dispositivi%20e%20Componenti/Amplificatori%20Rail-to-Rail.md)

---

### 2. [Amplificatori Fully-Differential e CMFB](../Microelettronica/Dispositivi%20e%20Componenti/Amplificatori%20Fully-Differential%20e%20CMFB.md)
* **Definizione e vantaggi:** 2 ingressi e 2 uscite sfasate di $180^\circ$. Raddoppio dell'escursione dinamica utile ($2 \times (V_{DD} - V_{SS})$ ideale, ideale per low-power), reiezione intrinseca dei disturbi di modo comune (PSRR, substrato) e cancellazione delle armoniche pari.
* **Perché il CMFB è obbligatorio:** A differenza dei circuiti single-ended, non vi sono carichi a diodo che fissano il punto di lavoro DC. Entrambe le uscite sono nodi ad altissima impedenza ($r_o$): qualunque micro-discrepanza di corrente $\Delta I = I_{\text{top}} - I_{\text{bottom}}$ carica i nodi e fa sbattere le uscite contro $V_{DD}$ o massa, portando i MOS in triodo o interdizione e azzerando il guadagno. La retroazione esterna differenziale non controlla il modo comune.
* **Circuiti CMFB:**
  * *Passivo con MOS in zona lineare:* Due transistor in triodo fungono da resistori variabili $R_{\text{eq}} \propto 1/(V_{OUT,CM} - V_{th})$. Se $V_{OUT,CM}$ sale, $R_{\text{eq}}$ scende, la corrente NMOS di scarica verso massa aumenta e l'uscita viene riportata giù.
  * *Attivo con amplificatore d'errore:* Una coppia di sensing misura il modo comune e modula i Gate dei generatori superiori o inferiori.
* **Uso single-ended per simmetria:** Usare una sola uscita di un Fully-Differential garantisce che internamente il circuito resti speculare al $100\%$, eliminando le asimmetrie di Slew Rate.

👉 Schemi e anelli di controllo: [Amplificatori Fully-Differential e CMFB](../Microelettronica/Dispositivi%20e%20Componenti/Amplificatori%20Fully-Differential%20e%20CMFB.md)

---

### 3. [Immunità alle EMI e Slew Rate Asimmetrico](../Microelettronica/Dispositivi%20e%20Componenti/Immunit%C3%A0%20alle%20EMI%20e%20Slew%20Rate%20Asimmetrico.md)
* **Il problema delle EMI ad alta frequenza (fuori banda):** Sebbene le frequenze dei disturbi RF (centinaia di MHz - GHz) siano fuori dalla banda passante dell'Op-Amp, la caratteristica quadratica non lineare del MOS agisce da **raddrizzatore d'inviluppo**, convertendo il disturbo in una corrente continua parassita $\Delta I_{\text{DC}} \propto V_m^2$ che sposta permanentemente il punto di riposo DC (**offset continuo**). Esperimento del Source Follower: shift permanente da $0.77\,\text{V}$ a $0.90\,\text{V}$ ($+130\,\text{mV}$).
* **Causa radice: Slew Rate Asimmetrico ($SR^+ \neq SR^-$):**
  * *Percorso del segnale:* In discesa la corrente scarica direttamente dal transistor d'ingresso verso massa (percorso a 0 ritardi); in salita deve attraversare lo specchio a diodo superiore, scaricando prima la capacità parassita del nodo di Gate $\tau_{\text{mirror}} \approx C_{p2}/g_m \implies SR^+ < SR^-$.
  * *Secondo stadio:* In salita la corrente massima è limitata dal generatore fisso $I_{\text{bias}}$, in discesa il transistor di pilotaggio può essere sovrapilotato conducendo correnti impulsive molto superiori.
  * *Capacità non lineari:* Le capacità di giunzione e Miller variano continuamente tra salita e discesa.
* **Il punto di equilibrio dell'offset:** L'offset non sale all'infinito verso $V_{DD}$ perché in anello chiuso la controreazione negativa ($V_{id} < 0$) e le correnti di fuga resistive bilanciano la carica pompata dall'EMI. Nel $\mu\text{A741}$ l'equilibrio si stabilizza a un disastroso offset di oltre $600\,\text{mV}$.
* **La soluzione Folded Cascode Fully-Differential:** Struttura perfettamente simmetrica con $SR(+) = 21.3\,\text{V}/\mu\text{s}$ e $SR(-) = 21.6\,\text{V}/\mu\text{s}$ (scarto $1.4\%$).
* **Regole di Layout Simmetrico:**
  * *Centroide comune per resistori:* Strisce alternate a pettine ($R_2 - R_1 - R_3 \dots$) per allineare i baricentri termici e di drogaggio.
  * *Centroide comune per la coppia differenziale:* Transistor d'ingresso a scacchiera 2D ($A_1-B_1 / B_2-A_2$) con Guard Ring verso il substrato.
  * *Transistor interdigitati e DUMMY:* Transistor suddivisi in dita con transistor fittizi esterni per proteggere le dita attive dall'over-etching di bordo.
* **Risultati sperimentali (AMS $0.8\,\mu\text{m}$):** Sotto disturbo RF fino a $10\,\text{GHz}$, il $\mu\text{A741}$ genera fino a $600\,\text{mV}$ di offset, mentre l'Op-Amp simmetrico resta piatto a **$0\,\text{mV}$**.

👉 Approfondimento con formule, grafici e layout: [Immunità alle EMI e Slew Rate Asimmetrico](../Microelettronica/Dispositivi%20e%20Componenti/Immunit%C3%A0%20alle%20EMI%20e%20Slew%20Rate%20Asimmetrico.md)

---

### 4. [Riferimenti di Corrente e Circuiti di Start-Up](../Microelettronica/Dispositivi%20e%20Componenti/Riferimenti%20di%20Corrente%20e%20Start-Up.md)
* **La necessità di circuiti di bias su silicio:** In un integrato non esistono generatori ideali di corrente; bisogna ricavarli da $V_{DD}$ e GND garantendo robustezza PVT (Process, Voltage, Temperature).
* **I Soluzione (Resistenza su $V_{DD}$):** Fallisce per forte sensibilità all'alimentazione ($\Delta I \propto \Delta V_{DD}$, PSRR pessimo) e dipendenza da $V_{th}$.
* **II Soluzione (Autopolarizzazione ad anello chiuso):** Due specchi incrociati NMOS/PMOS. Fallisce perché il sistema è indeterminato ($I_{out} = K I_{ref}$): le rette coincidono e il punto di riposo non è fissato.
* **III Soluzione (Riferimento Widlar MOS / Constant-$g_m$):** Inserimento di una resistenza $R_S$ di degenerazione sul source del transistor più largo ($K \cdot W/L$).
  * *Formula:* $I_{out} = \frac{2}{\mu C_{ox}(W/L)_1 R_S^2}\left(1 - \frac{1}{\sqrt{K}}\right)^2$. Indipendente da $V_{DD}$ al 1° ordine!
  * *Transconduttanza stabilizzata:* $g_{m1} = \frac{2}{R_S}(1 - 1/\sqrt{K})$, indipendente dai parametri tecnologici ($\mu, C_{ox}, V_{th}$).
* **Non-idealità ed Effetto Body:** In tecnologia con substrato p comune, la degenerazione su NMOS subisce l'effetto body ($V_{SB} > 0$), mentre su PMOS ogni transistor ha la propria n-well e il body può essere connesso al source ($V_{BS}=0$), annullando l'effetto body.
* **Il Problema dello Start-Up e Transistor $M_5$:** L'anello chiuso ammette il punto di equilibrio spuro a corrente zero ($I=0$, tutti i MOS interdetti). Si inserisce un NMOS a diodo $M_5$ tra i gate PMOS e i gate NMOS: all'accensione inietta corrente forzando l'avvio, a regime la sua $V_{GS5}$ scende sotto soglia e si spegne automaticamente a consumo zero.

👉 Schemi, dimostrazione analitica e circuito di start-up: [Riferimenti di Corrente e Circuiti di Start-Up](../Microelettronica/Dispositivi%20e%20Componenti/Riferimenti%20di%20Corrente%20e%20Start-Up.md)

---

*Pagine correlate del Vault:*
- [Riferimenti di Corrente e Circuiti di Start-Up](../Microelettronica/Dispositivi%20e%20Componenti/Riferimenti%20di%20Corrente%20e%20Start-Up.md)
- [Amplificatori Rail-to-Rail](../Microelettronica/Dispositivi%20e%20Componenti/Amplificatori%20Rail-to-Rail.md)
- [Amplificatori Fully-Differential e CMFB](../Microelettronica/Dispositivi%20e%20Componenti/Amplificatori%20Fully-Differential%20e%20CMFB.md)
- [Immunità alle EMI e Slew Rate Asimmetrico](../Microelettronica/Dispositivi%20e%20Componenti/Immunit%C3%A0%20alle%20EMI%20e%20Slew%20Rate%20Asimmetrico.md)
- [Folded Cascode e Recycling](../Microelettronica/Dispositivi%20e%20Componenti/Folded%20Cascode%20e%20Recycling.md)
- [Coppia Differenziale e Cascode Telescopico](../Microelettronica/Dispositivi%20e%20Componenti/Coppia%20Differenziale%20e%20Cascode%20Telescopico.md)
- [Layout e Tecniche di Progettazione dei MOS](../Microelettronica/Dispositivi%20e%20Componenti/Layout%20e%20Tecniche%20di%20Progettazione%20dei%20MOS.md)
- [Matching e Variabilita nei Componenti Integrati](../Microelettronica/Dispositivi%20e%20Componenti/Matching%20e%20Variabilita%20nei%20Componenti%20Integrati.md)
- [Integrati protetti da interferenze](../Microelettronica/Scaling%20e%20Limiti%20Fisici/Integrati%20protetti%20da%20interferenze.md)