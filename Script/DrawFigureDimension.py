import matplotlib.pyplot as plt
import sys
import os
import math

def main(argv):
    multi_E2 = [181435.4169, 291174.6131, 527564.0982, 708634.0794, 1330936.594, 1631169.76]
    multi_E4 = [52095.61369, 103119.62, 141657.6993, 184384.5553, 254791.8582, 433693.1547]
    multi_E8 = [21481.66497, 32103.91153, 39734.41831, 64734.48259, 87524.99883, 112615.6658]
    R2T_E2 = [347247.0502, 664917.6655, 1156402.81, 1788325.2458283834, 2559015.5831085346, 3568522.362646447]
    R2T_E4 = [207516.9559, 442617.0226, 831793.8583, 1483360.7078492541, 2467542.009816089, 3563669.001998989]
    R2T_E8 = [123551.537, 261645.9375, 534081.7792, 1043572.358, 1899963.78894, 3252334.8452]
    norms = [621780.7906, 899431.3441, 1273136.29, 1807686.25, 2561262.122, 3569938.26]


    multi_t2 = [7.870679092+4.91277322769165,18.91249013+5.3537677526474,37.34551238+6.83741250038147,75.16423969+7.7467738628387455,112.0329319+12.969057559967041,246.2638864+20.457154417037962]
    multi_t4 = [7.822011602+4.91277322769165,16.48362031+5.3537677526474,28.77259663+6.83741250038147,52.2303207+7.7467738628387455,106.2918244+12.969057559967041,252.7183057+20.457154417037962]
    multi_t8 = [7.526344633+4.91277322769165,14.63591934+5.3537677526474,23.84233632+6.83741250038147,52.62183063+7.7467738628387455,108.0498507+12.969057559967041,277.1995386+20.457154417037962]
    R2T_t2 = [2.208941722+4.91277322769165,4.576289177+5.3537677526474,9.134165525+6.83741250038147,18.34113441+7.7467738628387455,36.556795+12.969057559967041,72.97905729+20.457154417037962]
    R2T_t4 = [2.212045407+4.91277322769165,4.55089228+5.3537677526474,9.128172088+6.83741250038147,18.44434123+7.7467738628387455,36.63396974+12.969057559967041,73.08873255+20.457154417037962]
    R2T_t8 = [2.178207278+4.91277322769165,4.530453634+5.3537677526474,9.078847432+6.83741250038147,18.32820132+7.7467738628387455,36.6385232+12.969057559967041,73.13158507+20.457154417037962]
    query_time = [2.27315824,2.37157464,3.276722121,3.559090066,3.807260633,4.653567863]
    x=['12', '25', '50', '100', '200', '400']
    fig, axes = plt.subplots(2,3, figsize=(24, 6.6))
    axes[0][0].tick_params(axis='both', which='major', labelsize=15)
    axes[0][0].axhline(y=100000,ls="-",c=plt.cm.tab20c(19))
    axes[0][0].axhline(y=1000000,ls="-",c=plt.cm.tab20c(19))
    axes[0][0].set_facecolor("white")
    axes[0][0].plot(x, multi_E2,linewidth = 2.5, linestyle = '--',label='PMSJA',
        marker = 'v',markersize = 8,color=plt.cm.tab20c(6),
        markeredgecolor=plt.cm.tab20c(6),markeredgewidth = 2,markerfacecolor=plt.cm.tab20c(6))
    axes[0][0].plot(x, R2T_E2,linewidth = 2.5, linestyle = '-.',label='R2T',
        marker = 's',markersize = 8,color=plt.cm.tab20c(0),
        markeredgecolor=plt.cm.tab20c(0),markeredgewidth = 1,markerfacecolor=plt.cm.tab20c(0))

    axes[0][0].plot(x, norms,linewidth = 2.5,linestyle = ':',label='Query result',
        marker = 'o',markersize = 8,color=plt.cm.tab20c(9),
        markeredgecolor=plt.cm.tab20c(9),markeredgewidth = 1,markerfacecolor=plt.cm.tab20c(9))
    #axes[0][0].set_title('$\epsilon =2}$',fontsize=18)
    axes[0][0].set_ylabel("Error Level",fontsize=18)
    axes[0][0].legend(bbox_to_anchor=(0.1, 0.45, 1, 1),fontsize=19,ncol=3, facecolor="white")
    axes[0][0].set_yscale('log')
    axes[0][0].set_xticks([])


    axes[0][1].tick_params(axis='both', which='major', labelsize=15)
    axes[0][1].set_facecolor("white")
    axes[0][1].axhline(y=100000,ls="-",c=plt.cm.tab20c(19))
    axes[0][1].axhline(y=1000000,ls="-",c=plt.cm.tab20c(19))
    axes[0][1].plot(x, R2T_E4,linewidth = 2.5, linestyle = '-.',label='R2T',
        marker = 's',markersize = 8,color=plt.cm.tab20c(0),
        markeredgecolor=plt.cm.tab20c(0),markeredgewidth = 1,markerfacecolor=plt.cm.tab20c(0))
    axes[0][1].plot(x, multi_E4,linewidth = 2.5, linestyle = '--',label='PMSJA',
        marker = 'v',markersize = 8,color=plt.cm.tab20c(6),
        markeredgecolor=plt.cm.tab20c(6),markeredgewidth = 2,markerfacecolor=plt.cm.tab20c(6))
    axes[0][1].plot(x, norms,linewidth = 2.5,linestyle = ':',label='Query result',
        marker = 'o',markersize = 8,color=plt.cm.tab20c(9),
        markeredgecolor=plt.cm.tab20c(9),markeredgewidth = 1,markerfacecolor=plt.cm.tab20c(9))
    axes[0][1].set_yscale('log')
    #axes[0][1].set_title("$\mathbf{Q}_{8}$",fontsize=25, y=1.12)
    axes[0][1].set_xticks([])



    axes[0][2].tick_params(axis='both', which='major', labelsize=15)
    axes[0][2].set_facecolor("white")
    axes[0][2].axhline(y=1000000,ls="-",c=plt.cm.tab20c(19))
    axes[0][2].axhline(y=100000,ls="-",c=plt.cm.tab20c(19))
    axes[0][2].plot(x, R2T_E8,linewidth = 2.5, linestyle = '-.',label='R2T',
        marker = 's',markersize = 8,color=plt.cm.tab20c(0),
        markeredgecolor=plt.cm.tab20c(0),markeredgewidth = 1,markerfacecolor=plt.cm.tab20c(0))
    axes[0][2].plot(x, multi_E8,linewidth = 2.5, linestyle = '--',label='PMSJA',
        marker = 'v',markersize = 8,color=plt.cm.tab20c(6),
        markeredgecolor=plt.cm.tab20c(6),markeredgewidth = 2,markerfacecolor=plt.cm.tab20c(6))
    axes[0][2].plot(x, norms,linewidth = 2.5,linestyle = ':',label='Query result',
        marker = 'o',markersize = 8,color=plt.cm.tab20c(9),
        markeredgecolor=plt.cm.tab20c(9),markeredgewidth = 1,markerfacecolor=plt.cm.tab20c(9))
    axes[0][2].set_yscale('log')
    axes[0][2].set_xticks([])



    axes[1][0].tick_params(axis='both', which='major', labelsize=15)
    axes[1][0].set_facecolor("white")
    axes[1][0].axhline(y=100,ls="-",c=plt.cm.tab20c(19))
    axes[1][0].axhline(y=10,ls="-",c=plt.cm.tab20c(19))
    axes[1][0].axhline(y=1,ls="-",c=plt.cm.tab20c(19))
    axes[1][0].plot(x, R2T_t2,linewidth = 2.5, linestyle = '-.',label='R2T',
        marker = 's',markersize = 8,color=plt.cm.tab20c(0),
        markeredgecolor=plt.cm.tab20c(0),markeredgewidth = 1,markerfacecolor=plt.cm.tab20c(0))
    axes[1][0].plot(x, multi_t2,linewidth = 2.5, linestyle = '--',label='PMSJA',
        marker = 'v',markersize = 8,color=plt.cm.tab20c(6),
        markeredgecolor=plt.cm.tab20c(6),markeredgewidth = 2,markerfacecolor=plt.cm.tab20c(6))
    axes[1][0].plot(x, query_time,linewidth = 2.5,linestyle = ':',label='Query result',
        marker = 'o',markersize = 8,color=plt.cm.tab20c(9),
        markeredgecolor=plt.cm.tab20c(9),markeredgewidth = 1,markerfacecolor=plt.cm.tab20c(9))
    axes[1][0].set_yscale('log')
    axes[1][0].set_ylabel("Running Time(s)",fontsize=18)
    axes[1][0].set_xlabel("d",fontsize=18)

    axes[1][1].tick_params(axis='both', which='major', labelsize=15)
    axes[1][1].set_facecolor("white")
    axes[1][1].axhline(y=100,ls="-",c=plt.cm.tab20c(19))
    axes[1][1].axhline(y=10,ls="-",c=plt.cm.tab20c(19))
    axes[1][1].axhline(y=1,ls="-",c=plt.cm.tab20c(19))
    axes[1][1].plot(x, R2T_t4,linewidth = 2.5, linestyle = '-.',label='R2T',
        marker = 's',markersize = 8,color=plt.cm.tab20c(0),
        markeredgecolor=plt.cm.tab20c(0),markeredgewidth = 1,markerfacecolor=plt.cm.tab20c(0))
    axes[1][1].plot(x, multi_t4,linewidth = 2.5, linestyle = '--',label='PMSJA',
        marker = 'v',markersize = 8,color=plt.cm.tab20c(6),
        markeredgecolor=plt.cm.tab20c(6),markeredgewidth = 2,markerfacecolor=plt.cm.tab20c(6))
    axes[1][1].plot(x, query_time,linewidth = 2.5,linestyle = ':',label='Query result',
        marker = 'o',markersize = 8,color=plt.cm.tab20c(9),
        markeredgecolor=plt.cm.tab20c(9),markeredgewidth = 1,markerfacecolor=plt.cm.tab20c(9))
    axes[1][1].set_yscale('log')
    axes[1][1].set_xlabel("d",fontsize=18)

    axes[1][2].tick_params(axis='both', which='major', labelsize=15)
    axes[1][2].set_facecolor("white")
    axes[1][2].axhline(y=100,ls="-",c=plt.cm.tab20c(19))
    axes[1][2].axhline(y=10,ls="-",c=plt.cm.tab20c(19))
    axes[1][2].axhline(y=1,ls="-",c=plt.cm.tab20c(19))
    axes[1][2].plot(x, R2T_t8,linewidth = 2.5, linestyle = '-.',label='R2T',
        marker = 's',markersize = 8,color=plt.cm.tab20c(0),
        markeredgecolor=plt.cm.tab20c(0),markeredgewidth = 1,markerfacecolor=plt.cm.tab20c(0))
    axes[1][2].plot(x, multi_t8,linewidth = 2.5, linestyle = '--',label='PMSJA',
        marker = 'v',markersize = 8,color=plt.cm.tab20c(6),
        markeredgecolor=plt.cm.tab20c(6),markeredgewidth = 2,markerfacecolor=plt.cm.tab20c(6))
    axes[1][2].plot(x, query_time,linewidth = 2.5,linestyle = ':',label='Query result',
        marker = 'o',markersize = 8,color=plt.cm.tab20c(9),
        markeredgecolor=plt.cm.tab20c(9),markeredgewidth = 1,markerfacecolor=plt.cm.tab20c(9))
    axes[1][2].set_yscale('log')
    axes[1][2].set_xlabel("d",fontsize=18) 
    #plt.text( 0, 0,'$\epsilon =8$', size = 28 )
    axes[1][2].set_title('$𝜀 =8$', y=-0.45, fontsize=22)
    axes[1][1].set_title('$𝜀=4$', y=-0.45, fontsize=22)
    axes[1][0].set_title('$𝜀=2$', y=-0.45, fontsize=22)


    plt.savefig("../Figure/Dimension.pdf", bbox_inches='tight')



if __name__ == "__main__":
   main(sys.argv[1:])