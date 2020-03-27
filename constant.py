
no_name_list = [
    "resume",
    "curriculum vitae",
    "curriculum vitale",
    "curriculam vitae",
    "to,",
    "manager,",
    "ideology"
]

replace_list_email = [
    ["/ Email ID", "\nEmail:"],
    ["| E-mail:", "\nEmail:"],
    ["| E-Mail:", "\nEmail:"],
    ["|Email :", "\nEmail:"],
    ["| eMail:", "\nEmail:"],
    [" E-Mail ID", "\nEmail:"],
    [" E-Mail:", "\nEmail:"],
    [" Email:", "\nEmail:"],
    [" Email-", "\nEmail:"],
    [", Email ID", "\nEmail"],
    [", E-mail:", "\nEmail:"],
    ["/ EMAIL:", "\nEmail:"],
    ["     Email:", "\nEmail:"],
    ["? e-mail id :", "\nEmail:"],
    [", Email Id:", "\nEmail:"],
    ["~ E-Mail:", "\nEmail:"],
    ["; Email", '\nEmail'],
    ["; E-mail:", "\nEmail:"],
    [".Email:", "\nEmail:"],
    [" email id :", "\nEmail:"],
    [u"\uf03bEmail Id:", "\nEmail:"],
    [u"\uf09a:", "\nEmail:"],
    ["\nE:", "\nEmail:"],
    [u"|\uf02a:", "\nEmail:"],
    [u"\u2666E-mail", "\nEmail:"],
    ["| email:", "\nEmail:"],
    ["~ E-Mail", "\nEmail:"],
    ["e-mail", "\nEmail:"],
    [" EMAIL:", "\nEmail:"],
    [", E- Mail:", "\nEmail:"],
    [" E-mail:", "\nEmail:"],
    [" Email ID:", "\nEmail:"]
]

replace_list_phone = [
    [u"\u25ca Mobile:", "\nMobile:"],
    [u"\uf0c5:", "\nMobile:"],
    ["  Mobile:", "\nMobile:"],
    ["	Mobile:", "\nMobile:"],
    ["; Mobile:", "\nMobile:"],
    [", Tel:", "\nTel:"],
    [", Contact No.", "\nMobile:"],
    ["(Mobile)", "Mobile"],
    ["\nMobile+", "\nMobile:"],
    ["?Mobile no.:", "\nMobile:"],
    [" PHONE:", "\nPHONE:"],
    [", Phone:", "\nPhone:"],
    [", Phone :", "\nPhone:"],
    ["~ Phone ", "\nPhone:"],
    ["/ PH.:", "\nPhone:"],
    [", PH -", "\nPhone"],
    ["; Ph:", "\nPhone:"],
    ["\nPh ", "\nPhone:"],
    ["~ MOBILE:", "\nMOBILE:"],
    ["(Mob)", "Mobile"],
    ["\n(M) ", "\nMobile:"],
    ["\nM:", "\nMobile:"],
    [" M:", "\nMobile:"],
    ["\nNo:", "\nMobile:"],
    [": (M) ", "\nMobile:"],
    [u"\uf028Mobile", "Mobile:"],
    ["Cell No +", "Cell No: +"],
    [" | Cell:", " \n Cell No:"],
    ["(Cell):", "Cell No:"],
    ["| Contact:", "\nContact:"],
    ["~ Contact:", "\nContact:"],
    ["\tPh:", "\nPhone:"],
    ["\nP:", "\nPhone:"],
    [", Phone No.", "\nPhone No"],
    ["mobile no", "Mobile"],
]

replace_list_key = [
    ["/ DOB", "\nDOB"],
    [", DOB:", "\nDOB:"],
    ["	D O B:", "\nDOB:"],
    [": DOB:", "\nDOB:"],
    ["com DOB :", "com \nDOB:"],
    [", Language:", "\nLanguage:"],
    ["| Languages:", "\nLanguage:"],
    ["| Nationality:", "\nNationality:"],
    [", Video CV:", "\nVideo CV:"],
    [" ~ Languages Known:", "\nLanguages Known:"],
    [" ~ Passport Details:", "\nPassport Details:"],
    ["// LinkedIn:", "\nLinkedIn:"],
    [". Reference:", ".\nReference:"],
    ["| Marital Status:", "\nMarital Status:"],
    ["| Gender:", "\nGender:"],
    ["/ GENDER:", "\nGENDER:"],
    ["; SkypeID:", "\nSkype:"],
    [", skype -", "\nSkype:"],
    ["| Skype Id:", "\nSkype:"],
    ["? Address :", "\nAddress:"],
    ["| Best time", "\nBest time"],
    [".com  Contact:", ".com\nContact:"],
    ["PERMANENT\nADDRESS", "PERMANENT ADDRESS"],
    ["HOBBIES &\nINTERESTS", "HOBBIES & INTERESTS"],
    ["LANGUAGES\nKNOWN", "LANGUAGES KNOWN"],
    ["Certification Enrollment &\nAffiliation", "Certification"],
    ["Playing Carom,\nCooking", "Playing Carom, Cooking"],
    ["Personal details:Name", "Personal details:\nName"],
    ["University\nName", "University Name"],
    ["Hobbies &\nInterest:", "Hobbies & Interest:"],
    ["CAREER\nACCOMPLISHMENT", "Career Accomplishment"],
    [" Marital Status:", "\nMarital Status:"],
    [" Languages Known:", "\nLanguages Known:"],
    [", Nationality:", "\nNationality:"],
    [", Sex:", "\nSex:"],
    [", Marital status:", "\nMarital status:"],
    ["mailto", "Mail to"],
    ["Email Address:", "\nEmail:"],
    [" Address:", "\nAddress:"],
    ["; Date of Birth", "\nDate of Birth"],
    ["skype", "Skype"],
    [" LINKEDIN :", "\nLINKEDIN:"],
    [" ~ Languages:", "\nLanguages:"],
]

replace_list = [
    ["(E-mail)\n", "\n"],
    [" (M),", "\n"],
    [u"\u2013", "-"],
    [u"\u2019", "'"],
    [u" \u2022 ", "\n"],
    [u"\uf0bf", "\n"],
    [u"\uf0e8", "\n"],
    [u"\uf020", ""],
    [u"\uf0b7", ""],
    [u"\uf0dc", ""],
    [u"\u27a2", ""],
    [u"\u200b", ""],
    [u"\xa0", " "],
    [u"\u2014", "\n"],
    ["    ", "\n"],
    ["[pic]:", "\n"],
    ["[pic]", ''],
    ["| |", '\n'],
    [" | ", "\n"],
    [" - - ", "\n"],
    ["\t", "\n"],
    ["\n>", "\n"]
]


school_key_list = ['education society', 'college', ' board', 'institute', 'school', 'university', 'emhss']
school_no_same_key_list = ['college', 'institute', 'university', 'institute & university',
                           'board/university/college', 'institute/university']
school_no_key_list = ['college meets', 'college events', 'college topper', 'top 10', 'activities and societies']

degree_list = ['bachelor', 'b.com', 'b.sc', 'b. sc', 'diploma in',
               'e-mba', 'hrbp', 'h.s.c',
               'masters in', "master's in", "master's degree in", 'master of', 'mhrm', 'pgdm',
               'secondary education', 's.s.c', 't.y.b', 'tyb']
degree_list_case = ['BA', 'B.A', 'BBA', 'B.E', 'BMS', 'BSC', 'DPM', 'HR', 'HSC',
                    'ICSE', 'MA', 'MBA', 'MCA', 'MCM', 'MMS', 'MPM', 'PGPM', 'SSC', 'WBHSE']
degree_no_list = ['my ssc']
degree_no_same_list = ["Bachelor's", 'Masters']

month_long_list = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
month_short_list = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']