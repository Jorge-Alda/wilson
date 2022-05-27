from wilson import Wilson

w1 = Wilson({'ALPfa': 1e-6, 'ALPWW': 1e-6},
            basis='Warsaw', eft='SMEFT', scale=1000)
w2 = w1.match_run(basis='Warsaw', eft='SMEFT', scale=250)
print(w2.values['ALPWW'])
