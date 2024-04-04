score_agro3 = 0
score_slc = 0

#Primeira posição é Brasil Agro e segunda SLC Aggr

#Factors:
#Value - Identify overvalued and undervalued stocks
#Momentum - something that has been doing well will or not continue to do well
#Quality - tries to get at fundamental based statistics
#Volatily - depends on market regime and what you're trying to do
#Growth

# rank all securities in your universe from lowest factor exposure to highest


big_factor = [roe, m_ebitda, d_pl, liq_cor, pe, dy, ev_ebitda]

def comparador(score_1, score_2, factor):
    if factor == d_pl:
        if factor[0] < factor[1]:
            score_1 = score_1 + 1
        else:
           score_2 = score_2 + 1 
    else:
       if factor[0] > factor[1]:
           score_1 = score_1 + 1
       else:
          score_2 = score_2 + 1 

       return score_1, score_2


for i in big_factor:
    score_agro3, score_slc = comparador(score_agro3, score_slc, big_factor)
    
if score_agro3 > score_slc:
    buy = 'Brasil Agro'
    score_buy = score_agro3
    sell = 'SLC Agrícola'
    score_sell = score_slc
else:
    buy = 'SLC Agrícola'
    score_buy = score_slc
    sell = 'Brasil Agro'
    score_sell = score_agro3
        
print('-----------------------Recomendação-----------------------')
print('Buy: ' + buy + '   Score: ' + str(score_buy))
print('Sell: ' + sell + '   Score: ' + str(score_sell)) 
print('Os fatores analisados foram Lucratividade, Qualidade e Valor')
print('----------------------------------------------------------')
