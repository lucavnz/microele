Il **breakdown** (o rottura inversa) è il fenomeno macroscopico in cui, superata una determinata tensione inversa critica $V_{BR}$, la corrente in un diodo a giunzione $PN$ cresce vertiginosamente in modo quasi verticale.

Fisicamente non esiste un solo tipo di rottura: il breakdown può innescarsi per **effetto tunnel (Zener)**, per **moltiplicazione a valanga**, oppure per la combinazione di entrambi.

---

### 1. Il Breakdown come Riferimento: Generatore di Tensione (Non di Corrente!)

Nel grafico $I(V)$ in inversa, la curva dopo $V_{BR}$ diventa praticamente una **linea retta verticale**:

```text
       I ^
         |
    ─────┼─────────> V
         |       |
         |       |
         | (Vz)  | 
  ───────┘       |
  In breakdown   |
  la linea è     |
  VERTICALE!     |
```

* **Cosa significa linea verticale?**  
  Significa che per enormi variazioni di corrente $I$ (es. da $1\text{ mA}$ a $50\text{ mA}$), la tensione ai capi del diodo **rimane inchiodata al valore di soglia $V_Z$**.
* La resistenza dinamica interna è quasi nulla:
  $$r_z = \frac{dV}{dI} \approx 0\ \Omega$$
* Un bipolo che mantiene una tensione rigorosamente costante ai suoi capi a prescindere dalla corrente imposta dal circuito esterno si comporta, a tutti gli effetti, come un **generatore ideale di tensione** (o una batteria di riferimento).

---

### 2. Diodo Normale vs Diodo Zener: Perché nei normali è distruttivo?

**Tutte le giunzioni $PN$ al mondo hanno una tensione di rottura inversa.** La differenza sta nello scopo e nel dimensionamento:

1. **Nel diodo normale (rettificatore / segnale):**
   * Il suo compito è fare da valvola unidirezionale bloccando le tensioni inverse. Se va in breakdown, la funzione circuitale fallisce.
   * **Distruzione termica (*Thermal Runaway*):** se un diodo normale progettato per reggere $400\text{ V}$ entra in breakdown senza una resistenza che limiti la corrente, con appena $2\text{ A}$ dissipa:
     $$P = V_{BR} \cdot I = 400\text{ V} \cdot 2\text{ A} = 800\text{ W}$$
     Centinaia di Watt concentrati in un millimetro quadrato di silicio causano la fusione istantanea del reticolo cristallino per effetto Joule.
2. **Nel diodo Zener:**
   * Il breakdown di per sé **non rompe i legami chimici né danneggia il silicio**; è solo un passaggio rapido di cariche. L'unico nemico è il calore.
   * Il diodo Zener viene **progettato appositamente per lavorare stabilmente in breakdown**: ha tensioni di rottura basse e controllate (es. $3.3\text{ V}$, $5.1\text{ V}$, $12\text{ V}$) e una geometria termica dimensionata per smaltire la potenza dissipata senza surriscaldarsi.
     👉 Approfondimento: [Resistenza termica](../Introduzione/Resistenza%20termica.md).

---

### 3. Valanga vs Tunnel: I Due Motori Microscopici

Convenzionalmente chiamiamo "diodo Zener" qualunque componente stabilizzatore di tensione, ma a livello microscopico i meccanismi fisici sono due e dipendono dal drogaggio:

```text
Drogaggio giunzione:   ALTISSIMO (p+ / n+)                  BASSO / MEDIO
Spessore SCR (W):      Sottilissimo (< 10 nm)               Largo (micron)
                          │                                      │
Meccanismo:            TUNNEL (Zener)                       VALANGA (Impact Ionization)
                          │                                      │
Tensione di rottura:   V_BR < 4 V                           V_BR > 6 V
```

#### A. Effetto Tunnel (Rottura Zener pura, $V_{BR} < 4\text{ V}$)
* **Dove avviene:** in giunzioni iper-drogate su entrambi i lati ($p^+/n^+$).
* **Fisica del fenomeno:** la zona di svuotamento $W$ è nanometrica ($W < 10\text{ nm}$). Il campo elettrico supera $10^6\text{ V/cm}$. La banda di valenza del lato $P$ si allinea con la banda di conduzione del lato $N$: gli elettroni attraversano direttamente la barriera proibita per **tunneling quantistico**.
* **Perché non c'è valanga qui?** L'elettrone non ha lo spazio fisico sufficiente (il cammino libero medio) per accelerare e urtare gli atomi: scatta prima l'effetto tunnel.

#### B. Moltiplicazione a Valanga (*Impact Ionization*, $V_{BR} > 6\text{ V}$)
* **Dove avviene:** in giunzioni con drogaggio medio o basso (zona svuotata $W$ più larga).
* **Fisica del fenomeno:** la barriera è troppo spessa perché le cariche possano compiere il salto quantistico. Tuttavia, gli elettroni della debole corrente inversa hanno molto spazio per accelerare sotto l'azione del campo elettrico. Quando acquistano energia cinetica $E_{cin} \ge 1.5 E_g$, **urtano violentemente gli atomi del reticolo**, scalzando elettroni di valenza e generando nuove coppie elettrone-lacuna. I nuovi portatori accelerano a loro volta creando una reazione a catena (*moltiplicazione a valanga* con coefficiente $M \to \infty$).
* **Effetto Curvatura 2D (*Junction Curvature*):** nei diodi planari integrati, la diffusione laterale sotto l'ossido crea bordi curvi ($r_j$). Le linee di campo elettrico convergono sugli spigoli per effetto punta, facendo scattare la valanga a una tensione inferiore rispetto al caso teorico 1D ($V_{BR, 2D} < V_{BR, 1D}$).
  👉 Vedi: [Diodo](./Diodo.md) (Sezione Effetti di Seconda Dimensione).

---

### 4. La Fascia a 5 V: Coesistenza e Deriva Termica Nulla ($TC \approx 0$)

I due fenomeni fisici rispondono alla temperatura in modo esattamente opposto:

| Meccanismo | All'aumentare della temperatura $T$ | Coefficiente Termico ($TC$) | Causa fisica |
| :--- | :--- | :--- | :--- |
| **Tunnel (Zener)** | Il bandgap $E_g$ si restringe leggermente $\implies$ tunneling facilitato $\implies$ breakdown a tensione minore | **Negativo** ($TC < 0$, $\approx -2\text{ mV/}^\circ\text{C}$) | Restringimento termico del bandgap |
| **Valanga** | Aumentano le vibrazioni reticolari (fononi) $\implies$ più urti elastici casuali $\implies$ le cariche perdono energia e serve un campo più forte | **Positivo** ($TC > 0$, $\approx +2\text{ mV/}^\circ\text{C}$) | Riduzione del cammino libero medio per scattering |

#### Il punto a coefficiente nullo ($5.1\text{ V} - 5.6\text{ V}$):
Attorno a $5.1\text{--}5.6\text{ V}$ la barriera è sia abbastanza stretta per il tunneling sia abbastanza estesa per l'ionizzazione per impatto: **entrambi i fenomeni scattano insieme**.  
Il coefficiente negativo del Tunnel e quello positivo della Valanga **si cancellano a vicenda**, generando una tensione di riferimento eccezionalmente stabile rispetto ai cambi termici ($TC \approx 0\text{ ppm/}^\circ\text{C}$).

---

*Pagine correlate:*
- [Diodo](./Diodo.md)
- [BJT](./BJT.md)
- [Difficoltà nel fare un componente ideale](./Difficolt%C3%A0%20nel%20fare%20un%20componente%20ideale.md)
- [Resistenza termica](../Introduzione/Resistenza%20termica.md)
- [Analogico non si scende di dimensioni](../Introduzione/Analogico%20non%20si%20scende%20di%20dimensioni.md)
