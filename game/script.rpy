# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Noxius")
define s = Character("System")
define g = Character("Goblin")
define ne = Character("Necromancer")
define u = Character("???")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene hutan at Transform(xsize=1920, ysize=1080) with fade 

    "Suara dedaunan bergesekan dan kicauan burung terdengar samar di kejauhan"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show noxius neutral at Transform(zoom=0.8, xalign=0.5, yalign=0.5) with dissolve

    n "(Ugh...)"
    
    n "Di mana... ini? Ini jelas bukan kamarku..."

    hide noxius

    "Ia bangkit perlahan, memperhatikan sekeliling hutan yang asing"

    show noxius annoyed at Transform(zoom=0.8, xalign=0.5, yalign=0.5) with dissolve

    n "Hutan? Tapi ini... aneh. Rasanya beda.
    Apa aku... di dunia lain?"

    hide noxius 

    "Suara mekanis muncul dalam kepalanya, seperti notifikasi game"

    s "Selamat datang."

    show system at Transform(zoom=0.5, xalign=0.5, yalign=0.4) with dissolve

    n "Sistem? Seperti... game?"

    hide system

    show noxius neutral at Transform(zoom=0.8, xalign=0.5, yalign=0.5) with dissolve

    n "Yah, baiklah. Kalau ini dunia game, aku harus bertahan hidup dulu. \nKemah. Aku butuh kemah."

    hide noxius with dissolve

    scene hutan_malam at Transform(xsize=1920, ysize=1080) with fade

    jump minigame_klik_item


label minigame_klik_item:
    $ clicked_items = 0
    $ total_items = 5
    $ item_clicked_1 = False
    $ item_clicked_2 = False
    $ item_clicked_3 = False
    $ item_clicked_4 = False
    $ item_clicked_5 = False

    show screen klik_item_game

    $ renpy.pause(5.0)  # kasih waktu 5 detik buat player

    hide screen klik_item_game

    if clicked_items >= total_items:
        hide screen klik_item_game
        "Kamu berhasil mengklik semua item!"
        jump start2
    else:
        "Kamu gagal mengklik semua item tepat waktu."
        return

screen klik_item_game:

    timer 5.0 action Hide('klik_item_game')  # otomatis tutup setelah 5 detik

    text "Klik semua item dalam 5 detik!" xpos 0.5 ypos 0.05 xanchor 0.5

    if not item_clicked_1:
        imagebutton:
            idle "tools/batu.png"
            xpos 0.2 ypos 0.5
            action Function(lambda: increment_item_click(1))

    # sisanya sama


    if not item_clicked_2:
        imagebutton:
            idle "tools/daun.png"
            xpos 0.5 ypos 0.4
            action Function(lambda: increment_item_click(2))

    if not item_clicked_3:
        imagebutton:
            idle "tools/daun.png"
            xpos 0.8 ypos 0.3
            action Function(lambda: increment_item_click(3))

    if not item_clicked_4:
        imagebutton:
            idle "tools/ranting.png"
            xpos 0.3 ypos 0.1
            action Function(lambda: increment_item_click(4))

    if not item_clicked_5:
        imagebutton:
            idle "tools/daun.png"
            xpos 0.4 ypos 0.2
            action Function(lambda: increment_item_click(5))


init python:
    def increment_item_click(item_number, *args, **kwargs):
        if item_number == 1:
            renpy.store.item_clicked_1 = True
        elif item_number == 2:
            renpy.store.item_clicked_2 = True
        elif item_number == 3:
            renpy.store.item_clicked_3 = True
        elif item_number == 4:
            renpy.store.item_clicked_4 = True
        elif item_number == 5:
            renpy.store.item_clicked_5 = True

        if renpy.store.clicked_items < renpy.store.total_items:
            renpy.store.clicked_items += 1


label start2:
    scene hutan_malam at Transform(xsize=1920, ysize=1080) with fade

    "Waktu berlalu. MC membangun kemah sederhana dari ranting dan daun"

    show noxius smile at Transform(zoom=0.8, xalign=0.5, yalign=0.5) with dissolve

    n "Nggak buruk untuk awalan. Besok aku cari makanan. Sekarang... tidur."

    hide noxius with dissolve
    
    "Tiba-tiba, suara geraman terdengar dari semak-semak"

    show noxius annoyed at Transform(zoom=0.8, xalign=0.5, yalign=0.5) with dissolve

    n "Apa itu!?"

    hide noxius with dissolve

    "Seekor goblin LVL 5 muncul dan langsung menyerang"

    show goblin at Transform(xsize=700, ysize=700, xalign=0.5, yalign=0.5) with dissolve

    g "Hraghhhhh"

    hide goblin

    show noxius angry at Transform(zoom=0.8, xalign=0.5, yalign=0.5) with dissolve

    n "Sial! Aku bahkan belum punya senjata! Tapi... aku harus bertahan!"

    hide noxius

    jump minigame

label minigame:
    $ clicks = 0
    $ success = False

    # Tampilkan goblin di tengah
    show goblin at Transform(xsize=700, ysize=700, xalign=0.5, yalign=0.5) with dissolve

    # Tampilkan screen minigame
    show screen minigame_screen

    # Hitung mundur 3 detik
    $ renpy.pause(3.0, hard=True)

    hide screen minigame_screen
    hide goblin

    if clicks >= 5:
        $ success = True
        show noxius smile at Transform(zoom=0.8, xalign=0.5, yalign=0.5)
        "Kamu berhasil!"
        jump start3
        
    else:
        show noxius annoyed at Transform(zoom=0.8, xalign=0.5, yalign=0.5)
        "Kamu gagal."
        
    return

screen minigame_screen:
    # Area tengah layar (misalnya area 400x400 di tengah layar)
    imagebutton:
        xpos 0.5
        ypos 0.5
        anchor (0.5, 0.5)
        idle Null()
        hover Null()
        xysize (700, 700)
        action Function(increment_click)

    text "Cepat pukul Goblin itu [clicks]/5" at Transform(xalign=0.5, yalign=0.01) color "#000000" size 60 outlines [(2, "#FFFFFF", 0, 0)]

init python:
    def increment_click():
        global clicks
        clicks += 1

label start3:
    scene hutan_malam at Transform(xsize=1920, ysize=1080) with fade

    show latar at Transform(zoom=0.5, xalign=0.5, yalign=0.5) with dissolve

    centered "Musuh dikalahkan.
    \nNaik Level 1 -> 5
    \nSkill Unlocked: \nSummon Defeated \nCreature (Passive)"

    hide latar

    show noxius concerned at Transform(zoom=0.8, xalign=0.5, yalign=0.5) with dissolve

    n "Aku menang...?"

    n "Naik level juga..."

    show noxius evil at Transform(zoom=0.8, xalign=0.5, yalign=0.5) with dissolve

    n "Dan aku bisa menyummon makhluk yang kukalahkan? Gila. Ini mulai menarik"

    scene hutan2 at Transform(xsize=1920, ysize=1080) with fade 

    "Keesokan paginya..."

    show noxius smile at Transform(zoom=0.8, xalign=0.5, yalign=0.5) with dissolve

    n "Oke... saatnya cek barang—"

    show noxius concerned at Transform(zoom=0.8, xalign=0.5, yalign=0.5) with dissolve

    n "Eh!?"

    hide noxius 

    show slime at Transform(xalign=0.5, yalign=0.59) with dissolve

    "Barang-barangnya meleleh, ditutupi oleh slime kecil"

    hide slime

    show noxius angry at Transform(zoom=0.8, xalign=0.5, yalign=0.5) with dissolve

    n "Slime!? Dari mana datangnya!?"

    hide noxius

    jump minigame2

label minigame2:
    $ clicks = 0
    $ success = False

    # Tampilkan goblin di tengah
    show slime at Transform(xalign=0.5, yalign=0.59) with dissolve

    # Tampilkan screen minigame
    show screen minigame_screen2

    # Hitung mundur 3 detik
    $ renpy.pause(3.0, hard=True)

    hide screen minigame_screen2
    hide slime

    if clicks >= 8:
        $ success = True
        show noxius smile at Transform(zoom=0.8, xalign=0.5, yalign=0.5)
        "Kamu berhasil!"
        jump start4
        
    else:
        show noxius annoyed at Transform(zoom=0.8, xalign=0.5, yalign=0.5)
        "Kamu gagal."
        
    return

screen minigame_screen2:
    # Area tengah layar (misalnya area 400x400 di tengah layar)
    imagebutton:
        xpos 0.5
        ypos 0.5
        anchor (0.5, 0.5)
        idle Null()
        hover Null()
        xysize (529, 472)
        action Function(increment_click)

    text "Cepat pukul Slime itu [clicks]/8" at Transform(xalign=0.5, yalign=0.01) color "#000000" size 60 outlines [(2, "#FFFFFF", 0, 0)]

init python:
    def increment_click():
        global clicks
        clicks += 1

label start4:
    scene hutan2 at Transform(xsize=1920, ysize=1080) with fade 

    show slime at Transform(xalign=0.2, yalign=0.59) with dissolve
    show slime2 at Transform(xalign=0.5, yalign=0.59) with dissolve
    show slime3 at Transform(xalign=0.8, yalign=0.59) with dissolve

    "MC mencoba melawan, tapi slime-nya terlalu banyak"

    hide slime 
    hide slime2
    hide slime3

    show noxius concerned at Transform(zoom=0.8, xalign=0.5, yalign=0.5) with dissolve

    n "Jumlahnya terlalu banyak...! Persediaanku...!"

    hide noxius with dissolve

    "Setelah berjuang sia-sia, MC terpaksa melarikan diri"

    show noxius concerned at Transform(zoom=0.8, xalign=0.5, yalign=0.5) with dissolve

    n "Baru juga mulai dan udah begini!"
    
    n "Tapi ya udah... kalau ini memang awalnya, aku siap. Bawa aja semuanya!"

    scene cave at Transform(xsize=1920, ysize=1080) with fade 

    hide noxius 

    "Suara langkah kaki MC menjejak dedaunan kering di hutan yang sunyi"

    show noxius neutral at Transform(zoom=0.8, xalign=0.5, yalign=0.5) with dissolve

    n "Itu... gua? Sepertinya ada suara."

    show noxius annoyed at Transform(zoom=0.8, xalign=0.5, yalign=0.5)

    n "...Serigala. Habitat mereka"
 
    hide noxius with dissolve

    show wolf at Transform(xalign=0.5, yalign=0.59) with dissolve

    "MC mengintip dari balik semak. Seekor serigala dewasa terlihat meninggalkan gua untuk berburu"

    hide wolf

    show noxius evil at Transform(zoom=0.8, xalign=0.5, yalign=0.5) with dissolve

    n "Waktunya sempurna. Tanpa induk, anak-anak serigala itu nggak bisa banyak melawan."

    hide noxius

    "MC menyerbu masuk. Terdengar suara perlawanan singkat. Darah, raungan kecil, dan keheningan"

    show latar at Transform(zoom=0.5, xalign=0.5, yalign=0.5) with dissolve

    centered "Musuh dikalahkan.
    \nNaik Level: 5 → 10" 

    hide latar

    show noxius smile at Transform(zoom=0.8, xalign=0.5, yalign=0.5) with dissolve

    n "Level 10... Maju lumayan cepat"

    hide noxius 

    "Tiba-tiba suara langkah kaki lain terdengar, semakin dekat. MC buru-buru bersembunyi di balik batu"

    show noxius annoyed at Transform(zoom=0.8, xalign=0.5, yalign=0.5) with dissolve

    n "Seseorang...? Siapa itu?"

    hide noxius 

    show necromancer at Transform(xsize=1000, ysize=1000, xalign=0.5, yalign=0.5) with dissolve

    "Seseorang dengan jubah gelap masuk ke dalam gua, auranya mengintimidasi. Sistem MC otomatis menampilkan status"

    hide necromancer

    show latar at Transform(zoom=0.5, xalign=0.5, yalign=0.5) with dissolve

    centered "Target terdeteksi: ???
    \nLevel: 50
    \nStatus: Tidak Dikenal"

    hide latar

    show noxius concerned at Transform(zoom=0.8, xalign=0.5, yalign=0.5) with dissolve

    n "Level 50!? Gila...!"

    hide noxius 

    "Orang berjubah itu mendekati mayat serigala, lalu mengangkat tangannya. Aura hitam muncul"

    show necromancer at Transform(xsize=1000, ysize=1000, xalign=0.5, yalign=0.5) with dissolve

    u "Bangkitlah... layani aku dalam kematian."

    hide necromancer with dissolve

    "Serigala yang mati perlahan hidup kembali—mata bersinar biru, tubuh penuh luka tapi bergerak"

    show noxius concerned at Transform(zoom=0.8, xalign=0.5, yalign=0.5) with dissolve

    n "Necromancer...? Ini gawat. Harus pergi sekarang juga."

    hide noxius 

    "MC perlahan mundur keluar dari gua, namun tiba-tiba suara misterius itu terdengar lagi"

    show necromancer at Transform(xsize=1000, ysize=1000, xalign=0.5, yalign=0.5) with dissolve

    ne "...Ada yang mengintai. Kejar."

    hide necromancer with dissolve

    show undead at Transform(xalign=0.5, yalign=0.58) with dissolve

    "Serigala undead melolong dan berlari keluar gua mengejar MC"

    scene darkforest at Transform(xsize=1920, ysize=1080) with fade 

    show noxius annoyed at Transform(zoom=0.8, xalign=0.5, yalign=0.5) with dissolve

    n "Sial, mereka cepat banget! Mana bisa lari terus gini!?"

    "MC berhenti di sebuah tanah lapang, napas memburu"

    n "Nggak ada pilihan... Aku harus lawan mereka!"

    hide noxius

menu :
    "Summon—Goblin LVL 5!":
        jump goblin

    "Summon—Serigala LVL 3!":
        jump serigala
    
label goblin:
    scene darkforest at Transform(xsize=1920, ysize=1080) with fade 

    show noxius angry at Transform(zoom=0.8, xalign=0.5, yalign=0.5) with dissolve

    n "Semua, Bantu aku!"

    show noxius angry at Transform(xalign=0.1, yalign=0.5), Transform(xalign=0.5, yalign=0.5):
        linear 0.5 xalign 0.1   

    show goblin at Transform(xsize=700, ysize=700, xalign=0.7, yalign=0.5, xzoom=-1.0) with dissolve

    "Goblin yang sebelumnya dikalahkan muncul dalam bentuk spirit panggilan, siap bertarung"

    show noxius angry at Transform(zoom=0.8, xalign=0.1, yalign=0.5) with easeinleft

    n "Jangan kasih mereka lewat! Lindungi aku!"

    hide noxius 
    hide goblin

    jump minigame3

label minigame3:
    $ clicks = 0
    $ success = False

    show undead at Transform(xalign=0.5, yalign=0.58) with dissolve

    # Tampilkan screen minigame
    show screen minigame_screen3

    # Hitung mundur 3 detik
    $ renpy.pause(3.0, hard=True)

    hide screen minigame_screen3
    hide undead

    if clicks >= 10:
        $ success = True
        show noxius smile at Transform(zoom=0.8, xalign=0.5, yalign=0.5)
        "Kamu berhasil!"
        jump start5
        
    else:
        show noxius annoyed at Transform(zoom=0.8, xalign=0.5, yalign=0.5)
        "Kamu gagal."
        
    return

screen minigame_screen3:
    # Area tengah layar (misalnya area 400x400 di tengah layar)
    imagebutton:
        xpos 0.5
        ypos 0.58
        anchor (0.5, 0.5)
        idle Null()
        hover Null()
        xysize (500, 500)
        action Function(increment_click)

    text "Cepat Serang Serigala itu [clicks]/10" at Transform(xalign=0.5, yalign=0.01) color "#000000" size 60 outlines [(2, "#FFFFFF", 0, 0)]

init python:
    def increment_click():
        global clicks
        clicks += 1

label serigala:
    scene darkforest at Transform(xsize=1920, ysize=1080) with fade 

    show noxius angry at Transform(zoom=0.8, xalign=0.5, yalign=0.5) with dissolve

    n "Semua, Bantu aku!"

    show noxius angry at Transform(xalign=0.1, yalign=0.5), Transform(xalign=0.5, yalign=0.5):
        linear 0.5 xalign 0.1   

    show wolf at Transform(xalign=0.7, yalign=0.59, xzoom = -1.0) with dissolve

    "Serigala yang sebelumnya dikalahkan muncul dalam bentuk spirit panggilan, siap bertarung"

    show noxius angry at Transform(zoom=0.8, xalign=0.1, yalign=0.5) with easeinleft

    n "Jangan kasih mereka lewat! Lindungi aku!"

    hide noxius 
    hide wolf

    jump minigame4

label minigame4:
    $ clicks = 0
    $ success = False

    show undead at Transform(xalign=0.5, yalign=0.58) with dissolve

    # Tampilkan screen minigame
    show screen minigame_screen4

    # Hitung mundur 3 detik
    $ renpy.pause(3.0, hard=True)

    hide screen minigame_screen4
    hide undead

    if clicks >= 15:
        $ success = True
        show noxius smile at Transform(zoom=0.8, xalign=0.5, yalign=0.5)
        "Kamu berhasil!"
        jump start5
        
    else:
        show noxius annoyed at Transform(zoom=0.8, xalign=0.5, yalign=0.5)
        "Kamu gagal."
        
    return

screen minigame_screen4:
    # Area tengah layar (misalnya area 400x400 di tengah layar)
    imagebutton:
        xpos 0.5
        ypos 0.58
        anchor (0.5, 0.5)
        idle Null()
        hover Null()
        xysize (500, 500)
        action Function(increment_click)

    text "Cepat Serang Serigala itu [clicks]/15" at Transform(xalign=0.5, yalign=0.01) color "#000000" size 60 outlines [(2, "#FFFFFF", 0, 0)]

init python:
    def increment_click():
        global clicks
        clicks += 1

label start5:
    hide noxius

    "Pertarungan sengit terjadi. Serigala undead menerkam, summon MC melawan balik. Raungan, hantaman, dan aura gelap bertabrakan"

    "Satu per satu serigala undead tumbang"

    show noxius angry at Transform(zoom=0.8, xalign=0.5, yalign=0.5) with dissolve

    n "Terakhir! Hyaaa—!"

    hide noxius

    "Serangan terakhir menghancurkan serigala undead terakhir. Hening kembali"

    show latar at Transform(zoom=0.6, xalign=0.5, yalign=0.5) with dissolve

    centered "Musuh dikalahkan.
    \nNaik Level: 10 → 15
    \nSkill Update: 
    \nSummon Capacity Unlocked
    \nMaksimum makhluk summon: 
    \n3 jenis aktif"

    hide latar

    show noxius neutral at Transform(zoom=0.8, xalign=0.5, yalign=0.5) with dissolve

    n "...Aku masih hidup."
    
    n "Dan... aku makin kuat. Tapi siapa tadi orang itu?"

    "MC menatap ke arah gua dari kejauhan, ekspresinya waspada"

    show noxius annoyed at Transform(zoom=0.8, xalign=0.5, yalign=0.5)
    
    n "Dunia ini jauh lebih berbahaya dari yang kupikirkan. Tapi... aku nggak akan mundur."


    








    












    

    





    



    




    