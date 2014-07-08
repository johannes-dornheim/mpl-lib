"""
List of object functions
"""
import numpy as np
import os
import subprocess
def BCC_uniax_voce(parameters=[80,70,340,20],
                   exp_dat=[[0.0,0.1,0.2],[100,150,160]],
                   sx_fn = 'dum'):
                   #sx_fn = 'B_ST_2k_tan_bul_rs.sx'):
    """
    """

    ## Make the single crystal 
    import sx_opt
    tau0,tau1,thet0,thet1 = parameters
    sx_opt.BCC_voce(fn=sx_fn,
                    tau0=tau0,tau1=tau1,thet0=thet0,thet1=thet1,
                    fnout=sx_fn[::])
    ## run the test.
    # iflag=os.system('./vpsc')
    # if iflag!=0: raise IOError,'Error in vpsc'
    std_err=open('stderr_opti.out','w')
    std_out=open('stdout_opti.out','w')
    p=subprocess.Popen(['./vpsc'],stderr=std_err,stdout=std_out)
    p.wait()

    ## compare the curve.
    dat=np.loadtxt('STR_STR.OUT',skiprows=1).T
    mod_dat=[dat[2],dat[8]]
    return diff_two_curves(exp_dat,mod_dat)

def BCC_c3_voce(parameters=[80,70,340,20],
                   exp_dat=[[0.0,0.1,0.2],[100,150,160]],
                   sx_fn = 'dum'):
                   #sx_fn = 'B_ST_2k_tan_bul_rs.sx'):
    """
    """

    ## Make the single crystal 
    import sx_opt
    tau0,tau1,thet0,thet1 = parameters
    sx_opt.BCC_voce(fn=sx_fn,
                    tau0=tau0,tau1=tau1,thet0=thet0,thet1=thet1,
                    fnout=sx_fn[::])
    ## run the test.
    # iflag=os.system('./vpsc')
    # if iflag!=0: raise IOError,'Error in vpsc'
    std_err=open('stderr_opti.out','w')
    std_out=open('stdout_opti.out','w')
    p=subprocess.Popen(['./vpsc'],stderr=std_err,stdout=std_out)
    p.wait()

    print 'parameters: %7.2f %7.2f %7.2f %7.2f'%(parameters[0],parameters[1],parameters[2],parameters[3])

    ## compare the curve.
    dat=np.loadtxt('STR_STR.OUT',skiprows=1).T
    mod_dat=[-dat[4],-dat[10]]
    return diff_two_curves(exp_dat,mod_dat)

def compare_two_curves(dat1, dat2):
    """
    interpolate dat2 based on dat1's x spacings
    """
    import lib
    ys=lib.interpolate_curve(dat2[0],dat2[1],dat1[0])
    new_dat2= [dat1[0],ys]
    return new_dat2

def diff_two_curves(dat1,dat2):
    dat1=np.array(dat1); dat2=np.array(dat2)
    dat2 = compare_two_curves(dat1,dat2)
    y_diffs = np.abs(dat1[1]-dat2[1])
    return np.sqrt(np.sum(y_diffs**2))/(len(y_diffs)-1)
    
    
