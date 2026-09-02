In microelettronica l'area di silicio è preziosa. Per realizzare una resistenza integrata possiamo utilizzare principalmente due approcci: il **polisilicio** oppure una **sacca drogata nel silicio**.

---

### 1. Il Resistore in Polisilicio e la Maschera di Siliciuro (SAB)

Il metodo più diffuso consiste nel depositare una striscia di polisilicio:
* **Layout a Serpentina:** per ottenere valori di resistenza elevati serve una grande lunghezza $L$. Per non sprecare area orizzontale, la pista viene ripiegata a zigzag (serpentina) per impacchettare molta lunghezza in poco spazio ($R = R_\square \cdot \frac{L}{W}$).
  👉 Vedi: [Difficoltà nel fare un componente ideale](../Scaling%20e%20Limiti%20Fisici/Difficolt%C3%A0%20nel%20fare%20un%20componente%20ideale.md) per i parassiti capacitivi tra le anse.
* **La maschera di blocco (*Silicide Block* / *SAB*):** di base, la fonderia deposita uno strato di [siliciuro metallico](../Tecnologia%20e%20Fabbricazione/Siliciuro.md) su tutto il polisilicio e sulle aree di silicio "nudo" (Source/Drain) per abbattere le resistenze di contatto parassite.
  Per fare un resistore, è **obbligatorio usare una maschera specifica** che impedisca la formazione del siliciuro sul corpo della resistenza, altrimenti verrebbe cortocircuitata abbattendo il valore di $R$.

---

### 2. L'Effetto degli Angoli nel Layout (Raccordi a $90^\circ$ vs $45^\circ$)

Quando la pista del resistore viene ripiegata a serpentina, la corrente non fluisce in modo uniforme attraverso gli spigoli:
* **Addensamento di corrente (*Current Crowding*):** la corrente "taglia la curva" concentrandosi sullo spigolo interno (percorso a minore impedenza), mentre lo spigolo esterno resta una zona quasi inattiva.
  * Per un angolo a $90^\circ$, il rapporto $\frac{J_{\text{max}}}{J_{\text{min}}} \approx 70$.
  * Per un angolo a $45^\circ$, il rapporto scende a $\frac{J_{\text{max}}}{J_{\text{min}}} \approx 8$.
  👉 Vedi: [Elettromigrazione e tossicità dei metalli](../Tecnologia%20e%20Fabbricazione/Elettromigrazione%20e%20tossicit%C3%A0%20dei%20metalli.md) per i rischi di rottura legati ai picchi locali di densità di corrente.

* **Resistenza effettiva dell'angolo:** a causa della corrente non uniforme, la regione d'angolo offre meno resistenza rispetto a un tratto rettilineo:
  * Raccordo a $90^\circ$: $\Delta R_{90} \approx 0.59 \, R_S$ (invece di $1.0 \, R_S$, cioè un quadrato intero).
  * Raccordo a $45^\circ$: $\Delta R_{45} \approx 0.41 \, R_S$.

* **Formula pratica di calcolo con correzione $R_\Gamma$:**
  Sommando le quote geometriche esterne dei tratti lineari ($L_1 + L_2$), la resistenza totale si corregge con il termine $R_\Gamma$:
  $$R = R_S \frac{L_1 + L_2}{W} - R_\Gamma \quad \text{con} \quad R_\Gamma = R_S \frac{2\Delta L}{W} - \Delta R$$
  * **Per angolo a $45^\circ$:** $R_{\Gamma 45} \approx 0 \implies \mathbf{R \approx R_S \frac{L_1 + L_2}{W}}$ (nessuna correzione necessaria!).
  * **Per angolo a $90^\circ$:** $R_{\Gamma 90} \approx \mathbf{0.41 \, R_S} \implies \mathbf{R \approx R_S \frac{L_1 + L_2}{W} - 0.41 \, R_S}$ (si tolgono circa $0.41$ quadrati per ciascun angolo).

> **Regola di Layout:** gli angoli a $45^\circ$ sono fortemente preferiti sia perché azzerano l'errore di calcolo ($R_\Gamma \approx 0$), sia perché riducono drasticamente i picchi di densità di corrente e il rischio di elettromigrazione.

---

### 3. Il Resistore a Diffusione nel Substrato e la Non-Linearità

Un'alternativa è creare la resistenza direttamente dentro il silicio tramite una diffusione drogata (es. *N-Well* o sacca $N^+/P^+$):
* **La giunzione $pn$ parassita:** la sacca drogata forma inevitabilmente una giunzione $pn$ con il substrato circostante, circondata da una regione di svuotamento.
* **Modulazione della sezione e distorsione:** al variare delle tensioni applicate ai capi del resistore, la tensione inversa della giunzione $pn$ cambia $\implies$ la **regione di svuotamento si allarga o si restringe**, modulando la sezione utile di silicio in cui scorre la corrente.
* **Conclusione per l'analogico:** il valore di $R$ non è costante ma varia dinamicamente con il segnale applicato ($R(V)$ non lineare). Questo introduce **distorsione armonica**, motivo per cui nei circuiti analogici di precisione si evitano i resistori a diffusione e si preferisce il polisilicio non siliciurato.
  👉 Vedi: [Analogico non si scende di dimensioni](../Scaling%20e%20Limiti%20Fisici/Analogico%20non%20si%20scende%20di%20dimensioni.md) per i vincoli di linearità e distorsione nei circuiti analogici.

---

### 4. Dipendenza dalla Temperatura e Coefficiente Termico ($CT_L$)

La resistenza di quadro $R_\square$ di uno strato conduttore o semiconduttore varia con la temperatura $T$ secondo lo sviluppo in serie:

$$R_\square(T) = R_\square(T_{\text{rif}}) \left\{ 1 + CT_L(T - T_{\text{rif}}) + CT_Q(T - T_{\text{rif}})^2 + \dots \right\}$$

* **$T_{\text{rif}}$:** temperatura nominale di riferimento (tipicamente $30^\circ\text{C}$ o $300\text{ K}$).
* **$CT_L$ ($TCR$ - *Temperature Coefficient of Resistance*):** coefficiente termico lineare espresso in $\text{K}^{-1}$.

#### Il contrasto fisico fondamentale: Lo-Res Poly vs Hi-Res Poly

La resistività dipende da $\rho = \frac{1}{q \cdot n \cdot \mu}$. Al variare della temperatura, si manifestano due comportamenti opposti:

1. **Lo-Res Poly, Diffusioni e Metalli ($CT_L > 0$, Coefficiente Positivo PTC):**
   * Il polisilicio a bassa resistenza (*Lo-Res Poly*, usato per i Gate dei MOS con $R_\square \approx 10\,\Omega/\square$) è drogato a livelli altissimi ($N > 10^{20}\,\text{cm}^{-3}$), diventando un **semiconduttore degenere** con comportamento metallico.
   * A temperatura ambiente tutti i droganti sono già ionizzati ($n$ è fisso). L'aumento di temperatura incrementa l'agitazione del reticolo cristallino (urti con fononi), **riducendo la mobilità dei portatori** ($\mu(T) \downarrow$).
   * Con $\mu$ in calo e $n$ costante, la resistività aumenta $\implies \mathbf{CT_L > 0}$ (es. $+1.0 \times 10^{-3}/\text{K}$ per il *lo-res poly*, $+3.5 \times 10^{-3}/\text{K}$ per i metalli).

2. **Hi-Res Poly ($CT_L < 0$, Coefficiente Negativo NTC):**
   * Il polisilicio ad alta resistenza (*Hi-Res Poly*, $R_\square \approx 2\text{ k}\Omega/\square$) ha un **drogaggio moderato o basso** ed è policristallino (grani microscopici separati da *grain boundaries*).
   * Ai bordi di grano ci sono difetti e legami rotti che intrappolano carica, formando **barriere di potenziale elettrostatiche** inter-granulari.
   * I portatori (elettroni se drogato tipo $n$, lacune se drogato tipo $p$) per condurre devono scavalcare termicamente queste barriere per emissione termoionica.
   * All'aumentare della temperatura ($k_B T \uparrow$), il numero di portatori capaci di superare le barriere **cresce esponenzialmente**, sovrastando la riduzione di mobilità. La resistività crolla $\implies \mathbf{CT_L = -2.0 \times 10^{-3}/\text{K}}$.

> 💡 **Compensazione a Zero TCR:** Mettendo in serie una porzione di resistore a $CT_L > 0$ e una a $CT_L < 0$ dimensionate opportunamente ($R_1 \cdot CT_{L1} + R_2 \cdot CT_{L2} = 0$), si ottiene una resistenza complessiva **perfettamente insensibile alla temperatura**.

---

### 5. Controllo Geometrico e Rapporto d'Aspetto ($L/W > 5$)

Ogni resistore integrato termina con due pad ("teste") contenenti i contatti metallici:
$$R_{\text{tot}} = R_\square \frac{L}{W} + 2 R_{\text{testa}} + 2 R_{\text{contatto}}$$

* **Se $L/W$ è piccolo ($< 5$):** la resistenza di contatto e le distorsioni bidimensionali di corrente nelle teste (*current crowding*) costituiscono una quota enorme del totale ($30\%-50\%$). Poiché i contatti hanno grande variabilità di processo ($\pm 30\%$), il valore finale di $R$ è instabile e scarsamente controllabile.
* **Se $L/W > 5$ (lungo e stretto):** il corpo centrale a flusso 1D uniforme costituisce oltre il $90\%-95\%$ del valore totale. L'errore delle teste diventa trascurabile e la resistenza segue con precisione la geometria nominale.

👉 Per la fisica delle resistenze di contatto e l'effetto tunnel, vedi: [Contatti Ohmici e Giunzioni High-Low](./Contatti%20Ohmici%20e%20Giunzioni%20High-Low.md).  
👉 Per le tecniche di layout, simmetria, dummy e cancellazione dei gradienti termici e di stress, vedi: [Matching e Variabilita nei Componenti Integrati](./Matching%20e%20Variabilita%20nei%20Componenti%20Integrati.md).

---

*Pagine correlate:*
- [Contatti Ohmici e Giunzioni High-Low](./Contatti%20Ohmici%20e%20Giunzioni%20High-Low.md)
- [Matching e Variabilita nei Componenti Integrati](./Matching%20e%20Variabilita%20nei%20Componenti%20Integrati.md)
- [Narrow resistenze](./Narrow%20resistenze.md)
- [RTL e Prodotto Ritardo-Consumo (PDP)](../Famiglie%20Logiche/RTL%20e%20Prodotto%20Ritardo-Consumo%20%28PDP%29.md)
- [Siliciuro](../Tecnologia%20e%20Fabbricazione/Siliciuro.md)
- [Elettromigrazione e tossicità dei metalli](../Tecnologia%20e%20Fabbricazione/Elettromigrazione%20e%20tossicit%C3%A0%20dei%20metalli.md)
- [MOS](./MOS.md)
- [Condensatori](./Condensatori.md)
- [Difficoltà nel fare un componente ideale](../Scaling%20e%20Limiti%20Fisici/Difficolt%C3%A0%20nel%20fare%20un%20componente%20ideale.md)
- [Induttore](./Induttore.md)
- [Analogico non si scende di dimensioni](../Scaling%20e%20Limiti%20Fisici/Analogico%20non%20si%20scende%20di%20dimensioni.md)
- [Wafer produzione](../Tecnologia%20e%20Fabbricazione/Wafer%20produzione.md)