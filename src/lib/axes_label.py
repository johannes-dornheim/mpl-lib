## Collection of axes labels
def __ehkl__(ax,ft=15,iopt=0):
    """
    elastic strain (hkl) vs macroscopic flow
    """
    if iopt==0:
        ax.set_xlabel(r'$\Sigma_{11}$ [MPa]',dict(fontsize=ft))
        ax.set_ylabel(r'$\varepsilon^{hkl}$',dict(fontsize=ft))
    elif iopt==1:
        ax.set_ylabel(r'$\Sigma_{11}$ [MPa]',dict(fontsize=ft))
        ax.set_xlabel(r'$\varepsilon^{hkl}$',dict(fontsize=ft))
    elif iopt==2:
        ax.set_xlabel(r'$E_{11}$',dict(fontsize=ft))
        ax.set_ylabel(r'$\varepsilon^{hkl}$',dict(fontsize=ft))
    elif iopt==3:
        ax.set_ylabel(r'$E_{11}$',dict(fontsize=ft))
        ax.set_xlabel(r'$\varepsilon^{hkl}$',dict(fontsize=ft))
    pass

def __ph__(ax,ft=15,iopt=0):
    """
    Phase specific elastic strains vs macroscopic flow
    """
    if iopt==0:
        ax.set_xlabel(r'$\varepsilon^{\mathrm{el}}$',dict(fontsize=ft))
        ax.set_ylabel(r'$\Sigma_{11}$ [MPa]',dict(fontsize=ft))
    elif iopt==1:
        ax.set_xlabel(r'$\Sigma_{11}$ [MPa]',dict(fontsize=ft))
        ax.set_xlabel(r'$\varepsilon^{\mathrm{el}}$',dict(fontsize=ft))
    elif iopt==2:
        ax.set_xlabel(r'$E_{11}$',dict(fontsize=ft))
        ax.set_xlabel(r'$\varepsilon^{\mathrm{el}}$',dict(fontsize=ft))
    pass

def uni_sup(set_lab,ft,i,j,sup='eq',lab='sigma'):
    """
    x label or y label
    """
    sup ='\mathrm{%s}'%sup
    if lab=='sigma':   lab = r'$\Sigma^{%s}_{%i%i}$ [MPa]'%(sup,i,j)
    if lab=='epsilon': lab= r'$E^{%s}_{%i%i}$'%(sup,i,j)
    set_lab(lab,dict(fontsize=ft))

def __eff__(ax,ft):
    """
    Effective strain, effective stress
    """
    ax.set_xlabel(r'Effective strain $\bar{E}^{\mathrm{eff}}$',
                  dict(fontsize=ft))
    ax.set_ylabel(r'Effective stress $\bar{\Sigma}^{\mathrm{eff}}$ [MPa]',
                  dict(fontsize=ft))

def __eqv__(ax,ft,zero_xy=True):
    """
    Equivalent strain, effective stress
    """
    ax.set_xlabel(r'Equivalent strain $\bar{E}$',
                  dict(fontsize=ft))
    ax.set_ylabel(r'Equivalent stress $\bar{\Sigma}$ [MPa]',
                  dict(fontsize=ft))
    if zero_xy: ax.set_xlim(0.,); ax.set_ylim(0.,)
    #ax.grid('on')

def __vm__(ax,ft,zero_xy=True):
    """
    Von Mises strain, Von Mises stress
    """
    ax.set_xlabel(r'Von Mises strain $\bar{E}^{\mathrm{VM}}$',
                  dict(fontsize=ft))
    ax.set_ylabel(r'Von Mises stress $\bar{\Sigma}^{\mathrm{VM}}$ [MPa]',
                  dict(fontsize=ft))
    if zero_xy: ax.set_xlim(0.,); ax.set_ylim(0.,)
    #ax.grid('on')

def __effr__(ax,ft):
    ax.set_xlabel(r'Effective strain $\bar{E}^{\mathrm{eff}}$',
                  dict(fontsize=ft))
    ax.set_ylabel('R-value',dict(fontsize=ft))

def __eqvr__(ax,ft):
    ax.set_xlabel(r'Equivalent strain $\bar{E}$',dict(fontsize=ft))
    ax.set_ylabel('R-value',dict(fontsize=ft))

def __unix__(ax,ft,i=1,j=1):
    """
    uniaxial tension curve along stress(i,j) vs strain(i,j)
    """
    ax.set_xlabel(r'$\varepsilon_{%i%i}$'%(i,j),dict(fontsize=ft))
    ax.set_ylabel(r'$\sigma_{%i%i}$ [MPa]'%(i,j),dict(fontsize=ft))

def __vol__(ax,ft,i=1,j=1):
    """
    uniaxial volume evolution curve along uniaxial strain[i,j]
    """
    ax.set_xlabel(r'$\varepsilon_{%i%i}$'%(i,j),dict(fontsize=ft))
    ax.set_ylabel(r'$V_{ph}$',dict(fontsize=ft))

def __plane__(ax,ft,iopt=0):
    if iopt==0:
        xlab = r'$\Sigma_\mathrm{RD}$ [MPa]'
        ylab = r'$\Sigma_\mathrm{TD}$ [MPa]'
    if iopt==1:
        xlab = r'$E_\mathrm{RD}$'
        ylab = r'$E_\mathrm{TD}$'
    if iopt==2:
        xlab = r'$\Sigma_\mathrm{11}$ [MPa]'
        ylab = r'$\Sigma_\mathrm{22}$ [MPa]'
    ax.set_xlabel(xlab,dict(fontsize=ft))
    ax.set_ylabel(ylab,dict(fontsize=ft))
    ax.grid('on')
    ax.set_aspect('equal')

    mx1=ax.get_xlim()[1]
    mx2=ax.get_ylim()[1]
    mx = max([mx1,mx2])
    ax.set_xlim(0.,mx)
    ax.set_ylim(0.,mx)

def __deco_fld__(ax,ft=15,iopt=0,iasp=True):
    ft = dict(fontsize=ft)
    if iopt==0:
        ax.set_xlabel(r'$\mathrm{\bar{E}}_2$',ft)
        ax.set_ylabel(r'$\mathrm{\bar{E}}_1$',ft)
        ax.set_ylim(0.,)
    elif iopt==1:
        ax.set_xlabel(r'$\bar{\Sigma}_2$ [MPa]',ft)
        ax.set_ylabel(r'$\bar{\Sigma}_1$ [MPa]',ft)
        ax.set_xlim(0.,);ax.set_ylim(0.,)
    elif iopt==2:
        ax.set_xlabel(r'$\mathrm{\bar{E}}_\mathrm{TD}$',ft)
        ax.set_ylabel(r'$\mathrm{\bar{E}}_\mathrm{RD}$',ft)
    elif iopt==3:
        ax.set_xlabel(r'$\bar{\Sigma}_\mathrm{TD}$ [MPa]',ft)
        ax.set_ylabel(r'$\bar{\Sigma}_\mathrm{RD}$ [MPa]',ft)

    if iasp:ax.set_aspect('equal')

def __deco__(ax,ft=15,iopt=0,ij=None,hkl=None,ipsi_opt=0):
    """
    diffraction plot decorations
    """
    if ipsi_opt==0:   psi_xlab=r'$\sin^2{\psi}$'
    elif ipsi_opt==1: psi_xlab=r'$\mathrm{sign}(\psi)$ $\sin^2{\psi} $'
    elif ipsi_opt==2: psi_xlab=r'$\psi$'

    if hkl==None: hkl='hkl'
    if iopt==0:
        ax.set_xlabel(psi_xlab,dict(fontsize=ft))
        ax.set_ylabel(r'$\varepsilon^{\{%s\},(\phi,\psi)}$ [$\mu$strain]'%hkl,
                      dict(fontsize=ft))
    if iopt==1:
        ax.set_xlabel(psi_xlab,dict(fontsize=ft))
        if ij==None:
            label = r'$\mathbb{F}^{\{%s\},(\phi,\psi)}_{\mathrm{ij}} $ [$\mathrm{GPa^{-1}}$]'%hkl
        else:
            label = r'$\mathbb{F}^{\{%s\}, (\phi,\psi)}_{%i%i}$'%(
                hkl,ij[0],ij[1])

        ax.set_ylabel(label,dict(fontsize=ft))
        #ax.set_ylim(-2,2)

    if iopt==2:
        ax.set_xlabel(psi_xlab,dict(fontsize=ft))
        ax.set_ylabel(r'$\varepsilon_{\mathrm{IG}}^{\{%s\}, (\phi,\psi)}\ [\mu]$ '%hkl,
                      dict(fontsize=ft))
    elif iopt==3:
        ax.set_xlabel(r'$\bar{E}^{\mathrm{eff}}$',dict(fontsize=ft))
        ax.set_ylabel(r'$\bar{\Sigma}^{\mathrm{eff}}$ [MPa]',dict(fontsize=ft))

    elif iopt==4:
        ax.set_xlabel(r'$\psi$',dict(fontsize=ft))
        ax.set_ylabel(r'$d^{\{%s\}} (\phi,\psi)$'%hkl,
                      dict(fontsize=ft))
    elif iopt==5:
        ax.set_xlabel(r'$\psi$',dict(fontsize=ft))
        ax.set_ylabel(r'$\varepsilon^{\{%s\}}$'%hkl,
                      dict(fontsize=ft))
    elif iopt==6:
        ax.set_xlabel(r'Von Mises Equivalent strain $\bar{E}$',
                      dict(fontsize=ft))
        if ij==None:
            label = r'$\mathbb{F}^{\{%s\},(\phi,\psi)}_\mathrm{ij} $ [$\mathrm{GPa^{-1}}$]'%hkl
        else:
            label = r'$\mathbb{F}^{\{%s\},(\phi,\psi)}_{%i%i} $ [$\mathrm{GPa^{-1}}$]'%(
                hkl,ij[0],ij[1])
        ax.set_ylabel(label,dict(fontsize=ft))
    elif iopt==7:
        ax.set_xlabel(psi_xlab,dict(fontsize=ft))
        ax.set_ylabel(r'Volume Fraction $(\phi,\psi)$',dict(fontsize=ft))
    elif iopt==8:
        ax.set_xlabel(r'Von Mises Equivalent strain $\bar{E}$',
                      dict(fontsize=ft))
        ylabel_err =r'$(\bar{\Sigma}_\mathrm{w} -\Sigma_\mathrm{d})_{\mathrm{VM}}/(\bar{\Sigma}_\mathrm{w})_{\mathrm{VM}}$'
        ax.set_ylabel(ylabel_err,dict(fontsize=ft))
    elif iopt==9:
        ax.set_xlabel(r'Von Mises Equivalent strain $\bar{E}$',
                      dict(fontsize=ft))
        ylabel_err =r'Uncertainty $\mathbf{\sigma}^u_\mathrm{VM}$'
        ax.set_ylabel(ylabel_err,dict(fontsize=ft))
    ax.grid('on')
