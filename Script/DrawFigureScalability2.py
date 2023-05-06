import matplotlib.pyplot as plt
import sys
import os
import math

def main(argv):

    q3_norm = [208068.52797370742,417534.29577496,847260.3423100653,1747882.7239739841,3482701.6775576896,6977686.651,13952619.74]
    q8_norm = [2741.318478,5458.507397,10947.11177,21979.85191,43848.8048,87543.83384,174953.8753]
    multi_q3_e2 = [2671531.1616266626, 3260782.5039237253, 2812042.6639533807, 2707081.7905214946, 2705032.7794909263, 3070957.3502686876, 3824192.624381522]
    multi_q3_e4 = [848404.6532741194, 863888.1224612383, 707516.2050091946, 880116.9285942015, 743681.7309743635, 747235.8733640099, 808074.9303249206]
    multi_q3_e8 = [240188.9342845397, 228498.3901893852, 226159.2035786215, 230020.87054049285, 216561.2997572179, 246324.18122343277, 252213.8372843353]
    multi_q8_e2 = [16186.357619984015, 20384.218834823212, 24078.129587590956, 27986.35178316641, 32566.43019528485, 34341.78988873536, 29901.79186069036]
    multi_q8_e4 = [5441.700420357734, 6656.599608876189, 8003.496363162348, 9182.900618566453, 8926.290028248031, 9827.83371341682, 9165.330470511091]
    multi_q8_e8 = [1944.2725406062, 2378.997602730589, 3207.6204372044863, 2485.185790030577, 2617.619817105748, 2445.598961978577, 2940.6958658331732]
    r2t_q3_e2 = [208068.52797370742, 417534.29577496, 847260.3423100653, 1747882.7239739841, 3482701.6775576896, 6944252.303884126, 11592989.788942158]
    r2t_q3_e4 = [208068.52797370742, 417534.29577496, 847260.3423100653, 1747880.9407661285, 3465990.833792901, 5974145.937485915, 7297421.338709018]
    r2t_q3_e8 = [208068.52797370742, 417534.29577496, 847260.3423100653, 1740019.4374385094, 3088921.855084604, 3852405.3945533317, 4379614.574919878]
    r2t_q8_e2 = [2741.3184783968463, 5458.5073967156995, 10947.111765210037, 21979.85191032915, 43692.75359937085, 72521.12679451822, 91295.88852064167]
    r2t_q8_e4 = [2741.3184783968463, 5458.5073967156995, 10947.111765210037, 21916.543010721187, 37095.00140053172, 47048.48794660848, 60438.661147263956]
    r2t_q8_e8 = [2741.3184783968463, 5458.5073967156995, 10931.14882622213, 19826.36530751677, 24927.89290428883, 32376.295531954747, 37227.824252724]
    multi_q3_e2_t = [5.844515633583069, 12.607048606872558, 28.366321182250978, 91.58172206878662, 585.1216249704361, 2664.29621219635, 12613.746334648133]
    multi_q3_e4_t = [4.7783112049102785, 9.380989146232604, 25.46814396381378, 89.49868357181549, 481.6052212953567, 2852.74926097393, 13403.033118891715]
    multi_q3_e8_t = [4.276804900169372, 8.79414632320404, 26.32092413902283, 89.9076878786087, 541.2616533279419, 2553.7905626296997, 12756.810922288894]
    multi_q8_e2_t = [2.445045256614685, 4.720580804347992, 9.458019828796386, 19.0167262673378, 30.55252207517624, 50.15231604576111, 101.60361292362214]
    multi_q8_e4_t = [2.364026701450348, 4.65984674692154, 9.063939249515533, 18.50276870727539, 26.82757612466812, 51.89220787286759, 105.28431171178818]
    multi_q8_e8_t = [2.139290118217468, 4.344321084022522, 7.316500127315521, 12.351904714107514, 23.856527876853942, 50.787468421459195, 99.96795036792756]
    r2t_q3_e2_t = [5.979205250740051, 7.228609991073609, 10.297780609130859, 14.831916546821594, 10.983900260925292, 18.824261522293092, 26.692825770378114]
    r2t_q3_e4_t = [5.983881545066834, 7.2215039253234865, 10.196041584014893, 14.63450756072998, 11.208322834968566, 14.423419165611268, 26.32177357673645]
    r2t_q3_e8_t = [5.759925532341003, 7.667277383804321, 10.33031804561615, 14.426141858100891, 8.969045615196228, 13.968373560905457, 26.332325649261474]
    r2t_q8_e2_t = [7.355680298805237, 7.327828383445739, 7.3799148321151735, 7.775554418563843, 9.602885818481445, 12.867404675483703, 18.25649423599243]
    r2t_q8_e4_t = [7.365569424629212, 7.353875637054443, 7.554672431945801, 7.836424016952515, 9.687653851509094, 12.857036638259888, 18.195739412307738]
    r2t_q8_e8_t = [7.186484146118164, 7.202412152290345, 7.502514004707336, 7.926180338859558, 9.660654401779174, 12.877122402191162, 18.280356407165527]
    q3_t = [0.270414972,0.625949645,1.171914363,2.252792358,3.848053002,7.762633753,17.07959697]
    q8_t = [0.359623861,0.76525569,0.804084468,0.990594721,2.214243412,4.207965422,8.373177719]
    q3_info = [0.8143151044845581,1.5985900163650513,3.0247764110565187, 5.648025989532471, 9.536720204353333,19.55634970664978,43.89059467315674]
    q8_info = [0.944792366027832,1.8113633155822755,2.015710878372192,2.8039154052734374,5.801902770996094,11.207851576805115,22.17929599285126]

    for i in range(7):
        multi_q3_e2_t[i]+=q3_info[i]
        multi_q3_e4_t[i]+=q3_info[i]
        multi_q3_e8_t[i]+=q3_info[i]
        r2t_q3_e2_t[i]+=q3_info[i]
        r2t_q3_e4_t[i]+=q3_info[i]
        r2t_q3_e8_t[i]+=q3_info[i]
        multi_q8_e2_t[i]+=q8_info[i]
        multi_q8_e4_t[i]+=q8_info[i]
        multi_q8_e8_t[i]+=q8_info[i]
        r2t_q8_e2_t[i]+=q8_info[i]
        r2t_q8_e4_t[i]+=q8_info[i]
        r2t_q8_e8_t[i]+=q8_info[i]
    
    x=['0.125', '0.25', '0.5', '1', '2', '4', '8']
    fig, axes = plt.subplots(2,3, figsize=(24, 6.6))
    axes[0][0].tick_params(axis='both', which='major', labelsize=15)
    axes[0][0].axhline(y=10000,ls="-",c=plt.cm.tab20c(19))
    axes[0][0].axhline(y=100000,ls="-",c=plt.cm.tab20c(19))

    axes[0][0].set_facecolor("white")
    axes[0][0].plot(x, multi_q8_e2,linewidth = 2.5, linestyle = '--',label='PMSJA',
        marker = 'v',markersize = 8,color=plt.cm.tab20c(6),
        markeredgecolor=plt.cm.tab20c(6),markeredgewidth = 2,markerfacecolor=plt.cm.tab20c(6))
    axes[0][0].plot(x, r2t_q8_e2,linewidth = 2.5, linestyle = '-.',label='R2T',
        marker = 's',markersize = 8,color=plt.cm.tab20c(0),
        markeredgecolor=plt.cm.tab20c(0),markeredgewidth = 1,markerfacecolor=plt.cm.tab20c(0))

    axes[0][0].plot(x, q8_norm,linewidth = 2.5,linestyle = ':',label='Query result',
        marker = 'o',markersize = 8,color=plt.cm.tab20c(9),
        markeredgecolor=plt.cm.tab20c(9),markeredgewidth = 1,markerfacecolor=plt.cm.tab20c(9))
    axes[0][0].set_ylabel("Error Level",fontsize=18)
    #axes[0][0].legend(bbox_to_anchor=(0.1, 0.45, 1, 1),fontsize=19,ncol=3, facecolor="white")
    axes[0][0].set_yscale('log')
    axes[0][0].set_xticks([])


    axes[0][1].tick_params(axis='both', which='major', labelsize=15)
    axes[0][1].set_facecolor("white")
    axes[0][1].axhline(y=10000,ls="-",c=plt.cm.tab20c(19))
    axes[0][1].axhline(y=100000,ls="-",c=plt.cm.tab20c(19))

    axes[0][1].plot(x, r2t_q8_e4,linewidth = 2.5, linestyle = '-.',label='R2T',
        marker = 's',markersize = 8,color=plt.cm.tab20c(0),
        markeredgecolor=plt.cm.tab20c(0),markeredgewidth = 1,markerfacecolor=plt.cm.tab20c(0))
    axes[0][1].plot(x, multi_q8_e4,linewidth = 2.5, linestyle = '--',label='PMSJA',
        marker = 'v',markersize = 8,color=plt.cm.tab20c(6),
        markeredgecolor=plt.cm.tab20c(6),markeredgewidth = 2,markerfacecolor=plt.cm.tab20c(6))
    axes[0][1].plot(x, q8_norm,linewidth = 2.5,linestyle = ':',label='Query result',
        marker = 'o',markersize = 8,color=plt.cm.tab20c(9),
        markeredgecolor=plt.cm.tab20c(9),markeredgewidth = 1,markerfacecolor=plt.cm.tab20c(9))
    axes[0][1].set_yscale('log')
    #axes[0][1].set_title("$\mathbf{Q}_{7}$",fontsize=25, y = 1.12)
    axes[0][1].set_xticks([])


    axes[0][2].tick_params(axis='both', which='major', labelsize=15)
    axes[0][2].set_facecolor("white")
    axes[0][2].axhline(y=10000,ls="-",c=plt.cm.tab20c(19))
    axes[0][2].axhline(y=100000,ls="-",c=plt.cm.tab20c(19))

    axes[0][2].plot(x, r2t_q8_e8,linewidth = 2.5, linestyle = '-.',label='R2T',
        marker = 's',markersize = 8,color=plt.cm.tab20c(0),
        markeredgecolor=plt.cm.tab20c(0),markeredgewidth = 1,markerfacecolor=plt.cm.tab20c(0))
    axes[0][2].plot(x, multi_q8_e8,linewidth = 2.5, linestyle = '--',label='PMSJA',
        marker = 'v',markersize = 8,color=plt.cm.tab20c(6),
        markeredgecolor=plt.cm.tab20c(6),markeredgewidth = 2,markerfacecolor=plt.cm.tab20c(6))
    axes[0][2].plot(x, q8_norm,linewidth = 2.5,linestyle = ':',label='Query result',
        marker = 'o',markersize = 8,color=plt.cm.tab20c(9),
        markeredgecolor=plt.cm.tab20c(9),markeredgewidth = 1,markerfacecolor=plt.cm.tab20c(9))
    axes[0][2].set_yscale('log')
    axes[0][2].set_xticks([])



    axes[1][0].tick_params(axis='both', which='major', labelsize=15)
    axes[1][0].set_facecolor("white")
    axes[1][0].axhline(y=10,ls="-",c=plt.cm.tab20c(19))
    axes[1][0].axhline(y=100,ls="-",c=plt.cm.tab20c(19))
    axes[1][0].axhline(y=1,ls="-",c=plt.cm.tab20c(19))
    axes[1][0].plot(x, r2t_q8_e2_t,linewidth = 2.5, linestyle = '-.',label='R2T',
        marker = 's',markersize = 8,color=plt.cm.tab20c(0),
        markeredgecolor=plt.cm.tab20c(0),markeredgewidth = 1,markerfacecolor=plt.cm.tab20c(0))
    axes[1][0].plot(x, multi_q8_e2_t,linewidth = 2.5, linestyle = '--',label='PMSJA',
        marker = 'v',markersize = 8,color=plt.cm.tab20c(6),
        markeredgecolor=plt.cm.tab20c(6),markeredgewidth = 2,markerfacecolor=plt.cm.tab20c(6))
    axes[1][0].plot(x, q8_t,linewidth = 2.5,linestyle = ':',label='Query result',
        marker = 'o',markersize = 8,color=plt.cm.tab20c(9),
        markeredgecolor=plt.cm.tab20c(9),markeredgewidth = 1,markerfacecolor=plt.cm.tab20c(9))
    axes[1][0].set_yscale('log')
    axes[1][0].set_ylabel("Running Time(s)",fontsize=18)
    axes[1][0].set_xlabel("Scale",fontsize=16)

    axes[1][1].tick_params(axis='both', which='major', labelsize=15)
    axes[1][1].set_facecolor("white")
    axes[1][1].axhline(y=100,ls="-",c=plt.cm.tab20c(19))
    axes[1][1].axhline(y=10,ls="-",c=plt.cm.tab20c(19))
    axes[1][1].axhline(y=1,ls="-",c=plt.cm.tab20c(19))
    axes[1][1].plot(x, r2t_q8_e4_t,linewidth = 2.5, linestyle = '-.',label='R2T',
        marker = 's',markersize = 8,color=plt.cm.tab20c(0),
        markeredgecolor=plt.cm.tab20c(0),markeredgewidth = 1,markerfacecolor=plt.cm.tab20c(0))
    axes[1][1].plot(x, multi_q8_e4_t,linewidth = 2.5, linestyle = '--',label='PMSJA',
        marker = 'v',markersize = 8,color=plt.cm.tab20c(6),
        markeredgecolor=plt.cm.tab20c(6),markeredgewidth = 2,markerfacecolor=plt.cm.tab20c(6))
    axes[1][1].plot(x, q8_t,linewidth = 2.5,linestyle = ':',label='Query result',
        marker = 'o',markersize = 8,color=plt.cm.tab20c(9),
        markeredgecolor=plt.cm.tab20c(9),markeredgewidth = 1,markerfacecolor=plt.cm.tab20c(9))
    axes[1][1].set_yscale('log')
    axes[1][1].set_xlabel("Scale",fontsize=16)

    axes[1][2].tick_params(axis='both', which='major', labelsize=15)
    axes[1][2].set_facecolor("white")
    axes[1][2].axhline(y=100,ls="-",c=plt.cm.tab20c(19))
    axes[1][2].axhline(y=10,ls="-",c=plt.cm.tab20c(19))
    axes[1][2].axhline(y=1,ls="-",c=plt.cm.tab20c(19))
    axes[1][2].plot(x, r2t_q8_e8_t,linewidth = 2.5, linestyle = '-.',label='R2T',
        marker = 's',markersize = 8,color=plt.cm.tab20c(0),
        markeredgecolor=plt.cm.tab20c(0),markeredgewidth = 1,markerfacecolor=plt.cm.tab20c(0))
    axes[1][2].plot(x, multi_q8_e8_t,linewidth = 2.5, linestyle = '--',label='PMSJA',
        marker = 'v',markersize = 8,color=plt.cm.tab20c(6),
        markeredgecolor=plt.cm.tab20c(6),markeredgewidth = 2,markerfacecolor=plt.cm.tab20c(6))
    axes[1][2].plot(x, q8_t,linewidth = 2.5,linestyle = ':',label='Query result',
        marker = 'o',markersize = 8,color=plt.cm.tab20c(9),
        markeredgecolor=plt.cm.tab20c(9),markeredgewidth = 1,markerfacecolor=plt.cm.tab20c(9))
    axes[1][2].set_yscale('log')
    axes[1][2].set_xlabel("Scale",fontsize=16)  
    axes[1][2].set_title('$𝜀 =8$', y=-0.45, fontsize=22)
    axes[1][1].set_title('$𝜀=4$', y=-0.45, fontsize=22)
    axes[1][0].set_title('$𝜀=2$', y=-0.45, fontsize=22)

    plt.savefig("../Figure/Scalability2.pdf", bbox_inches='tight')









if __name__ == "__main__":
   main(sys.argv[1:])