"""
Script per la visualizzazione delle regioni di funzionamento del MOSFET
e della caratteristica I_D - V_GS sia in scala lineare che semilogaritmica,
più la mappa 2D sul piano (V_GS, V_DS).
"""

import numpy as np
import matplotlib.pyplot as plt

# ==============================================================================
# PARAMETRI FISICI E TECNOLOGICI (Modello continuo EKV didattico)
# ==============================================================================
Vth = 0.5       # Tensione di soglia [V]
n = 1.3         # Fattore di partitore di sottosoglia (body factor: 1 + Cdep/Cox)
VT = 0.026      # Tensione termica k_B*T/q a 300 K (~26 mV)
Ispec = 2e-6    # Corrente specifica di normalizzazione [A] (2 uA)

def ekv_id(vgs, vds):
    """
    Modello continuo EKV: copre in modo continuo ed elegante:
    - Debole inversione (sottosoglia): andamento esponenziale per diffusione
    - Moderata inversione: raccordo continuo
    - Forte inversione: andamento quadratico (saturazione) o lineare (triodo)
    - Sia regime lineare che saturazione per ogni livello di inversione.
    """
    vp = (vgs - Vth) / n
    arg_f = np.clip(vp / (2 * VT), -40, 40)
    arg_r = np.clip((vp - vds) / (2 * VT), -40, 40)
    
    # Funzione softplus log(1 + e^x)
    def softplus(x):
        return np.where(x > 25, x, np.log(1.0 + np.exp(x)))
    
    i_f = softplus(arg_f)**2
    i_r = softplus(arg_r)**2
    return Ispec * (i_f - i_r)

# ==============================================================================
# 1. CARATTERISTICA I_D - V_GS (Lineare e Semilogaritmica)
# ==============================================================================
vgs = np.linspace(0.1, 1.4, 600)
vds_low = 0.05   # 50 mV (Resta in lineare/triodo per quasi tutta la forte inversione)
vds_mid = 0.35   # 350 mV (Evidenzia il passaggio: Parabola di Sat -> Retta di Lin)
vds_high = 1.0   # 1.0 V (Resta in saturazione per tutto l'intervallo)

id_low = ekv_id(vgs, vds_low) * 1e6   # in microAmpere [uA]
id_mid = ekv_id(vgs, vds_mid) * 1e6
id_high = ekv_id(vgs, vds_high) * 1e6

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6.5), dpi=200)
fig.patch.set_facecolor('#ffffff')

# --- SUBPLOT 1: SCALA LINEARE ---
ax1.set_facecolor('#fcfdfe')
ax1.plot(vgs, id_high, color='#1e3a8a', lw=2.5, label=r'$V_{DS} = 1.0\,\mathrm{V}$ (Sempre Saturazione)')
ax1.plot(vgs, id_mid, color='#d97706', lw=2.5, label=r'$V_{DS} = 0.35\,\mathrm{V}$ (Saturazione $\to$ Lineare)')
ax1.plot(vgs, id_low, color='#059669', lw=2.5, label=r'$V_{DS} = 0.05\,\mathrm{V}$ (Sempre Lineare/Triodo)')

# Confini di soglia e transizione
vgs_trans = Vth + n * vds_mid  # Punto di passaggio per Vds = 0.35 V
ax1.axvline(Vth, color='#dc2626', ls='--', lw=1.5, alpha=0.8, label=r'Soglia $V_{th} = 0.5\,\mathrm{V}$')
ax1.axvline(vgs_trans, color='#d97706', ls=':', lw=2.0, label=r'Transizione Sat $\to$ Lin ($V_{ov} = n V_{DS}$)')

# Fasce di inversione di Gate
ax1.axvspan(0.1, Vth - 0.08, color='#93c5fd', alpha=0.18, label='Debole Inversione (Sottosoglia)')
ax1.axvspan(Vth - 0.08, Vth + 0.08, color='#fef08a', alpha=0.25, label='Moderata Inversione')
ax1.axvspan(Vth + 0.08, 1.4, color='#bbf7d0', alpha=0.15, label='Forte Inversione')

# Annotazioni sulla curva Vds = 0.35 V
ax1.annotate(r"$\mathbf{Tratto\ Parabolico}$" + "\n" + r"(Saturazione: $V_{ov} < n V_{DS}$)" + "\n" + r"$I_D \propto (V_{GS}-V_{th})^2$", 
             xy=(0.75, ekv_id(0.75, vds_mid)*1e6), xytext=(0.52, 70),
             arrowprops=dict(arrowstyle="->", color="#b45309", lw=1.8),
             fontsize=9.5, color="#78350f",
             bbox=dict(boxstyle="round,pad=0.35", fc="#fef3c7", ec="#f59e0b", lw=1.2))

ax1.annotate(r"$\mathbf{Tratto\ Lineare\ (Retta)}$" + "\n" + r"(Triodo: $V_{ov} > n V_{DS}$)" + "\n" + r"$I_D \approx k V_{DS} \cdot V_{GS} + \mathrm{cost}$", 
             xy=(1.2, ekv_id(1.2, vds_mid)*1e6), xytext=(0.95, 125),
             arrowprops=dict(arrowstyle="->", color="#b45309", lw=1.8),
             fontsize=9.5, color="#78350f",
             bbox=dict(boxstyle="round,pad=0.35", fc="#fef3c7", ec="#f59e0b", lw=1.2))

ax1.set_title(r"Caratteristica $I_D - V_{GS}$ a $V_{DS}$ Fissato (Scala Lineare)", fontsize=12.5, fontweight='bold', pad=12)
ax1.set_xlabel(r"Tensione Gate-Source $V_{GS}$ [V]", fontsize=11, fontweight='bold')
ax1.set_ylabel(r"Corrente di Drain $I_D$ [$\mu$A]", fontsize=11, fontweight='bold')
ax1.set_xlim(0.1, 1.4)
ax1.set_ylim(0, 200)
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.legend(loc='upper left', fontsize=8.2, framealpha=0.95)

# --- SUBPLOT 2: SCALA SEMILOGARITMICA ---
ax2.set_facecolor('#fcfdfe')
ax2.semilogy(vgs, id_high, color='#1e3a8a', lw=2.5, label=r'$V_{DS} = 1.0\,\mathrm{V}$ (Saturazione)')
ax2.semilogy(vgs, id_mid, color='#d97706', lw=2.5, ls='--', label=r'$V_{DS} = 0.35\,\mathrm{V}$ (Saturazione)')
ax2.semilogy(vgs, id_low, color='#059669', lw=2.5, label=r'$V_{DS} = 0.05\,\mathrm{V}$ (Lineare, $V_{DS} \approx 2 V_T$)')

ax2.axvline(Vth, color='#dc2626', ls='--', lw=1.5, alpha=0.8)
ax2.axvspan(0.1, Vth - 0.08, color='#93c5fd', alpha=0.18)
ax2.axvspan(Vth - 0.08, Vth + 0.08, color='#fef08a', alpha=0.25)
ax2.axvspan(Vth + 0.08, 1.4, color='#bbf7d0', alpha=0.15)

ax2.annotate(r"$\mathbf{Debole\ Inversione\ =\ Sottosoglia}$" + "\n" + r"Diffusione pura: esponenziale" + "\n" + r"$S = n \ln(10) V_T \approx 78\,\mathrm{mV/dec}$", 
             xy=(0.32, ekv_id(0.32, vds_high)*1e6), xytext=(0.13, 1e-2),
             arrowprops=dict(arrowstyle="->", color="#1e3a8a", lw=1.6),
             fontsize=9, color="#1e3a8a",
             bbox=dict(boxstyle="round,pad=0.35", fc="#dbeafe", ec="#3b82f6", lw=1.2))

ax2.annotate(r"Per $V_{DS} \geq 3\div 4 V_T \approx 100\,\mathrm{mV}$," + "\n" + r"le curve sono SOVRAPPOSTE!" + "\n" + r"Perché sono ENTRAMBE in" + "\n" + r"$\mathbf{Saturazione\ di\ Debole\ Inversione}$", 
             xy=(0.42, ekv_id(0.42, vds_high)*1e6), xytext=(0.48, 1e-5),
             arrowprops=dict(arrowstyle="->", color="#111827", lw=1.2),
             fontsize=8.5, color="#111827",
             bbox=dict(boxstyle="round,pad=0.35", fc="#f3f4f6", ec="#9ca3af", lw=1))

ax2.set_title(r"Caratteristica $I_D - V_{GS}$ (Scala Semilogaritmica)", fontsize=12.5, fontweight='bold', pad=12)
ax2.set_xlabel(r"Tensione Gate-Source $V_{GS}$ [V]", fontsize=11, fontweight='bold')
ax2.set_ylabel(r"Corrente $\log_{10}(I_D)$ [$\mu$A]", fontsize=11, fontweight='bold')
ax2.set_xlim(0.1, 1.4)
ax2.set_ylim(1e-6, 300)
ax2.grid(True, which='both', linestyle='--', alpha=0.5)
ax2.legend(loc='lower right', fontsize=8.2, framealpha=0.95)

plt.tight_layout()
plt.savefig('Immagini/mosfet_id_vgs_regioni.png', dpi=200)
print("Salvato: Immagini/mosfet_id_vgs_regioni.png")

# ==============================================================================
# 2. MAPPA 2D DELLE REGIONI SUL PIANO (V_GS, V_DS)
# ==============================================================================
fig, ax = plt.subplots(figsize=(10, 7), dpi=200)
fig.patch.set_facecolor('#ffffff')
ax.set_facecolor('#ffffff')

Vth_val = 0.5
vgs_max = 1.4
vds_max = 1.0

vgs_weak_max = Vth_val - 0.08
vgs_mod_max = Vth_val + 0.08

vgs_arr = np.linspace(0, vgs_max, 500)
# Tensione di saturazione unificata
vdsat = np.where(vgs_arr < Vth_val, 4*VT, np.sqrt((4*VT)**2 + ((vgs_arr - Vth_val)/n)**2))

# 6 Zone colorate
ax.fill_between(vgs_arr[vgs_arr <= vgs_weak_max], 0, 4*VT, color='#93c5fd', alpha=0.35, label='1. Debole Inv. - Lineare')
ax.fill_between(vgs_arr[vgs_arr <= vgs_weak_max], 4*VT, vds_max, color='#3b82f6', alpha=0.25, label='2. Debole Inv. - Saturazione')

mod_mask = (vgs_arr >= vgs_weak_max) & (vgs_arr <= vgs_mod_max)
ax.fill_between(vgs_arr[mod_mask], 0, vdsat[mod_mask], color='#fde047', alpha=0.4, label='3. Moderata Inv. - Lineare')
ax.fill_between(vgs_arr[mod_mask], vdsat[mod_mask], vds_max, color='#eab308', alpha=0.3, label='4. Moderata Inv. - Saturazione')

strong_mask = vgs_arr >= vgs_mod_max
ax.fill_between(vgs_arr[strong_mask], 0, vdsat[strong_mask], color='#86efac', alpha=0.35, label='5. Forte Inv. - Lineare (Triodo)')
ax.fill_between(vgs_arr[strong_mask], vdsat[strong_mask], vds_max, color='#22c55e', alpha=0.25, label='6. Forte Inv. - Saturazione (Pinch-off)')

# Linea Vdsat
ax.plot(vgs_arr, vdsat, color='#b91c1c', lw=2.5, ls='-', label=r'Confine di Saturazione $V_{DS} = V_{dsat}$')

# Linee soglia
ax.axvline(Vth_val, color='#dc2626', ls='--', lw=1.5, alpha=0.8, label=r'Soglia $V_{th} = 0.5\,\mathrm{V}$')
ax.axvline(vgs_weak_max, color='#64748b', ls=':', lw=1.2)
ax.axvline(vgs_mod_max, color='#64748b', ls=':', lw=1.2)

# Taglio a Vds = 0.35 V fisso
ax.axhline(0.35, color='#d97706', lw=2.5, ls='-.', label=r'Taglio a $V_{DS} = 0.35\,\mathrm{V}$ fissato (Caratteristica $I_D-V_{GS}$)')
ax.annotate('', xy=(1.35, 0.35), xytext=(0.1, 0.35),
            arrowprops=dict(arrowstyle="->", color="#d97706", lw=3.0))

ax.scatter([0.25, 0.5, 0.72, 1.15], [0.35, 0.35, 0.35, 0.35], color='#d97706', s=60, zorder=5)

ax.text(0.22, 0.42, "Passo 1:\nDebole Sat\n(Esponenziale)", fontsize=8.5, fontweight='bold', color='#1e3a8a', ha='center',
        bbox=dict(boxstyle="round,pad=0.25", fc="#eff6ff", ec="#93c5fd"))
ax.text(0.50, 0.50, "Passo 2:\nModerata Sat\n(Transizione)", fontsize=8.5, fontweight='bold', color='#854d0e', ha='center',
        bbox=dict(boxstyle="round,pad=0.25", fc="#fefce8", ec="#fde047"))
ax.text(0.72, 0.42, "Passo 3:\nForte Sat\n(PARABOLA!)", fontsize=8.5, fontweight='bold', color='#15803d', ha='center',
        bbox=dict(boxstyle="round,pad=0.25", fc="#f0fdf4", ec="#86efac"))
ax.text(1.15, 0.22, "Passo 4:\nForte Lin/Triodo\n(RETTA!)", fontsize=8.5, fontweight='bold', color='#047857', ha='center',
        bbox=dict(boxstyle="round,pad=0.25", fc="#ecfdf5", ec="#6ee7b7"))

ax.text(0.95, 0.75, r"$\mathbf{ZONA\ DI\ SATURAZIONE}$" + "\n" + r"$V_{DS} \geq V_{dsat}$" + "\n" + r"(Canale strozzato al Drain / Drift sat.)", 
        fontsize=10, color='#1e293b', ha='center',
        bbox=dict(boxstyle="round,pad=0.4", fc="#ffffff", ec="#cbd5e1", alpha=0.9))

ax.text(1.15, 0.07, r"$\mathbf{ZONA\ LINEARE\ (TRIODO)}$" + "\n" + r"$V_{DS} < V_{dsat}$ (Canale continuo)", 
        fontsize=9.5, color='#1e293b', ha='center',
        bbox=dict(boxstyle="round,pad=0.4", fc="#ffffff", ec="#cbd5e1", alpha=0.9))

ax.set_title(r"Mappa 2D delle Regioni del MOSFET nel Piano $(V_{GS},\ V_{DS})$", fontsize=13, fontweight='bold', pad=12)
ax.set_xlabel(r"Tensione di Controllo di Gate $V_{GS}$ [V]  $\longrightarrow$  Regime di Inversione (Carica nel canale)", fontsize=11, fontweight='bold')
ax.set_ylabel(r"Tensione di Drain $V_{DS}$ [V]  $\longrightarrow$  Condizione di Strozzamento", fontsize=11, fontweight='bold')
ax.set_xlim(0, vgs_max)
ax.set_ylim(0, vds_max)
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='upper left', fontsize=8.0, framealpha=0.95)

plt.tight_layout()
plt.savefig('Immagini/mosfet_mappa_regioni_2d.png', dpi=200)
print("Salvato: Immagini/mosfet_mappa_regioni_2d.png")

if __name__ == '__main__':
    print("Grafici generati con successo in Immagini/")
