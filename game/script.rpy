init python: 
    import requests
    url = "http://blooming-wave-67070.herokuapp.com"
    requests.post(url+"/reset")

define lior = Character("Lior noy")
define students = Character("Students")
define tammi = Character("Tammi tamir")
define karnaf = Character("karnaf man")
define yossi_calc = Character("Yossi ")
define yossi = Character("Yossi")
define avner = Character("Avner")
define azugy = Character("Azugy")
define janitor = Character("Scary janitor")
define yonit = Character("Yonit Levy")



label start:
    $ counter = 0
    $ resolved = []
    scene news
    yonit "NEWS REPORT"
    yonit "129,213 new people were found positive for Covid-19 in the past 24 Hours."
    yonit "The situation is getting out of control after it was found that Moderna and Pfizer’s vaccines are causing the disease and not protecting from getting it."
    yonit "Rumors have been heard that a new experimental vaccine is in production in the Interdisplinary Center in Hertzliya, but no official comment was sent by Prof’ Raichman, IDC’s owner."
    yonit "By forign sources, Prof’ Raichman hides 5 samples in his highly secured office in the IDC."
    yonit "and now, moving on to season 8 of Ninja Israel, with the hosts Dekel Vaknin and Ela Li Lahav."
    
    scene black
    with fade
    students "Almost everyone we know got sick! We have to get that vaccine!!"
    students "Lets break into the campus tomorrow, before someone else will do it."

    scene nextday
    with fade
    $ renpy.pause(1.5)
    

    scene bg bla
    with fade

    students "Let's get to Raichman's office as fast as possible!"
    students "Wait! isn't it..."
    
    show lior noy with easeinright
    
    lior "Excuse me?"
    lior "Hi.. Yeah you guys"
    lior "What are you doing here? The campus should be closed"


    students "You know why we are here.. we are looking for the vaccine from the news! We are sure you’re here for the same reason don’t you?"
    lior "Exactly what I thought.. But I know prof’ Raichman, I’m sure you’ll have to be creative to be able to get into his office"
    lior "You should go talk to Tami in the Flags Rahava, she’ll know how to start"

    show screen back_to_map
    jump map

label flags:
    if "flags1" in resolved:
        jump flags2
    scene black
    show tammi tamir
    with dissolve
    if counter == 0:
        tammi "Students? shoudln't you be in home learning how to spell the word Dijkstra?"
        students "Um.. kinda, but we are here for something else"
        students "We are looking for the vaccine that they talked about in the news, someone told us you should know where to start"
        tammi "Oh ok... I don't know much, but I might help"
        tammi "But first.. Since i’ve been using complex algorithms to solve my problems for the past 20 years, I kind of forgot how to count.. think you can help me how many flags are there in the rahava?"
        tammi "I used to know the number, if you'll say the right one - i'll know if its true"
        $ response = renpy.input("Number of Flags")
    else:
        $ response = renpy.input("I'm sure that not true..")
    $ response = response.strip()
    if response == "60":
        tammi "Great! Now I can check if my revolutionary flag sorting algorithm is working properly! Thank you!"
        tammi "Its Called FSA, by the way"
        students "So.. about the vaccine?.."
        tammi "I think I heard something about the vaccine in the aquarioum today from a student that was talking there… maybe he is still there."
        $ resolved.append("flags1")
        $ requests.post(url+"/resolved", data = {'data' : 'flags1'})
        $ counter = 0
        jump map
    else:
        tammi "This is incorrect"
        $ counter += 1
        if counter > 3:
            $ counter = 1
            tammi "You've done me wrong one time to many now you will get a penalty, Dijkstra wouldn't disappoint me like this"
            "Penalty 30 seconds"
            $ renpy.pause(30)
        jump flags

label flags2:
    scene bg bla
    show tammi tamir
    tammi "There is nothing else for you to do here"
    jump map

label aquarium:
    scene black
    if "flags1" not in resolved or "aquarium2" in resolved:
        show azugy
        azugy "Go away I'm trying to do homeworks"
        jump map
    if "aquarium1" in resolved:
        jump aquarium2
    show azugy
    with fade
    students "Hi, Is there a chance you know anything about that vaccine that they was talking about on the news?"
    
    azugy "Shhh! How do you know I know something?"
    azugy "Anyway, I’m making a Pistachio Crust Salmon but couldn’t get any fresh salmon from today"
    azugy "If you’ll get me a few salmon cut, I might tell you what I know"
    $ resolved.append("aquarium1")
    $ requests.post(url+"/resolved", data = {'data' : 'aquarium1'})
    jump map

label aquarium2:
    scene black
    show azugy
    if "karnaf3" in resolved:
        azugy "Wow! you really got me the salmon"
        azugy "Ok.. i’ll tell you what I heard"
        azugy "There is a Linear Algebra teacher that is teaching in Zoom but from the class he used to teach in our first Semester. He is the one who calculated the effectivness of the vaccine. Go look for him."
        $ requests.post(url+"/resolved", data = {'data' : 'aquarium2'})
        $ resolved.append("aquarium2")
        jump map
    else:
        azugy "Where is my salmon?"
        jump map


label karnaf:
    scene bg bla
    if "karnaf1" in resolved:
        jump karnaf2
    show karnaf

    karnaf "Hi guys, how can I help you? coffee anyone?"
    if "aquarium1" not in resolved:
        jump map

    show farnaf man
    students "Is there any chance you have a salmon cut in the kitchen?"
    karnaf "W..What? A salmon cut? We don’t sell that here, but you can get a salmon sandwich if you want"
    students "We don’t want a sandwich, just the cut you make the sandwiches from, ok?"
    karnaf "I’ll tell you what.. I was asked to make a birthday cake for “Zell Programs”’s founder. it should include his birthday and the amount of money that was raised by projects from Zell’s program. Help my finding those, and you’ll get the Salmon cut that was left."
    $ requests.post(url+"/resolved", data = {'data' : 'karnaf1'})
    $ resolved.append("karnaf1")
    jump karnaf2

label karnaf2:
    if "karnaf2" in resolved:
        jump karnaf3
    $ response = renpy.input("So what is his birthday again?” (dd/mm/yyyy format)")
    $ response = response.strip()
    if response == "14/11/2019":
        $ resolved.append("karnaf2")
        $ requests.post(url+"/resolved", data = {'data' : 'karnaf2'})
    else:
        karnaf "Wrong answer bro"
        jump karnaf2

label karnaf3:
    if "karnaf3" in resolved:
        jump karnaf4
    $ response = renpy.input("And the money? (No commas, digits only)")
    $ response = response.strip()
    if response == "1100000000":
        $ resolved.append("karnaf3")
        $ requests.post(url+"/resolved", data = {'data' : 'karnaf3'})
        karnaf "Thank you so much! Here is your salmon."
        jump map
    else:
        karnaf "Wrong answer bro"
        jump karnaf3

label karnaf4:
    scene bg bla
    show karnaf
    karnaf "Leave me alone alredy bro"
    jump map

label psycho:
    scene bg bla
    show avner
    if "aquarium2" not in resolved:
        avner "Come back later I'm in the middle of zoom lecture"
        jump map
    else:
        if "talkedtoavner" not in resolved:
            avner "Students! Finally! Some Students"
            avner "You’re Vlad, two Daniels and Gal, right?"
            avner "I haven’t seen a student for a year. So glad you’re here!"
            avner "But…. what are you doing here? the campus should be empty"
            students "We heard you worked on the experimental vaccine that everybody is talking about. arn’t you?"
            avner "I’m not sure I want to answer that.. why are you guys asking?"
            students "We want to find it, we have to find it, before someone else will!"
            avner "Since you all always kept your camera open during the previous semester, i’ll help you with joy."
            avner "The vaccines are locked in the safe in Raichman’s office, I don’t have the key to the safe, but I can help you get into the office. The passcode to the office is the number of the “ADAMA”, following the number of the definition of NulA"
            avner "I would tell you the numbers, but since i’m lecturing on Zoom, my memory isn’t as it used to."
            avner "I also think Yossi is the one who put the vaccines in Raichman's office. Go talked to him, but I also heard he is super busy with a conspiracy theorms on Reddit"
            avner "Now get out, I have a class in a minute."
            $ resolved.append("talkedtoavner")
        else:
            avner "I Told you already! its is the number of the “ADAMA”, following the number of the definition of NulA"
            jump map
    jump map


label richman:
    jump map

label comms:
    scene bg bla
    show janitor
    janitor "Hey!! what are you doing here the campus is close!!!"
    jump map

label bussines:
    jump map

label law:
    jump map

label exists:
    jump map

label cs:
    show yossi
    with dissolve
    if "talkedtoavner" not in resolved:
        yossi "I'm in the middle of something"
        jump map
    if "helpyossi" in resolved:
        yossi "I told you go see Max"
        jump map
        
    else:            
        if counter == 0:
            yossi "*ON THE PHONE*"
            yossi "I swear it exists! I proved it, It cannot be!"
            yossi "I’ll prove it to you. Square root of 2 exists, I just know it’s true"
            yossi "Students! Aren’t you in your second year in computer science studies? You came just in time"
            students "Just in time for… what exactly?"
            yossi "There is a huge conspiracy on facebook, people says the square root of 2 isn’t real. They say it never existed!!"
            yossi "I need to know the date i’ve proved it to you, i’ll show the world i’m right"
            students "Ok… but first, maybe you know something about the new IDC vaccine?"
            yossi "I’m Yossi Shamai. I know everything. Just help me first, i’ll help you after."
            $ response = renpy.input("What was that holy date???! (dd/mm/yyyy Format) (14/11/2019)")
        else:
            $ response = renpy.input("Dont lie to me")
        $ response = response.strip()
        if response == "14/11/2019":
                yossi "Wow! Thank you, Talk to Max, I have no time, I need to show the world I was right"
                hide yossi with dissolve
                $ resolved.append("helpyossi")
                jump map
        else:
            yossi "This is incorrect"
            $ counter += 1
            jump cs
        jump map    












label diplomat:
    jump map

label library:
    jump map

label entre:
    jump map

label doorms:
    jump map

label end:
    "And so you have the vaccines at hand congratulations"
    "{b}The end{/b}"

label map:
    show screen map
    window hide
    pause

screen back_to_map:
    textbutton "Back to map":
        align (0.01, 0.1)
        action Show("map")

screen map:
    imagemap:
        ground "campus.jpeg"

        $ resolved = requests.get(url+"/resolved").json()

        hotspot(0, 0, 1280, 720) action [Hide("map"),Jump("map")]

        hotspot(995, 221, 42, 74) action [Hide("map"),Jump("aquarium")]
        hotspot(561, 243, 156, 198) action [Hide("map"),Jump("richman")]
        hotspot(808, 75, 360, 81) action [Hide("map"),Jump("comms")]
        hotspot(601, 68, 130, 79) action [Hide("map"),Jump("karnaf")]
        hotspot(304, 152, 153, 131) action [Hide("map"),Jump("bussines")]
        hotspot(351, 283, 58, 186) action [Hide("map"),Jump("diplomat")]
        hotspot(103, 344, 45, 203) action [Hide("map"),Jump("flags")]
        hotspot(25, 342, 69, 206) action [Hide("map"),Jump("psycho")]
        hotspot(20, 19, 191, 112) action [Hide("map"),Jump("law")]
        hotspot(28, 130, 63, 165) action [Hide("map"),Jump("exists")]
        hotspot(1041, 200, 95, 95) action [Hide("map"),Jump("cs")]
        hotspot(350, 503, 185, 174) action [Hide("map"),Jump("library")]
        hotspot(1016, 590, 173, 104) action [Hide("map"),Jump("entre")]
        hotspot(24, 607, 168, 83) action [Hide("map"),Jump("doorms")]
        