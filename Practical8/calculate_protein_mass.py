# create a list to store information
AA = {
    'G': 57.02,
    'A': 71.04,
    'S': 87.03,
    'P': 97.05,
    'V': 99.07,
    'T': 101.05,
    'C': 103.01,
    'I': 113.08,
    'L': 113.08,
    'N': 114.04,
    'D': 115.03,
    'Q': 128.06,
    'K': 128.09,
    'E': 129.04,
    'M': 131.04,
    'H': 137.06,
    'F': 147.07,
    'R': 156.10,
    'Y': 163.06,
    'W': 186.08
}
# write function: takes an AA sequence, create a function that calculates mass
def cal_mass(seq):
    total_mass = 0.00
    for a in seq:
        if a not in AA:
            print("Error,",a,"can't be found") # reports error if AA can't be found
            return None
        total_mass = total_mass + AA[a]
    print(f"The total mass of sequence '{seq}' is {total_mass}")
    return total_mass
# include an example
cal_mass('GGGGGG') 
cal_mass('GGGX')

