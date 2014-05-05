import matplotlib.pyplot as plt

def fancy_legend(ax,loc='best',size=12):
    ax.legend(loc=loc,fancybox=True, framealpha=0.5,
              prop={'size':size})

def ticks_bins_ax_u(axes,n=4):
    ticks_bins_ax(axes,axis='x',n=n)
    ticks_bins_ax(axes,axis='y',n=n)

def ticks_bins_ax(axes,axis='x',n=4):
    for i in range(len(axes)):
        ticks_bins(axes[i],axis=axis,n=n)

def ticks_bins(ax,axis='x',n=4):
    ax.locator_params(nbins=n,axis=axis)

def rm_lab(ax,axis='y'):
    if axis=='x': plt.setp(ax.get_xticklabels(), visible=False)
    if axis=='y': plt.setp(ax.get_yticklabels(), visible=False)

    if axis=='x': ax.set_xlabel('')
    if axis=='y': ax.set_ylabel('')

def rm_ax(ax,axis='x'):
    if axis=='x': ax.get_xaxis().set_visible(False)
    if axis=='y': ax.get_yaxis().set_visible(False)

def rm_inner(ax):
    ## delete inner axes ticks
    for i in range(len(ax)-1):
        rm_lab(ax[i+1],axis='x')
        rm_lab(ax[i+1],axis='y')

def rm_all_lab(ax):
    for i in range(len(ax)):
        rm_lab(ax[i],axis='x')
        rm_lab(ax[i],axis='y')

def wide_fig(
        ifig=1,uw=2.8, uh=3,nw=5,
        w0=0.2, ws=0.7, w1=0.1,
        left = 0.05, right = 0.02,
        nh=1,
        h0=0.2, hs=0.7, h1=0.1,
        down = 0.05, up = 0.02, iarange=False):
    """
    Make a figure that has horizontally aligned sub axes

    Arguments
    ---------
    ifig : mpl figure number

    uw  : unit width for a subaxes
    uh  : unit height
    nw  : number of axes

    h0  : spacing h0 for a subaxes
    hs  : width of uniax axes
    h1  : h0+hs+h1 is the total heigth of an axes

    w0  : w0,ws, and w1 are corresponding values for width
    ws
    w1
    l   : left spacing in the figure canvas
    r   : right spacing in the figure canvas
    """
    fig = plt.figure(figsize=(uw*nw,uh*nh))

    hsum = h0 + hs + h1
    h0 = h0/hsum; hs = hs/hsum; h1 = h1/hsum

    wsum = w0 + ws + w1
    w0 = w0/wsum; ws = ws/wsum; w1 = w1/wsum

    dw = (1. -left - right)/nw
    dh = (1. -up - down)/nh

    w0 = w0 * dw
    ws = ws * dw
    w1 = w1 * dw

    h0 = h0 * dh
    hs = hs * dh
    h1 = h1 * dh

    iax=-1
    if iarange==False:
        for j in range(nh):
            b = down + h0 + dh * j
            d = hs
            for i in range(nw):
                iax=iax+1
                a = left + w0 + dw * i
                c = ws
                fig.add_axes([a,b,c,d]) # w0, h0, w, h
                cax=fig.axes[iax] # current axes

                ticks_bins(ax=cax,axis='x',n=4)
                ticks_bins(ax=cax,axis='y',n=4)

    elif iarange:
        for j in range(nh):
            b = down+h0+dh*(nh-j-1)
            d = hs
            for i in range(nw):
                iax=iax+1
                a = left + w0 + dw * i
                c = ws
                fig.add_axes([a,b,c,d]) # w0, h0, w, h
                cax=fig.axes[iax] # current axes

                ticks_bins(ax=cax,axis='x',n=4)
                ticks_bins(ax=cax,axis='y',n=4)

    return fig


def axes3():
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure()
    ax=fig.add_subplot(111, projection='3d')
    return ax


def tune_xy_lim(axs):
    tune_x_lim(axs,axis='x')
    tune_x_lim(axs,axis='y')


def tune_x_lim(axs,axis='x'):
    """
    axis='x' or 'y'
    """
    X0 = None; X1 = None
    for i in range(len(axs)):
        if axis=='x': x0,x1 = axs[i].get_xlim()
        if axis=='y': x0,x1 = axs[i].get_ylim()
        if X0==None: X0=x0
        if X1==None: X1=x1
        if x0<X0:X0=x0
        if x1>X1:X1=x1

    for i in range(len(axs)):
        if axis=='x': axs[i].set_xlim(X0,X1)
        if axis=='y': axs[i].set_ylim(X0,X1)


def norm_cmap(mx,mn,val=None):
    import matplotlib as mpl
    import matplotlib.cm as cm
    norm = mpl.colors.Normalize(vmin=mn,vmax=mx)
    cmap = cm.gist_rainbow
    m = cm.ScalarMappable(norm=norm, cmap=cmap)

    if val==None: return cmap, m
    else: return cmap, m.to_rgba(val)
