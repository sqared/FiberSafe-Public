
class Login:
    login_usrname = 'username'
    login_pass = 'password'
    login_button = '//*[@id="root"]/div/div[2]/div/div/div/div/div[2]/form/div[3]/button'

class Dashboard:
    decline = '/html/body/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/h5'
    progress ='//*[@id="main-content"]/div[2]/div[2]/div[2]/div/div/div/div[2]'
    inspection = '//*[@id="main-content"]/div[2]/div[2]/div[3]/div/div/div/div[2]'
    submitted = '//*[@id="main-content"]/div[2]/div[2]/div[4]/div/div/div/div[2]'
    unassigned = '//*[@id="main-content"]/div[2]/div[2]/div[5]/div/div/div/div[2]'
    fibercut  = '//*[@id="main-content"]/div[2]/div[2]/div[6]/div/div/div/div[2]'
    regiondrop = '/html/body/div/div/div[2]/div[3]/div[1]/div/div[1]/div[3]/div/select'
    statedrop = '/html/body/div/div/div[2]/div[3]/div[1]/div/div[1]/div[4]/div/select'
    wilayahdrop = '/html/body/div/div/div[2]/div[3]/div[1]/div/div[1]/div[5]/div/select'
    zonedrop = '/html/body/div/div/div[2]/div[3]/div[1]/div/div[1]/div[6]/div/select'
    chartdrop = '//*[@id="chart_type"]'
    activities = '//*[@id="main-content"]/div[2]/div[3]/div[2]/div/div[1]/div/div[2]/ul/li[1]/div/div/span[1]'
    backbutton = '//*[@id="main-content"]/div[2]/div/div/div/div[1]/div/div[2]/button'
    alerts = '//*[@id="main-content"]/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/ul/li[1]'

class Map:
    menubarmap = "/html/body/div[1]/nav/div/div/ul[1]/li[2]/a"
    search = '/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div/input'
    clickbutton = "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div[2]/div[1]/div[1]/form/div/div[2]/div/label/input"
    clickbutton1 = "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div[2]/div[1]/div[1]/form/div/div[1]/div/label/input"

class Report:
    expand = "/html/body/div[1]/nav/div/div/ul[1]/div[1]/li/a"
    clickoption = "/html/body/div[1]/nav/div/div/ul[1]/div[1]/li/div/ul/li[3]/a"
    search1 = '/html/body/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[1]/div/label/input'
    clicksearch = "/html/body/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[1]/div/i"
    backbutton = "/html/body/div/div/div[2]/div/div/div/div[1]/div/div[2]/button/div/span"
    edit = "/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div[2]/div/div[3]/i"
    remark = '/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div[2]/div/div[4]/div[2]/textarea'
    clickcancel = "/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div[2]/div/div[5]/div[2]/div/div[2]/div[1]/div/i"
    frame = "/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div[2]/div/div[5]/div[2]/div"
    year = "/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div[2]/div/div[5]/div[2]/div/div[2]/div[2]/div/table/thead/tr[1]/th[2]"
    month = "/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div[2]/div/div[5]/div[2]/div/div[2]/div[2]/div/table[2]/tbody/tr[2]/td[1]"
    day = "/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div[2]/div/div[5]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[2]/td[1]"
    save = "/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div[2]/div/div[3]/i[2]"
    seedetails = "/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div[1]/div/div/span[3]/button"
    inspection_status = "/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div/div/div[2]/div/div[1]/i"
    remark1 = '/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div/div/div[2]/div/div[2]/div[2]/textarea'
    editclick = "/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div/div/div[2]/div/div[3]/i"
    clickbox = "/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div/div/div[2]/div/div[2]/div[2]/label/input"
    remark2 = "/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div/div/div[2]/div/div[3]/div[2]/textarea"
    submit = "/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div/div/div[2]/div/div[5]/button/span[2]"
    editrevisit = "/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[3]/div[2]/div/div/div[2]/div/div[3]/i"
    require = "/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[3]/div[2]/div/div/div[2]/div/div[3]/div[2]/label/input"
    frame1 = "/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[3]/div[2]/div/div/div[2]/div/div[3]/div[4]/div[1]"
    year1 = "/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[3]/div[2]/div/div/div[2]/div/div[3]/div[4]/div[1]/div[2]/div[2]/div/table/thead/tr[1]/th[2]"
    month1 = "/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[3]/div[2]/div/div/div[2]/div/div[3]/div[4]/div[1]/div[2]/div[2]/div/table[2]/tbody/tr[2]/td[1]"
    day1 = "/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[3]/div[2]/div/div/div[2]/div/div[3]/div[4]/div/div[2]/div[2]/div/table/tbody/tr[2]/td[1]"
    submit1 = "/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[3]/div[2]/div/div/div[2]/div/div[4]/button/span[2]"
    choice = '/html/body/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[1]/table/tbody/tr[6]'

class Setting:
    side_bar_setting = "/html/body/div/nav/div/div/ul[1]/li[4]/a"
    generate_qr = "/html/body/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div[2]/button/span"
    download_qr = "/html/body/div[2]/div/div[1]/div/div/div[3]/button[1]"
    email_button = "/html/body/div[2]/div/div[1]/div/div/div[3]/button[2]"
    receipents_email= "/html/body/div[2]/div/div[1]/div/div/div[2]/div/div/div[1]/div/input"
    addtional_message = "/html/body/div[2]/div/div[1]/div/div/div[2]/div/div/textarea"
    cancel = "/html/body/div[2]/div/div[1]/div/div/div[1]/button/span"
    send_button = "/html/body/div[2]/div/div[1]/div/div/div[3]/button[2]"

class Job:
    edit_button = "/html/body/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/form/div[9]/div/div/button/span[2]"
    job_owner_drop = "/html/body/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/form/div[1]/div[1]/div/select"
    job_team_member_drop = "/html/body/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/form/div[1]/div[2]/div/select"
    hour = "/html/body/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/form/div[3]/div[1]/div/input"
    minute = "/html/body/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/form/div[3]/div[2]/div/input"
    job_first_reminder = "/html/body/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/form/div[5]/div[1]/div/input"
    job_second_reminder = "/html/body/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/form/div[5]/div[2]/div/input"
    job_third_reminder ="/html/body/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/form/div[5]/div[3]/div/input"
    contractor_first_reminder ="/html/body/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/form/div[7]/div[1]/div/input"
    contractor_scheduler_reminder = "/html/body/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/form/div[7]/div[2]/div/input"
    radius ="/html/body/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/form/div[8]/div/div/input"
    cancel ="/html/body/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/form/div[9]/div/div/button[1]/div/span"
    save = "/html/body/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/form/div[9]/div/div/button[2]"
    cancel_save ="/html/body/div[2]/div/div[1]/div/div/div[3]/button[2]"
    yes_save ="/html/body/div[2]/div/div[1]/div/div/div[3]/button[1]"

class Post:
    post = "/html/body/div/div/div[2]/div[2]/div[2]/div/div/ul/li[2]/a"
    edit_button_post = "/html/body/div/div/div[2]/div[2]/div[2]/div/div/div/div[2]/form/div[3]/div/div/button"
    low_min ="/html/body/div/div/div[2]/div[2]/div[2]/div/div/div/div[2]/form/div[2]/div[1]/div[2]/div[1]/div/input"
    low_max ="/html/body/div/div/div[2]/div[2]/div[2]/div/div/div/div[2]/form/div[2]/div[1]/div[2]/div[2]/div/input"
    medium_min ="/html/body/div/div/div[2]/div[2]/div[2]/div/div/div/div[2]/form/div[2]/div[2]/div[2]/div[1]/div/input"
    medium_max = "/html/body/div/div/div[2]/div[2]/div[2]/div/div/div/div[2]/form/div[2]/div[2]/div[2]/div[2]/div/input"
    high_min ="/html/body/div/div/div[2]/div[2]/div[2]/div/div/div/div[2]/form/div[2]/div[3]/div[2]/div[1]/div/input"
    high_max ="/html/body/div/div/div[2]/div[2]/div[2]/div/div/div/div[2]/form/div[2]/div[3]/div[2]/div[2]/div/input"
    cancel_post ="/html/body/div/div/div[2]/div[2]/div[2]/div/div/div/div[2]/form/div[3]/div/div/button[1]/div/span"
    save_post = "/html/body/div/div/div[2]/div[2]/div[2]/div/div/div/div[2]/form/div[3]/div/div/button[2]"
    cancel_save = "/html/body/div[2]/div/div[1]/div/div/div[3]/button[2]"
    yes_save ="/html/body/div[2]/div/div[1]/div/div/div[3]/button[1]"

class Alert:
    alert_setting="/html/body/div/div/div[2]/div[2]/div[2]/div/div/ul/li[3]/a"
    edit_button_alert = "/html/body/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/form/div[5]/div/div/button/span[2]"
    distance_threshold ="/html/body/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/form/div[1]/div/div/input"
    alert_distance ="/html/body/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/form/div[2]/div/div/input"
    duplicate_alert ="/html/body/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/form/div[4]/div/div/input"
    number_of_days = "/html/body/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/form/div[5]/div/div/input"
    cancel_alert ="/html/body/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/form/div[6]/div/div/button[1]"
    save_alert ="/html/body/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/form/div[6]/div/div/button[2]/span[2]"
    cancel_save="/html/body/div[2]/div/div[1]/div/div/div[3]/button[2]"
    yes_save="/html/body/div[2]/div/div[1]/div/div/div[3]/button[1]"

class Navigation:
    reportmenu = "//*[@id=\"sidenav-main\"]/div/div/ul[1]/div[1]/li/a"
    worklistnav = '//*[@id="sidenav-main"]/div/div/ul[1]/div[1]/li/div/ul/li[3]/a'

class Worklist:
    toggleView = '//*[@id="main-content"]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div[1]/div/button[2]'
    filtericon = '/html/body/div/div[2]/nav/div/div[1]/button'
    filterstatus = '/html/body/div/div[1]/div/div/form/div[1]/div[5]/div/select'
    inprogress = '//*[@id="alert_status"]/option[3]'
    applyfilter = '/html/body/div/div[1]/div/div/form/div[2]/div/button/span[2]'
    ##Development
    #tndetail = '//*[@id="main-content"]/div[2]/div[2]/div/div/div[2]/div[4]/div[1]/div/div[3]/div[2]/button'
    ##Production
    tndetail = '/html/body/div/div[2]/div[2]/div[2]/div/div/div[2]/div[4]/div/div/div[2]/div[2]/button'
    tncheckbox = '/html/body/div/div[2]/div[2]/div[2]/div/div/div[2]/div[4]/div[2]/div/div[1]/div/div[2]/div/input'
    markinvalid = '/html/body/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div[2]/div/div[2]/button'
    showmore = '/html/body/div/div[2]/div[2]/div[2]/div/div/div[2]/div[5]/div/button'
    searchbar = '/html/body/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/input'
    searchbtn = '/html/body/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/button'
    enlargeimg = '/html/body/div/div[2]/div[2]/div[2]/div/div/div[2]/div[4]/div[1]/div/img'
    ##Use to get alert from List View based on row, accept value 1-10
    def Listalert(j):
        listalert = '//*[@id="user-table"]/tbody/tr['+str(j)+']'
        return listalert
    
    ##Use to get alert from Thumbnail View based on row, accept value 1-8 (Can accept more if show more is clicked) 
    def Thumbnailalert(i):
        tnalert = '//*[@id="main-content"]/div[2]/div[2]/div/div/div[2]/div[4]/div['+str(i)+']'
        return tnalert

class Inspectioninfo:
    backbutton = '/html/body/div/div/div[2]/div/div/div/div[1]/div/div[2]/button'
    