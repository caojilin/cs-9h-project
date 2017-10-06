def start_interface():
    #To Start the program
    print("Welcome to our Python-powered Unit Converter v2.0 by Cjl!")
    print("You can convert Distances , Weights , Volumes to one another, but only")
    print("within units of the same category, which are shown below. E.g.: 1 mi in ft")
    print()
    print("Distances: ft cm mm mi m yd km in")
    print("","Weights: lb mg kg oz g")
    print("","Volumes: floz qt cup mL L gal pint")
    print()
start_interface()

def convert_to_base(source_unit,source_num,d_unit):
    '''take a source_unit to see if it is base unit, if it's not convert it to base unit
        return a converted num in given unit
    '''

    """Distances: ft cm mm mi m yd km in
       Weights: lb mg kg oz g
       Volumes: floz qt cup mL L gal pint
    """
    distance ={'ft':3.28084,'cm':100,'mm':1000,'mi':0.000621371,'m':1,'yd':1.09361,'km':0.001,'in':39.3701}
    Weights = {'lb':2.20462,'mg':1000000,'kg':1,'oz':35.274,'g':1000}
    Volumes = {'floz':33.814,'qt':1.05669,'cup':4.22675,'mL':1000,'L':1,'gal':0.264172,'pint':2.11338}
    source_num = float(source_num)
    if in_distance(source_unit):
        if source_unit is 'm':
            return source_num * distance[d_unit]
        elif d_unit is 'm':
            return source_num / distance[source_unit]
        else:
            base_num = source_num / distance[source_unit]
            return base_num * distance[d_unit]
    if in_weight(source_unit):
        if source_unit is 'kg':
            return source_num * Weights[d_unit]
        elif d_unit is 'kg':
            return source_num / Weights[d_unit]
        else:
            base_num = source_num / Weights[source_unit]
            return base_num * Weights[d_unit]
    if in_volume(source_unit):
        if source_unit is 'L':
            return source_num * Volumes[d_unit]
        elif d_unit is 'L':
            return source_num / Volumes[d_unit]
        else:
            base_num = source_num / Volumes[source_unit]
            return base_num * Volumes[d_unit]
"""
To see if the data is in the given units
"""
distance_dict = 'ft cm mm mi m yd km in'
weight_dict = 'lb mg kg oz g'
volume_dict = 'floz qt cup mL L gal pint'

def in_distance(str):
    return True if str in distance_dict else False

def in_weight(str):
    return True if str in weight_dict else False

def in_volume(str):
    return True if str in volume_dict else False



while True:# program will excecute until close it
    '''Take input from user'''
    try: #User may put wrong info
        input_data = input('Convert [AMT SOURCE_UNIT in DEST_UNIT, or (q)uit]: ')
        ''' User may input like this:
            10 mi in m
            1 lb in oz
            123.456789 kg in mg
        '''
        if input_data in ['q','quit']:
            print("Thanks for converting with us. Y'all come back now, y'hear?")
            exit()

        the_list = input_data.split(" ")
        source_num = the_list[0]
        source_unit = the_list[1]
        d_unit = the_list[3]
        output = convert_to_base(source_unit,source_num,d_unit)
        print(source_num,source_unit,"=",output,d_unit)
    except(ValueError,Exception):
        print('WRONG FORMAT')
