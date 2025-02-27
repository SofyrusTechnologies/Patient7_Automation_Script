class DashboardSelectors:
    WELCOME_MESSAGE = "/html/body/div[1]/div/div/main/div/div[1]/div[1]/div/div[1]/div"
    PATIENT_LIST_BUTTON = "/html/body/div[1]/div/div/nav/div[1]/div/button[3]"

class PatientListSelectors:
    PAGE_TITLE = "/html/body/div[1]/div/div/main/div/div[2]/div[1]/div/div/table/thead/tr/th[1]/div"
    ADD_PATIENT_BUTTON = "/html/body/div[1]/div/header/div/div[1]/button/div/span[2]"

class AddPatientSelectors:
    FIRST_NAME = "/html/body/div[1]/div/div/main/div/div/div/div[2]/div/form/div[1]/div[2]/div[1]/div[1]/div/input"
    LAST_NAME = "/html/body/div[1]/div/div/main/div/div/div/div[2]/div/form/div[1]/div[2]/div[1]/div[3]/div/input"
    
    DOB = "/html/body/div[1]/div/div/main/div/div/div/div[2]/div/form/div[1]/div[2]/div[1]/div[6]/div/input"
    MOBILE = "/html/body/div[1]/div/div/main/div/div/div/div[2]/div/form/div[1]/div[2]/div[1]/div[11]/div/input"
    EMAIL = "/html/body/div[1]/div/div/main/div/div/div/div[2]/div/form/div[1]/div[2]/div[1]/div[12]/div/input"
    ADDRESS = "/html/body/div[1]/div/div/main/div/div/div/div[2]/div/form/div[1]/div[2]/div[3]/div[1]/div/div/input"
    PATIENT_ELEMENT = "/html/body/div[1]/div/div/nav/div[1]/div/button[3]"
    PATIENT_COLORCODE = "/html/body/div[1]/div/div/main/div/div[2]/div[1]/div/div/table/thead/tr/th[1]/div"
    NEW_PATIENT = "/html/body/div[1]/div/div/main/div/div[2]/div[1]/div/div/table/tbody/tr[1]"
    PATIENT_DETAILS = "/html/body/div[1]/div/div/main/div/div[2]/div[1]/div/div/table/tbody/tr[1]/td[9]/div/button[1]"
    OPEN_PATIENT_DETAILS = "/html/body/div[1]/div/div/main/div/div/div/div/div/div[1]/div[1]/div/div/div[2]/div[1]/div[1]/h2"
    
    
class AddMedicationSelector:
    MRN_NO ="/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div/div[2]/div/div[1]/button[1]/span"
    MEDICATION_NAME = "/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div/div/div/div/div[1]/div/div/form/div/div[1]/div/div/input"
    DOSAGE = "/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div/div/div/div/div[1]/div/div/form/div/div[2]/div/input"
    FREQUENCY = "/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div/div/div/div/div[1]/div/div/form/div/div[4]/div/div/input"
    ADD_MEDICATION = "/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div/div/div/div/div[1]/div/div/form/div/div[5]/button[1]"
    # MEDICATION_ELEMENT = "/html/body/div[1]/div/div/main/div/div[2]/div[1]/div/div/table/tbody/tr[1]"
    # MEDICATION_DETAILS = "/html/body/div[1]/div/div/main/div/div[2]/div[1]/div/div/table/tbody/tr[1]/td[9]/div/button[2]"
    # OPEN_MEDICATION_DETAILS = "/html/body/div[1]/div/div/main/div/div/div/div/div/div[1]/div[1]/div/div/div[2]/div[1]/div[1]/h2"
    
    
    
class AddUserSelectors:
    GetUserInformation = "/html/body/div[1]/div/div/main/div/div/div[2]/div/div[7]/div/div[2]/div/div[1]/div/div/table/thead/tr/th[4]"
    Click_AddUser = "/html/body/div[1]/div/div/main/div/div/div[2]/div/div[1]/div[2]/button"
    FIRST_NAME = "/html/body/div[1]/div/div/main/div/div/div[2]/div[2]/div/form/div[3]/div[2]/div/div[1]/div[2]/div/div[1]/input"
    LAST_NAME = "/html/body/div[1]/div/div/main/div/div/div[2]/div[2]/div/form/div[3]/div[2]/div/div[2]/div[1]/input"
    ROLE = "/html/body/div[1]/div/div/main/div/div/div[2]/div[2]/div/form/div[3]/div[2]/div/div[4]/div/div/input"
    SELECT_ROLE = "/html/body/div[1]/div/div/main/div/div/div[2]/div[2]/div/form/div[3]/div[2]/div/div[4]/div[2]/div/div/div/div/div/div[2]"
    SPEC = "/html/body/div[1]/div/div/main/div/div/div[2]/div[2]/div/form/div[3]/div[2]/div/div[5]/div[1]/div/input"
    SELECT_SPEC = "/html/body/div[1]/div/div/main/div/div/div[2]/div[2]/div/form/div[3]/div[2]/div/div[5]/div[2]/div/div/div/div/div/div[1]"
    ADMIN_PRIV = "/html/body/div[1]/div/div/main/div/div/div[2]/div[2]/div/form/div[3]/div[2]/div/div[9]/div[2]"
    EMAIL = "/html/body/div[1]/div/div/main/div/div/div[2]/div[2]/div/form/div[3]/div[2]/div/div[7]/div[1]/input"
    SAVE_BUTTON = "/html/body/div[1]/div/div/main/div/div/div[2]/div[2]/div/form/div[9]/button[2]"
    YOPMAIL = "/html/body/div/div[2]/main/div[3]/div/div[1]/div[2]/div/div/form/div/div[1]"
    
class AddTaskSelectors:
    ADDTASKBUTTON = "/html/body/div[1]/div/div/main/div/div/div[1]/div[3]/button"
    TASKTITLE = "/html/body/div[4]/div/div/div/div[2]/section/div/div/div/div[1]/div/div[2]/form/div[1]/div[1]/div/input"
    AASIGNROLE = "/html/body/div[4]/div/div/div/div[2]/section/div/div/div/div[1]/div/div[2]/form/div[1]/div[3]/div[1]/div"
    SELECTROLE = "/html/body/div[4]/div/div/div/div[2]/section/div/div/div/div[1]/div/div[2]/form/div[1]/div[3]/div[2]/div/div/div[1]/div/div/div[2]"
    TASKTYPE = "/html/body/div[4]/div/div/div/div[2]/section/div/div/div/div[1]/div/div[2]/form/div[3]/div[2]/div[1]/div/div[1]/input"
    ASSIGNTASK = "/html/body/div[4]/div/div/div/div[2]/section/div/div/div/div[1]/div/div[2]/form/div[4]/button[2]"
    ASSERT = "/html/body/div[1]/div/div/main/div/div/div[2]/div[2]/div/div/div[1]/div/div/table/tbody/tr[1]/td[2]"
    
    
    
    
