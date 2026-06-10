import numpy as np

v_in = 16.8 #max input voltage
v_out = 12
I_out = 3.5
f_sw = 1000e3
I_idle = 0.5
dI_out = I_out - I_idle
v_tolerance = 0.05
dv_out = v_out * v_tolerance
v_out_ripple = 0.01 * v_out

######Inductor######################################
K = 0.3
L_out = (v_in-v_out)/(I_out*K) * v_out/(v_in*f_sw)

L_out = 3.3e-6

#Therefore I_ripple:
I_ripple = (v_out * (v_in - v_out)) / (v_in * L_out * f_sw)


#####Capacitors#####################################
C_out1 = (2*dI_out)/(f_sw*dv_out)                #Load step (system running from idle to full power).

C_out2_upper = L_out * ((I_out**2)-(I_idle**2))  
C_out2_lower = (v_out + dv_out)**2 - v_out**2  

C_out2 = C_out2_upper/C_out2_lower #Inductor energy dump

C_out3 = (1/(8*f_sw)) * 1/(v_out_ripple/I_ripple) # Ripple

D = v_out/v_in
C_out4 = dI_out/(f_sw*dv_out*K) * ((1-D)*(1+K)+(K**2)/12 * (2-D))

C_out = [C_out1, C_out2, C_out3, C_out4]

C_FF = (v_out*max(C_out)) / (120*100e3 * np.sqrt(1/v_out))



print(
    f"Output inductor:  {L_out} H\n"
    f"Output ripple:    {I_ripple} A\n"
    f"Output capacitor: {max(C_out)*1e6} uF\n"
    f"C_FF: {C_FF*1e12} pF\n"
)


