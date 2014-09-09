import numpy as np
class FlowCurve:
    """
    Flow characteristic in full 3x3 dimensions
    """
    def __init__(self,name=None,description=None):
        """        """
        self.nstp = 0
        self.sigma = np.zeros((3,3,self.nstp))*np.nan
        self.epsilon = np.zeros((3,3,self.nstp))*np.nan
        self.flag_sigma = np.zeros((3,3))
        self.flag_epsilon = np.zeros((3,3))
        self.flag_6s    = np.zeros((6,))
        self.flag_6e    = np.zeros((6,))

        self.is_stress_available = False
        self.is_strain_available = False

    # voigt vectorial nomenclature (0 - 5)
        self.vo = [[0,0],[1,1],[2,2],[1,2],[0,1],[0,2]]

        self.ivo = np.ones((3,3),dtype='int')
        for i in range(3):
            self.ivo[i,i] = i

        self.ivo[1,2] = 3
        self.ivo[2,1] = 3
        self.ivo[0,1] = 4
        self.ivo[1,0] = 4
        self.ivo[0,2] = 5
        self.ivo[2,0] = 5

        self.name = name
        self.descr = description

    def get_eqv(self):
        """
        equivalent scholar value that represents
        the full tensorial states
        """
        if self.is_stress_available and \
           self.is_strain_available:
            self.get_energy()
            self.get_vm_stress()
            self.epsilon_vm = self.w/self.sigma_vm

            # print 'VM stress:', self.sigma_vm
            # print 'VM strain:', self.epsilon_vm

        elif self.is_stress_available and \
             not (self.is_strain_available):
            self.get_vm_strain()

    def get_energy(self):
        w = 0
        for i in range(3):
            for j in range(3):
                w = w + self.epsilon[i,j] * self.sigma[i,j]
        self.w = w

    def get_deviatoric_stress(self):
        self.sigma_dev = np.zeros(self.sigma.shape)
        ijx = np.identity(3)
        hydro = 0.
        for i in range(3):
            hydro = hydro + self.sigma[i,i]
        for i in range(3):
            for j in range(3):
                self.sigma_dev[i,j] = self.sigma[i,j]\
                                      - 1./3. * hydro * ijx[i,j]

    def get_deviatoric_strain(self):
        self.epsilon_dev = np.zeros(self.epsilon.shape)
        ijx = np.identity(3)
        vol = 0.
        for i in range(3):
            vol = vol + self.epsilon[i,i]
        for i in range(3):
            for j in range(3):
                self.epsilon_dev[i,j] = self.epsilon[i,j]\
                                        - 1./3. * vol * ijx[i,j]

    def get_vm_stress(self):
        """
        Get Von Mises equivalent stress
        """
        self.get_deviatoric_stress()
        vm = 0.
        for i in range(3):
            for j in range(3):
                vm = vm + self.sigma_dev[i,j]**2
        vm = 3./2. * vm
        self.sigma_vm = np.sqrt(vm)

    def get_vm_strain(self):
        """
        Note that VM strain should be calculated based on
        energy conservation. However, there are times only
        strain is available whereas stress isn't. This method
        is intended to be used.
        """
        self.get_deviatoric_strain()
        vm = 0.
        for i in range(3):
            for j in range(3):
                vm = vm + self.epsilon_dev[i,j]**2
        vm = 2./3. * vm
        self.epsilon_vm = np.sqrt(vm)
        self.nstp = len(self.epsilon_vm)

    def plot(self,ifig=1):
        import matplotlib.pyplot as plt
        fig = plt.figure(ifig)
        ax = fig.add_subplot(111)
        for k in range(6):
            if self.flag_6e[k]==1 and self.flag_6s[k]==1:
                i,j = self.vo[k]
                ax.plot(self.epsilon[i,j],self.sigma[i,j],'-x',
                        label='(%i,%i)'%(i+1,j+1))
        ax.legend(loc='best')

    def get_model(self,fn):
        """
        Read stress/strain data from VPSC/EVPSC format STR_STR.OUT
        with an unknown number of head lines (typically 1)
        """
        ## determine nhead from fn
        nhead = find_nhead(fn)
        dat    = np.loadtxt(fn,skiprows=nhead).T
        strain = dat[2:8]
        stress = dat[8:14]
        self.get_6stress(x=stress)
        self.get_6strain(x=strain)

    def get_pmodel(self,fn):
        dat    = np.loadtxt(fn,skiprows=1).T
        stress = dat[6:12]
        strain = dat[12:18]
        self.get_6stress(x=stress)
        self.get_6strain(x=strain)

    def get_pmodel_lat(self,fn):
        dat = np.loadtxt(fn,skiprows=1).T
        e_phl = dat[18:24]
        self.get_6strain(x=e_phl)

    def get_stress(self,x,i,j):
        self.is_stress_available = True
        self.flag_sigma[i,j] = 1
        self.flag_6s[self.ivo[i,j]] = 1
        if len(x)>self.nstp:
            self.size(len(x))
        for k in range(len(x)):
            self.sigma[i,j,k] = x[k]

    def get_strain(self,x,i,j):
        self.is_strain_available = True
        self.flag_epsilon[i,j] = 1
        self.flag_6e[self.ivo[i,j]] = 1
        if len(x)>self.nstp:
            self.size(len(x))
        for k in range(len(x)):
            self.epsilon[i,j,k] = x[k]

    def get_6stress(self,x):
        """
        stress dimension: (6,nstp)
        """
        self.is_stress_available = True
        self.flag_sigma[:,:] = 1
        self.flag_6s[:] = 1
        n = x.shape[-1]
        if n>self.nstp:
            self.size(n)
        for k in range(len(self.vo)):
            i,j = self.vo[k]
            self.sigma[i,j,0:n] = x[k,0:n].copy()
            self.sigma[j,i,0:n] = x[k,0:n].copy()

    def get_6strain(self,x):
        """
        strain dimension: (6,nstp)
        """
        self.is_strain_available = True
        self.flag_epsilon[:,:] = 1
        self.flag_6e[:] = 1
        n = x.shape[-1]
        if n>self.nstp:
            self.size(n)
        for k in range(len(self.vo)):
            i,j = self.vo[k]
            self.epsilon[i,j,0:n] = x[k,0:n].copy()
            self.epsilon[j,i,0:n] = x[k,0:n].copy()

    def get_33stress(self,x):
        for i in range(3):
            for j in range(3):
                self.get_stress(x[i,j],i,j)
    def get_33strain(self,x):
        for i in range(3):
            for j in range(3):
                self.get_strain(x[i,j],i,j)

    def set_zero_sigma_ij(self,i,j):
        self.set_zero_sigma_k(k=self.ivo[i,j])

    def set_zero_epsilon_ij(self,i,j):
        self.set_zero_epsilon_k(k=self.ivo[i,j])

    def set_zero_sigma_k(self,k=None):
        i,j = self.vo[k]
        n = self.nstp
        self.sigma[i,j,0:n] = 0
        self.sigma[j,i,0:n] = 0

    def set_zero_epsilon_k(self,k=None):
        i,j = self.vo[k]
        n = self.nstp
        self.epsilon[i,j,0:n] = 0
        self.epsilon[j,i,0:n] = 0

    def set_zero_shear_strain(self):
        for i in range(3):
            for j in range(3):
                if i!=j: self.set_zero_epsilon_ij(i,j)

    def set_zero_shear_stress(self):
        for i in range(3):
            for j in range(3):
                if i!=j: self.set_zero_sigma_ij(i,j)

    def check(self):
        if self.sigma.shape!=self.epsilon.shape:
            raise IOError, 'Flow data array size is not matched.'

    def set_uni_axial(self):
        self.get_stress([0,100,300,400,500],0,0)
        self.set_zero_sigma_ij(1,1)
        self.set_zero_sigma_ij(2,2)
        self.set_zero_shear_stress()

        self.get_strain([0,0.00001,0.002,0.05,0.015],0,0)
        self.get_strain([0,-0.000003,-0.001,-0.025,-0.0075],1,1)
        self.get_strain([0,-0.000003,-0.001,-0.025,-0.0075],2,2)
        self.set_zero_shear_strain()

    def set_bi_axial(self):
        self.get_stress([0,100,300,400,500],0,0)
        self.get_stress([0,100,300,400,500],1,1)
        self.set_zero_sigma_ij(2,2)
        self.set_zero_shear_stress()

        self.get_strain([0,0.00001,0.002,0.05,0.015],0,0)
        self.get_strain([0,-0.000003,-0.001,-0.025,-0.0075],1,1)
        self.get_strain([0,-0.000003,-0.001,-0.025,-0.0075],2,2)
        self.set_zero_shear_strain()

    def size(self,n):
        oldn = self.nstp
        newsigma   = np.zeros((3,3,n))*np.nan
        newepsilon = np.zeros((3,3,n))*np.nan
        self.nstp = n
        if oldn==0:pass
        if oldn>0:
            for i in range(oldn):
                newsigma[:,:,i] = self.sigma[:,:,i].copy()
                newepsilon[:,:,i] = self.epsilon[:,:,i].copy()

        self.sigma=newsigma.copy()
        self.epsilon=newepsilon.copy()


def true2engi(true_e,true_s):
    engi_e = __truestrain2e__(true_e[::])
    engi_s = true_s/(1+engi_e)
    return engi_e, engi_s

def __truestrain2e__(e):
    """Convert true strain to that of engineering"""
    return np.exp(e)-1.

def __IsEqFlow__(a,b):
    answer = True
    if not((a.flag_sigma==b.flag_sigma).all):
        print 'sigma flag is not matched'
        answer = False
    if not((a.sigma==b.sigma).all):
        print 'sigma is not the same'
        answer = False
    if not((a.flag_epsilon==b.flag_epsilon).all):
        print 'epsilon flag is not matched'
        answer = False
    if not((a.epsilon==b.epsilon).all):
        print 'epsilon is not the same'
        answer = False
    return answer


def average_flow_curve(xs,ys,n=10):
    """
    Return average flow curve
    """
    ndatset = len(xs)
    ## set proper x spacing
    mx = 0
    for i in range(ndatset):
        m = max(xs[i])
        if m>mx: mx = m

    x_ref = np.linspace(0,mx,n)

    ## interpolate each data files
    Y = []
    for i in range(ndatset):
        xp = xs[i]; fp = ys[i]
        y_i = np.interp(x_ref,xp,fp) # new interpolate y
        Y.append(y_i)
    Y = np.array(Y)
    ## average and standard deviation
    avg = []
    std = []
    for i in range(n):
        f = Y.T[i]
        a=np.average(f)
        b=np.std(f)
        avg.append(a)
        std.append(b)

    return x_ref, avg, std


def find_nhead(fn='STR_STR.OUT'):
    """
    Find the number of 'string' heads on an array file

    =========
    Arguments
    fn = 'STR_STR.OUT'

    =======
    Returns
    The number of heads
    """
    f=open(fn,'r');lines=f.readlines();f.close()
    nhead=0
    success=False
    while not(success):
        try:
            map(float,lines[nhead].split())
        except ValueError:
            nhead=nhead+1
        else:
            success=True
    return nhead
            
"""
"""

class WPH:
    """
    May contain its corresponding Flow objective
    with respect to mechanical deformation flow
    """
    def __init__(self,iph=None):
        """
        Argument name: iph
        """
        self.iph=iph
        self.flow = FlowCurve()
        self.nstp = 0
        self.vf = []
        pass
    def get_wph(self,dat,i,j,strain=None,stress=None):
        self.get_vf(dat)
        if strain!=None: self.get_strain(strain,i,j)
        if stress!=None: self.get_stress(stress,i,j)

    def get_vf(self,dat):
        self.vf = dat
        self.nstp = len(self.vf)
    def get_strain(self,dat,i,j):
        self.flow.get_strain(dat,i,j)
    def get_stress(self,dat,i,j):
        self.flow.get_stress(dat,i,j)
    def check(self):
        self.flow.check()
        if self.flow.nstp!=self.nstp:
            raise IOError, 'Flow curve and WPH array size'\
                ' is not matched'
        self.nstp!=self.flow.nstp
