# Resistenza Termica nei Microchip

Il calore generato dai transistor nel silicio ($P_d$) deve scappare verso l'esterno per evitare che la temperatura della giunzione superi il limite massimo $T_{j,max}$.

Per l'analogia con la legge di Ohm termica:
$$\Delta T = R_{th} \cdot P_d$$

---

### 1. Le resistenze del chip "nudo" (Senza Dissipatore)

* **$R_{th,j-c}$ (*Junction-to-Case*):** rappresenta la "fatica" che fa il calore per passare dal silicio interno della giunzione fino alla superficie esterna del case. È **intrinseca** al componente (fissata dal costruttore nel datasheet) e dall'esterno non possiamo farci nulla.
* **$R_{th,c-a}$ (*Case-to-Ambient*):** è la fatica che fa il calore per passare dal case all'aria dell'ambiente in cui stiamo operando. Essendo il case piccolo, scambia malissimo ed è un valore **altissimo**.

In questa configurazione:
$$R_{th,tot} = R_{th,j-c} + R_{th,c-a}$$
$$T_j = T_a + (R_{th,j-c} + R_{th,c-a}) \cdot P_d$$

---

### 2. Come interviene il Dissipatore?

Il dissipatore **sostituisce e bypassa $R_{th,c-a}$**, creando una corsia preferenziale a bassissima resistenza:

* **$R_{th,c-s}$ (*Case-to-Sink*):** è la resistenza che incontra il calore per passare dalla faccia del case al dissipatore. Si mette la pasta termica proprio per riempire le micro-fessure d'aria e renderla trascurabile.
* **$R_{th,s-a}$ (*Sink-to-Ambient*):** è la resistenza per passare dalle alette del dissipatore all'aria dell'ambiente (bassissima grazie all'enorme superficie metallica di scambio).

Con il dissipatore, la resistenza totale diventa:
$$R_{th,tot} = R_{th,j-c} + R_{th,c-s} + R_{th,s-a}$$
$$T_j = T_a + (R_{th,j-c} + R_{th,c-s} + R_{th,s-a}) \cdot P_d$$