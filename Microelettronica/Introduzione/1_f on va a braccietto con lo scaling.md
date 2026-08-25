All'interfaccia tra ossido e canale ci sono delle trappole energetiche (*traps*). Alcuni elettroni ci cadono dentro e dopo un certo tempo vengono rilasciati: questo genera il **rumore $1/f$** (flicker noise).

Questo fenomeno porta a continue fluttuazioni di $I_D$ e di $V_{th}$.

---

### Perché se rimpicciolisco il transistor il rumore $1/f$ peggiora?

$V_{th}$ fluttua... ma perché fluttua? Tra canale e gate c'è la capacità di gate $C_G = C_{ox} \cdot W \cdot L$.

Delle cariche cadono nelle trappole $\to$ si crea una variazione di carica $\Delta Q$. Per la legge della capacità:
$$\Delta Q = C_G \cdot \Delta V \implies \Delta V_{th} = \frac{\Delta Q}{C_G} = \frac{\Delta Q}{C_{ox} \cdot W \cdot L}$$

**Perché quel $\Delta V$ è proprio $\Delta V_{th}$?**
Sostanzialmente per accendere il canale conta l'overdrive $(V_{gs} - V_{th})$. Avere un $\Delta V_{th}$ che fluttua ha lo stesso identico effetto di un $\Delta V_{gs}$ applicato all'ingresso che mi rema contro.

Quindi elettrostaticamente:
* **Transistor gigante:** capacità $C_G$ grande $\implies \Delta V_{th}$ piccolo (disturbo trascurabile).
* **Transistor piccolo:** capacità $C_G$ minuscola $\implies \Delta V_{th}$ grande (disturbo enorme).

---

### Il punto di vista statistico (perché non scala uguale in percentuale?)

Possiamo vederla anche così:
* In un **transistor gigante**, ci sono tantissimi elettroni che scorrono nel canale. Se anche un po' di cariche cadono dentro... sti cazzi: sono tantissimi, in percentuale non è successo sostanzialmente nulla.
* Se invece ho un **piccolo corridoio** con $10$ elettroni e $1$ ci cade... disastro!

**Perché accade questo se aumentando l'area aumentano anche le trappole?**
Perché le trappole **non lavorano in modo sincronizzato**, sono indipendenti e casuali:
* Il numero medio di trappole cresce con l'area ($N \propto \text{Area}$).
* La fluttuazione casuale di carica $\Delta Q$ cresce solo con la radice: $\Delta Q \propto \sqrt{\text{Area}}$.
* La capacità di gate cresce linearmente al 100%: $C_G \propto \text{Area}$.

Mettendo insieme i due effetti:
$$\Delta V_{th} = \frac{\Delta Q}{C_G} \propto \frac{\sqrt{\text{Area}}}{\text{Area}} = \frac{1}{\sqrt{\text{Area}}}$$

E per la potenza del rumore (che va con il quadrato della tensione):
$$S_v(f) \propto (\Delta V_{th})^2 \propto \frac{1}{\text{Area}} = \frac{1}{W \cdot L}$$