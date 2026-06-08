K = 0.3
v_in = 16.8 #max input voltage
v_out = 12
I_out = 3.5
f_sw = 900e3

L_out = (v_in-v_out)/(I_out*K) * v_out/(v_in*f_sw)

print("Output inductor is: ", L_out)
