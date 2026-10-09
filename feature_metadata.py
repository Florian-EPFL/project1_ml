# Semantic grouping of features based on the BRFSS codebook. 
# Each group contains a list of original and derived features. 

FEATURE_GROUPS = {
    "survey_administration": {
        "original": [
            "_STATE", "FMONTH", "IDATE", "IMONTH", "IDAY", "IYEAR", "DISPCODE", "SEQNO", "_PSU",
            "CTELENUM", "PVTRESD1", "COLGHOUS", "STATERES", "CELLFON3", "LADULT", "NUMADULT",
            "NUMMEN", "NUMWOMEN", "CTELNUM1", "CELLFON2", "CADULT", "PVTRESD2", "CCLGHOUS",
            "CSTATE", "LANDLINE", "HHADULT", "QSTVER", "QSTLANG", "MSCODE"
        ],
        "derived": [
            "_STSTR", "_STRWT", "_RAWRAKE", "_WT2RAKE", "_CLLCPWT", "_DUALUSE", "_DUALCOR", "_LLCPWT"
        ]
    },

    "demographics_socioeconomic": {
        "original": [
            "SEX", "MARITAL", "EDUCA", "RENTHOM1", "NUMHHOL2", "NUMPHON2", "CPDEMO1",
            "VETERAN3", "EMPLOY1", "CHILDREN", "INCOME2", "INTERNET", "PREGNANT",
            "SXORIENT", "TRNSGNDR"
        ],
        "derived": [
            "_PRACE1", "_MRACE1", "_HISPANC", "_RACE", "_RACEG21", "_RACEGR3", "_RACE_G1",
            "_AGEG5YR", "_AGE65YR", "_AGE80", "_AGE_G", "_CHLDCNT", "_EDUCAG", "_INCOMG"
        ]
    },

    "anthropometrics": {
        "original": ["WEIGHT2", "HEIGHT3"],
        "derived": ["HTIN4", "HTM4", "WTKG3", "_BMI5", "_BMI5CAT", "_RFBMI5"]
    },

    "general_health_function": {
        "original": [
            "GENHLTH", "PHYSHLTH", "MENTHLTH", "POORHLTH", "QLACTLM2", "USEEQUIP",
            "BLIND", "DECIDE", "DIFFWALK", "DIFFDRES", "DIFFALON"
        ],
        "derived": ["_RFHLTH"]
    },

    "healthcare_access": {
        "original": ["HLTHPLN1", "PERSDOC2", "MEDCOST", "CHECKUP1"],
        "derived": ["_HCVU651"]
    },

    "cardiovascular_metabolic": {
        "original": [
            "BPHIGH4", "BPMEDS", "BLOODCHO", "CHOLCHK", "TOLDHI2", "CVDSTRK3",
            "CHCKIDNY", "DIABETE3", "DIABAGE2", "HAREHAB1", "STREHAB1",
            "CVDASPRN", "ASPUNSAF", "RLIVPAIN", "RDUCHART", "RDUCSTRK"
        ],
        "derived": ["_RFHYPE5", "_CHOLCHK", "_RFCHOL"]
    },

    "diabetes_management": {
        "original": [
            "PDIABTST", "PREDIAB1", "INSULIN", "BLDSUGAR", "FEETCHK2", "DOCTDIAB",
            "CHKHEMO3", "FEETCHK", "EYEEXAM", "DIABEYE", "DIABEDU"
        ],
        "derived": []
    },

    "respiratory": {
        "original": [
            "ASTHMA3", "ASTHNOW", "CHCCOPD1", "ASTHMAGE", "ASATTACK", "ASERVIST",
            "ASDRVIST", "ASRCHKUP", "ASACTLIM", "ASYMPTOM", "ASNOSLEP", "ASTHMED3", "ASINHALR"
        ],
        "derived": ["_LTASTH1", "_CASTHM1", "_ASTHMS1"]
    },

    "cancer_history": {
        "original": ["CHCSCNCR", "CHCOCNCR"],
        "derived": []
    },

    "arthritis_musculoskeletal": {
        "original": [
            "HAVARTH3", "LMTJOIN3", "ARTHDIS2", "ARTHSOCL", "JOINPAIN",
            "ARTTODAY", "ARTHWGT", "ARTHEXER", "ARTHEDU"
        ],
        "derived": ["_DRDXAR1", "_LMTACT1", "_LMTWRK1", "_LMTSCL1"]
    },

    "tobacco_alcohol": {
        "original": [
            "SMOKE100", "SMOKDAY2", "STOPSMK2", "LASTSMK2", "USENOW3",
            "ALCDAY5", "AVEDRNK2", "DRNK3GE5", "MAXDRNKS"
        ],
        "derived": [
            "_SMOKER3", "_RFSMOK3", "DRNKANY5", "DROCDY3_",
            "_RFBING5", "_DRNKWEK", "_RFDRHV5"
        ]
    },

    "diet_nutrition": {
        "original": [
            "FRUITJU1", "FRUIT1", "FVBEANS", "FVGREEN", "FVORANG",
            "VEGETAB1", "WTCHSALT", "LONGWTCH", "DRADVISE"
        ],
        "derived": [
            "FTJUDA1_", "FRUTDA1_", "BEANDAY_", "GRENDAY_", "ORNGDAY_", "VEGEDA1_",
            "_MISFRTN", "_MISVEGN", "_FRTRESP", "_VEGRESP", "_FRUTSUM", "_VEGESUM",
            "_FRTLT1", "_VEGLT1", "_FRT16", "_VEG23", "_FRUITEX", "_VEGETEX"
        ]
    },

    "physical_activity": {
        "original": [
            "EXERANY2", "EXRACT11", "EXEROFT1", "EXERHMM1",
            "EXRACT21", "EXEROFT2", "EXERHMM2", "STRENGTH"
        ],
        "derived": [
            "_TOTINDA", "METVL11_", "METVL21_", "MAXVO2_", "FC60_", "ACTIN11_", "ACTIN21_",
            "PADUR1_", "PADUR2_", "PAFREQ1_", "PAFREQ2_", "_MINAC11", "_MINAC21", "STRFREQ_",
            "PAMISS1_", "PAMIN11_", "PAMIN21_", "PA1MIN_", "PAVIG11_", "PAVIG21_", "PA1VIGM_",
            "_PACAT1", "_PAINDX1", "_PA150R2", "_PA300R2", "_PA30021",
            "_PASTRNG", "_PAREC1", "_PASTAE1"
        ]
    },

    "preventive_health_screening": {
        "original": [
            "SEATBELT", "FLUSHOT6", "FLSHTMY2", "IMFVPLAC", "PNEUVAC3",
            "HIVTST6", "HIVTSTD3", "WHRTST10",
            "TETANUS", "HPVADVC2", "HPVADSHT", "SHINGLE2",
            "HADMAM", "HOWLONG", "HADPAP2", "LASTPAP2", "HPVTEST", "HPLSTTST", "HADHYST2",
            "PROFEXAM", "LENGEXAM", "BLDSTOOL", "LSTBLDS3", "HADSIGM3",
            "HADSGCO1", "LASTSIG3", "PCPSAAD2", "PCPSADI1", "PCPSARE1",
            "PSATEST1", "PSATIME", "PCPSARS1", "PCPSADE1", "PCDMDECN"
        ],
        "derived": ["_RFSEAT2", "_RFSEAT3", "_FLSHOT6", "_PNEUMO2", "_AIDTST3"]
    },

    "vision": {
        "original": [
            "VIDFCLT2", "VIREDIF3", "VIPRFVS2", "VINOCRE2", "VIEYEXM2",
            "VIINSUR2", "VICTRCT4", "VIGLUMA2", "VIMACDG2"
        ],
        "derived": []
    },

    "cognitive_health": {
        "original": ["CIMEMLOS", "CDHOUSE", "CDASSIST", "CDHELP", "CDSOCIAL", "CDDISCUS"],
        "derived": []
    },

    "mental_health": {
        "original": [
            "ADDEPEV2", "ADPLEASR", "ADDOWN", "ADSLEEP", "ADENERGY",
            "ADEAT1", "ADFAIL", "ADTHINK", "ADMOVE", "MISTMNT", "ADANXEV"
        ],
        "derived": []
    },

    "social_context": {
        "original": [
            "SCNTMNY1", "SCNTMEL1", "SCNTPAID", "SCNTWRK1",
            "SCNTLPAD", "SCNTLWK1", "EMTSUPRT", "LSATISFY"
        ],
        "derived": []
    },

    "caregiving_child": {
        "original": [
            "CAREGIV1", "CRGVREL1", "CRGVLNG1", "CRGVHRS1", "CRGVPRB1",
            "CRGVPERS", "CRGVHOUS", "CRGVMST2", "CRGVEXPT",
            "RCSGENDR", "RCSRLTN2", "CASTHDX2", "CASTHNO2"
        ],
        "derived": ["_CHISPNC", "_CRACE1", "_CPRACE"]
    }
}
# Dependency graph of derived features. Each derived feature is associated with a list of parent features.
# None means derived according to the codebook, but this report does not give the direct construction.

PARENTS = {
    # Survey / weighting
    "_STSTR": ["_STATE", "_GEOSTR", "_DENSTR2"],
    "_STRWT": ["NRECSTR", "NRECSEL"],
    "_RAWRAKE": ["NUMADULT", "_IMPNPH"],
    "_WT2RAKE": ["_STRWT", "_RAWRAKE"],
    "_CLLCPWT": None,
    "_DUALUSE": None,
    "_DUALCOR": None,
    "_LLCPWT": None,

    # Child / race / demographic recodes
    "_CHISPNC": None,
    "_CRACE1": None,
    "_CPRACE": None,
    "_PRACE1": ["MRACASC1", "ORACE3"],
    "_MRACE1": ["MRACASC1"],
    "_HISPANC": None,
    "_RACE": ["_HISPANC", "_MRACE1"],
    "_RACEG21": ["_RACE"],
    "_RACEGR3": ["_RACE"],
    "_RACE_G1": ["_RACE"],
    "_AGEG5YR": ["AGE"],
    "_AGE65YR": ["AGE"],
    "_AGE80": ["_IMPAGE"],
    "_AGE_G": ["_IMPAGE"],
    "_CHLDCNT": ["CHILDREN"],
    "_EDUCAG": ["EDUCA"],
    "_INCOMG": ["INCOME2"],

    # Anthropometrics
    "HTIN4": ["HEIGHT3"],
    "HTM4": ["HEIGHT3"],
    "WTKG3": ["WEIGHT2"],
    "_BMI5": ["WTKG3", "HTM4"],
    "_BMI5CAT": ["_BMI5"],
    "_RFBMI5": ["_BMI5"],

    # General health / healthcare / chronic conditions
    "_RFHLTH": ["GENHLTH"],
    "_HCVU651": ["AGE", "HLTHPLN1"],
    "_RFHYPE5": ["BPHIGH4"],
    "_CHOLCHK": ["BLOODCHO", "CHOLCHK"],
    "_RFCHOL": ["BLOODCHO", "TOLDHI2"],
    "_LTASTH1": ["ASTHMA3"],
    "_CASTHM1": ["ASTHMA3", "ASTHNOW"],
    "_ASTHMS1": ["ASTHMA3", "ASTHNOW"],
    "_DRDXAR1": ["HAVARTH3"],

    # Arthritis burden
    "_LMTACT1": ["HAVARTH3", "LMTJOIN3"],
    "_LMTWRK1": ["HAVARTH3", "ARTHDIS2"],
    "_LMTSCL1": ["HAVARTH3", "ARTHSOCL"],

    # Smoking / alcohol
    "_SMOKER3": ["SMOKE100", "SMOKDAY2"],
    "_RFSMOK3": ["_SMOKER3"],
    "DRNKANY5": ["ALCDAY5"],
    "DROCDY3_": ["ALCDAY5"],
    "_RFBING5": ["ALCDAY5", "DRNK3GE5"],
    "_DRNKWEK": ["AVEDRNK2", "DROCDY3_"],
    "_RFDRHV5": ["SEX", "_DRNKWEK"],

    # Diet / nutrition
    "FTJUDA1_": ["FRUITJU1"],
    "FRUTDA1_": ["FRUIT1"],
    "BEANDAY_": ["FVBEANS"],
    "GRENDAY_": ["FVGREEN"],
    "ORNGDAY_": ["FVORANG"],
    "VEGEDA1_": ["VEGETAB1"],

    "_MISFRTN": ["FTJUDA1_", "FRUTDA1_"],
    "_MISVEGN": ["BEANDAY_", "GRENDAY_", "ORNGDAY_", "VEGEDA1_"],

    "_FRTRESP": ["_MISFRTN"],
    "_VEGRESP": ["_MISVEGN"],

    "_FRUTSUM": ["FTJUDA1_", "FRUTDA1_"],
    "_VEGESUM": ["BEANDAY_", "GRENDAY_", "ORNGDAY_", "VEGEDA1_"],

    "_FRTLT1": ["_FRUTSUM"],
    "_VEGLT1": ["_VEGESUM"],

    "_FRT16": ["_FRUTSUM"],
    "_VEG23": ["_VEGESUM"],

    "_FRUITEX": ["_MISFRTN", "_FRT16"],
    "_VEGETEX": ["_MISVEGN", "_VEG23"],

    # Physical activity
    "_TOTINDA": ["EXERANY2"],

    "METVL11_": ["EXRACT11"],
    "METVL21_": ["EXRACT21"],

    # Age/sex-specific physiological quantities
    "MAXVO2_": ["AGE", "SEX"],
    "FC60_": ["MAXVO2_"],

    # Activity intensity
    "ACTIN11_": ["METVL11_", "FC60_"],
    "ACTIN21_": ["METVL21_", "FC60_"],

    # Duration
    "PADUR1_": ["EXERHMM1"],
    "PADUR2_": ["EXERHMM2"],

    # Frequency
    "PAFREQ1_": ["EXEROFT1"],
    "PAFREQ2_": ["EXEROFT2"],

    # Weekly minutes
    "_MINAC11": ["PADUR1_", "PAFREQ1_"],
    "_MINAC21": ["PADUR2_", "PAFREQ2_"],

    # Strength exercise
    "STRFREQ_": ["STRENGTH"],

    # Missingness indicator for activity data
    "PAMISS1_": [
        "EXERANY2", "EXRACT11", "EXEROFT1", "EXERHMM1",
        "EXRACT21", "EXEROFT2", "EXERHMM2"
    ],

    # Moderate-equivalent / total weekly activity
    "PAMIN11_": ["_MINAC11", "ACTIN11_"],
    "PAMIN21_": ["_MINAC21", "ACTIN21_"],
    "PA1MIN_": ["PAMIN11_", "PAMIN21_"],

    # Vigorous weekly activity
    "PAVIG11_": ["_MINAC11", "ACTIN11_"],
    "PAVIG21_": ["_MINAC21", "ACTIN21_"],
    "PA1VIGM_": ["PAVIG11_", "PAVIG21_"],

    # Final activity categories / recommendations
    "_PACAT1": ["PA1MIN_", "PA1VIGM_"],
    "_PAINDX1": ["PA1MIN_", "PA1VIGM_"],
    "_PA150R2": ["PA1MIN_", "PA1VIGM_"],
    "_PA300R2": ["PA1MIN_", "PA1VIGM_"],
    "_PA30021": ["_PA300R2"],
    "_PASTRNG": ["STRFREQ_"],
    "_PAREC1": ["_PAINDX1", "_PASTRNG"],
    "_PASTAE1": ["_PAREC1"],

    # Preventive health
    "_RFSEAT2": ["SEATBELT"],
    "_RFSEAT3": ["SEATBELT"],
    "_FLSHOT6": ["AGE", "FLUSHOT6"],
    "_PNEUMO2": ["AGE", "PNEUVAC3"],
    "_AIDTST3": ["HIVTST6"]
}

# Feature-level metadata, including category, type, and parent features.

FEATURE_SET = {
    feature
    for category in FEATURE_GROUPS.values()
    for feature_type in category.values()
    for feature in feature_type
}

FEATURE_INFO = {}

for category, feature_types in FEATURE_GROUPS.items():
    for feature_type, features in feature_types.items():
        for feature in features:

            if feature_type == "original":
                parents = []
                parent_in_dataset = None

            else:
                parents = PARENTS.get(feature)

                if parents is None:
                    parent_in_dataset = None
                else:
                    parent_in_dataset = all(
                        parent in FEATURE_SET for parent in parents
                    )

            FEATURE_INFO[feature] = {
                "category": category,
                "type": feature_type,
                "parents": parents,
                "parent_in_dataset": parent_in_dataset
            }