Nei dispositivi a semiconduttore, il collegamento con il mondo esterno avviene tramite contatti metallici. Il comportamento elettrico di queste interfacce è regolato dalla fisica delle bande e dalla natura dei portatori.

---

### 1. Cos'è un Contatto Ohmico?

La definizione ingegneristica di **Contatto Ohmico** è: *un'interfaccia metallo-semiconduttore con caratteristica $I-V$ rigorosamente lineare e simmetrica, e una resistenza parassita specifica di contatto ($\rho_c$) trascurabile rispetto alla resistenza del corpo del dispositivo*.

Non introduce cadute di potenziale non lineari né fenomeni rettificanti (effetto diodo).

---

### 2. Metallo su Semiconduttore: Diodo Schottky vs Effetto Tunneling

All'interfaccia tra un metallo e un semiconduttore si forma **quasi sempre** una barriera energetica di altezza $\Phi_B$ (barriera di Schottky), dovuta alla differenza tra la funzione lavoro del metallo $\Phi_M$ e l'affinità elettronica del silicio, accentuata dal fenomeno del *Fermi-level pinning* per gli stati superficiali.

Il modo in cui le cariche superano questa barriera dipende interamente dal **livello di drogaggio** del semiconduttore:

```text
A. METALLO SU SEMICONDUTTORE POCO DROGATO          B. METALLO SU SEMICONDUTTORE IPER-DROGATO (N+)
            (Diodo Schottky)                                      (Contatto Ohmico)

   Metallo  |   Semiconduttore N                       Metallo  |   Semiconduttore N+
            |      /\                                           |   |
            |     /  \   <-- Barriera Larga                     |   ||
            |    /    \____  (W_dep ~ micron)                   |   || <-- Barriera Sottilissima
            |   /                                               |  / |____ (W_dep < 2 nm)
            |  /                                                | /
            | /                                                 |/  ======> TUNNELING QUANTISTICO
```

#### A. Basso Drogaggio ($N_D \sim 10^{15}\text{ cm}^{-3}$) $\implies$ Diodo Schottky Rettificante
* La regione di svuotamento all'interfaccia è larga ($W_{dep} \propto \frac{1}{\sqrt{N_D}} \sim 0.5 \div 1\,\mu\text{m}$).
* Gli elettroni non possono attraversare la barriera per via quantistica: possono superarla solo per **emissione termoionica** scavalcandone la sommità.
* Il passaggio è asimmetrico: facile in un verso, bloccato nell'altro $\implies$ si comporta come un **diodo Schottky rettificante**.

#### B. Iper-Drogaggio ($N_D > 10^{19}\text{ cm}^{-3}$) $\implies$ Contatto Ohmico per Tunneling (*Field Emission*)
* Aumentando il drogaggio a livelli degeneri, la larghezza della regione di svuotamento si contrae a dimensioni nanometriche:
  $$W_{dep} \propto \frac{1}{\sqrt{N_D}} < 2\text{ nm}$$
* Gli elettroni non hanno più bisogno di scavalcare termicamente la barriera: **la attraversano da parte a parte per effetto tunnel quantistico** (*Field Emission*).
* La resistenza specifica di contatto crolla a valori microscopici ($\rho_c < 10^{-7}\,\Omega\cdot\text{cm}^2$) e la corrente scorre liberamente in entrambe le direzioni.
👉 Approfondimento: [Siliciuro](../Tecnologia%20e%20Fabbricazione/Siliciuro.md) per l'abbassamento congiunto di $\Phi_B$ e $W_{dep}$ nei processi industriali *Salicide*.

---

### 3. La Giunzione $N-N^+$ (*High-Low Junction*): Perché NON è Rettificante?

Un'altra situazione comune (ad esempio nel diodo [PIN](./Diodo%20PIN%20e%20Modulazione%20di%20Conducibilita.md) o nelle sacche del [Diodo integrato](./Diodo.md)) è l'interfaccia tra due zone dello stesso tipo ma con drogaggio differente: $N$ (poco drogato, es. $10^{15}\text{ cm}^{-3}$) e $N^+$ (molto drogato, es. $10^{19}\text{ cm}^{-3}$).

All'equilibrio termico si forma un piccolo dislivello energetico di potenziale intrinseco:
$$V_{bi} = \frac{k_B T}{q} \ln\left(\frac{N_D^+}{N_D}\right) \approx 0.2 \div 0.3\text{ V}$$

```text
Banda di Conduzione Ec:

       Regione N                     Regione N+
(Poco drogato, 10^15)           (Molto drogato, 10^19)
-------------------
                   \
                    \  <--- Gradino (V_bi ~ 0.2 V)
                     \
                      -------------------  Ec
                     ===================  Ef (Livello di Fermi)
```

#### Perché non si comporta come un diodo?
1. **Stessi Portatori Maggioritari:**  
   In una giunzione $P-N$, la corrente inversa si blocca perché deve essere sostenuta dai portatori minoritari ($n_p \approx 0$). Nella giunzione $N-N^+$ **i portatori sono elettroni maggioritari in entrambi i lati** ($10^{15}$ contro $10^{19}$).
2. **Nessuna Zona di Svuotamento:**  
   Sul lato $N$ si forma uno strato di **accumulo** di elettroni (che aumenta la conducibilità locale anziché diminuirla).
3. **Nessuna Tensione di Soglia:**  
   Anche applicando frazioni di millivolt ($1\text{ mV}$), la corrente scorre istantaneamente seguendo la legge di Ohm:
   $$V = R_{bulk} \cdot I$$
   La caratteristica $I-V$ è una retta passante per l'origine, senza alcuna soglia di accensione.

#### La Funzione di "Specchio Elettrostatico" (*Back Surface Field* - BSF)
Quegli $0.2\text{ V}$ interni non ostacolano gli elettroni, ma creano un campo elettrico locale che **respinge le lacune (portatori minoritari nella zona $N$)**, impedendo loro di raggiungere il contatto metallico e ricombinarsi. Questa tecnica è ampiamente utilizzata nei fotorivelatori, nelle celle solari e nei collettori dei [BJT](./BJT.md).

---

### 4. Il Paradosso del $V_{bi}$ in Cortocircuito: Perché Non Scorre Corrente a Vuoto?

In una giunzione $PN$ isolata esiste un potenziale interno $V_{bi} \approx 0.7\text{ V}$. Se colleghiamo l'anodo e il catodo con un filo di rame cortocircuitandoli, **non scorre alcuna corrente**.

Se scorresse corrente, violeremmo il **Secondo Principio della Termodinamica** (creazione di energia elettrica dal nulla a temperatura costante).

```text
        +------------------ FILO DI RAME ------------------+
        |                                                  |
     [RAME]                                             [RAME]
        |  <-- Contatto Rame-P            Contatto N-Rame --> |
     [ P+ ] ============================================= [ N+ ]
                        Giunzione P-N (V_bi)
```

La spiegazione fisica poggia su due principi:

1. **Bilancio Microscopico dei Flussi ($J_{tot} = 0$):**  
   All'interno della giunzione $PN$, la corrente di diffusione (dovuta al gradiente di concentrazione) e la corrente di deriva/drift (dovuta al campo elettrico di $V_{bi}$) si equivalgono punto per punto:
   $$J_{\text{diffusione}} + J_{\text{deriva}} = 0$$
2. **Cancellazione dei Potenziali di Contatto ($\sum V = 0$):**  
   Chiudendo il circuito con il filo metallico, introduciamo due giunzioni metallo-semiconduttore (Rame-$P$ e $N$-Rame). Ciascuna di queste interfacce sviluppa un proprio potenziale di contatto.  
   Lungo l'intera maglia chiusa:
   $$V_{\text{totale}} = V_{bi, PN} + \Delta V_{\text{N-Rame}} + \Delta V_{\text{Rame-P}} = V_{bi} - V_{bi} = \mathbf{0\text{ V}}$$
3. **Allineamento del Livello di Fermi ($E_F = \text{costante}$):**  
   All'equilibrio termico, il potenziale elettrochimico (livello di Fermi $E_F$) deve essere **perfettamente piatto e uniforme** lungo l'intero circuito chiuso. Senza un dislivello in $E_F$, non esiste alcuna forza termodinamica netta che possa muovere le cariche.

---

*Pagine correlate:*
- [Diodo PIN e Modulazione di Conducibilita](./Diodo%20PIN%20e%20Modulazione%20di%20Conducibilita.md)
- [Diodo](./Diodo.md)
- [Siliciuro](../Tecnologia%20e%20Fabbricazione/Siliciuro.md)
- [Resistore](./Resistore.md)
- [Vias](../Tecnologia%20e%20Fabbricazione/Vias.md)
- [Breakdown e Diodo Zener](./Breakdown%20e%20Diodo%20Zener.md)
- [BJT](./BJT.md)
- [MOS](./MOS.md)
- [Difficoltà nel fare un componente ideale](../Scaling%20e%20Limiti%20Fisici/Difficolt%C3%A0%20nel%20fare%20un%20componente%20ideale.md)
