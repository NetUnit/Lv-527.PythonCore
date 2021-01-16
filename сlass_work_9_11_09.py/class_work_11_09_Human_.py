import numpy as np
from math import sqrt
import string
import re
import time

# classwork3 - 'class Polygon' - SoftServe#9 - Lesson9 OOP


'''
    Create a class Human, everyone has a name, create a method in the class that
    displays a welcome message to a each person. Create a class method in the class
    that returns information that it is a species of "Homosapiens". And also in the
    class create a static method that returns an arbitrary message.
'''


class RoughData:

    '''
        I just pasted this data from the:
            https://www.babynamewizard.com/the-top-1000-baby-names-of \
            -2011-united-states-of-america

    '''

    data_raw = 'Sophia	21695	2	 	1	Jacob	20153	1 \
    2	Isabella	19745	1	 	2	Mason	19396	12 \
    3	Emma	18674	3	 	3	William	17151	5 \
    4	Olivia	17169	4	 	4	Jayden	16861	4 \
    5	Ava	15383	5	 	5	Noah	16719	7 \
    6	Emily	14164	6	 	6	Michael	16598	3 \
    7	Abigail	13149	7	 	7	Ethan	16567	2 \
    8	Madison	12298	8	 	8	Alexander	15591	6 \
    9	Mia	11451	10	 	9	Aiden	15389	9 \
    10	Chloe	10917	9	 	10	Daniel	15138	8 \
    11	Elizabeth	9972	12	 	11	Anthony	14181	10 \
    12	Ella	9501	13	 	12	Matthew	14051	16 \
    13	Addison	9246	11	 	13	Elijah	13817	18 \
    14	Natalie	8593	14	 	14	Joshua	13601	11 \
    15	Lily	8112	17	 	15	Liam	13347	30 \
    16	Grace	7560	18	 	16	Andrew	13152	14 \
    17	Samantha	7330	15	 	17	James	13133	19 \
    18	Avery	7303	23	 	18	David	13098	15 \
    19	Sofia	7285	26	 	19	Benjamin	12942	22 \
    20	Aubrey	7135	44	 	20	Logan	12913	17 \
    21	Brooklyn	7115	34	 	21	Christopher	12885	13 \
    22	Lillian	6857	21	 	22	Joseph	12798	20 \
    23	Victoria	6832	32	 	23	Jackson	12277	25 \
    24	Evelyn	6670	39	 	24	Gabriel	12226	21 \
    25	Hannah	6497	22	 	25	Ryan	11424	23 \
    26	Alexis	6482	16	 	26	Samuel	11198	24 \
    27	Charlotte	6365	45	 	27	John	10934	26 \
    28	Zoey	6354	47	 	28	Nathan	10421	27 \
    29	Leah	6337	24	 	29	Lucas	10324	35 \
    30	Amelia	6307	41	 	30	Christian	10228	29 \
    31	Zoe	6234	31	 	31	Jonathan	10145	28 \
    32	Hailey	6232	19	 	32	Caleb	9915	33 \
    33	Layla	6048	37	 	33	Dylan	9701	31 \
    34	Gabriella	6040	33	 	34	Landon	9700	32 \
    35	Nevaeh	6030	25	 	35	Isaac	9508	39 \
    36	Kaylee	5999	35	 	36	Gavin	8971	37 \
    37	Alyssa	5962	20	 	37	Brayden	8962	40 \
    38	Anna	5601	28	 	38	Tyler	8759	34 \
    39	Sarah	5472	30	 	39	Luke	8636	41 \
    40	Allison	5426	38	 	40	Evan	8584	36 \
    41	Savannah	5406	46	 	41	Carter	8549	48 \
    42	Ashley	5368	27	 	42	Nicholas	8517	38 \
    43	Audrey	5183	52	 	43	Isaiah	8411	45 \
    44	Taylor	5157	36	 	44	Owen	8281	47 \
    45	Brianna	5156	29	 	45	Jack	8118	44 \
    46	Aaliyah	5082	56	 	46	Jordan	8008	46 \
    47	Riley	5002	40	 	47	Brandon	7764	43 \
    48	Camila	4956	61	 	48	Wyatt	7626	57 \
    49	Khloe	4918	42	 	49	Julian	7558	53 \
    50	Claire	4871	53	 	50	Aaron	7555	55'

    def __init__(self, data_raw=data_raw):
        self.data_raw = data_raw

    def remove_garbage(self):
        cleaner = (re.sub(r'[\d]', ' ', self.data_raw)).split()
        return cleaner


cleaning = RoughData()
cleaned = cleaning.remove_garbage()


'''
    !!! ВАЖЛИВО:
        cleaned вже є в глобальному просторі Python,
        тому можемо ним користуватися в КЛАСІ Human
'''


class Human:

    hum_1 = 'Kelly'
    hum_2 = 'John'
    hum_3 = 'Silvia'
    names = cleaned

    def __init__(self, hum_1=hum_1, hum_2=hum_2, hum_3=hum_3, names=names):
        self.hum_1 = hum_1
        self.hum_2 = hum_2
        self.hum_3 = hum_3
        self.names = names

    def __str__(self):
        return 'The names of our humans r: %s, %s and %s' % (self.hum_1, self.hum_2, self.hum_3)

    def reg_greetings(self):
        return 'Hi: %s, %s and %s. All the best to U guys in 2021' % (self.hum_1, self.hum_2, self.hum_3)

    def sep_greeting(self):
        inquiry = input('Please enter your name: ')
        if inquiry in [self.hum_1, self.hum_2, self.hum_3]:
            return 'This program sends special greetings to \'%s\'. Have a nice day \'%s\'!' % (inquiry, inquiry)
        else:
            return 'I\'m afraid we can\'t send U a special greeting \'%s\'. Have a nice day \'%s\'!' % inquiry, inquiry)

    # if this method runs it means that class Rough Data has been done properly
    def check_out_names(self):
        return self.names

    def human_not_human(self):
        inquiry=input('Please set-up the person\'s name: ')
        return 'Huhh. This person is definitely a \'Homosapiens\' type of specie' if inquiry in self.names else 'Crap :}. We may invite an animal to the party!'

    # allows us to use this algorithm without gigving a method parameter
    @ staticmethod
    def warn_message():
        return 'Dear user, convincing request to execute the RoughData class, in order to provide the animal control'


instance1=Human()

# 1.1 welcome message to each person
print(instance1.reg_greetings())

# 1.2 separate welcome (additional method)
print(instance1.sep_greeting())

# 1.3 call of the class attributes
print(f'{Human.hum_1}, {Human.hum_2}, {Human.hum_3}: special guests')

# 1.4 call of the class attributes and sort in alphabeticall order
print(sorted([getattr(Human, 'hum_3'), getattr(Human, 'hum_2'), getattr(
    Human, 'hum_1')]), 'special guests in aplhabetical order')

# checkout if cleaner implemented in our class
# print(instance1.check_out_names())
# print(Human.names)


instance2=Human()
# 2.1 homosapiens check-out (if don't want to invite an animal to the party)
print(instance2.human_not_human())

# warning message through staticmethod
time.sleep(1)
instance3=Human()
print(instance3.warn_message())
