# Koosta tõeväärtustabel kahele avaldisele
# A AND (B OR C)
# (A  B) OR NOT(C AND A)

# https://docs.google.com/spreadsheets/d/1sUFsE-bOm3isqKUGlIgjZWtdfqv7jDXp9lkch2pNCWc/edit?usp=sharing
# https://beta.wikiversity.org/wiki/V%C3%B5rdlustehted_ja_loogikatehted

# Piilu excel'isse! ;)
# https://docs.google.com/spreadsheets/d/1iDM5PUTLeQMNpQfoar7n52QYeESt42gh3im4WtejwPc/edit#gid=0 


#alamavaldis			        alamavaldised						
#B OR C | A AND (B OR C)|	A ~ B	|C AND A |	NOT(C AND A) |	(A ~ B) OR NOT(C AND A)|			
#  0    |     0		    |     1	    |   0	 |      1	     |           1			   | 
#  1    |     0		    |     1	    |   0	 |      1	     |           1			   | 
#  1    |     0		    |     0	    |   0	 |      1	     |           1			   | 
#  1    |     0		    |     0	    |   0	 |      1	     |           1			   | 
#  0    |     1		    |     0	    |   0	 |      1	     |           1			   | 
#  1    |     1		    |     0	    |   1	 |      0	     |           0			   | 
#  1    |     1		    |     1	    |   0	 |      1	     |           1			   | 
#  1    |     1		    |     1 	|   1	 |      0	     |           1	           | 
		
# A ~ B:                   Kui mõlemad numbrid on samad, siis on tehe tõene. Tõesust märgitakse "1"-ga ja väära "0"-iga
# C AND A:                 (Mõlemas peab olema "1", muidu on "0"	
# NOT(C AND A):            C and A vastand	
# (A ~ B) OR NOT(C AND A): Number peab olema kas A~B tulbas või C and A tulbas, et olla "1"			