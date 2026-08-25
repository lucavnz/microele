In microelettronica l'area di silicio è preziosa. Per realizzare una resistenza integrata possiamo utilizzare principalmente due approcci: il **polisilicio** oppure una **sacca drogata nel silicio**.

---

### 1. Il Resistore in Polisilicio e la Maschera di Siliciuro (SAB)

Il metodo più diffuso consiste nel depositare una striscia di polisilicio:
* **Layout a Serpentina:** per ottenere valori di resistenza elevati serve una grande lunghezza $L$. Per non sprecare area orizzontale, la pista viene ripiegata a zigzag (serpentina) per impacchettare molta lunghezza in poco spazio ($R = R_\square \cdot \frac{L}{W}$).
  👉 Vedi: [Difficoltà nel fare un componente ideale](./Difficolt%C3%A0%20nel%20fare%20un%20componente%20ideale.md) per i parassiti capacitivi tra le anse.
* **La maschera di blocco (*Silicide Block* / *SAB*):** di base, la fonderia deposita uno strato di [siliciuro metallico](./Siliciuro.md) su tutto il polisilicio e sulle aree di silicio "nudo" (Source/Drain) per abbattere le resistenze di contatto parassite.
  Per fare un resistore, è **obbligatorio usare una maschera specifica** che impedisca la formazione del siliciuro sul corpo della resistenza, altrimenti verrebbe cortocircuitata abbattendo il valore di $R$.

---

### 2. Il Resistore a Diffusione nel Substrato e la Non-Linearità

Un'alternativa è creare la resistenza direttamente dentro il silicio tramite una diffusione drogata (es. *N-Well* o sacca $N^+/P^+$):
* **La giunzione $pn$ parassita:** la sacca drogata forma inevitabilmente una giunzione $pn$ con il substrato circostante, circondata da una regione di svuotamento.
* **Modulazione della sezione e distorsione:** al variare delle tensioni applicate ai capi del resistore, la tensione inversa della giunzione $pn$ cambia $\implies$ la **regione di svuotamento si allarga o si restringe**, modulando la sezione utile di silicio in cui scorre la corrente.
* **Conclusione per l'analogico:** il valore di $R$ non è costante ma varia dinamicamente con il segnale applicato ($R(V)$ non lineare). Questo introduce **distorsione armonica**, motivo per cui nei circuiti analogici di precisione si evitano i resistori a diffusione e si preferisce il polisilicio non siliciurato.
  👉 Vedi: [Analogico non si scende di dimensioni](../Introduzione/Analogico%20non%20si%20scende%20di%20dimensioni.md) per i vincoli di linearità e distorsione nei circuiti analogici.

---

*Pagine correlate:*
- [Siliciuro](./Siliciuro.md)
- [MOS](./MOS.md)
- [Condensatori](./Condensatori.md)
- [Difficoltà nel fare un componente ideale](./Difficolt%C3%A0%20nel%20fare%20un%20componente%20ideale.md)
- [Analogico non si scende di dimensioni](../Introduzione/Analogico%20non%20si%20scende%20di%20dimensioni.md)
- [Wafer produzione](./Wafer%20produzione.md)