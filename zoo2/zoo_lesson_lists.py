criteria_list_list          =   [
            [('groß' or 'riesig') and 'ohren', 'rüssel', 'gut' and 'gedächtnis', 'stoßzähne', 'flieg' or 'flug'],       #Elefant
            [('gut' and 'kleidet') or 'frack' or 'anzug', 'schenk' and 'kieselstein',
            ('brigade' or 'major') and 'general', 'schnabel', 'monogam'],                                               #Pinguin
            ['bärig', ('besitz' or 'gehör') and 'china', 'schwarz' and 'weiß', 'kung' and 'fu', 'bambus'],              #Pandabär
            [('renn' or 'lauf') and'schnell' ,'intelligent', ('krass' or 'toll') and 'super',
             'scharf' and 'zähne', 'raub' and 'tier']]                                                                   #Raptor
animal_list                 =   [
            'Elefant', 'Pinguin', 'Pandabär', 'Raptor']

average_animal_size_weight  =   {
            'Elefant': (260, 4500), 'Pinguin': (60, 4), 'Pandabär': (180, 100), 'Raptor': (None, None)}

probability_list            =   [
            'nur geraten', 'eher unwahrscheinlich', 'eventuell', 'womöglich', 'wahrscheinlich', 'sehr wahrscheinlich']