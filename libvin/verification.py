"""
Copyright Lukasz Szybalski
VIN Vehicle information number checker,
Inputs vin number and outputs true/false 
"""
from libvin.static import ALPHA_NUMBER_CONVERSION, VIN_ENTRY_ERROR_MAP


def convert_vin(field):
    """Stores alpha to number conversion as defined by the vehicle information number standard.
    """
    if field.isdigit():
        return int(field)
    else:
        if field in ALPHA_NUMBER_CONVERSION:
            return ALPHA_NUMBER_CONVERSION[field]
        else:
            return False
            
def is_valid_vin(vin):
    """
    Vehicle Information Number. This will return whether the entered vin number is authentic/correct.
    
    Example:
    
    >>> import libvin
    >>> libvin.is_valid_vin(my_vin_number)
    """
    vin=str(vin).strip()
    if len(vin) != 17:
        return False
    else:
        converted=[]
        vin=vin.upper()
        for i in range(len(vin)):
            converted.insert(i,convert_vin(vin[i]))
        multiplier=[8,7,6,5,4,3,2,10,0,9,8,7,6,5,4,3,2]
        add=0
        for i in range(len(vin)):
            add+=(converted[i]*multiplier[i])
        final= (add%11)
        if final ==10:
            final='x'
        if str(final)==vin[8]:
            return True
        else:
            return False

def repair_vin(vin):
	"""
	Attempts to repair a VIN for common data entry errors.
	
	"""
	o = ''
	vin = vin.upper()
	
	for c in vin:
		if c in VIN_ENTRY_ERROR_MAP:
			o += VIN_ENTRY_ERROR_MAP[c]
		else:
			o += c
	
	return o
		
