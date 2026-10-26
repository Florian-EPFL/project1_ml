# semantic grouping of features based on the BRFSS codebook 
# each group contains a list of original and derived features

FEATURE_GROUPS = {
    "survey_administration": [
        "_STATE", "FMONTH", "IDATE", "IMONTH", "IDAY", "IYEAR", "DISPCODE", "SEQNO",
        "_PSU", "CTELENUM", "PVTRESD1", "COLGHOUS", "STATERES", "CELLFON3", "LADULT",
        "NUMADULT", "NUMMEN", "NUMWOMEN", "CTELNUM1", "CELLFON2", "CADULT", "PVTRESD2",
        "CCLGHOUS", "CSTATE", "LANDLINE", "HHADULT", "QSTVER", "QSTLANG", "MSCODE",
        "_STSTR", "_STRWT", "_RAWRAKE", "_WT2RAKE", "_CLLCPWT", "_DUALUSE", "_DUALCOR",
        "_LLCPWT"],

    "demographics_socioeconomic": [
        "SEX", "MARITAL", "EDUCA", "RENTHOM1", "NUMHHOL2", "NUMPHON2", "CPDEMO1",
        "VETERAN3", "EMPLOY1", "CHILDREN", "INCOME2", "INTERNET", "PREGNANT",
        "SXORIENT", "TRNSGNDR", "_PRACE1", "_MRACE1", "_HISPANC", "_RACE", "_RACEG21", 
        "_RACEGR3", "_RACE_G1", "_AGEG5YR", "_AGE65YR", "_AGE80", "_AGE_G", "_CHLDCNT", 
        "_EDUCAG", "_INCOMG"],

    "anthropometrics": [
        "WEIGHT2", "HEIGHT3", "HTIN4", "HTM4", "WTKG3", "_BMI5", "_BMI5CAT", "_RFBMI5"],

    "general_health_function": [
        "GENHLTH", "PHYSHLTH", "MENTHLTH", "POORHLTH", "QLACTLM2", "USEEQUIP", "BLIND",
        "DECIDE", "DIFFWALK", "DIFFDRES", "DIFFALON", "_RFHLTH"],

    "healthcare_access": [
        "HLTHPLN1", "PERSDOC2", "MEDCOST", "CHECKUP1", "_HCVU651"],

    "cardiovascular_metabolic": [
        "BPHIGH4", "BPMEDS", "BLOODCHO", "CHOLCHK", "TOLDHI2", "CVDSTRK3", "CHCKIDNY",
        "DIABETE3", "DIABAGE2", "HAREHAB1", "STREHAB1", "CVDASPRN", "ASPUNSAF",
        "RLIVPAIN", "RDUCHART", "RDUCSTRK", "_RFHYPE5", "_CHOLCHK", "_RFCHOL"],

    "diabetes_management": [
        "PDIABTST", "PREDIAB1", "INSULIN", "BLDSUGAR", "FEETCHK2", "DOCTDIAB",
        "CHKHEMO3", "FEETCHK", "EYEEXAM", "DIABEYE", "DIABEDU"],

    "respiratory": [
        "ASTHMA3", "ASTHNOW", "CHCCOPD1", "ASTHMAGE", "ASATTACK", "ASERVIST",
        "ASDRVIST", "ASRCHKUP", "ASACTLIM", "ASYMPTOM", "ASNOSLEP", "ASTHMED3",
        "ASINHALR", "_LTASTH1", "_CASTHM1", "_ASTHMS1"],

    "cancer_history": ["CHCSCNCR", "CHCOCNCR"],

    "arthritis_musculoskeletal": [
        "HAVARTH3", "LMTJOIN3", "ARTHDIS2", "ARTHSOCL", "JOINPAIN", "ARTTODAY",
        "ARTHWGT", "ARTHEXER", "ARTHEDU", "_DRDXAR1", "_LMTACT1", "_LMTWRK1", "_LMTSCL1"],

    "tobacco_alcohol": [
        "SMOKE100", "SMOKDAY2", "STOPSMK2", "LASTSMK2", "USENOW3", "ALCDAY5",
        "AVEDRNK2", "DRNK3GE5", "MAXDRNKS", "_SMOKER3", "_RFSMOK3", "DRNKANY5", 
        "DROCDY3_", "_RFBING5", "_DRNKWEK", "_RFDRHV5"],

    "diet_nutrition": [
        "FRUITJU1", "FRUIT1", "FVBEANS", "FVGREEN", "FVORANG", "VEGETAB1", "WTCHSALT",
        "LONGWTCH", "DRADVISE", "_FRT16", "_VEG23", "_FRUITEX", "_VEGETEX",
        "FTJUDA1_", "FRUTDA1_", "BEANDAY_", "GRENDAY_", "ORNGDAY_", "VEGEDA1_",
        "_MISFRTN", "_MISVEGN", "_FRTRESP", "_VEGRESP", "_FRUTSUM", "_VEGESUM",
        "_FRTLT1", "_VEGLT1"],

    "physical_activity": [
        "EXERANY2", "EXRACT11", "EXEROFT1", "EXERHMM1", "EXRACT21", "EXEROFT2",
        "EXERHMM2", "STRENGTH", "_PA30021", "_PASTRNG", "_PAREC1", "_PASTAE1",
        "_TOTINDA", "METVL11_", "METVL21_", "MAXVO2_", "FC60_", "ACTIN11_", "ACTIN21_",
        "PADUR1_", "PADUR2_", "PAFREQ1_", "PAFREQ2_", "_MINAC11", "_MINAC21",
        "STRFREQ_", "PAMISS1_", "PAMIN11_", "PAMIN21_", "PA1MIN_", "PAVIG11_",
        "PAVIG21_", "PA1VIGM_", "_PACAT1", "_PAINDX1", "_PA150R2", "_PA300R2"],

    "preventive_health_screening": [
        "SEATBELT", "FLUSHOT6", "FLSHTMY2", "IMFVPLAC", "PNEUVAC3", "HIVTST6",
        "HIVTSTD3", "WHRTST10", "TETANUS", "HPVADVC2", "HPVADSHT", "SHINGLE2", "HADMAM",
        "HOWLONG", "HADPAP2", "LASTPAP2", "HPVTEST", "HPLSTTST", "HADHYST2", "PROFEXAM",
        "LENGEXAM", "BLDSTOOL", "LSTBLDS3", "HADSIGM3", "HADSGCO1", "LASTSIG3",
        "PCPSAAD2", "PCPSADI1", "PCPSARE1", "PSATEST1", "PSATIME", "PCPSARS1",
        "PCPSADE1", "PCDMDECN", "_RFSEAT2", "_RFSEAT3", "_FLSHOT6", "_PNEUMO2", "_AIDTST3"],

    "vision": [
        "VIDFCLT2", "VIREDIF3", "VIPRFVS2", "VINOCRE2", "VIEYEXM2", "VIINSUR2",
        "VICTRCT4", "VIGLUMA2", "VIMACDG2"],

    "cognitive_health": [
        "CIMEMLOS", "CDHOUSE", "CDASSIST", "CDHELP", "CDSOCIAL", "CDDISCUS"],

    "mental_health": [
        "ADDEPEV2", "ADPLEASR", "ADDOWN", "ADSLEEP", "ADENERGY", "ADEAT1", "ADFAIL",
        "ADTHINK", "ADMOVE", "MISTMNT", "ADANXEV"],

    "social_context": [
        "SCNTMNY1", "SCNTMEL1", "SCNTPAID", "SCNTWRK1", "SCNTLPAD", "SCNTLWK1",
        "EMTSUPRT", "LSATISFY"],

    "caregiving_child": [
        "CAREGIV1", "CRGVREL1", "CRGVLNG1", "CRGVHRS1", "CRGVPRB1", "CRGVPERS",
        "CRGVHOUS", "CRGVMST2", "CRGVEXPT", "RCSGENDR", "RCSRLTN2", "CASTHDX2",
        "CASTHNO2", "_CHISPNC", "_CRACE1", "_CPRACE"],
}

FEATURE_TYPE_GROUPS = {
'binary': ['ADANXEV', 'ADDEPEV2', 'ARTHDIS2',
'ARTHEDU', 'ARTHEXER', 'ARTHWGT', 'ASATTACK', 'ASTHMA3', 'ASTHNOW', 'BLDSTOOL',
'BLIND', 'BLOODCHO', 'BPMEDS', 'CADULT', 'CASTHDX2', 'CASTHNO2', 'CCLGHOUS', 
'CDDISCUS', 'CELLFON2', 'CELLFON3', 'CHCCOPD1', 'CHCKIDNY', 'CHCOCNCR', 
'CHCSCNCR', 'CIMEMLOS', 'COLGHOUS', 'CPDEMO1', 'CRGVEXPT', 'CRGVHOUS', 'CRGVPERS',
'CSTATE', 'CTELENUM', 'CTELNUM1', 'CVDASPRN', 'CVDSTRK3', 'DECIDE', 'DIABEDU',
'DIABEYE', 'DIFFALON', 'DIFFDRES', 'DIFFWALK', 'DISPCODE', 'DRADVISE', 'DRNKANY5',
'EXERANY2', 'FLUSHOT6', 'HADHYST2', 'HADMAM', 'HADPAP2', 'HADSGCO1', 'HADSIGM3',
'HAREHAB1', 'HAVARTH3', 'HIVTST6', 'HLTHPLN1', 'HPVTEST', 'INSULIN', 'INTERNET',
'IYEAR', 'LADULT', 'LANDLINE', 'LMTJOIN3', 'MEDCOST', 'MISTMNT', 'NUMHHOL2', 
'PAMISS1_', 'PCPSAAD2', 'PCPSADI1', 'PCPSARE1', 'PDIABTST', 'PNEUVAC3', 'PREGNANT',
'PROFEXAM', 'PSATEST1', 'PVTRESD1', 'PVTRESD2', 'QLACTLM2', 'RCSGENDR', 'RDUCHART',
'RDUCSTRK', 'RLIVPAIN', 'SEX', 'SHINGLE2', 'SMOKE100', 'STATERES', 'STOPSMK2', 
'STREHAB1', 'TOLDHI2', 'USEEQUIP', 'VETERAN3', 'VIGLUMA2', 'VIMACDG2', 'WTCHSALT',
'_AGE65YR', '_AIDTST3', '_CASTHM1', '_CHISPNC', '_DRDXAR1', '_FLSHOT6', '_FRT16',
'_FRTLT1', '_FRTRESP', '_HCVU651', '_HISPANC', '_LTASTH1', '_PA30021', '_PAINDX1',
'_PASTAE1', '_PASTRNG', '_PNEUMO2', '_RACEG21', '_RFBING5', '_RFBMI5', '_RFCHOL',
'_RFDRHV5', '_RFHLTH', '_RFHYPE5', '_RFSEAT2', '_RFSEAT3', '_RFSMOK3', '_TOTINDA',
'_VEG23', '_VEGLT1', '_VEGRESP'],

'categorical': ['ASPUNSAF', 'BPHIGH4', 'CAREGIV1', 'CRGVMST2', 'CRGVPRB1',
'CRGVREL1', 'DIABETE3', 'EMPLOY1', 'EXRACT11', 'EXRACT21', 'FMONTH', 'HPVADSHT',
'HPVADVC2', 'IDAY', 'IMFVPLAC', 'IMONTH', 'MARITAL', 'MSCODE', 'PCDMDECN',
'PCPSADE1', 'PCPSARS1', 'PERSDOC2', 'PREDIAB1', 'QSTLANG', 'QSTVER', 'RCSRLTN2',
'RENTHOM1', 'SCNTLPAD', 'SCNTPAID', 'SEQNO', 'SXORIENT', 'TETANUS', 'TRNSGNDR',
'VICTRCT4', 'VIINSUR2', 'VINOCRE2', 'WHRTST10', '_ASTHMS1', '_CPRACE', '_CRACE1',
'_DUALUSE', '_FRUITEX', '_LMTACT1', '_LMTSCL1', '_LMTWRK1', '_MRACE1', '_PAREC1',
'_PRACE1', '_PSU', '_RACE', '_RACEGR3', '_RACE_G1','_SMOKER3', '_STATE', '_STSTR',
'_VEGETEX'],

'ordinal': ['ACTIN11_', 'ACTIN21_', 'ARTHSOCL', 'ARTTODAY', 'ASINHALR', 'ASNOSLEP',
'ASTHMED3', 'ASYMPTOM', 'CDASSIST', 'CDHELP', 'CDHOUSE', 'CDSOCIAL', 'CHECKUP1',
'CHOLCHK', 'CRGVHRS1', 'CRGVLNG1', 'EDUCA', 'EMTSUPRT', 'EYEEXAM', 'GENHLTH',
'HOWLONG', 'HPLSTTST', 'INCOME2', 'JOINPAIN', 'LASTPAP2', 'LASTSIG3', 'LASTSMK2',
'LENGEXAM', 'LSATISFY', 'LSTBLDS3', 'PSATIME', 'SCNTMEL1', 'SCNTMNY1', 'SEATBELT',
'SMOKDAY2', 'USENOW3', 'VIDFCLT2', 'VIEYEXM2', 'VIPRFVS2', 'VIREDIF3', '_AGEG5YR',
'_AGE_G', '_BMI5CAT', '_CHLDCNT', '_CHOLCHK', '_EDUCAG', '_INCOMG', '_PA150R2', 
'_PA300R2', '_PACAT1'],

'discrete': ['ADDOWN', 'ADEAT1', 'ADENERGY', 'ADFAIL', 'ADMOVE', 'ADPLEASR',
'ADSLEEP', 'ADTHINK', 'ASACTLIM', 'ASDRVIST', 'ASERVIST', 'ASRCHKUP', 'AVEDRNK2',
'CHILDREN', 'DIABAGE2', 'DOCTDIAB', 'DRNK3GE5', 'FEETCHK', 'HHADULT', 'MAXDRNKS', 
'MENTHLTH', 'NUMADULT', 'NUMMEN', 'NUMPHON2', 'NUMWOMEN', 'PA1MIN_', 'PA1VIGM_',
'PADUR1_', 'PADUR2_', 'PAMIN11_', 'PAMIN21_', 'PAVIG11_', 'PAVIG21_', 'PHYSHLTH',
'POORHLTH', 'SCNTLWK1', 'SCNTWRK1', '_AGE80', '_MINAC11', '_MINAC21', '_MISFRTN',
'_MISVEGN'],

'continuous': ['BEANDAY_', 'DROCDY3_', 'FC60_', 'FRUTDA1_', 'FTJUDA1_', 'GRENDAY_',
'HTIN4', 'HTM4', 'MAXVO2_', 'METVL11_', 'METVL21_', 'ORNGDAY_', 'PAFREQ1_', 
'PAFREQ2_', 'STRFREQ_', 'VEGEDA1_', 'WTKG3', '_BMI5', '_CLLCPWT', '_DRNKWEK',
'_DUALCOR', '_FRUTSUM', '_LLCPWT', '_RAWRAKE', '_STRWT', '_VEGESUM', '_WT2RAKE'],
 
'encoded': ['ALCDAY5', 'ASTHMAGE', 'BLDSUGAR', 'CHKHEMO3', 'EXERHMM1', 'EXERHMM2',
'EXEROFT1', 'EXEROFT2', 'FEETCHK2', 'FLSHTMY2', 'FRUIT1', 'FRUITJU1', 'FVBEANS',
'FVGREEN', 'FVORANG', 'HEIGHT3', 'HIVTSTD3', 'IDATE', 'LONGWTCH', 'STRENGTH',
'VEGETAB1', 'WEIGHT2']}

NONRESPONSE_PATTERNS = {'dk7_ref9': {'dont_know': [7], 'refused': [9]},
 'dk77_ref99': {'dont_know': [77], 'refused': [99]},
 'dk777_ref999': {'dont_know': [777], 'refused': [999]},
 'dk7777_ref9999': {'dont_know': [7777], 'refused': [9999]},
 'dk777777_ref999999': {'dont_know': [777777], 'refused': [999999]},
 'dk97_ref99': {'dont_know': [97], 'refused': [99]},
 'dk98_ref99': {'dont_know': [98], 'refused': [99]},
 'dk98': {'dont_know': [98]},
 'dk7': {'dont_know': [7]},
 'ref9': {'refused': [9]},
 'ref99': {'refused': [99]},
 'combined9': {'unknown_or_refused': [9]},
 'combined3': {'unknown_or_refused': [3]},
 'combined14': {'unknown_or_refused': [14]},
 'combined900': {'unknown_or_refused': [900]},
 'combined99900': {'unknown_or_refused': [99900]},
 'combined999_99': {'unknown_or_refused': [999.99]},
 'combined999': {'unknown_or_refused': [999.0]},
 'combined99': {'unknown_or_refused': [99.0]}}

NONRESPONSE_GROUPS = {'dk7_ref9': ['ADANXEV', 'ADDEPEV2', 'ARTHDIS2', 'ARTHEDU',
'ARTHEXER', 'ARTHSOCL', 'ARTHWGT', 'ARTTODAY', 'ASINHALR', 'ASPUNSAF', 'ASTHMA3',
'ASTHMED3', 'ASTHNOW', 'ASYMPTOM', 'BLDSTOOL', 'BLIND', 'BLOODCHO', 'BPHIGH4',
'BPMEDS', 'CAREGIV1', 'CASTHDX2', 'CASTHNO2', 'CDASSIST', 'CDDISCUS', 'CDHELP',
'CDHOUSE', 'CDSOCIAL', 'CHCCOPD1', 'CHCKIDNY', 'CHCOCNCR', 'CHCSCNCR', 'CHECKUP1',
'CHOLCHK', 'CIMEMLOS', 'CPDEMO1', 'CRGVEXPT', 'CRGVHOUS', 'CRGVHRS1', 'CRGVLNG1',
'CRGVMST2', 'CRGVPERS', 'CVDASPRN', 'CVDSTRK3', 'DECIDE', 'DIABEDU', 'DIABETE3',
'DIABEYE', 'DIFFALON', 'DIFFDRES', 'DIFFWALK', 'DRADVISE', 'DRNKANY5', 'EMTSUPRT', 
'EXERANY2', 'EYEEXAM', 'FLUSHOT6', 'GENHLTH', 'HADHYST2', 'HADMAM', 'HADPAP2',
'HADSGCO1', 'HADSIGM3', 'HAREHAB1', 'HAVARTH3', 'HIVTST6', 'HLTHPLN1', 'HOWLONG',
'HPLSTTST', 'HPVADVC2', 'HPVTEST', 'INTERNET', 'LANDLINE', 'LASTPAP2', 'LASTSIG3',
'LENGEXAM', 'LMTJOIN3', 'LSATISFY', 'LSTBLDS3', 'MEDCOST', 'MISTMNT', 'NUMHHOL2',
'NUMPHON2', 'PCDMDECN', 'PCPSAAD2', 'PCPSADI1', 'PCPSARE1', 'PCPSARS1', 'PDIABTST',
'PERSDOC2', 'PNEUVAC3', 'PREDIAB1', 'PREGNANT', 'PROFEXAM', 'PSATEST1', 'PSATIME',
'QLACTLM2', 'RCSRLTN2', 'RDUCHART', 'RDUCSTRK', 'RENTHOM1', 'RLIVPAIN', 'SCNTLPAD',
'SCNTMEL1', 'SCNTMNY1', 'SCNTPAID', 'SEATBELT', 'SHINGLE2', 'SMOKDAY2', 'SMOKE100',
'STOPSMK2', 'STREHAB1', 'SXORIENT', 'TETANUS', 'TOLDHI2', 'TRNSGNDR', 'USEEQUIP',
'USENOW3', 'VETERAN3', 'VIEYEXM2', 'VIINSUR2', 'VIPRFVS2', 'WTCHSALT'],

'dk77_ref99': ['ADDOWN', 'ADEAT1', 'ADENERGY', 'ADFAIL', 'ADMOVE', 'ADPLEASR',
'ADSLEEP', 'ADTHINK', 'AVEDRNK2', 'CHKHEMO3', 'CRGVPRB1', 'CRGVREL1', 'DOCTDIAB',
'DRNK3GE5', 'EXRACT11', 'EXRACT21', 'FEETCHK', 'HHADULT', 'HPVADSHT', 'IMFVPLAC',
'INCOME2', 'JOINPAIN', 'LASTSMK2', 'MAXDRNKS', 'MENTHLTH', 'PHYSHLTH', 'POORHLTH',
'VINOCRE2', 'WHRTST10', '_CPRACE', '_CRACE1', '_MRACE1', '_PRACE1'],

'dk777_ref999': ['ALCDAY5', 'ASACTLIM', 'BLDSUGAR', 'EXERHMM1', 'EXERHMM2',
'EXEROFT1', 'EXEROFT2', 'FEETCHK2', 'FRUIT1', 'FRUITJU1', 'FVBEANS',
'FVGREEN', 'FVORANG', 'LONGWTCH', 'STRENGTH', 'VEGETAB1'],

'dk7777_ref9999': ['HEIGHT3', 'WEIGHT2'],

'dk777777_ref999999': ['FLSHTMY2', 'HIVTSTD3'],

'dk97_ref99': ['SCNTLWK1', 'SCNTWRK1'],

'dk98_ref99': ['ASRCHKUP', 'ASTHMAGE', 'DIABAGE2'],

'dk98': ['ASDRVIST', 'ASERVIST'],

'dk7': ['ASATTACK', 'ASNOSLEP', 'VICTRCT4', 'VIDFCLT2', 'VIGLUMA2', 
         'VIMACDG2', 'VIREDIF3'],

'ref9': ['EDUCA', 'EMPLOY1', 'INSULIN', 'MARITAL', 'PCPSADE1', 'RCSGENDR'],

'ref99': ['CHILDREN'],

'combined9': ['PAMISS1_', '_AIDTST3', '_ASTHMS1', '_CASTHM1', '_CHISPNC',
'_CHLDCNT', '_CHOLCHK', '_EDUCAG', '_FLSHOT6', '_FRTLT1', '_HCVU651',
'_HISPANC', '_INCOMG', '_LMTACT1', '_LMTSCL1', '_LMTWRK1', '_LTASTH1','_PA150R2', 
'_PA30021', '_PA300R2', '_PACAT1', '_PAINDX1', '_PAREC1', '_PASTAE1', '_PASTRNG',
'_PNEUMO2', '_RACE', '_RACEG21', '_RACEGR3', '_RFBING5', '_RFBMI5', '_RFCHOL',
'_RFDRHV5', '_RFHLTH', '_RFHYPE5', '_RFSEAT2', '_RFSEAT3', '_RFSMOK3', '_SMOKER3',
'_TOTINDA', '_VEGLT1'],

'combined3': ['_AGE65YR'],

'combined14': ['_AGEG5YR'],

'combined900': ['DROCDY3_'],

'combined99900': ['_DRNKWEK'],

'combined999_99': ['WTKG3'],

'combined999': ['FC60_', 'MAXVO2_'],

'combined99': ['PAFREQ1_', 'PAFREQ2_', 'STRFREQ_']}

# valid responses that cannot be represented correctly on a feature's ordinary numerical or ordinal scale
NON_NUMERIC_VALID_CODES = {'LASTSMK2': [8],
 'SEATBELT': [8],
 'SCNTMNY1': [8],
 'SCNTMEL1': [8],
 'VIDFCLT2': [6, 8],
 'VIREDIF3': [6],
 'VIEYEXM2': [8],
 'CHKHEMO3': [98],
 'ASTHMAGE': [97],
 'FEETCHK2': [555],
 'LONGWTCH': [555],
 'FRUITJU1': [300],
 'FRUIT1': [300],
 'FVBEANS': [300],
 'FVGREEN': [300],
 'FVORANG': [300],
 'VEGETAB1': [300]}

# ordinal features with levels to be recoded
ORDINAL_LEVELS = {'CHECKUP1': [1, 2, 3, 4, 8],
 'EYEEXAM': [1, 2, 3, 4, 8],
 'ASYMPTOM': [8, 1, 2, 3, 4, 5],
 'ASNOSLEP': [8, 1, 2, 3, 4, 5],
 'ASTHMED3': [8, 1, 2, 3],
 'ASINHALR': [8, 1, 2, 3, 4, 5, 6]}

# conversion of special response codes into numerically equivalent values
VALUE_RECODES = {'PHYSHLTH': {88: 0},
 'MENTHLTH': {88: 0},
 'POORHLTH': {88: 0},
 'CHILDREN': {88: 0},
 'DOCTDIAB': {88: 0},
 'CHKHEMO3': {88: 0},
 'FEETCHK': {88: 0},
 'ASERVIST': {88: 0},
 'ASDRVIST': {88: 0},
 'ASRCHKUP': {88: 0},
 'ASACTLIM': {888: 0},
 'DRNK3GE5': {88: 0},
 'ADPLEASR': {88: 0},
 'ADDOWN': {88: 0},
 'ADSLEEP': {88: 0},
 'ADENERGY': {88: 0},
 'ADEAT1': {88: 0},
 'ADFAIL': {88: 0},
 'ADTHINK': {88: 0},
 'ADMOVE': {88: 0},
 'SCNTWRK1': {98: 0},
 'SCNTLWK1': {98: 0},
 'ALCDAY5': {888: 0},
 'BLDSUGAR': {888: 0},
 'FEETCHK2': {888: 0},
 'STRENGTH': {888: 0},
 'FRUITJU1': {555: 0},
 'FRUIT1': {555: 0},
 'FVBEANS': {555: 0},
 'FVGREEN': {555: 0},
 'FVORANG': {555: 0},
 'VEGETAB1': {555: 0}}

# features not used for modeling
EXCLUDED_FEATURES = [
    # record identifiers
    "SEQNO", "_PSU",
    # survey design variables and sampling weights
    "_STSTR", "_STRWT", "_RAWRAKE", "_WT2RAKE", "_CLLCPWT", "_LLCPWT", "_DUALCOR",
    # survey administration
    "CTELENUM", "CTELNUM1", "CELLFON2", "STATERES", "COLGHOUS", "CCLGHOUS",
    "LADULT", "DISPCODE", "QSTVER",
    # interview date
    "FMONTH", "IDATE", "IMONTH", "IDAY", "IYEAR",
    # dates of last flu shot or HIV test in form of month-year codes
    "FLSHTMY2", "HIVTSTD3"]

# build lookup dictionaries
_type = {}
_response = {}

# per-feature dictionary with type
for t, features in FEATURE_TYPE_GROUPS.items():
    for f in features:
        _type[f] = t

# per-feature dictionary with non-response scheme
for s, features in NONRESPONSE_GROUPS.items():
    for f in features:
        _response[f] = s

FEATURE_INFO = {}
for category, features in FEATURE_GROUPS.items():
    for f in features:
        scheme = _response.get(f)
        FEATURE_INFO[f] = {
            "category": category,
            "data_type": _type[f],
            "nonresponse_codes": {k: v.copy() for k, v in NONRESPONSE_PATTERNS.get(scheme, {}).items()},
            "value_recode": VALUE_RECODES.get(f, {}).copy(),
            "non_numeric_valid_codes": NON_NUMERIC_VALID_CODES.get(f, []).copy(),
            "ordinal_levels": ORDINAL_LEVELS[f].copy() if f in ORDINAL_LEVELS else None,
        }
