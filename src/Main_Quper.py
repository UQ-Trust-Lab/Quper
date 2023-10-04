
from past.builtins import execfile
import sys
sys.path.append('./completeness')
sys.path.append('./timeliness')
sys.path.append('./availability')
sys.path.append('./readability')
import completeness.predict_content
from completeness.compliance_of_disclosure import all_process
from completeness.compliance_of_disclosure import list_files
print('Result of compliance_of_disclosure')
execfile('./completeness/compliance_of_disclosure.py')
print("********************************************************************************************************************")
print('Result of timeliness')
execfile('./timeliness/timeline.py')
print("********************************************************************************************************************")
print('Result of availability')
execfile('./availability/get_external_link.py')
execfile('./availability/get_language_type.py')
print("********************************************************************************************************************")
print('Result of readability')
execfile('./readability/doubleNeg_obscure_qualifiers.py')
execfile('./readability/main_idea_location.py')
execfile('./readability/readability.py')