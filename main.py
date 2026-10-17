import pyshorteners
shortner = str(input('''\033[0;30;42mAvailable URL/Link Shorteners:\033[0;33;40m
Input "\033[1;32;40m1\033[0;33;40m" for \033[1;32;40mClck.ru\033[0;33;40m 
Input "\033[1;32;40m2\033[0;33;40m" for \033[1;32;40mDa.gd\033[0;33;40m
Input "\033[1;32;40m3\033[0;33;40m" for \033[1;32;40mIs.gd\033[0;33;40m
Input "\033[1;32;40m4\033[0;33;40m" for \033[1;32;40mTtm.sh\033[0;33;40m
Input "\033[1;32;40m5\033[0;33;40m" for \033[1;32;40mOs.db\033[0;33;40m
Input "\033[1;32;40m6\033[0;33;40m" for \033[1;32;40mTinyURL.com\033[0;33;40m
Input "\033[1;32;40m7\033[0;33;40m" for \033[1;32;40mChilp.it\033[0;33;40m
Input "\033[1;32;40m8\033[0;33;40m" for \033[1;32;40mBit.ly\033[0;33;40m (\033[0;34;40mRequires Account\033[0;33;40m)
Input "\033[1;32;40m9\033[0;33;40m" for \033[1;32;40mCutt.ly\033[0;33;40m (\033[0;34;40mRequires Account\033[0;33;40m)
Input "\033[1;32;40m10\033[0;33;40m" for \033[1;32;40mAdf.ly\033[0;33;40m (\033[0;34;40mRequires Account\033[0;33;40m)
Input "\033[1;32;40m11\033[0;33;40m" for \033[1;32;40mOw.ly\033[0;33;40m (\033[0;34;40mRequires Account\033[0;33;40m)
Input "\033[1;32;40m12\033[0;33;40m" for \033[1;32;40mShort.cm\033[0;33;40m (\033[0;34;40mRequires Account + Domain\033[0;33;40m)
Input "\033[1;32;40m13\033[0;33;40m" for \033[1;32;40mTiny.cc\033[0;33;40m (\033[0;31;40mRequires Account + Barely Works\033[0;33;40m)
Input "\033[1;32;40m14\033[0;33;40m" for \033[1;32;40mGit.io\033[0;33;40m (\033[0;31;40mDead\033[0;33;40m)
Input "\033[1;32;40m15\033[0;33;40m" for \033[1;32;40mPo.st\033[0;33;40m (\033[0;31;40mDead\033[0;33;40m)
Input "\033[1;32;40m16\033[0;33;40m" for \033[1;32;40mQps.ru\033[0;33;40m (\033[0;31;40mDead\033[0;33;40m)
\033[0;30;42mInput:\033[1;32;40m '''))

#----------------------------------------1
def adfly():
    print("\n\033[0;30;42mAdf.ly Initialized\033[0;33;40m")
    try:
        user = str(input("\033[0;30;45madf.ly User ID:\033[0;35;40m "))
        api = str(input("\033[0;30;45madf.ly API key:\033[0;35;40m "))
        dom = str(input('''\033[0;30;42mAvailable Domains:\033[0;33;40m
Input "\033[1;32;40m1\033[0;33;40m" for \033[1;32;40mad.fly\033[0;33;40m
Input "\033[1;32;40m2\033[0;33;40m" for \033[1;32;40mq.gs\033[0;33;40m
Input "\033[1;32;40m3\033[0;33;40m" for \033[1;32;40mj.gs\033[0;33;40m
Input "\033[1;32;40m4\033[0;33;40m" for \033[1;32;40mRandom\033[0;33;40m
\033[0;30;42mInput:\033[1;32;40m '''))
        if dom == "1":
            dom = "adf.ly"
        elif dom == "2":
            dom = "q.gs"
        elif dom == "3":
            dom = "j.gs"
        elif dom == "4":
            dom = "0"
        else:
            print("\033[1;30;41mError:\033[0;31;40m No domain found\033[0;33;40m")
        url = str(input("\033[0;30;45mInput the link you want to shorten:\033[0;35;40m "))
        print("Generating short link...")
        adfly = pyshorteners.Shortener(api_key=api, user_id=user, domain=dom).adfly.short(url)
        print("\n\033[0;30;45mShortened link:\033[0;36;40m "+adfly)
    except:
        print("\033[1;30;41mError:\033[0;31;40m Please try again\033[0;33;40m")

#----------------------------------------2
def bitly():
    print("\n\033[0;30;42mBit.ly Initialized\033[0;33;40m")
    try:
        api = str(input("\033[0;30;45mbit.ly API key:\033[0;35;40m "))
        url = str(input("\033[0;30;45mInput the link you want to shorten:\033[0;35;40m "))
        print("Generating short link...")
        bitly = pyshorteners.Shortener(api_key = api).bitly.short(url)
        print("\n\033[0;30;45mShortened link:\033[0;36;40m "+bitly)
    except:
        print("\033[1;30;41mError:\033[0;31;40m Please try again\033[0;33;40m")
        
#----------------------------------------3
def chilpit():
    print("\n\033[0;30;42mChilp.it Initialized\033[0;33;40m")
    try:
        url = str(input("\033[0;30;45mInput the link you want to shorten:\033[0;35;40m "))
        print("Generating short link...")
        chilpit = pyshorteners.Shortener().chilpit.short(url)
        print("\n\033[0;30;45mShortened link:\033[0;36;40m "+chilpit)
    except:
        print("\033[1;30;41mError:\033[0;31;40m Please try again\033[0;33;40m")
        
#----------------------------------------4
def clckru():
    print("\n\033[0;30;42mClck.ru Initialized\033[0;33;40m")
    try:
        url = str(input("\033[0;30;45mInput the link you want to shorten:\033[0;35;40m "))
        print("Generating short link...")
        clckru = pyshorteners.Shortener().clckru.short(url)
        print("\n\033[0;30;45mShortened link:\033[0;36;40m "+clckru)
    except:
        print("\033[1;30;41mError:\033[0;31;40m Please try again\033[0;33;40m")        

#----------------------------------------5
def cuttly():
    print("\n\033[0;30;42mCutt.ly Initialized\033[0;33;40m")
    try:
        api = str(input("\033[0;30;45mcutt.ly API key:\033[0;35;40m "))
        url = str(input("\033[0;30;45mInput the link you want to shorten:\033[0;35;40m "))
        print("Generating short link...")
        cuttly = pyshorteners.Shortener(api_key=api).cuttly.short(url)
        print("\n\033[0;30;45mShortened link:\033[0;36;40m "+cuttly)
    except:
        print("\033[1;30;41mError:\033[0;31;40m Please try again\033[0;33;40m")

#----------------------------------------6
def dagd():
    print("\n\033[0;30;42mDa.gd Initialized\033[0;33;40m")
    try:
        url = str(input("\033[0;30;45mInput the link you want to shorten:\033[0;35;40m "))
        print("Generating short link...")
        dagd = pyshorteners.Shortener().dagd.short(url)
        print("\n\033[0;30;45mShortened link:\033[0;36;40m "+dagd)
    except:
        print("\033[1;30;41mError:\033[0;31;40m Please try again\033[0;33;40m")
        
#----------------------------------------7
def gitio():
    print("\n\033[1;30;41git.io:\033[0;31;40m Sorry, we're no longer accepting new links to shorten\033[0;33;40m")

#----------------------------------------8
def isgd():
    print("\n\033[0;30;42mIs.gd Initialized\033[0;33;40m")
    try:
        url = str(input("\033[0;30;45mInput the link you want to shorten:\033[0;35;40m "))
        print("Generating short link...")
        isgd = pyshorteners.Shortener().isgd.short(url)
        print("\n\033[0;30;45mShortened link:\033[0;36;40m "+isgd)        
    except:
        print("\033[1;30;41mError:\033[0;31;40m Please try again\033[0;33;40m")

#----------------------------------------9
def nullpointer():
    print("\n\033[0;30;42mTtm.sh Initialized\033[0;33;40m")
    try:
        url = str(input("\033[0;30;45mInput the link you want to shorten:\033[0;35;40m "))
        print("Generating short link...")
        nullpointer = pyshorteners.Shortener(domain="https://ttm.sh").nullpointer.short(url)
        print("\n\033[0;30;45mShortened link:\033[0;36;40m "+nullpointer)
    except:
        print("\033[1;30;41mError:\033[0;31;40m Please try again\033[0;33;40m")    
#----------------------------------------10
def osdb():
    print("\n\033[0;30;42mOs.db Initialized\033[0;33;40m")
    try:
        url = str(input("\033[0;30;45mInput the link you want to shorten:\033[0;35;40m "))
        print("Generating short link...")
        osdb = pyshorteners.Shortener().osdb.short(url)
        print("\n\033[0;30;45mShortened link:\033[0;36;40m "+osdb)
    except:
        print("\033[1;30;41mError:\033[0;31;40m Please try again\033[0;33;40m")

#----------------------------------------11
def owly():
    print("\n\033[0;30;42mOw.ly Initialized\033[0;33;40m")
    try:
        api = str(input("\033[0;30;45mow.ly API key:\033[0;35;40m "))
        url = str(input("\033[0;30;45mInput the link you want to shorten:\033[0;35;40m "))
        print("Generating short link...")
        owly = pyshorteners.Shortener(api_key=api).owly.short(url)
        print("\n\033[0;30;45mShortened link:\033[0;36;40m "+owly)
    except:
        print("\033[1;30;41mError:\033[0;31;40m Please try again\033[0;33;40m")

#----------------------------------------12
def post():
    print("\n\033[0;31;40mSorry, po.st is no longer available\033[0;33;40m")

#----------------------------------------13
def qpsru():
    print("\n\033[0;30;42mqps.ru services were closed on 10 Oct, 2019\033[0;33;40m")
    
#----------------------------------------14
def shortcm():
    print("\n\033[0;30;42mShort.cm Initialized\033[0;33;40m")
    try:
        api = str(input("\033[0;30;45mshort.cm API key:\033[0;35;40m "))
        dom = str(input("\033[0;30;45mName of domain you own:\033[0;35;40m "))
        url = str(input("\033[0;30;45mInput the link you want to shorten:\033[0;35;40m "))
        print("Generating short link...")
        shortcm = pyshorteners.Shortener(api_key=api, domain=dom).shortcm.short(url)
        print("\n\033[0;30;45mShortened link:\033[0;36;40m "+shortcm)
    except:
        print("\033[1;30;41mError:\033[0;31;40m Please try again\033[0;33;40m")
#----------------------------------------15
def tinycc():
    print("\n\033[0;30;42mTiny.cc Initialized\033[0;33;40m")
    try:
        user = str(input("\033[0;30;45mtiny.cc Username:\033[0;35;40m "))
        api = str(input("\033[0;30;45mYourtiny.cc API key:\033[0;35;40m "))
        url = str(input("\033[0;30;45mInput the link you want to shorten:\033[0;35;40m "))
        print("Generating short link...")
        tinycc = pyshorteners.Shortener(api_key=api, login=user).tinycc.short(url)
        print("\n\033[0;30;45mShortened link:\033[0;36;40m "+tinycc)
    except:
        print("\033[1;30;41mError:\033[0;31;40m Please try again\033[0;33;40m")    

#----------------------------------------16
def tinyurl():
    print("\n\033[0;30;42mTinyURL.com Initialized\033[0;33;40m")
    try:
        url = str(input("\033[0;30;45mInput the link you want to shorten:\033[0;35;40m "))
        print("Generating short link...")
        tinyurl = pyshorteners.Shortener().tinyurl.short(url)
        print("\033[0;30;45mShortened link:\033[0;36;40m "+tinyurl)
    except:
        print("\033[1;30;41mError:\033[0;31;40m Please try again\033[0;33;40m")

#----------------------------------------

if shortner == "1":
    clckru()
elif shortner == "2":
    dagd()
elif shortner == "3":
    isgd()
elif shortner == "4":
    nullpointer()
elif shortner == "5":
    osdb()
elif shortner == "6":
    tinyurl()
elif shortner == "7":
    chilpit()
elif shortner == "8":
    bitly()
elif shortner == "9":
    cuttly()
elif shortner == "10":
    adfly()
elif shortner == "11":
    owly()
elif shortner == "12":
    shortcm()
elif shortner == "13":
    tinycc()
elif shortner == "14":
    gitio()
elif shortner == "15":
    post()
elif shortner == "16":
    qpsru()
else:
    print("\033[1;30;41mError:\033[0;31;40m Wrong input\033[0;33;40m")