## Collection of axes labels
def __ehkl__(ax,ft=15,iopt=0):
    """
    elastic strain (hkl) vs macroscopic flow
    """
    if iopt==0:
        ax.set_xlabel(r'$\Sigma_{11}$',dict(fontsize=ft))
        ax.set_ylabel(r'$\varepsilon^{hkl}$',dict(fontsize=ft))
    elif iopt==1:
        ax.set_ylabel(r'$\Sigma_{11}$',dict(fontsize=ft))
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
        ax.set_ylabel(r'$\Sigma_{11}$',dict(fontsize=ft))
    elif iopt==1:
        ax.set_xlabel(r'$\Sigma_{11}$',dict(fontsize=ft))
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
    if lab=='sigma':   lab = r'$\Sigma^{%s}_{%i%i}$'%(sup,i,j)
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

def __eqv__(ax,ft):
    """
    Equivalent strain, effective stress
    """
    ax.set_xlabel(r'Equivalent strain $\bar{E}$',
                  dict(fontsize=ft))
    ax.set_ylabel(r'Equivalent stress $\bar{\Sigma}$ [MPa]',
                  dict(fontsize=ft))

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
    ax.set_ylabel(r'$\sigma_{%i%i}$'%(i,j),dict(fontsize=ft))

def __vol__(ax,ft,i=1,j=1):
    """
    uniaxial volume evolution curve along uniaxial strain[i,j]
    """
    ax.set_xlabel(r'$\varepsilon_{%i%i}$'%(i,j),dict(fontsize=ft))
    ax.set_ylabel(r'$V_{ph}$',dict(fontsize=ft))

def __deco__(ax,ft=15,iopt=0,ij=None):
    """
    """
    if iopt==0:
        ax.set_xlabel(r'$\sin^2{\psi}$',dict(fontsize=ft))
        ax.set_ylabel(r'$\varepsilon^{\mathrm{hkl}}$',
                      dict(fontsize=ft))
    if iopt==1:
        ax.set_xlabel(r'$\sin^2{\psi}$',dict(fontsize=ft))
        if ij==None:
            label = r'$F_{ij}$'
        else:
            label = r'$F_{%i%i}$'%(
                ij[0],ij[1])
        ax.set_ylabel(label,dict(fontsize=ft))
        #ax.set_ylim(-2,2)

    if iopt==2:
        ax.set_xlabel(r'$\sin^2{\psi}$',dict(fontsize=ft))
        ax.set_ylabel(r'$\varepsilon_{\mathrm{IG}}^{\mathrm{hkl}}$',
                      dict(fontsize=ft))
    if iopt==3:
        ax.set_xlabel(r'$\bar{E}^{\mathrm{eff}}$',dict(fontsize=ft))
        ax.set_ylabel(r'$\bar{\Sigma}^{\mathrm{eff}}$',dict(fontsize=ft))
    ax.grid('on')
