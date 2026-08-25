Mettiamo da parte i paroloni dei libri e guardiamo **la fisica nuda e cruda del circuito**:

La risposta secca a tutte e tre le tue domande è:

1. **Compare carica sul metallo del Gate?** $\implies$ **SÌ.**
2. **Cambia il potenziale sul metallo del Gate?** $\implies$ **NO! Resta inchiodato a quello che decide il circuito.**
3. **Cambia la tensione di soglia del transistor?** $\implies$ **NO! Resta fissa e perfetta (Zero DIBL).**

Adesso ti spiego **PERCHÉ** in modo chiarissimo, senza giri di parole.

---

### 1. Perché il potenziale sul Gate NON cambia?

Immagina il Gate: **non è un pezzo di metallo isolato che galleggia nell'aria!**
Il Gate è collegato con una pista di rame a un **generatore di tensione esterno** (la batteria, l'alimentazione, o la porta logica precedente che lo sta pilotando).

```
          GENERATORE ESTERNO (Driver / Batteria)
               ┌──────────┐
               │ V_G = 0V │  ◄── Generatore a BASSA IMPEDENZA (fissa il potenziale)
               └────┬─────┘
                    │  Pista Metallica
                    │
           ═════════▼═════════  PIASTRA DEL GATE (Metallo)
           ░░░░░░░░░░░░░░░░░░░  Ossido di Gate (Isolante)
           ───────────────────  Canale (Silicio)
```

Un generatore di tensione ideale è un **serbatoio infinito di cariche**:
* Quando il Drain va a $V_{DD}$ (carica positiva), richiama cariche negative verso il Gate.
* Da dove arrivano queste cariche negative? **Le manda all'istante il generatore esterno lungo il filo!**
* Il generatore spinge elettroni sul metallo del Gate per fare in modo che **la tensione del Gate resti ESATTAMENTE a $0\text{ V}$**.
* **Risultato:** Sul metallo del Gate *compare della carica* ($Q = C_{gd} \cdot V_D$), ma **la tensione $V_G$ NON cambia di un singolo millivolt** perché il generatore la tiene bloccata!

> **Se il Gate fosse staccato (flottante nel vuoto):** allora sì, quella carica farebbe salire il potenziale del Gate.
> **Ma nei circuiti reali il Gate è sempre attaccato al suo driver**, quindi il suo potenziale è **INCHIODATO** a quello che dice il circuito.

---

### 2. Perché allora diciamo che la soglia NON cambia (Zero DIBL)?

Che cos'è la **tensione di soglia ($V_{th}$)**?
La soglia è: *"Quanti Volt devo applicare con il generatore sul Gate per riuscire ad accendere il canale?"*

Facciamo il confronto tra Bulk ed FD-SOI:

#### Nel BULK (Perché la soglia cambia con il DIBL):
* Le linee di campo del Drain viaggiano **sotto il Gate**, nel fondo del silicio, e vanno a toccare il Source.
* Il Drain abbassa la barriera del Source dal basso.
* Quindi al generatore esterno basta mettere meno tensione sul Gate (es. $0.2\text{ V}$ invece di $0.5\text{ V}$) per accendere il canale. 
* **La soglia è scesa per colpa del Drain ($V_{th} \downarrow$, DIBL)!**

#### Nell'FD-SOI (Perché la soglia NON cambia):
* Le linee di campo del Drain cercano di viaggiare verso il Source, ma sbattono contro la piastra del Gate (che sta a $0\text{ V}$) e contro il Back-Gate (che sta a massa).
* Il Gate metallico **mangia e neutralizza tutte le linee di campo del Drain** assorbendole sulla sua superficie.
* **Nessuna linea di campo del Drain riesce a raggiungere il Source!**
* Il Source non sente minimamente la presenza della tensione di Drain.
* Per accendere il canale, il generatore esterno deve per forza mettere i suoi soliti $0.5\text{ V}$ completi.
* **La soglia $V_{th}$ resta IDENTICA e NON SCENDE al variare di $V_{DD}$ (Zero DIBL)!**

---

### Riassunto in 3 Punti:

1. **Il Drain prova a tirare su il potenziale:** emette linee di campo elettrico.
2. **Il Gate fa da scudo (Gabbia di Faraday):** intercetta queste linee e, grazie al generatore esterno che lo alimenta, assorbe le cariche necessarie mantenendo la sua tensione rigorosamente costante.
3. **Il Source è protetto al 100%:** il Drain non può abbassargli la barriera, e la soglia $V_{th}$ del transistor rimane fissa e stabile.